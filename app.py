from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
def get_gemini_repsonse(input,image,prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,image[0],prompt])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

st.set_page_config(page_title="Image Analysis")

st.header("Image Analysis Using Gemini Pro Vision")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Submit")

input_prompt="""
You are a medical practitioner in a hospital. It is given that the image that is sent is of a patient suffering
         from some disease. You have to analyse the image given below and try to guess the type of disease the person 
         probably has. List out the reasons why you came to the conclusion(List it out in points). Also tell which doctor to go to. If you are
         unable to discern the type of disease, kindly state that the patient goes to a General Physician. Else you can
         specify which type of doctor to go to. For example: cardiologist or an oncologist. If you find anything other
        than patient's images (for example- if there is an image of a food item), kindly prompt them to give the proper
        image. Make the important text bold.


"""

if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_repsonse(input_prompt,image_data,input)
    st.subheader("The Response is")
    st.write(response)

