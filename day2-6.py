names=[]
scores=[]
total=0
highest=0
lowest=100
C=int(input('輸入人數'))
for a in range(C):
    A=input('輸入名字')
    B=int(input('輸入分數'))
    names.append(A)
    scores.append(B)
for b in range(C):
    total=total+scores[b]
print(total)
avg=float(total/C)
print(avg)
for c in range(C):
    if scores[c]>highest:
       highest=scores[c]
print(highest)
for d in range(C):
    if scores[d]<lowest:
        lowest=scores[d]
print(lowest)
        

    






