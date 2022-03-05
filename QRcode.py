# -*- coding: utf-8 -*-
"""

This is a simple program which create a qrcode that gives access to
the link to my linkedIn account.
"""

"""
first we need to install some modules
Pillow => pip install pillow
qrcode => pip install qrcode
opencv-python => pip install opencv-python
"""

import cv2 as cv  # from opencv-python
import qrcode

""" create the QRCode
"""

# qr => an empty QRcode , parameter=> %of information that can be recover after damage
qr = qrcode.QRCode(version = 3,
    error_correction= qrcode.constants.ERROR_CORRECT_H,
    box_size = 3,
    border = 5
    )
# we add data to our qrcode
qr.add_data(["https://www.linkedin.com/in/yvana-patricia-tchamgoue-7617991bb/"])

# we add some color and background, we can add more properties to our qrcode, as a logo... 
img = qr.make_image(fill_color="purple",back_color = "white")
# save our qrcode by specifying its name
img.save("mon_qrcode.png")


""" read the qrcode
"""
image = cv.imread("mon_qrcode.png") # ouvrir la photo du qrcode
detecteur = cv.QRCodeDetector() # permet de detecter et scanner le qrcode
# put the data of the qrcode uin 'valeur' an print it.
valeur, point, qr= detecteur.detectAndDecode(image)
print(valeur)
