# -*- coding: utf-8 -*-
names = ['张三','李四','王麻子','隔壁老王','小明','小红']
# for name in names:
#     print(name + ",周末来我家吃饭哈。")
# print("李四由于个人原因无法来了")
# names.insert(1,"小明")
# for name in names:
#     print(name + ",周末来我家吃饭哈。")
# say = '我只能邀请两位嘉宾共进晚餐的消息'
# print(say)
for name in names:
    names.pop()
    if names.__len__() < 3:
        break
# print(names)

n = names.__len__()
i = 0;
while n > 0:
    del names[-1]
    n = names.__len__()
    i = i + 1
    if i == 2:
        break
# print(names)
names.insert(1,"xiaoli")
# print(names)
names.insert(1,"xiaowu")
# print(names)
names.append("xiaofang")
print(names)

# names.sort(reverse=False)
# print(sorted(names,reverse=True))
names.reverse()
print(names)
names.reverse()
print(names)
