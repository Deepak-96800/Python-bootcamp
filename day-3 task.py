from tkinter import *

window=Tk()
window.title("Registration form")
window.geometry("600x500")
window.configure(background="lightblue")

firstname=Label(window,text="First Name").grid(row=0,column=0)
lastname=Label(window,text="Last Name").grid(row=1,column=0)
email=Label(window,text="Email ID").grid(row=2,column=0)
college=Label(window,text="College").grid(row=3,column=0)
address=Label(window,text="Address").grid(row=4,column=0)
mobile=Label(window,text="Mobile Number").grid(row=5,column=0)
Country =Label(window,text = "Country").grid(row = 7,column = 0)
list1 = ['Canada','India','UK','Nepal','Iceland','South Africa']
c=StringVar()
droplist=OptionMenu(window,c, *list1)
droplist.config(width=15)
c.set('select your country')
droplist.grid(row=7,column=1)

var1=IntVar()

Checkbutton(window,text="Accept Terms and Condition", variable=var1).grid(row=8,column=1)

Gender =Label(window ,text = "Gender",width=20,font=("bold", 10)).grid(row=6,column=0)
var = IntVar()
Radiobutton(window, text="Male",padx = 30, variable=var, value=1).grid(row=6,column=1)
Radiobutton(window, text="Female",padx = 20, variable=var, value=2).grid(row=6,column=2)


firstname1=Entry(window).grid(row=0,column=1)
lastname1=Entry(window).grid(row=1,column=1)
email1=Entry(window).grid(row=2,column=1)
college1=Entry(window).grid(row=3,column=1)
address1=Entry(window).grid(row=4,column=1)
mobile1=Entry(window).grid(row=5,column=1)



Button(window, text="Submit", width=10,bg='brown',fg='white').grid(row =11,column =2)

window.mainloop()