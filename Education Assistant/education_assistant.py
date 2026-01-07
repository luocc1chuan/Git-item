import os
from openai import  OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.getenv('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com"
)
print("-"*5,"欢迎使用IEP特教小助手","-"*5)
while True:
    print("\n-----------------------")
    chlid_name=input("1.请输入孩子的姓名（或输入“拜拜”即可退出）：")
    if chlid_name=="拜拜":
        print("感谢您的使用，欢迎您的下次进入！")
        break
    chlid_age=input("2.请输入孩子的年龄：")
    chlid_sympotom=input("3.请输入诊断结果（如自闭症、多动症）：")
    chlid_behavior=input("4.请简述孩子目前最大的行为问题：")
    user_prompt=f"我的学生{chlid_name}今年{chlid_age}岁了，诊断结果是{chlid_sympotom},目前最大的问题是{chlid_behavior},请根据此信息为他生成一份IEP长期目标"
    print(f"正在为学生{chlid_name}制定计划...(请稍等）")
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "你是一名资深的特殊教育老师，擅长制定IEP计划"},
                {"role": "user", "content": user_prompt},
            ],
            stream=False
        )
        print("-"*10,"结果均为AI分析 请理性看待","-"*10)
        print(response.choices[0].message.content)
    except Exception as a:
        print(f"出错了：{a}")
        print("请检查网络或者key是否出错！")



