# -*- coding: utf-8 -*-
__author__ = 'lijianming'

'''
模块安装-MAC版本:
pip install pillow     PIL模块
pip install qrcode     二维码模块

参数含义：
version：值为1~40的整数，控制二维码的大小（最小值是1，是个12×12的矩阵）。 如果想让程序自动确定，将值设置为 None 并使用 fit 参数即可。

error_correction：控制二维码的错误纠正功能。可取值下列4个常量。
　　ERROR_CORRECT_L：大约7%或更少的错误能被纠正。
　　ERROR_CORRECT_M（默认）：大约15%或更少的错误能被纠正。
　　ROR_CORRECT_H：大约30%或更少的错误能被纠正。

box_size：控制二维码中每个小格子包含的像素数。

border：控制边框（二维码与图片边界的距离）包含的格子数（默认为4，是相关标准规定的最小值）
'''

import qrcode
import os

#url = 'http://ci.tieba.baidu.com/view/Android客户端/job/Tieba_Android_Gradle_8.6_Release_Branch/88/artifact/gen_apk/tieba.apk'
url = 'http://ci.tieba.baidu.com/view/Android客户端/job/Tieba_Android_Gradle_8.6_Release_Branch/86/artifact/gen_apk/tieba.apk'
output = 'QR.jpeg'

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_M,box_size=10, border=4)
qr.add_data(url)
qr.make(fit=True)
x = qr.make_image()
qr_file = os.path.join(output)
with open(qr_file, 'wb')as f:
    print os.path.splitext(output)[1].replace('.','')
    x.save(f, os.path.splitext(output)[1].replace('.',''))
