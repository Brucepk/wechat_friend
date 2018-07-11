#coding=utf8
import itchat
import matplotlib.pyplot as plt

itchat.auto_login(hotReload=True)
friends=itchat.get_friends(update=True)[0:]  #获取所有好友信息
male = female = other =0
for i in friends[1:]:
    sex=i["Sex"]
    if sex==1:
        male+=1
    elif sex==2:
        female+=1
    else:
        other+=1
total=len(friends[1:])

print("男性好友： %.2f%%" % (float(male)/total*100) + "\n" +
"女性好友： %.2f%%" % (float(female) / total * 100) + "\n" +
"不明性别好友： %.2f%%" % (float(other) / total * 100))

plt.xlabel("sex")
plt.ylabel("count")
plt.title("Gender statistics")
a=plt.subplot(1,1,1)
plt.bar(10, male, facecolor='red', width=3, label='male')
plt.bar(15, female, facecolor='yellow', width=3, label='female')
plt.bar(20, other, facecolor='blue', width=3, label='other')
plt.legend()
plt.show()
