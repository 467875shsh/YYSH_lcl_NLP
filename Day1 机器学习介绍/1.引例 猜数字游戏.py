import random

x = random.randint(0,100)
i = 1;
while(i < 6):
    print("请输入一个数字")
    y = int(input())
    if(y > x):
        print("输入的数字大于目标数字")
        if(5 - i == 0):
            print("很遗憾，您没有猜对")
            print(f"游戏结束,答案是：{x}")
        print(f"这是第{i}次猜测，您还有{5-i}次机会")
    elif(y < x):
        print("输入的数字小于目标数字")
        if(5 - i == 0):
            print("很遗憾，您没有猜对")
            print(f"游戏结束,答案是：{x}")
        print(f"这是第{i}次猜测，您还有{5-i}次机会")
    else:
        print(f"这是第{i}次猜测,恭喜你，猜对了")
        break
    i += 1
