import os, zipfile
from datetime import datetime as dt
foldername="서울1반{}월{}일김민지".format(dt.now().month, dt.now().day)
src = r'C://Users/student/algorithm//{}'.format(foldername)

my_zip = zipfile.ZipFile('C:\\Users\\student\\algorithm\\{}.zip'.format(foldername), 'w')
my_zip.write('C:\\Users\\student\\algorithm\\{}'.format(foldername), compress_type=zipfile.ZIP_DEFLATED)
my_zip.close()