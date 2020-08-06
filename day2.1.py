import random
A=random.randint(1,20)
T=0
while True:
    B=input('輸入一1~20之數字')
    B=int(B)
    if A==B:
        print('right')
        break
    elif B>20or B<1:
        print('輸入錯誤')
    elif B>A:
        print('太大')
    else:
        print('太小')
    T=T+1
    if T==5:
        break
    else:
        continue





