import cv2 as cv
import numpy as np
import pandas as pd
import streamlit as st
from colorblind import colorblind

st.title('Colorblind Project')

st.sidebar.title('Project Sidebar')
st.sidebar.subheader('Pages')

app_mode = st.sidebar.selectbox(
    'Choose', ['Home', 'By Image', 'More about Colorblind'])

if app_mode == 'Home':
    st.markdown(
        'This project is created to increase the awareness of public about colorblindness')

    st.video('https://youtu.be/GCQE1U2EQ_4')


elif app_mode == 'By Image':
    st.markdown('''
    Colorblind is a computer vision library that converts images into a colorblind friendly version depending on the type of colorblindness. The three supported types of colorblindness/color weakness are:
    - Deuteranopia: red-green weakness, particularly green
    - Protanopia: red-green weakness, particularly red
    - Tritanopia: blue weakness
    ''')
    row1col1, row1col2 = st.columns([2, 1])
    image_file = row1col1.file_uploader(
        "Upload an Image", type=["jpg", "jpeg", "png"])
    color_type = row1col2.radio("Choose the Type of Colorblind", [
                                "Protanopia", "Deuteranopia", "Tritanopia"])
    row2col1, row2col2 = st.columns(2)
    if image_file is not None:
        # Read image
        file_bytes = np.asarray(bytearray(image_file.read()), dtype=np.uint8)
        # Process image for OpenCV
        image = cv.imdecode(file_bytes, 1)
        image = image[..., ::-1]
        if color_type == "Protanopia":
            converted_image = colorblind.simulate_colorblindness(
                image, colorblind_type='protanopia')
        elif color_type == "Deuteranopia":
            converted_image = colorblind.simulate_colorblindness(
                image, colorblind_type='deuteranopia')
        elif color_type == "Tritanopia":
            converted_image = colorblind.simulate_colorblindness(
                image, colorblind_type='tritanopia')
        row2col1.text('Original Image')
        row2col1.image(image_file)
        row2col2.text('Output Image')
        row2col2.image(converted_image, clamp=True, channels='BGR')
    else:
        pass
elif app_mode == 'More about Colorblind':
    st.markdown(
        '''
        ### More information related to color blindness \n
        [Coblis — Color Blindness Simulator](https://www.color-blindness.com/coblis-color-blindness-simulator/)
        ''')
