from openai import OpenAI
import base64
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
  api_key=os.getenv("API_KEY"),
  base_url=os.getenv("BASE_URL")
)


PROMPT="""
Generate an image depicting a vibrant and dynamic scene at the 'AI Thực Chiến' competition. The image should show young people actively engaged in programming and lively discussions. Overlayed prominently is a graphic with scrolling text that reads: 'BUILD LLM FOR VIETNAMESE'
"""
response = client.chat.completions.create(
  model="gemini-2.5-flash-image-preview",
  messages=[{"role": "user", "content": PROMPT}],
  modalities=["image"]
)

# Lưu ảnh từ dữ liệu base64
base64_string = response.choices[0].message.images[0].get("image_url").get("url")
if ',' in base64_string:
  header, encoded = base64_string.split(',', 1)
else:
  encoded = base64_string
image_data = base64.b64decode(encoded)
with open("generated_chat_image.png", "wb") as f:
  f.write(image_data)
print("Image saved to generated_chat_image.png")
