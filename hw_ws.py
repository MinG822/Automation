import webbrowser
import os

# 구글드라이브를 열어준다
googledrive_url = 'https://drive.google.com/drive/folders/18Q6JfAhCWV4hlsZ4W6UEPn6C0tqFKb05'
webbrowser.open(googledrive_url)

# hw_ws 폴더에 오늘 차 폴더를 만들고 hw와 ws md 파일들을 만들고 파일을 열어준다
os.chdir('/Users/student/hw_ws/')

for i in range(1,100):
    if not os.path.isdir(str(i).zfill(2)):
        num=str(i).zfill(2)
        os.mkdir(num)
        hw_name=f'{num}_homework'
        ws_name=f'{num}_workshop'
        os.chdir(f'/Users/student/hw_ws/{num}/')
        with open(f'{hw_name}.md', 'w', encoding='utf-8') as f:
            f.write(f'# {num}_homework \n## 01\n')
        with open(f'{ws_name}.md', 'w', encoding='utf-8') as f:
            f.write(f'# {num}_workshop \n## 01\n')
        os.startfile(f'{hw_name}.md')
        os.startfile(f'{ws_name}.md')
        break

