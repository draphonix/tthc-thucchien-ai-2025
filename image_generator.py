import litellm
import base64

# --- Cấu hình ---
AI_API_BASE = "https://api.thucchien.ai"
AI_API_KEY = "sk-ugPPYGIHp5QnLBP-ppz0aA"  # TODO: Replace with your actual API key


# --- Gọi API để tạo hình ảnh ---
response = litellm.image_generation(
  prompt="Hình ảnh một nữ MC người Việt Nam trẻ trung xinh đẹp đang ngồi ở đài truyền hình",
  model="litellm_proxy/imagen-4",
  n=1,
  api_key=AI_API_KEY,
  api_base=AI_API_BASE,
  aspect_ratio="16:9",
)

# --- Xử lý và lưu từng ảnh ---
for i, image_obj in enumerate(response.data):
  b64_data = image_obj['b64_json']
  image_data = base64.b64decode(b64_data)

  save_path = f"generated_image_{i+1}.png"
  with open(save_path, 'wb') as f:
      f.write(image_data)
      print(f"Image saved to {save_path}")
