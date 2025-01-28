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


# initialize the buffer variable
merged_pdf_buffer = None

# file uploader form
with st.form('my_form', clear_on_submit=True):
    files = st.file_uploader('Upload PDF files', accept_multiple_files=True, type=['.pdf'])
    submitted = st.form_submit_button('Combine Files')

    if submitted:
        if not files:
            st.warning('Please Upload PDF Files.')

        else:
            try:
                merger = PdfWriter()
                for file in files:
                    merger.append(file)

                merged_pdf_buffer = BytesIO()
                merger.write(merged_pdf_buffer)
                merged_pdf_buffer.seek(0)
                merger.close()

                st.success('Files merged successfully!')

            except Exception as e:
                st.error(f"An error occurred: {e}")


# download button
if merged_pdf_buffer:
    st.download_button(
        label = 'Download Merged File',
        data = merged_pdf_buffer,
        file_name = 'merged_file.pdf',
        mime = 'application/pdf'
    )
