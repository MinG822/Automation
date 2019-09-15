import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from datetime import datetime as dt
from decouple import config
import os

naver_server = smtplib.SMTP_SSL('smtp.naver.com',456)
naver_server.login(config('NAVER_ID'),config('NAVER_SECRET'))


msg = MIMEBase('multipart','mixed')
cont=MIMEText('예압','plain','utf-8')

cont['Subject']='test메일'
cont['From']=config('NAVER_ID')
cont['To']=config('NAVER_ID')
msg.attach(cont)

fname="서울1반{}월{}일김민지".format(dt.now().month, dt.now().day)
filename='C:\\Users\\student\\algorithm\\{}.zip'.format(fname)

path = r'C://Users//student//algorithm//{}'.format(filename)
part = MIMEBase("application",'octest-stream')
part.set_payload(open(path,'rb').read())

encoders.encode_base64(part)
part.add_header('Content-Disposition','attachment; filename={}'.format(os.path.basename(path)))
msg.attach(part)
naver_server.sendmail(config('NAVER_ID'),config('NAVER_ID'),msg.as_string())
naver_server.quit()
