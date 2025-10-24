import os
import litellm
from litellm import completion

from dotenv import load_dotenv

load_dotenv()

litellm.api_base = os.getenv("BASE_URL")
litellm.api_key = os.getenv("API_KEY")

response = completion(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "user",
            "content": "Tổng hợp và phân tích điểm nổi bật về tình hình phát triển AI tại Việt Nam (tính đến tháng 10/2025)",
        }
    ],
    web_search_options={
        "search_context_size": "medium"  # Options: "low", "medium", "high"
    }
)
print(response)
