import os
from dotenv import load_dotenv
import openai

# 加载 .env 文件中的环境变量
load_dotenv()

# 从环境变量获取 API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# 测试 API 连接
# print(openai.models.list())

# 
from openai import OpenAI
client = OpenAI()  # 已经从环境变量读取 OPENAI_API_KEY
models = client.models.list()

print(f"共返回 {len(models.data)} 个模型，前 99个是：")
for model in models.data[:99]:
    print("-", model.id)
