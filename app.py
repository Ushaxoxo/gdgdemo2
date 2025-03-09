import streamlit as streamlit
import fitz
import google.generativeai as genai
import os

api= os.getenv("API_KEY")
print(api)