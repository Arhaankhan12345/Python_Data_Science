# streamlit run app1/helli.py
from PIL import Image
import streamlit as st

st.title("sample App")

st.header("This is a header")
st.subheader("This is subheader")

image = st.camera_input("Take a picture")
if image:
    im = Image.open(image)
    # purple gradient image 
    color = st.color_picker("pick a color","#00f900")
    im2 = Image.new("RGB",im.size,color)
    # overlay the two image 
    im = Image.blend(im,im2,0.5)
    # resize by 30%
    im = im.resize((int(im.size[0]*0.3),int(im.size[1]*0.3)))
    st.image(im)

    filename = st.text_input("save as","image.png")
    if st.button("save"):
        im.save(filename)
        st.snow()
