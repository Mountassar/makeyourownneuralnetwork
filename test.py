from shutil import copy2
import cv2
import os, sys
from PIL import ImageTk, Image, ImageDraw, ImageOps
import PIL
from tkinter import *

width = 150
height = 150
center = height//2
white = (255, 255, 255)
green = (0,128,0)
label=str(input("digit to predict"))

def save():
    #filename = ("2828_my_own_"+str(label))
    image1.save("2828_my_own_{}.png".format(label))
    image = PIL.Image.open("2828_my_own_{}.png".format(label))
    #Scale the image down to the thumbnail size.
    image = ImageOps.fit(image, (28, 28))
    image.save("2828_my_own_{}.png".format(label))
    src=("C:/Users/Newip-Woll/Desktop/Character Recognition Machine Learning Projects/Dirk Code Book/Source code for Dirk's Book/2828_my_own_{}.png".format(label))
    dest=("C:/Users/Newip-Woll/Desktop/Character Recognition Machine Learning Projects/Dirk Code Book/Source code for Dirk's Book/my_own_images".format(label))
    copy2(src,dest)    
    print('Generated thumbnail: {}'.format(dest))
    print("output:"+dest)

def paint(event):
    # python_green = "#476042"
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    cv.create_oval(x1, y1, x2, y2, fill="black",width=20)
    draw.line([x1, y1, x2, y2],fill="black",width=20)

root = Tk()

# Tkinter create a canvas to draw on
cv = Canvas(root, width=width, height=height, bg='white')
cv.pack()

# PIL create an empty image and draw object to draw on
# memory only, not visible
image1 = PIL.Image.new("RGB", (width, height), white)
draw = ImageDraw.Draw(image1)

# do the Tkinter canvas drawings (visible)
# cv.create_line([0, center, width, center], fill='green')

cv.pack(expand=YES, fill=BOTH)
cv.bind("<B1-Motion>", paint)

# do the PIL image/draw (in memory) drawings
# draw.line([0, center, width, center], green)

# PIL image can be saved as .png .jpg .gif or .bmp file (among others)
# filename = "my_drawing.png"
# image1.save(filename)
button=Button(text="save",command=save)
button.pack()
root.mainloop()
