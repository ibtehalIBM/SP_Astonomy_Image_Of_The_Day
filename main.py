import streamlit as st
import requests as r

url = "https://api.nasa.gov/planetary/apod?" \
      "api_key=YclxOjDyAU3GNzZH2wwcIglfoLcV1WvujcUtncet"
response = r.get(url).json()

title = response['title']
image_url = response['url']
descr = response['explanation']

# image_request = r.get('https://en.wikipedia.org/wiki/Cat#/media/File:Orange_tabby_cat_sitting_on_fallen_leaves-Hisashi-01A.jpg')
# with open('image.png', 'wb') as img:
#     img.write(image_request.content)

st.title(title)
# st.image('image.png')
st.write(descr)

