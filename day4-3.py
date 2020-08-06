import os.path
if os.path.isfile('成績表.txt'):
    print('此檔案存在')
else:
    print('查無此檔案')
不知道是啥={}
print('歡迎來到奇怪成績系統')
while True:
    print('1.登錄成績')
    print('2.列出所有成績')
    print('3.查詢成績')
    print('4.close')
    功能=input('請選擇功能:')
    if 功能=='1':
        英文=input('輸入人名:')
        中文=input('輸入成績:')
        不知道是啥[英文]=中文
        fo=open('成績表.txt','w')
        fo.write(英文)
        fo.write(':')
        fo.write(中文)
        fo.close
    if 功能=='2':
        print(不知道是啥)
    if 功能=='3':
        啥大=input('輸入要查詢的人名:')
        print(不知道是啥[啥大])
    if 功能=='4':
        print('離開')
        break