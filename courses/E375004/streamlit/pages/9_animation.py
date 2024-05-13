import streamlit as st
import numpy as np
from PIL import Image
from urllib.request import urlopen
import io

fd = urlopen(r"https://th.bing.com/th/id/R.ecce9e23906dee22b0a6cc844c8cc676?rik=%2fMezSX3zPKy7yQ&riu=http%3a%2f%2fwww.wcahs.com%2fuploads%2f2%2f9%2f4%2f0%2f29404057%2fpublished%2fkittens-two-isolated.jpg%3f1575922792&ehk=Kn4M2CTUF%2fe4GRHEH9w88D5g11ahPMaOSrhWmmKAeFw%3d&risl=&pid=ImgRaw&r=0")
image_file = io.BytesIO(fd.read())

imag = Image.open(image_file)
img = np.array(imag)
filter = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])/9 # edge detection
n = 5
filter = np.ones((n,n))/(n**2)

image = st.image(img, caption='kitty')
# Interactive Streamlit elements, like these sliders, return their value.
# This gives you an extremely simple interaction model.
# iterations = st.sidebar.slider("Level of detail", 2, 20, 10, 1)
# separation = st.sidebar.slider("Separation", 0.7, 2.0, 0.7885)

# # Non-interactive elements return a placeholder to their location
# # in the app. Here we're storing progress_bar to update it later.
# progress_bar = st.sidebar.progress(0)

# These two elements will be filled in later, so we create a placeholder
# for them using st.empty()
# frame_text = st.sidebar.empty()
# image = st.empty()

# m, n, s = 960, 640, 400
# x = np.linspace(-m / s, m / s, num=m).reshape((1, m))
# y = np.linspace(-n / s, n / s, num=n).reshape((n, 1))


    
# Get image dimensions
img_height, img_width, num_channels = img.shape

# Get filter dimensions
filter_height, filter_width = filter.shape

# Add borders of zeros to picture
pad_width = filter_width // 2
pad_height = filter_height // 2

padded_img = np.zeros((img_height + 2*pad_height, img_width + 2*pad_width, num_channels))
padded_img[pad_height:-pad_height, pad_width:-pad_width, :] = img

# Convolution
filtered_im = img

for height in range(img_height):
    for width in range(img_width):
        for chan in range(num_channels):
            filtered_im[height, width, chan] = np.sum(filter * padded_img[height:height + filter_height, width:width + filter_width, chan])
        image.image(filtered_im)

    print(f'Done with chanel_n {chan + 1}, h:{img_height}, w:{img_width}')


# Update the image placeholder by calling the image() function on it.



# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")