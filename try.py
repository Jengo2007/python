x=0
while x==0:
    try:
        num=int(input())
        num+=5
        print(num)
    except ValueError:
        print("Введите число")
    finally:
        print("finally")