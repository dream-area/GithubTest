import sys


def calculator(num):
    """计算税后薪资的函数，参数为原始收入"""

    # 应纳税所得额为收入减5000
    shouldPay = num - 5000

    # 用条件判断语句，根据扣税表写出不同薪资的扣税公式
    if shouldPay <= 0:
        tax = 0
    elif 0 < shouldPay <= 3000:
        tax = shouldPay * 0.03
    elif 3000 < shouldPay <= 12000:
        tax = 3000 * 0.03 + (shouldPay-3000) * 0.10
    elif 12000 < shouldPay <= 25000:
        tax = 3000 * 0.03 + 9000 * 0.10 + (shouldPay-12000) * 0.20
    elif 25000 < shouldPay <= 35000:
        tax = 3000 * 0.03 + 9000 * 0.10 + 13000*0.20 + (shouldPay-25000) * 0.25
    elif 35000 < shouldPay <= 55000:
        tax = 3000 * 0.03 + 9000 * 0.10 + 13000*0.20 + 10000*0.25 +(shouldPay-35000) * 0.30
    elif 55000 < shouldPay <= 80000:
        tax = 3000 * 0.03 + 9000 * 0.10 + 13000*0.20 + 10000*0.25 + 20000*0.30 +(shouldPay-55000) * 0.35
    else:
        tax = 3000 * 0.03 + 9000 * 0.10 + 13000*0.20 + 10000*0.25 + 20000*0.30 + 25000 * 0.35 + (shouldPay-55000) * 0.45

    # 下面的请你补充


    # 最终收入为税前收入减去税款，并保留两位小数
    salary = num - tax


    # 返回最终收入
    
    #return salary
    return '{:.2f}'.format(salary)

#print('你的税后收入是：{:.2f}'.format(calculator(income)))


if __name__ == "__main__":
    for item in sys.argv[1:]:
        id , income = item.split(':')
        try:
            income = int(income)
        except ValueError:
            print('{}:请在薪资的位置输入数字'.format(id))
            continue
        print('{}:{}'.format(id,calculator(income)))