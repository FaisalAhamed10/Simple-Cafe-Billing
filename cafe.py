import customtkinter
from tkinter import *
from tkinter import messagebox
from datetime import date

app = customtkinter.CTk()
app.title('Modern Cafe')
app.geometry('1209x768+50+50')
app.resizable(0,0)
app.config(bg="brown4")

price_list = [50, 40, 30, 30, 40, 50]
total_price = 0

bill_frame = customtkinter.CTkFrame(app, width=520, height=800, fg_color="#545457")
bill_frame.place(x=700, y=0)

menu_label = customtkinter.CTkLabel(app, text="Modern Cafe", font=('glazier', 29, 'bold'), text_color="#FFFFFF", bg_color="#8B2323")
menu_label.place(x=230, y=5)

img1 = PhotoImage(file=r"cafe latte.png")
img2 = PhotoImage(file=r"iced coffee.png")
img3 = PhotoImage(file=r"cold brew.png")
img4 = PhotoImage(file=r"coffee mocha.png")
img5 = PhotoImage(file=r"cortado.png")
img6 = PhotoImage(file=r"flat white.png")
def pay():
    global total_price
    if(customer_entry.get()==''):
        messagebox.showwarning(title="Error",message="please enter your name.")
    else:
        total_price=int(quntity1_combobox.get())*price_list[0]+int(quntity2_combobox.get())*price_list[1]+int(quntity3_combobox.get())*price_list[2]+int(quntity4_combobox.get())*price_list[3]+int(quntity5_combobox.get())*price_list[4]+int(quntity6_combobox.get())*price_list[5]
        if(total_price==0):
            messagebox.showwarning(title="Error",message="please select some dishes.")
        else:
            name_label=customtkinter.CTkLabel(bill_frame,text=f'Customer Name: {customer_entry.get()}',font=('glazier', 18, 'bold'),bg_color="#8B2323",width=550,height=50)
            name_label.place(x=0,y=100)
            price_label = customtkinter.CTkLabel(bill_frame, text=f'Total Price: {total_price}$',font=('glazier', 18, 'bold'), bg_color="#8B2323", width=550,height=50)
            price_label.place(x=0, y=200)
            date_label = customtkinter.CTkLabel(bill_frame, text=f'Bill Date: {date.today()}',font=('glazier', 18, 'bold'), bg_color="#8B2323", width=550,height=50)
            date_label.place(x=0, y=300)

def new():
    customer_entry.delete(0,END)
    quntity1_combobox.set(0)
    quntity2_combobox.set(0)
    quntity3_combobox.set(0)
    quntity4_combobox.set(0)
    quntity5_combobox.set(0)
    quntity6_combobox.set(0)

def save():
    f=open(f'{customer_entry.get()}Bill',"w")
    f.write(f'Customer Name: {customer_entry.get()}\n')
    f.write(f'Total Price: {total_price} $\n')
    f.write(f'Bill Date: {date.today()}')
    messagebox.showwarning(title="saved",message="Bill has been saved. ")

img1_label=customtkinter.CTkLabel(app, image=img1,text="cafe latte\n price: 50$",font=('glazier', 15, 'bold'),text_color="#FFFFFF",fg_color="#090b17",width=200,height=200,corner_radius=20,compound=TOP,anchor=N)
img1_label.place(x=30,y=70)

img2_label=customtkinter.CTkLabel(app, image=img2,text="iced coffee\n price: 40$",font=('glazier', 15, 'bold'),text_color="#FFFFFF",fg_color="#090b17",width=200,height=200,corner_radius=20,compound=TOP,anchor=N)
img2_label.place(x=250,y=70)

img3_label=customtkinter.CTkLabel(app, image=img3,text="cold brew\n price: 30$",font=('glazier', 15, 'bold'),text_color="#FFFFFF",fg_color="#090b17",width=200,height=200,corner_radius=20,compound=TOP,anchor=N)
img3_label.place(x=470,y=70)

