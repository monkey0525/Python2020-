def shit (總分,人數):
    return 總分/人數
人數=input("有幾人:")
人數=int(人數)
成績表=[]
總分=0
for 第幾個 in range (人數):
    分數=input("輸入分數:")
    分數=int(分數)
    成績表.append(分數)
for 分數 in 成績表 :
    總分=總分+分數
平均=0
平均=總分/(人數)
print("平均分數:",平均)
shit(總分,人數)