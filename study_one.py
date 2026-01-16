while True:
    try:
        score=(input("请输入第一科成绩（输入exit退出）："))
        if score=="exit":
            print("成绩已全部计算完毕，欢迎下次使用！")
            break
        s1=float(score)
        s2=float(input("请输入第二科成绩："))
        s3=float(input("请输入第三科成绩："))
        s4=float(input("请输入第四科成绩："))
        s5=float(input("期末考成绩："))

        average_score=(s1+s2+s3+s4)/4
        final_score=(average_score*0.4)+(s5*0.6)

        print("该学生期末成绩已计算完毕：%.1f分"%final_score)
        print("-"*30)

        continue
    except ValueError as a:
        print(f"出现错误“{a}")
        print("请勿输入非数字！")
        continue
    except Exception as b:
        print(f"未知错误：{b}")
        print("请重新输入！")
        continue