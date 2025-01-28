# import modules
import os
import json
from io import BytesIO
from pypdf import PdfWriter
import streamlit as st
from streamlit_lottie import st_lottie

# streamlit page configuration
st.set_page_config(page_title='PDF Merger',
                   page_icon=':page_facing_up:',
                   layout = 'centered'
                   )
st.title('PDF Merger')

# lottie animation
with open('assets/images/cover.json','r') as f:
    lottie_cover = json.load(f)
st.lottie(lottie_cover, speed=0.5, reverse=False, loop=True, quality='low', height=500)

# short application description
multi = '''
Merge multiple PDF files seamlessly with this simple application. 
Upload your files, and with a single click, download the combined document as a single PDF.
'''

st.markdown(multi)

# file uploader
uploaded_files = st.file_uploader('Upload PDF file(s)', accept_multiple_files=True, type=['.pdf'])

merger = PdfWriter()

if uploaded_files:
    for file in uploaded_files:
        merger.append(file)

    buffers = BytesIO()
    merger.write(buffers)
    buffers.seek(0)
    merger.close()

    # download button
    st.download_button(
        label = 'Download Merged File',
        data = buffers,
        file_name = 'merged_file.pdf',
        mime = 'application/pdf'
    )
