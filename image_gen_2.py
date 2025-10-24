from openai import OpenAI
import base64

# --- Cấu hình ---
AI_API_BASE = "https://api.thucchien.ai/v1"
AI_API_KEY = "sk-ugPPYGIHp5QnLBP-ppz0aA" # Thay bằng API key của bạn
IMAGE_SAVE_PATH = "generated_chat_image_1.png"

# --- Khởi tạo client ---
client = OpenAI(
  api_key=AI_API_KEY,
  base_url=AI_API_BASE,
)

# --- Bước 1: Gọi API để tạo hình ảnh ---
try:
  response = client.chat.completions.create(
      model="gemini-2.5-flash-image-preview",
      messages=[
          {
              "role": "user",
              "content": "Một nữ MC người việt nam trẻ trung xinh đẹp đang ngồi ở đài truyền hình"
          }
      ],
      modalities=["image"]  # Chỉ định trả về dữ liệu ảnh
  )

  # Trích xuất dữ liệu ảnh base64
  base64_string = response.choices[0].message.images[0].get('image_url').get("url")
  print("Image data received successfully.")

  # --- Bước 2: Giải mã và lưu hình ảnh ---
  if ',' in base64_string:
      header, encoded = base64_string.split(',', 1)
  else:
      encoded = base64_string

  image_data = base64.b64decode(encoded)

  with open(IMAGE_SAVE_PATH, 'wb') as f:
      f.write(image_data)
      
  print(f"Image saved to {IMAGE_SAVE_PATH}")

except Exception as e:
  print(f"An error occurred: {e}")