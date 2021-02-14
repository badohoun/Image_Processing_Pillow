import streamlit as st

from PIL import Image

import matplotlib.pyplot as plt

from PIL import ImageFilter , ImageEnhance




icon = Image.open("Defend_Intelligence.png")

st.set_page_config(
   page_title="Image processing with Pillow in Python",
   page_icon = icon,
   layout = "centered",
   initial_sidebar_state ="auto"

)


image = Image.open("Pillow.jpg")

st.image(image)



audio_file = open("Nouvel enregistrement 59.m4a", "rb")
audio_bytes = audio_file.read()

image = Image.open("36052611.IMG_9735birds.jpg")
fig = plt.figure()

option = st.selectbox(
"Select an Option",
[
  "HomePage" ,
  "Show Image",
  "Rotate Image",
  "Create Thumbnail",
  "Crop",
  "Merge Images",
  "Flip Image",
  "Black & white",
  "Filters Sharpen",
  "TfImage"

]
)

if option == "HomePage":
    st.header("Image processing with Pillow in Python")
    """

    # Image processing with Pillow in Python  :
     Please select a page on the left
    """



    st.image(image)
    st.audio(audio_bytes)

    st.balloons()
if option == "Show Image":
    plt.imshow(image)
    plt.axis("off")
    st.pyplot(fig)
elif option == "Rotate Image":
    rotated_image = image.rotate(90)
    plt.imshow(rotated_image)
    plt.axis("off")
    st.pyplot(fig)
elif option == "Create Thumbnail":
    size = 300,300
    image.thumbnail(size)
    image.save("thumb.png")
    plt.imshow(image)
    st.pyplot(fig)
elif option == "Crop":
    box = (50 , 100 , 400 , 400)
    image.crop(box)
    image.save("crop.png")
    plt.imshow(image)
    plt.axis("off")
    st.pyplot(fig)
elif option == "Merge Images":
    logo = Image.open("10380894.png")
    position = (1,2)
    image.paste(logo , position)
    plt.imshow(image)
    plt.axis("off")
    st.pyplot()
elif option == "Flip Image":
    flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)
    plt.imshow(flipped_image)
    plt.axis("off")
    st.pyplot(fig)

elif option == "Black & white":
    bw = image.convert("1")
    plt.imshow(bw)
    plt.axis("off")
    st.pyplot(fig)
elif option == "Filters Sharpen":
    sharp = image.filter(ImageFilter.SHARPEN)
    plt.imshow(sharp)
    plt.axis("off")
    st.pyplot(fig)
elif option == "TfImage":
    flipped = tf.image.flip_left_right("36052611.IMG_9735birds.jpg")
    plt.imshow(flipped)
    plt.axis("off")
    st.pyplot(fig)
