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

#
# import os
# from openai import OpenAI
# from dotenv import load_dotenv
# load_dotenv()
#
# #身份验证
# client = OpenAI(
#     api_key=os.getenv('DEEPSEEK_API_KEY'),
#     base_url="https://api.deepseek.com"
# )
#
# #开头界面
# print("="*30)
# print("-"*3,"欢迎使用IEP特教小助手","-"*3)
# print("\t让生活充满爱与关怀\t")
#
# #用户互动输入
# chlid_name=input("1、请输入孩子的姓名：")
# chlid_age=input("2、请输入孩子的年龄：")
# chlid_sympotom=input("3、请输入孩子的诊断结果(如自闭症、多动症）：")
# chlid_behavior=input("请简述孩子目前最大的行为问题：")
#
# #将所有互动问题总和
# User_prompt=f"我的学生叫{chlid_name}，今年{chlid_age}岁了，目前的诊断结果为{chlid_sympotom}，最大的行为问题是{chlid_behavior}，请帮他生成一份长期目标计划"
#
# print("------------------------")
# print("识别信息成功，正在思考中...")
# response = client.chat.completions.create(
#     model="deepseek-chat",
#     messages=[
#         {"role": "system", "content": "你是一名资深的特殊教育专家，擅长制定IEP计划"},
#         {"role": "user", "content": "User_prompt"},
#     ],
#     stream=False
# )
# print("-"*10,"上述结果均为AI分析 请理性看待","-"*10)
#
#
# print(response.choices[0].message.content)
