from tkinter import *
from tkinter import messagebox

from PIL import ImageTk
import pymysql
#functionality part

def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error', 'All Field Are Required')
    else:
        try:
            con=pymysql.connect(host='localhost', user='root', password='AngryBird19')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection is not established try again')
            return
        query = 'use userdata'
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid username or password')
        else:
            messagebox.showinfo('Welcome','Login is Successful')
            login_window.destroy()
            import cafe

def login_page():
    login_window.destroy()
    import cafe

def signup_page():
    login_window.destroy()
    import signup
def hide():
    openeye.config(file='closeeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

def on_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)
#GUI part
login_window=Tk()
login_window.geometry('1209x768+50+50')
login_window.resizable(0,0)
login_window.title('Login Page')
bgImage=ImageTk.PhotoImage(file='bg.jpg')


bgLabel=Label(login_window,image=bgImage)
bgLabel.grid(row=0,column=0)

heading=Label(login_window,text='USER LOGIN',font=('glazier',29,'bold'),bg='white',fg='brown4')
heading.place(x=200,y=100)

usernameEntry=Entry(login_window,width=25,font=('glazier',15,'bold'),bd=0,fg='brown4')
usernameEntry.place(x=210,y=220)
usernameEntry.insert(0,'Username')

usernameEntry.bind('<FocusIn>',on_enter)

Frame(login_window,width=220,height=2,bg='brown4').place(x=210,y=250)

passwordEntry=Entry(login_window,width=25,font=('glazier',15,'bold'),bd=0,fg='brown4')
passwordEntry.place(x=210,y=299)
passwordEntry.insert(0,'Password')


passwordEntry.bind('<FocusIn>',password_enter)
Frame(login_window,width=220,height=2,bg='brown4').place(x=210,y=330)
openeye=PhotoImage(file='openeye.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=395,y=290)

forgetButton=Button(login_window,text='Forgot Password?',bd=0,bg='white',activebackground='white',cursor='hand2',font=('glazier',8,'bold'),fg='brown4',activeforeground='brown4')
forgetButton.place(x=335,y=350)

loginButton=Button(login_window,text='Login',font=('Open Sans',16,'bold'),fg='white',bg='brown4',activeforeground='white',activebackground='brown4',command=login_user)
loginButton.place(x=290,y=400)
orLabel=Label(login_window,text='------------ OR ------------',font=('Open Sans',16),fg='brown4',bg='white')
orLabel.place(x=219,y=460)

facebook_logo=PhotoImage(file='facebook.png')
fbLabel=Label(login_window,image=facebook_logo,bg='white')
fbLabel.place(x=220,y=500)

google_logo=PhotoImage(file='google.png')
googleLabel=Label(login_window,image=google_logo,bg='white')
googleLabel.place(x=295,y=492)

twitter_logo=PhotoImage(file='twitter.png')
twitterLabel=Label(login_window,image=twitter_logo,bg='white')
twitterLabel.place(x=380,y=498)

signupLabel=Label(login_window,text='Dont have an account?',font=('glazier',11),fg='brown4',bg='white')
signupLabel.place(x=215,y=580)

newaccountButton=Button(login_window,text='Create new one',font=('glazier',9,'bold'),fg='blue',bg='white',activeforeground='blue',activebackground='white',cursor='hand2',bd=0,command=signup_page)
newaccountButton.place(x=370,y=580)
login_window.mainloop()