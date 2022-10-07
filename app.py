from distutils.log import info
from tkinter import *
import joblib

# RESET FUNCTION FOR RESETING VALUES AND HIDDING THE RESULT
def reset_values():
    if p_1.get()=="" and p_2.get()=="" and p_3.get()=="" and p_4.get()=="" and p_5.get()=="" and p_6.get()=="":
        reset_button.place(x=280,y=440)
    else:
        p_1.set("")
        p_2.set("")
        p_3.set("")
        p_4.set("")
        p_5.set("")
        p_6.set("")
        label_10.pack_forget() # HIDDING THE RESULT
        reset_button.place(x=280,y=440)
def show_entry():
    p1 = float(e1.get())
    p2 = float(e2.get())
    p3 = float(e3.get())
    p4 = float(e4.get())
    p5 = float(e5.get())
    p6 = float(e6.get())
    global label_10 # TO ACCESS THE LABEL OUTSIDE THE FUNCTION
    string = "" # TO STORE THE RESULT IN STRING FORMAT
    model = joblib.load('model1_joblib_gr')
    result = model.predict([[p1,p2,p3,p4,p5,p6]])
    result = list(result.astype(int)) # CONVERTING THE RESULT INTO LIST
    for i in result: # ITERATING THE LIST TO GET STRING OF THE LIST
        string+= str(i) #TYPE CASTING THE LIST INTO STRING

    label_10 = Label(master,text="$ {}".format(string),font=("bold", 15),bg="white") # FORMATING THE RESULT
    label_10.pack(side=BOTTOM)
    
    
    
   
master = Tk()
master.geometry('500x560')
master.configure(bg="light green")
master.title("Health Insaurance Prediction")
# VARIABLES USED FOR RESET FUNCTION
global p_1
global p_2
global p_3
global p_4
global p_5
global p_6

# TEXTVARIABLE STORE ONLY STRING VALUES
p_1 = StringVar()
p_2 = StringVar()
p_3 = StringVar()
p_4 = StringVar()
p_5 = StringVar()
p_6 = StringVar()

label_0 = Label(master, text="Health Insaurance Prediction",font=("bold", 20),justify = "center", bg = "white", fg = "black").place(x=80,y=10)

label_1 = Label(master, text="Enter Age",font=("bold", 10),bg="light green").place(x=50,y=80)
e1 = Entry(master, width=50, textvariable = p_1)
e1.place(x=50,y=110)

label_2 = Label(master, text="Enter Male Or Female [1/0]",font=("bold", 10),bg="light green").place(x=50,y=140)
e2 = Entry(master, width=50, textvariable = p_2)
e2.place(x=50,y=170)

label_3 = Label(master, text="Enter BMI Value",font=("bold", 10),bg="light green").place(x=50,y=200)
e3 = Entry(master, width=50, textvariable = p_3)
e3.place(x=50,y=230)

label_4 = Label(master, text="Enter No. of Children",font=("bold", 10),bg="light green").place(x=50,y=260)
e4 = Entry(master, width=50, textvariable = p_4)
e4.place(x=50,y=290)

label_5 = Label(master, text="Enter Smoker Yes/No [1/0]",font=("bold", 10),bg="light green").place(x=50,y=320)
e5 = Entry(master, width=50, textvariable = p_5)
e5.place(x=50,y=350)

label_6 = Label(master, text="Enter Region southwest, southeast, northwest, northeast [1/2/3/4] ",font=("bold", 10),bg="light green").place(x=50,y=380)
e6 = Entry(master, width=50, textvariable = p_6)
e6.place(x=50,y=410)

Button(master, text='Predict',width=15,bg='white',fg='black', command = show_entry).place(x=90,y=440)

reset_button = Button(master, text='Reset',width=15,bg='white',fg='black', command = reset_values)
reset_button.place(x=280,y=440)

label_9 = Label(master, text="Predicted Insurance Cost",font=("bold", 15),bg="light green")
label_9.pack(side=BOTTOM)

master.mainloop()
