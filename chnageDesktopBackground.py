import os
import random

# path to the desktop background images
imgPath = '/home/user/Pictures/wallpapers'

filelist= [file for file in os.listdir('/home/user/Pictures/wallpapers') if file.endswith('.png') or file.endswith('.jpg')]
img = random.choice(filelist)

# Current background image
currentImg = os.system("gsettings get org.gnome.desktop.background picture")

# Set new background image
os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/user/Pictures/wallpapers/"+img)
