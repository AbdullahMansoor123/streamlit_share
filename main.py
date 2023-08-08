import glob
import os


import cv2
import streamlit as st


st.title('Demo Streamlit Share')

files = glob.glob(os.getcwd() + '/*.png')
file_name = tuple(os.path.basename(i) for i in files)
print(file_name)
source = st.selectbox('Select a file for display', tuple(file_name))
source_path = os.path.join(os.getcwd(), source)

image = cv2.imread(source_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

st.image(image, caption="Output Image")
