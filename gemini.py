import google.generativeai as genai
import os
from dotenv import load_dotenv
import requests


def trans_jp_to_kr(text):
    load_dotenv(dotenv_path="./env.env")
    genai.configure(api_key=os.getenv("API_KEY"))

    model = genai.GenerativeModel(model_name="gemini-1.5-pro-exp-0827")

    gemini_response = model.generate_content((text + '를 한국어로 번역해줄래'))
    print(gemini_response.text)

