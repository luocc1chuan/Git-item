# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

#身份验证 创建
client = OpenAI(
    api_key=os.getenv('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

#发送请求
response = client.chat.completions.create(
    model="deepseek-chat",  #我选择为Deepseek_chat模型
    messages=[
        {"role": "system", "content": "你是我的特教助手"},#contente:模型的性格、语气的设置
        {"role": "user", "content": "你好，你是谁？"},  #用户的问答
    ],
    stream=False
)

print(response.choices[0].message.content)
