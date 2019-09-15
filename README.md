# Automation

​	반복되는 작지만 귀찮은 일들을 자동화하는 파이썬 코드를 업로드한 리포이다. 3.7에서만 지원하는 f string 가 포함되어있으며 외부 라이브러리들이 설치되어있어야하며, 본인 상황에 맞게 경로와 폴더 이름를 설정해 주어야한다.

## 1. hw_ws.py

​	구글 드라이브에 올려둔 숙제 pdf를 확인하고, `/Users/student/hw_ws/`경로에 해당 회차 (ex 05) 를 이름으로 하는 폴더를 만들고, 폴더 내에 hw.md 와 ws.md파일을 만들고 그 파일들을 열어주는 코드. algo시리즈는 아직 검토 중이다.

## 2. algo_create.py

​	`/Users/student/algorithm/` 경로에 오늘 날짜로 `서울1반{}월{}일김민지` 폴더를 만들어 주며 해당 폴더 내에 문제 파일 4개(1.py, 2.py, 3.py, 4.py)를 만들고 파일 참으로 문제 파일을 실행해준다. 

## 3. algo_zip.py

​	algo_create로 만들어진 폴더를 압축시켜주는 코드. zipfile 라이브러리의 ZipFile함수를 사용했다.

## 4. algo_mail.py

​	smtplib라이브러리를 이용해 naver서버에 로그인하고,  email.mime.base의 MIMEBase와 email.mime.mime.text의 MIMEText로 메일을 작성하고 algo_zip.py로 압축한 파일을 첨부해 메일을 보내주는 코드.