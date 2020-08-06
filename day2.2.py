A=int(input('輸入一正整數'))
B=2
while B<A:
    if A%B==0:
        print('是合數')
        break
    B=B+1
if B==A:
    print('是質數')
    
            
            