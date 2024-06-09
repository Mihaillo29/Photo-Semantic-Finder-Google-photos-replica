# Photo-Semantic-Finder---Google-photos-replica
 "Photo Semantic Finder: Replicate Google Photos' aiming to replicate its functionality of searching images using natural language queries. With this application, users can upload their images and search for them using descriptive captions such as "car", "child playing", or "birthdays".

## How it works

1. **Upload Images**: Users can upload their images through the web interface.
  
2. **Caption Generation**: The uploaded images are passed through the BLIP Image Captioning model to generate descriptive captions.
  
3. **Search by Caption**: Users can search for images using natural language queries. The application retrieves images whose captions match the query.

![Screenshot 2024-06-09 221845](https://github.com/Mihaillo29/Photo-Semantic-Finder---Google-photos-replica/assets/117961472/15733937-c29e-422a-92b7-a2be5d543afc)

<hr>

### Feature included

- **Semantic Image Search**: Utilizes state-of-the-art natural language processing models like [Salesforce's BLIP Image Captioning Large](https://huggingface.co/Salesforce/blip-image-captioning-large) to generate descriptive captions for uploaded images.
  
- **Streamlit Web Application**: The frontend of the application is built using Streamlit, providing an intuitive user interface for uploading images and querying them using natural language.
  
- [x] Uploading and Preview <details> <summary>Preview image </summary>![Screenshot 2024-06-09 210626](https://github.com/Mihaillo29/Photo-Semantic-Finder-/assets/117961472/0ebc7906-8454-4b70-b018-d069bb1c30f5)</details>

- [x] Grid Interface <details> <summary>Preview image </summary> ![Screenshot 2024-06-09 210724](https://github.com/Mihaillo29/Photo-Semantic-Finder-/assets/117961472/5e06890f-b6ab-42bc-9914-ce3939a3c0d5)</details>

- [x] Searching using description <details> <summary>Preview image </summary>
![Screenshot 2024-06-09 205943](https://github.com/Mihaillo29/Photo-Semantic-Finder-/assets/117961472/0489dfc1-e41d-40ed-9792-7171d68980eb)
 sol:![Screenshot 2024-06-09 210543](https://github.com/Mihaillo29/Photo-Semantic-Finder-/assets/117961472/52970d00-f1ef-44b5-bb67-174b2c9c3f3e)</details>

- [x] others <details> <summary>Preview image </summary>  
![Screenshot 2024-06-09 205540](https://github.com/Mihaillo29/Photo-Semantic-Finder-/assets/117961472/2c322e1b-9b2b-48c0-8a37-dabad0dd746b)</details>

## Technologies Used

- **Streamlit**: Used for building the web application frontend.
  
- **Hugging Face Transformers**: Leveraged the [Salesforce/blip-image-captioning-large](https://huggingface.co/Salesforce/blip-image-captioning-large) model for generating image captions.
  
- **Python**: The backend and scripting language used for the application development.

## Usage

>**_Download the model from [Hugging Face](https://huggingface.co/Salesforce/blip-image-captioning-large) or else from [here](https://drive.google.com/file/d/1GhvR7xM5yqr2arQhIJVCEw1QZz32Yfup/view?usp=sharing) and then extract it in 'Models' folder_**
>
1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/photo-semantic-finder.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:

    ```bash
    streamlit run photo_Semantics.py
    ```

## Contributing

Contributions are welcome! Feel free to open issues for feature requests, bug fixes, or general improvements. Pull requests are also appreciated.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

