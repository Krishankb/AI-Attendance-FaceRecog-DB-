import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from matplotlib import image
from backend import Database
from facerecog import *

#################################Database code

database = Database()
selected_tuple =None

def get_selected_row(event):
    try:
        global selected_tuple
        index=f1_list1.curselection()[0]
        selected_tuple = f1_list1.get(index)
        f1_e1.delete(0,END)
        f1_e1.insert(END,selected_tuple[1])
        f1_e2.delete(0,END)
        f1_e2.insert(END,selected_tuple[1])
        f1_e3.delete(0,END)
        f1_e3.insert(END,selected_tuple[2])
        f1_e4.delete(0,END)
        f1_e4.insert(END,selected_tuple[3])
        f1_e5.delete(0,END)
        f1_e5.insert(END,selected_tuple[4])
        f1_e6.delete(0,END)
        f1_e6.insert(END,selected_tuple[5])
    except IndexError:
        pass

def view_command():
    f1_list1.delete(0,END)
    for row in database.view():
        f1_list1.insert(END,row)

def tables_command():
    f2_list1.delete(0,END)
    for row in database.tableview():
        f2_list1.insert(END,row)   

def desctable_command():
    f2_list1.delete(0,END)
    for row in database.desctable(f2_table_text.get()):
        f2_list1.insert(END,row)             

def aiview_command():
    f3_list1.delete(0,END)
    for row in database.aisview():
        f3_list1.insert(END,row)

def search_command():
    f1_list1.delete(0,END)
    for row in database.search(f1_name_text.get(),f1_usn_text.get(),f1_gender_text.get(),f1_phone_text.get(),f1_teacher_text.get()):
        f1_list1.insert(END,row)

def add_command():
    database.insert(f1_name_text.get(),f1_usn_text.get(),f1_gender_text.get(),f1_phone_text.get(),f1_teacher_text.get())
    f1_list1.delete(0,END)
    f1_list1.insert(END,(f1_name_text.get(),f1_usn_text.get(),f1_gender_text.get(),f1_phone_text.get(),f1_teacher_text.get()))

def delete_command():
    database.delete(selected_tuple[0])

def update_command():
    database.update(selected_tuple[0],f1_name_text.get(),f1_usn_text.get(),f1_gender_text.get(),f1_phone_text.get(),f1_teacher_text.get())

def webcam_command():
    FaceTools()

#Ends here


window = tk.Tk()
window.wm_title("AI Attendance")
#window.state("zoomed")

def show_frame(frames):
    frames.tkraise()

window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)

frame0 = tk.Frame(window)
frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)

for frame in (frame0,frame1,frame2,frame3):
    frame.grid(row=0,column=0,sticky="nsew")


#############################    FRAME0

#starts here
img0=Image.open("img/frame0.jpg")
img0=img0.resize((1530,710),Image.ANTIALIAS)
photoimg0 = ImageTk.PhotoImage(img0)

f0_lb2 = Label(frame0,image=photoimg0)
f0_lb2.place(x=0,y=0,width=1530,height=710)

title_lab=Label(frame0,text="AI DBMS Attendance",font=("times new roman",45,"bold"),bg="white",fg="red")
title_lab.place(x=0,y=0,width=1530,height=75)


#Studend Button
imggg=Image.open("img/smartAttendance.jpg")
imggg=imggg.resize((220,220),Image.ANTIALIAS)
photoimggg=ImageTk.PhotoImage(imggg)
add_b1=Button(frame0,image=photoimggg,command=lambda:show_frame(frame1),cursor="hand2")
add_b1.place(x=200,y=100,width=220,height=220)


frame0_title_button=Button(frame0,text="Student Info",width=10,command=lambda:show_frame(frame1),cursor="hand2",font=("times new roman",15,"bold"),bg="orange",fg="white")
frame0_title_button.place(x=250,y=330,width=200,height=75)

#Table Button
imgg=Image.open("img/developer.jpg")
imgg=imgg.resize((220,220),Image.ANTIALIAS)
photoimgg=ImageTk.PhotoImage(imgg)

tb_b1=Button(frame0,image=photoimgg,cursor="hand2",command=lambda:show_frame(frame2))
tb_b1.place(x=600,y=100,width=220,height=220)

frame01_title_button=Button(frame0,text="Tables",width=10,command=lambda:show_frame(frame2),cursor="hand2",font=("times new roman",15,"bold"),bg="orange",fg="white")
frame01_title_button.place(x=650,y=330,width=100,height=50)


