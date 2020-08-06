import os.path

if os.path.isfile('這啥.txt'):
    print('此檔案存在')
else:
    print('查無此檔案')
    
fo=open('這啥.txt','w')
fo.write('shit')
fo.close
