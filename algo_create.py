import webbrowser
from datetime import datetime as dt
import os, subprocess, threading
import subprocess

# 알고리즘폴더에 오늘치 제출 폴더를 만들어주기
os.chdir('/Users/student/algorithm/')
foldername="서울1반{}월{}일김민지".format(dt.now().month, dt.now().day)

#해당 폴더 내에 문제파일 4개 만들기
os.mkdir(foldername)
os.chdir('/Users/student/algorithm/{}'.format(foldername))
for i in range(1,5):
    with open('{}.py'.format(i), 'w', encoding='utf-8') as f:
        f.write('#{}'.format(i))
    
# 파일 참으로 문제 파일 실행하기
os.chdir('\\Program Files\\JetBrains\\PyCharm Community Edition 2018.2.3\\bin\\')
subprocess.run(['pycharm.exe', '/Users/student/algorithm/{}'.format(foldername)])
