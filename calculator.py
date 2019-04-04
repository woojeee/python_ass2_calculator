import module
import sys


while True:
    cal_select = int(
        input("1: add\n2: sub\n3: multiply\n4: divide\n5: stop\n:"))

    if cal_select <= 0 or cal_select > 5:
        print('주어진대로만 입력합니다 실시')
        continue

    if cal_select == 5:
        exit()

    num1 = int(input("num1:"))
    num2 = int(input("num2:"))
    numset = module.Calculator(num1, num2)

    if cal_select == 1:
        print(numset.add())
    elif cal_select == 2:
        print(numset.sub())
    elif cal_select == 3:
        print(numset.mul())
    else:
        if numset.b == 0:
            print("문송은 대가리 박는다 실시")
            continue
        else:
            print(numset.div())
    print("\n\n")
