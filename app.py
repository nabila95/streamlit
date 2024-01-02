import streamlit as st
import pandas as pd
st.set_page_config(
    page_title='Scraping BDM',
    page_icon='🐯',
    layout='centered',
)
#load data

df=pd.read_json('data.json').T

#Title
st.title('MY First App Streamlit -V1')
#TEXT
st.write('Ceci est une zone de text')
#Markdown
st.markdown(

    """
`print("hello world)`
"""
)

#Checkbox
if st.checkbox('show information'):
    st.write(df)

#SelectBox
    user_select=st.selectbox('Select your article', range(len(df)))
    col1,col2=st.columns(2)
    with col1:
        #show Image
        st.image(df.iloc[user_select].image)
    with col2:
        st.write(df.iloc[user_select].title)


# Formulaire
with st.form("First Form"):
    user_input = st.text_input("Tap your text")     # Input
    
    if st.form_submit_button('Send'):               # Submit Button Form
        st.write(user_input)