#AI Button
img5=Image.open("img/img1.jpeg")
img5=img5.resize((220,210),Image.ANTIALIAS)
photoimg5=ImageTk.PhotoImage(img5)

ad_b1=Button(frame0,image=photoimg5,cursor="hand2",command=lambda:show_frame(frame3))
ad_b1.place(x=920,y=100,width=220,height=220)


frame02_title_button=Button(frame0,text="AI",width=10,command=lambda:show_frame(frame3),cursor="hand2",font=("times new roman",15,"bold"),bg="orange",fg="white")
frame02_title_button.place(x=1000,y=330,width=100,height=50)


developer_frame0=Label(frame0,text="Developers",font=("times new roman",25,"bold"),fg="red")
developer_frame0.place(x=600,y=450)

krishan=Label(frame0,text="Krishan K B 1HK19IS040",font=("times new roman",20,"italic"),fg="green")
krishan.place(x=600,y=500)

hussain=Label(frame0,text="Hussainkhan A Jahagirdar 1HK19IS029",font=("times new roman",20,"italic"),fg="green")
hussain.place(x=600,y=550)
#Ends here



#######################    FRAME1

#starts here
img2=Image.open("img/1398323.jpg")
img2=img2.resize((1530,710),Image.ANTIALIAS)
photoimg2 = ImageTk.PhotoImage(img2)

f1_lb2 = Label(frame1,image=photoimg2)
f1_lb2.place(x=0,y=0,width=1530,height=710)

#frame1_title = tk.Label(frame1,text="This is frame1",bg="red")
#frame1_title.pack(fill="x")


f1_l1 = Label(frame1,text = "Table Name",font=("times new roman",20,"bold"),fg="red")
f1_l1.place(x=20,y=80,width=150,height=50)

f1_l2 = Label(frame1,text= "Name",font=("times new roman",20,"bold"),fg="red")
f1_l2.place(x=20,y=160,width=150,height=50)

f1_l3 = Label(frame1,text= "USN",font=("times new roman",20,"bold"),fg="red")
f1_l3.place(x=360,y=160,width=150,height=50)

f1_l4 = Label(frame1,text= "Gender",font=("times new roman",20,"bold"),fg="red")
f1_l4.place(x=20,y=240,width=120,height=50)

f1_l5 = Label(frame1,text= "phone",font=("times new roman",20,"bold"),fg="red")
f1_l5.place(x=350,y=240,width=120,height=50)

f1_l6 = Label(frame1,text= "Teacher",font=("times new roman",20,"bold"),fg="red")
f1_l6.place(x=680,y=240,width=120,height=50)


f1_table_text = StringVar()
f1_e1= Entry(frame1,textvariable=f1_table_text)
f1_e1.place(x=180,y=80,width=150,height=50)

f1_name_text = StringVar()
f1_e2= Entry(frame1,textvariable=f1_name_text)
f1_e2.place(x=180,y=160,width=150,height=50)

f1_usn_text = StringVar()
f1_e3= Entry(frame1,textvariable=f1_usn_text)
f1_e3.place(x=520,y=160,width=150,height=50)

f1_gender_text = StringVar()
f1_e4= Entry(frame1,textvariable=f1_gender_text)
f1_e4.place(x=150,y=240,width=150,height=50)

f1_phone_text = StringVar()
f1_e5= Entry(frame1,textvariable=f1_phone_text)
f1_e5.place(x=480,y=240,width=150,height=50)

f1_teacher_text = StringVar()
f1_e6= Entry(frame1,textvariable=f1_teacher_text)
f1_e6.place(x=810,y=240,width=150,height=50)

f1_list1= Listbox(frame1)
f1_list1.place(x=90,y=350,width=600,height=300)

f1_sb1=Scrollbar(frame1)
f1_sb1.place(x=780,y=400,width=20,height=200)

f1_list1.configure(yscrollcommand=f1_sb1.set)
f1_sb1.configure(command=f1_list1.yview)

f1_sb2=Scrollbar(frame1,orient='horizontal')
f1_sb2.place(x=300,y=315,width=200)

f1_list1.configure(xscrollcommand=f1_sb2.set)
f1_sb2.configure(command=f1_list1.xview)

f1_list1.bind('<<ListboxSelect>>',get_selected_row)

f1_b1=Button(frame1,text="View All",cursor="hand2",font=("times new roman",15,"bold"),bg="orange",fg="white",command=view_command)
f1_b1.place(x=1030,y=39,width=150,height=50)

