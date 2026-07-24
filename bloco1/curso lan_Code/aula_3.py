import time, random, qrcode
img = qrcode.make('https://youtube.com/@lan_code')
img.save('qr_canal.png')