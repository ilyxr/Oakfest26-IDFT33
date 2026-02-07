#Cybersecurity is cancer

from google import genai
from google.genai import types
import httpx
import os

from dotenv import load_dotenv

load_dotenv()

api_key1 = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key1)

#doc_url = str(input("Enter: "))
doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"

doc_data = httpx.get(doc_url).content

prompt = "Summarize this document"
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        types.Part.from_bytes(
            data=doc_data,
            mime_type='application/pdf',
        ),
        prompt
    ]
)

print(response.text)