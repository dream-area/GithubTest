import random


chose = 0
cardhero = ('关羽','赵云','马超','诸葛亮','曹操','刘备','颜良','文丑','夏侯惇','典韦','夏侯渊','吕布','黄忠')
# 13 heroes
#print(cardhero)

backage = list()


while chose != 4:
    print("充值使你变得更加强大！")
    print("请选择指令：")
    print("1.抽卡")
    print("2.查看背包")
    print("3.整理背包")
    print("4.离开")
    chose = int(input())
    if chose not in range(1,5):
    	print('请重新输入有效选择指令！！')
    	continue
    if chose == 1:
        chose_num = int(input('请输入抽卡次数:'))
        for i in range(0,chose_num):
            chose_rand = random.randint(0,12)
            backage.append(cardhero[chose_rand])
            print("您抽到了英雄卡：{}。".format(backage[-1]))
    if chose ==2 :
        print("您的背包：",backage)
    if chose ==3 :
    	backage.sort()
    	print("经过整理后，您的背包：",backage)
    if chose ==4 :
    	continue
print('游戏结束！！')
print("您的背包：",backage)


