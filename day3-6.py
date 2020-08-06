不知道是啥={}
print('歡迎來到要自己輸入的奇怪英文字典')
while True:
    print('1.建立詞彙')
    print('2.列出所有單字')
    print('3.英翻中')
    print('4.中翻英')
    print('5.close')
    功能=input('請選擇功能:')
    if 功能=='1':
        英文=input('輸入英文:')
        中文=input('輸入中文:')
        不知道是啥[英文]=中文
    if 功能=='2':
        print(不知道是啥)
    if 功能=='3':
        啥大=input('輸入要翻譯的英文:')
        print(不知道是啥[啥大])
    if 功能=='4':
        啥小=input('輸入要翻譯的中文:')
        for key,value in 不知道是啥.items():
            if value==啥小:
                print(key)    
    if 功能=='5':
        print('離開')
        break
   