img4_label=customtkinter.CTkLabel(app, image=img4,text="coffee mocha\n price: 30$",font=('glazier', 15, 'bold'),text_color="#FFFFFF",fg_color="#090b17",width=200,height=200,corner_radius=20,compound=TOP,anchor=N)
img4_label.place(x=30,y=330)

img5_label=customtkinter.CTkLabel(app, image=img5,text="cortado\n price: 40$",font=('glazier', 15, 'bold'),text_color="#FFFFFF",fg_color="#090b17",width=200,height=200,corner_radius=20,compound=TOP,anchor=N)
img5_label.place(x=250,y=330)

img6_label=customtkinter.CTkLabel(app, image=img6,text="coffee mocha\n price: 50$",font=('glazier', 15, 'bold'),text_color="#FFFFFF",fg_color="#090b17",width=200,height=200,corner_radius=20,compound=TOP,anchor=N)
img6_label.place(x=470,y=330)

quntity1_combobox=customtkinter.CTkComboBox(app,font=('glazier', 12, 'bold'),text_color="#000000",fg_color="#FFFFFF",values=('0','1','2','3'),state="readonly")
quntity1_combobox.place(x=60,y=280)
quntity1_combobox.set(0)

quntity2_combobox=customtkinter.CTkComboBox(app,font=('glazier', 12, 'bold'),text_color="#000000",fg_color="#FFFFFF",values=('0','1','2','3'),state="readonly")
quntity2_combobox.place(x=280,y=280)
quntity2_combobox.set(0)

quntity3_combobox=customtkinter.CTkComboBox(app,font=('glazier', 12, 'bold'),text_color="#000000",fg_color="#FFFFFF",values=('0','1','2','3'),state="readonly")
quntity3_combobox.place(x=500,y=280)
quntity3_combobox.set(0)

quntity4_combobox=customtkinter.CTkComboBox(app,font=('glazier', 12, 'bold'),text_color="#000000",fg_color="#FFFFFF",values=('0','1','2','3'),state="readonly")
quntity4_combobox.place(x=60,y=540)
quntity4_combobox.set(0)

quntity5_combobox=customtkinter.CTkComboBox(app,font=('glazier', 12, 'bold'),text_color="#000000",fg_color="#FFFFFF",values=('0','1','2','3'),state="readonly")
quntity5_combobox.place(x=280,y=540)
quntity5_combobox.set(0)

quntity6_combobox=customtkinter.CTkComboBox(app,font=('glazier', 12, 'bold'),text_color="#000000",fg_color="#FFFFFF",values=('0','1','2','3'),state="readonly")
quntity6_combobox.place(x=500,y=540)
quntity6_combobox.set(0)


customer_label=customtkinter.CTkLabel(app,text="Customer Name:",font=('glazier', 15, 'bold'),text_color="#FFFFFF",fg_color="brown4")
customer_label.place(x=40,y=600)

customer_entry=customtkinter.CTkEntry(app,font=('glazier', 15, 'bold'),fg_color="#FFFFFF",text_color="#000000",border_color="#FFFFFF",width=200)
customer_entry.place(x=190,y=600)

pay_button=customtkinter.CTkButton(app,command=pay,text='Pay Bill',font=('glazier', 15, 'bold'),fg_color="#ad0c78",hover_color="#ad0c78",corner_radius=20,cursor="hand2")
pay_button.place(x=100,y=680)

save_button=customtkinter.CTkButton(app,command=save,text='save Bill',font=('glazier', 15, 'bold'),fg_color="#058007",hover_color="#058007",corner_radius=20,cursor="hand2")
save_button.place(x=250,y=680)

new_button=customtkinter.CTkButton(app,command=new,text='New Bill',font=('glazier', 15, 'bold'),fg_color="#c26406",hover_color="#c26406",corner_radius=20,cursor="hand2")
new_button.place(x=400,y=680)
use

app.mainloop()
