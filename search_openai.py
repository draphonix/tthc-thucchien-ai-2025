from openai import OpenAI
import base64
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
  api_key=os.getenv("API_KEY"),
  base_url=os.getenv("BASE_URL")
)



response = client.chat.completions.create(
  model="gemini-2.5-flash",
  messages=[{"role": "user", "content": "Những lợi ích của việc ứng dựng AI vào Dịch vụ công "}],
  tools=[{"type": "web_search"}],
  reasoning_effort="medium"
)

print(response.choices[0].message.content)
