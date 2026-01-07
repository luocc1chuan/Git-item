import time
def outer(func):
    def inter(student,*args,**kwargs):
        print(f"【IEP训练开始】训练对象：{student}")
        start=time.time()
        result=func(student,*args,**kwargs)
        end=time.time()
        sum=round(end-start,2)  #用round代替了:.4f,保留2位小数
        print(f"【IEP训练完成】耗时：{sum}秒|状态：完成√")
        return result
    return inter
@outer
def speech_tarin(student):
    """个性化言语训练第一阶段"""
    print(f"→正在为{student}进行第一阶段的语言训练："
          "从模仿发音、音节到单词，纠正发音到听懂指令，识别句子，回答简单问题")
    time.sleep(0.8) #模拟特教真实案例场景
@outer
def cognition_tarin(student):
    """个性化言语训练第二阶段"""
    print(f"→正在为{student}进行第二阶段语言训练："
          "用单词、短语、句子表达需求与描述")
    time.sleep(0.99) #模拟特教真实案例场景
if __name__=="__main__":
    speech_tarin("小红")
    cognition_tarin("芳芳")