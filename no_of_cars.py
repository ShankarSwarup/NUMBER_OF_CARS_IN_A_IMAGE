from tkinter import * 
from tkinter import filedialog as fd
import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

class cars:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x500+200+50")
        self.root.title("NO OF CARS")
        self.root.resizable(False, False)

        self.download_path = StringVar()

        title = Label(self.root, text="NUMBER OF CARS", font=("times new roman", 40), bg='#053246',
                      fg='white').place(x=0, y=0, relwidth=1)

        lbl_location=Label(self.root,text='Pick a Location',font=("times new roman",15),bg='white').place(x=10,y=100)
        txt_location=Entry(self.root,textvariable=self.download_path,font=("times new roman",13),bg="#d9fcff").place(x=260,y=100,width=340,height=30)


        btn_dir = Button(self.root, text='Choose File', command=self.Browse, font=("times new roman", 13, 'bold'), bg='#607d8b',
                         fg='white').place(x=640, y=100, width=150, height=20)

        btn_check = Button(self.root, text='Check', command=self.check, font=("times new roman", 13, 'bold'), bg='black',
                         fg='white').place(x=300, y=160, width=150, height=20)

        self.lbl_res=Label(self.root,text='',font=("times new roman",18),bg='white')
        self.lbl_res.place(x=270,y=220)



    def Browse(self):
        download_Directory = fd.askopenfilename(initialdir="YOUR DIRECTORY PATH")
        self.download_path.set(download_Directory)

    def check(self):
        im=cv2.imread(self.download_path.get())
        bbox,label,conf=cv.detect_common_objects(im)
        self.lbl_res.config(text=f'Number of cars in the image are '+str(label.count('car')),fg='green')



root=Tk()
obj=cars(root)
root.mainloop()