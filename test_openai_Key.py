import os
from dotenv import load_dotenv
from openai import OpenAI

# load_dotenv()  # 若 .env 不在当前目录，可写 load_dotenv(dotenv_path="/Users/.../HW2_/.env")

from pathlib import Path
load_dotenv(Path(__file__).resolve().parent / ".env")

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("没有加载到 OPENAI_API_KEY，请检查 .env")

client = OpenAI(api_key=api_key)  # 如果环境变量已成功加载，也可以写 client = OpenAI()
response = client.models.list()
print(response)

print(openai.models.list())

print(os.getenv("OPENAI_API_KEY"))

print("Loaded key?", os.getenv("OPENAI_API_KEY") is not None)
