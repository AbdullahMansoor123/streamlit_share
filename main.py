import glob
import os
from PIL import Image

import cv2
import streamlit as st

st.title('Demo Streamlit Share')
files = glob.glob(os.getcwd() + '/*.jpg')

source = st.selectbox('Select a file for display', tuple(files))

image = Image.open(source)
st.image(image, caption="Output Image")
