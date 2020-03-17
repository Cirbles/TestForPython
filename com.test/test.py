# -*- coding: utf-8 -*-
# message = 'hello horld!'
# print(message)
# print(message.upper())
# print(message.upper().lower())
# print(message.find('!'))
# print(message.replace('!','?'))
# print(message.title())
# print(message.upper())
# print(message.lower())

# firstName = "abc"
# lastName = "lovelac"
# fullName = firstName + " " + lastName
# # print(fullName)
# print('hello,' + fullName.title() + "!!!")

# print('\tpython')
# print("\n2020年"
#       +"\n\t3月13日"
#       +"\n\t\t16:56:24")

# favorit_language = ' python  '
# 删除末尾的空格
# favorit_language = favorit_language.rstrip()
# 删除头部的空格
# favorit_language = favorit_language.lstrip()
# 删除两头的空格
# favorit_language = favorit_language.strip()
# print(favorit_language)

# a = " abc "
# print(a.rstrip())
# print(a.lstrip())
# print(a.strip())

# messages = "he's a dog"
# rs = ""
# target_list = ""
# # print(messages.__len__())
# for target_list in messages:
#     if target_list != " ":
#         rs += target_list
#     else:
#         pass
# print(rs)
# print(messages.replace(" ",""))

# age = 30
# print("happy" + str(age) + "rd birthday")
bicycles = ['trek','redline','cannondale','redline', 'redline', 'specialized']
# print(bicycles)
# print(bicycles[0])
# for bicycle in bicycles:
#     print(bicycle.title())
# print("我的第一辆车子是"+bicycles[0].title()+"。")
# bicycles[0] = "bus"
# bicycles.append("bike")
# print(bicycles)
# bicycles.insert(1,"zhangsan")
print(bicycles)
# del bicycles[1]
# print(bicycles)
# popVlue = bicycles.pop(2)
# print(bicycles)
# print(popVlue)
bicycles.remove('redline')
print(bicycles)