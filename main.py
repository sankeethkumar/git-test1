# class student:
#
#     def __init__(self,name,standard,marks):
#         self.name=name
#         self.standard=standard
#         self.marks=marks
#
#
# student1=student("sankeeth",10,933)
# student2=student("ramesh",10,944)
# print(student1.name)
# print(student2.name)

# from Question import Question
#
# Question_prompts=[
#      "what color are apples?\n(a) Red/Green\n (b) Purple\n (c) orange \n\n",
#      "what color are banans?\n(a) teal\n(b) mangenta\n (c) yellow\n\n",
#      "what color are strawberries?\n (a) yellow\n (b) red\n (c)blue\n\n"
# ]
# questions=[
#     Question(question_prompts[0], "a"),
#     Question(question_prompts[1], "c"),
#     Question(question_prompts[2], "b"),
# ]
#
# def run_test(questions):
#      score=0
#      for question in questions:
#          answer = input(question.prompt)
#          if answer == question.answer:
#              score+= 1
#      print("you got  " + str(score) + "/" + str(len(questions)) + "correct")
#
# run_test(questions)


                 #inheritance

from Chef import Chef
from ChineseChef  import ChineseChef

myChef = Chef()
myChef.make_special_dish()

myChineseChef=ChineseChef()
myChineseChef.make_special_dish()