f1_b2=Button(frame1,text="Search Entry",cursor="hand2",font=("times new roman",15,"bold"),bg="orange",fg="white",command=search_command)
f1_b2.place(x=1030,y=100,width=150,height=50)

f1_b3=Button(frame1,text="Add Entry",cursor="hand2",font=("times new roman",15,"bold"),bg="orange",fg="white",command=add_command)
f1_b3.place(x=1030,y=160,width=150,height=50)

f1_b4=Button(frame1,text="Update Entry",cursor="hand2",font=("times new roman",15,"bold"),bg="orange",fg="white",command=update_command)
f1_b4.place(x=1030,y=220,width=150,height=50)

f1_b5=Button(frame1,text="Delete Entry",cursor="hand2",font=("times new roman",15,"bold"),bg="orange",fg="white",command=delete_command)
f1_b5.place(x=1030,y=280,width=150,height=50)

f1_b6=Button(frame1,text="close",cursor="hand2",font=("times new roman",15,"bold"),bg="Red",fg="white",command=window.destroy)
f1_b6.place(x=1030,y=360,width=150,height=50)

frame1_title_button=Button(frame1,text="Table Struc",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white",command=lambda:show_frame(frame2))
frame1_title_button.place(x=1030,y=420,width=150,height=50)

frame1_home_button=Button(frame1,text="Home",cursor="hand2",font=("times new roman",15,"bold"),bg="green",fg="white",command=lambda:show_frame(frame0))
frame1_home_button.place(x=1030,y=559,width=150,height=50)

#ends here

#############################    FRAME2

img3=Image.open("img/wallpaper2.jpg")
img3=img3.resize((1530,710),Image.ANTIALIAS)
photoimg3 = ImageTk.PhotoImage(img3)

f2_lb2 = Label(frame2,image=photoimg3)
f2_lb2.place(x=0,y=0,width=1530,height=710)

frame2_title = tk.Label(frame2,text="This is frame2",bg="yellow")
frame2_title.pack(fill="x")
frame2_title_button=Button(frame2,text="GOto",width=10,command=lambda:show_frame(frame1))
frame2_title_button.pack(fill="x")

f2_b1=Button(frame2,text="Tables",cursor="hand2",font=("times new roman",15,"bold"),bg="orange",fg="white",command=tables_command)
f2_b1.place(x=80,y=80,width=150,height=50)

f2_b2=Button(frame2,text="Description",cursor="hand2",font=("times new roman",15,"bold"),bg="orange",fg="white",command=desctable_command)
f2_b2.place(x=300,y=80,width=150,height=50)

f2_table_text = StringVar()
f2_e2= Entry(frame2,textvariable=f2_table_text)
f2_e2.place(x=470,y=80,width=150,height=50)

f2_list1= Listbox(frame2,width=150,height=60)
f2_list1.place(x=30,y=350)

f2_list1.bind('<<ListboxSelect>>',get_selected_row)

#frame2_title_button.grid(row=8,column=3)
#ends here

############################# Frame3

#starts here
img4=Image.open("img/wallpaper31.jpg")
img4=img4.resize((1530,710),Image.ANTIALIAS)
photoimg4 = ImageTk.PhotoImage(img4)

f3_lb2 = Label(frame3,image=photoimg4)
f3_lb2.place(x=0,y=0,width=1530,height=710)

f3_b1=Button(frame3,text="Training",cursor="hand2",font=("times new roman",15,"bold"),bg="orange",fg="white")
f3_b1.place(x=50,y=50,width=110,height=40)

f3_b2=Button(frame3,text="Webcam",cursor="hand2",font=("times new roman",15,"bold"),bg="orange",fg="white",command=webcam_command)
f3_b2.place(x=170,y=50,width=110,height=40)

f3_b3=Button(frame3,text="Screen Capture",cursor="hand2",font=("times new roman",15,"bold"),bg="orange",fg="white")
f3_b3.place(x=290,y=50,width=165,height=40)

f3_b4=Button(frame3,text="Display",cursor="hand2",font=("times new roman",15,"bold"),bg="orange",fg="white",command=aiview_command)
f3_b4.place(x=150,y=250,width=110,height=40)

f3_list1= Listbox(frame3)
f3_list1.place(x=30,y=350,width=550,height=240)

f3_list1.bind('<<ListboxSelect>>',get_selected_row)



#ends here


show_frame(frame0)

window.mainloop()