import streamlit as st
from story_generator import generate_story_from_images, narrate_story
from PIL import Image

st.title("AI Story Teller")
st.markdown("Upload up to 10 images, choose a style and let AI write and narrate a story based on them.")

with st.sidebar:
    st.header("Controls")

    # Dropdown for story style
    style = st.selectbox(
        "Select Story Style", ["Fairy Tale", "Adventure", "Sci-Fi", "Mystery", "Romance", "Horror", "Comedy", "Drama", "Morale"], 
        index=0
    )

    # Side panel for image upload
    uploaded_files = st.file_uploader("Upload Images", accept_multiple_files=True, type=["png", "jpg", "jpeg"], key="images")

    generate_story = st.button("Generate Story & Narration", type="primary")

# Button to generate story
if generate_story:
    if not uploaded_files:
        st.warning("Please upload at least one image.")
    elif len(uploaded_files) > 10:
        st.warning(f"You can upload up to 10 images. You have uploaded {len(uploaded_files)}.")
    else:
        with st.spinner("Generating story & narration... This may take a few moments."):
            try:
                images = [Image.open(file) for file in uploaded_files]
                st.subheader("Visual Inspiration")
                image_columns = st.columns(len(images))
                for i, img in enumerate(images):
                    with image_columns[i]:
                        st.image(img, use_column_width=True)
                story = generate_story_from_images(images, style)

                if "Error" in story or "failed" in story or "API KEY" in story:
                    st.error(story)
                else:
                    st.subheader(f"Generated {style} Style Story")
                    st.success(story)

                st.subheader("Listen to the Narration")
                audio_bytes = narrate_story(story)
                if audio_bytes:
                    st.audio(audio_bytes,format="audio/mp3")
                
            except Exception as e:
                st.error(f"An error occurred while generating the story: {e}")
