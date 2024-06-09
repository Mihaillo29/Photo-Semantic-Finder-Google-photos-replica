from transformers import pipeline
import streamlit as st
from pathlib import Path
from PIL import Image
import os
import uuid

############################################
# Pipeline
############################################
@st.cache_resource()
def load_model_pipeline(task, model_path, device="cuda"):
    model = pipeline(task, model=model_path, device=device)
    return model

# Generates a descriptive caption for the image using a pre-trained model.
def get_image_semantics(image):
    semantics = model(images=image, max_new_tokens=50)[0]['generated_text']  # Specify max_new_tokens
    return semantics

# Renames the image with a unique identifier (UUID) and detected semantics, then saves it.
def rename_and_save_image(image, save_path, semantics):
    new_file_name = f"{uuid.uuid4()}_{semantics.replace(' ', '_')}.jpg"  # Create a new file name with underscores instead of spaces.
    new_save_path = os.path.join(Path(save_path), new_file_name)  # Determine the full save path.
    
    # Convert image to 'RGB' mode if it's in 'RGBA'
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    
    image.save(new_save_path)  # Save the image at the new location.
    return new_save_path  # Return the new save path.

# Saves uploaded files and processes them with an image captioning model.
def save_and_process_files(uploaded_files, upload_dir):
    progress_bar = st.progress(0)  # Create a progress bar to track file processing.
    count = st.empty()  # Create a placeholder to display the count of processed files.
    for i, uploaded_file in enumerate(uploaded_files):
        image = Image.open(uploaded_file)  # Open the uploaded file as an image.
        semantics = get_image_semantics(image)  # Get image semantics (descriptive caption).
        
        # Rename the image file based on its content and save it.
        rename_and_save_image(image, upload_dir, semantics)
        progress_bar.progress(int((i+1)/len(uploaded_files)*100))  # Update the progress bar.
        count.text(f"{i+1}/{len(uploaded_files)} images processed")  # Update the count display.

# Retrieves image files from the specified directory.
def get_image_files(upload_dir):
    return [os.path.join(upload_dir, filename)  # Combine directory path with file name.
            for filename in os.listdir(upload_dir)  # List all files in the directory.
            if filename.endswith(('.png', '.jpg', '.jpeg'))]  # Filter for image files only.

# Filters images based on a search query.
def filter_images(search_query, upload_dir):
    image_files = get_image_files(upload_dir)  # Get all image files from the directory.
    if search_query:
        keywords = search_query.lower().split()  # Split the search query into keywords.
        # Keep only files whose names contain all the keywords.
        filtered_files = [file for file in image_files if all(keyword in Path(file).stem.lower() for keyword in keywords)]
        return filtered_files
    else:
        return image_files

# Displays images in a grid layout 
def display_images_in_grid(image_files):
    if image_files:
        num_cols = 4  # Number of columns in the grid.
        cols = st.columns(num_cols)  # Create columns.
        for index, file_path in enumerate(image_files):
            image = Image.open(file_path)  # Open the image file.
            with cols[index % num_cols]:
                st.image(image, use_column_width='always')  # Display the image in a column.
                col1, col2 = st.columns([1, 1])
                with col1:
                    st.download_button(
                        label="Download",
                        data=open(file_path, "rb").read(),
                        file_name=Path(file_path).name,
                        mime="image/jpeg",
                        key=f"download_{file_path}"
                    )
                with col2:
                    if st.button('Delete', key=f"delete_{file_path}"):
                        os.remove(file_path)
                        st.experimental_rerun()
    else:
        st.write("No images found.")

############################################
# Streamlit Application
############################################

st.set_page_config(page_title="Google Photos Replica", layout="wide")
st.title("Photo Semantic Finder")
st.markdown("<h6 style='text-decoration: underline;'>Upload and Organize Your Photos with AI-generated Captions</h6>", unsafe_allow_html=True)

# Sidebar for model path and settings
with st.sidebar:
    st.header("Settings")
    model_path = "./Models"
    device = st.selectbox("Device", ["cuda", "cpu"], index=0)
    model = load_model_pipeline('image-to-text', model_path, device=device)

# Ensure the directory for uploaded images exists.
upload_dir = 'uploaded_images'
os.makedirs(upload_dir, exist_ok=True)

# Section for uploading images
st.header("Upload Images")
if 'file_uploader_key' not in st.session_state:
    st.session_state['file_uploader_key'] = uuid.uuid4().hex

uploaded_images = st.file_uploader("Choose photos", accept_multiple_files=True,
                                   type=["jpg", "jpeg", "png"], key=st.session_state['file_uploader_key'])

if uploaded_images:
    st.subheader("Preview Uploaded Images")
    cols = st.columns(4)
    for i, uploaded_file in enumerate(uploaded_images):
        image = Image.open(uploaded_file)
        cols[i % 4].image(image, caption=uploaded_file.name, use_column_width='always')
    
    if st.button("Continue"):
        save_and_process_files(uploaded_images, upload_dir)
        st.session_state['file_uploader_key'] = uuid.uuid4().hex
        st.experimental_rerun()

# Section for searching images
st.header("Search Images")
search_query = st.text_input("", placeholder="Enter keywords to search for images")

filtered_files = filter_images(search_query, upload_dir)
display_images_in_grid(filtered_files)
