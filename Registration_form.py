from tkinter import *
import pymysql
import tkinter.messagebox
import time


def welcome(lun,lps,tk1):
    un = lun.get()
    ps = lps.get()

    con = pymysql.connect("localhost", "root", "root123", "student_info")
    cur = con.cursor()

    query = "select uname, pas from information"
    i1 = cur.execute(query)
    record = cur.fetchall()
    print(i1)
    print(record)
    i = 0
    j = 0
    for r in record:
        if r[0] == un and r[1] == ps:
            i = 1
        elif r[0] == un and r[1] != ps:
            j = 1

    if i == 1:
        tk1.destroy()
        tk3 = Tk()
        tk3.geometry("600x400+350+90")
        tk3.resizable(0, 0)

        l3 = Label(text="WELCOME", font=("calibri", 40, "bold"))
        l3.pack()

        about = Button(text="About", bd=1, width=6,bg="cyan",  font=("calibri", 10, "bold"), command=lambda :about_own(un,tk3))
        about.place(x=0, y=80)

        all_data = Button(text="All data", bd=1, width=10,bg="cyan", font=("calibri", 10, "bold"), command=lambda: info(un,tk3))
        all_data.place(x=300, y=80)

        change_pass = Button(text="Chang Password", bd=1, width=15,bg="cyan", font=("calibri", 10, "bold"), command=lambda: chg_pass(un,tk3))
        change_pass.place(x=50, y=80)

        upda_info = Button(text="Update information", bd=1, width=18,bg="cyan", font=("calibri", 10, "bold"), command=lambda :update_info(un, tk3))
        upda_info.place(x=165, y=80)

        logout = Button(text="Logout", bd=1, width=9, bg="cyan", font=("calibri", 10, "bold"), command=lambda :log_out(tk3))
        logout.place(x=530, y=80)

        search_ = Button(text="Search", bd=1, width=6, bg="cyan", font=("calibri", 10, "bold"), command=lambda :search(un,tk3))
        search_.place(x=379, y=80)

        delete = Button(text="Delete Account", bd=1, width=15, bg="cyan", font=("calibri", 10, "bold"), command=lambda :delete_(un,tk3))
        delete.place(x=430, y=80)
        tk3.mainloop()

    else:
        if j == 1:
            tkinter.messagebox.showerror("error", "password is wrong")
        else:
            tkinter.messagebox.showerror("error", "you are not registered user !!")


def log_out(tk3):
    r = tkinter.messagebox.askyesno("?","are you sure you want to LOGOUT from the account")
    if r:
        tk3.destroy()
        login()


def about_own(un,tk3):
    tk3.destroy()
    tk5 = Tk()
    tk5.geometry("600x500+350+90")

    l = Label(text="About you", font=("calibri", 40, "bold"))
    l.pack()
    y3 = 140
    for i in ['id', 'name', 'father''s name', 'dob', 'Email', 'Mobile', 'Address', 'Pin code', 'Username', 'password']:
        l = Label(text=i, font=("calibri", 15, "bold"))
        l.place(x=30, y=y3)
        y3 = y3 + 30

    con = pymysql.connect("localhost", "root", "root123", "student_info")
    cur = con.cursor()

    query = "select id, name_, fname, dob, email,mob, add_, pin, uname, pas from information where uname = %s"
    tuple_value = (un)
    i1 = cur.execute(query, tuple_value)
    record = cur.fetchall()
    print(i1)
    print(record)

    y2 = 140
    for i in record:
        for j in i:
            l = Label(text=j, font=("calibri", 15))
            l.place(x=180, y=y2)
            y2 = y2 + 30

    about = Button(text="About", bd=1, width=6,bg="cyan", font=("calibri", 10, "bold"), command=lambda: about_own(un, tk5))
    about.place(x=0, y=80)

    change_pass = Button(text="Chang Password", bd=1, width=15,bg="cyan", font=("calibri", 10, "bold"),
                         command=lambda: chg_pass(un, tk5))
    change_pass.place(x=50, y=80)

    upda_info = Button(text="Update information", bd=1, width=18,bg="cyan", font=("calibri", 10, "bold"), command=lambda: update_info(un, tk5))
    upda_info.place(x=165, y=80)

    all_data = Button(text="All data", bd=1, width=10, bg="cyan", font=("calibri", 10, "bold"), command=lambda: info(un,tk5))
    all_data.place(x=300, y=80)

    logout = Button(text="Logout", bd=1, width=9,bg="cyan", font=("calibri", 10, "bold"), command=lambda :log_out(tk5))
    logout.place(x=540, y=80)

    search_ = Button(text="Search", bd=1, width=6, bg="cyan", font=("calibri", 10, "bold"),command=lambda: search(un,tk5))
    search_.place(x=379, y=80)

    delete = Button(text="Delete Account", bd=1, width=15, bg="cyan", font=("calibri", 10, "bold"),command=lambda :delete_(un,tk5))
    delete.place(x=430, y=80)

    tk5.mainloop()


def delete_(un,tk3):
    tk3.destroy()
    tk7 = Tk()
    tk7.geometry("600x400+350+90")

    def delete1(un,tk7):
        r = tkinter.messagebox.askyesno("warning","are you sure you want to delete your account")
        print(r)
        if r:
            con = pymysql.connect("localhost", "root", "root123", "student_info")
            cur = con.cursor()
            query = "delete from information where uname = '%s'"%(un)
            i1 = cur.execute(query)
            con.commit()
            con.close()
            cur.close()
            tk7.destroy()
            login()

    b1 = Label(text="Delete account", font=("calibri", 40, "bold"))
    b1.pack()
    b = Label(text="If you delete your account click here", font=("calibri", 15, "bold"))
    b.place(x=100, y=200)
    b=Button(text="DELETE", bd=2, fg="red", command=lambda :delete1(un,tk7))
    b.place(x=430, y=200)

    about = Button(text="About", bd=1, width=6, bg="cyan", font=("calibri", 10, "bold"), command=lambda: about_own(un, tk7))
    about.place(x=0, y=80)

    all_data = Button(text="All data", bd=1, width=10, bg="cyan", font=("calibri", 10, "bold"), command=lambda: info(un, tk7))
    all_data.place(x=300, y=80)

    change_pass = Button(text="Chang Password", bd=1, width=15, bg="cyan", font=("calibri", 10, "bold"), command=lambda: chg_pass(un, tk7))
    change_pass.place(x=50, y=80)

    upda_info = Button(text="Update information", bd=1, width=18, bg="cyan", font=("calibri", 10, "bold"), command=lambda: update_info(un, tk7))
    upda_info.place(x=165, y=80)

    logout = Button(text="Logout", bd=1, width=9, bg="cyan", font=("calibri", 10, "bold"),  command=lambda :log_out(tk7))
    logout.place(x=530, y=80)

    search_ = Button(text="Search", bd=1, width=6, bg="cyan", font=("calibri", 10, "bold"), command=lambda: search(un, tk7))
    search_.place(x=379, y=80)

    delete = Button(text="Delete Account", bd=1, width=15, bg="cyan", font=("calibri", 10, "bold"), command=lambda: delete_(un, tk7))
    delete.place(x=430, y=80)
    tk7.mainloop()


def info(un,tk3):
    tk3.destroy()
    tk4 = Tk()
    tk4.geometry("600x400+350+90")

    con = pymysql.connect("localhost", "root", "root123", "student_info")
    cur = con.cursor()

    query = "select * from information"
    i1 = cur.execute(query)
    record = cur.fetchall()
    print(i1)
    print(record)

    x3=20
    for i in ['id','name','father''s name','dob','Email','Mobile','Address','Pin code','Username','password']:
        l = Label(text=i, font=80)
        l.place(x=x3, y=50)
        x3=x3+130

    y1 = 90
    for i in record:
        x1 = 20
        for j in i:
            l = Label(text=j, font=10)
            l.place(x=x1, y=y1)
            x1 = x1+130
        y1 = y1+50

    about = Button(text="About", bd=1, width=6, bg="cyan", font=("calibri", 10, "bold"), command=lambda: about_own(un, tk4))
    about.place(x=0, y=20)

    change_pass = Button(text="Chang Password", bd=1, width=15, bg="cyan", font=("calibri", 10, "bold"), command=lambda: chg_pass(un, tk4))
    change_pass.place(x=50, y=20)

    upda_info = Button(text="Update information", bd=1, width=18, bg="cyan", font=("calibri", 10, "bold"), command=lambda: update_info(un, tk4))
    upda_info.place(x=165, y=20)

    all_data = Button(text="All data", bd=1, width=10, bg="cyan", font=("calibri", 10, "bold"), command=lambda: info(tk4))
    all_data.place(x=300, y=20)

    logout = Button(text="Logout", bd=1, width=9, bg="cyan", font=("calibri", 10, "bold"),  command=lambda :log_out(tk4))
    logout.place(x=540, y=20)

    search_ = Button(text="Search", bd=1, width=6, bg="cyan", font=("calibri", 10, "bold"), command=lambda :search(un, tk4))
    search_.place(x=379, y=20)

    delete = Button(text="Delete Account", bd=1, width=15, bg="cyan", font=("calibri", 10, "bold"), command=lambda :delete_(un,tk4))
    delete.place(x=430, y=20)

    tk4.mainloop()


def chg_pass(un,tk3):
    tk3.destroy()
    tk4 = Tk()
    tk4.geometry("600x400+350+90")

    l = Label(text='change password', font=("calibri", 40, "bold"))
    l.place(x=90, y=10)
    l1 = Label(text="Enter old password", font=10)
    l1.place(x=40+100,y=90+30)
    l2 = Label(text="Enter new password", font=10)
    l2.place(x=40+100, y=140+30)
    l3 = Label(text="conform new password", font=10)
    l3.place(x=40+100, y=190+30)

    e1 = Entry(show="*")
    e2 = Entry(show="*")
    e3 = Entry(show="*")
    e1.place(x=250+100, y=90+30)
    e2.place(x=250+100, y=140+30)
    e3.place(x=250+100, y=190+30)

    def newpass(un):
        old = e1.get()
        new1 = e2.get()
        new2 = e3.get()

        con = pymysql.connect('localhost', 'root', 'root123', 'student_info')
        cur = con.cursor()

        query = 'select pas from information'
        i = cur.execute(query)
        record = cur.fetchall()
        print(record)
        flag = 0
        for r in record:
            if r[0] == old:
                flag = 1

        if flag == 0:
            tkinter.messagebox.showerror("error", 'old password is wrong')

        else:
            if new1 != new2:
                tkinter.messagebox.showerror("error", "password and conform password are not same")
            else:
                query1 = "update information set pas=%s, repass=%s where uname=%s"
                tuple_value = (new1, new1,un)
                cur.execute(query1, tuple_value)
                con.commit()
                cur.close()
                tkinter.messagebox.showinfo("success", "password change successful")
    b1 = Button(text='submit', bd=3, width=10, command=lambda :newpass(un))
    b1.place(x=200, y=280)

    about = Button(text="About", bd=1, width=6,bg="cyan", font=("calibri", 10, "bold"), command=lambda: about_own(un, tk4))
    about.place(x=0, y=80)

    change_pass = Button(text="Chang Password", bd=1, width=15,bg="cyan", font=("calibri", 10, "bold"), command=lambda: chg_pass(un, tk4))
    change_pass.place(x=50, y=80)

    upda_info = Button(text="Update information", bd=1, width=18,bg="cyan", font=("calibri", 10, "bold"), command=lambda: update_info(un, tk4))
    upda_info.place(x=165, y=80)

    all_data = Button(text="All data", bd=1, width=10, bg="cyan", font=("calibri", 10, "bold"), command=lambda: info(un,tk4))
    all_data.place(x=300, y=80)

    logout = Button(text="Logout", bd=1, width=9 ,bg="cyan", font=("calibri", 10, "bold"), command=lambda :log_out(tk4))
    logout.place(x=540, y=80)

    search_ = Button(text="Search", bd=1, width=6, bg="cyan", font=("calibri", 10, "bold"), command=lambda :search(un,tk4))
    search_.place(x=379, y=80)
    delete = Button(text="Delete Account", bd=1, width=15, bg="cyan", font=("calibri", 10, "bold"),command=lambda :delete_(un,tk4))
    delete.place(x=430, y=80)

    def reset():
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)

    b2 = Button(text='reset', bd=3, width=10, command=reset)
    b2.place(x=350, y=280)

    b3 = Button(text='home', bd=0)
    b3.place(x=10,y=10)
    tk4.mainloop()


def update_info(un,tk3):
    tk3.destroy()
    tk5 = Tk()
    tk5.geometry("600x400+350+90")
    l = Label(text="Update your information", font=("calibri", 40, "bold"))
    l.pack()
    l1 = Label(text="enter your new email", font=10)
    l1.place(x=100, y=120)
    l2 = Label(text="enter your new mobile number", font=10)
    l2.place(x=100, y=160)

    e1 = Entry()
    e1.place(x=350, y=120)
    e2 = Entry()
    e2.place(x=350, y=160)

    def reset():
        e1.delete(0, END)
        e2.delete(0, END)

    def update_email(un):
        new_email = e1.get()
        if len(new_email) == 0:
            tkinter.messagebox.showerror("error", "fill all the field")
        else:
            email_check = re.fullmatch("[\w]{1,20}@[\w]{2,20}.[A-Za-z]{2,3}", new_email)
            if (email_check):
                con = pymysql.connect("localhost", "root", "root123", "student_info")
                cur = con.cursor()
                query = "update information set email=%s where uname=%s"
                tuple_value = (new_email,un)
                cur.execute(query,tuple_value)
                con.commit()
                cur.close()
                tkinter.messagebox.showinfo("success", "Email change successful \n Update time : {}".format(time.asctime()))
            else:
                tkinter.messagebox.showerror("email", "email is not correct")

    def update_mobile(un):
        new_mob = e2.get()
        if len(new_mob )== 0:
            tkinter.messagebox.showerror("error", "fill all the field")
        else:
            mob_check = re.search("^[0-9]{10}$", new_mob)
            if mob_check:
                con = pymysql.connect("localhost", "root", "root123", "student_info")
                cur = con.cursor()
                query = "update information set mob=%s where uname=%s"
                tuple_value = (new_mob, un)
                cur.execute(query, tuple_value)
                con.commit()
                cur.close()
                tkinter.messagebox.showinfo("success", "Mobile number change successful \n Update time : {}".format(time.asctime()))
            else:
                tkinter.messagebox.showerror("error", "mobile number is not correct pattern")

    b1 = Button(text="Update", bd=0, font=("calibri", 15, "bold" ), command=lambda :update_email(un))
    b1.place(x=470, y=110)

    b2 = Button(text="Update", bd=0, font=("calibri", 15, "bold"), command=lambda :update_mobile(un))
    b2.place(x=470, y=150)

    b3 = Button(text="Reset", bd=3, width=10, command=reset)
    b3.place(x=250, y=250)

    about = Button(text="About", bd=1, width=6,bg="cyan", font=("calibri", 10, "bold"), command=lambda: about_own(un, tk5))
    about.place(x=0, y=80)

    change_pass = Button(text="Chang Password", bd=1, width=15,bg="cyan", font=("calibri", 10, "bold"), command=lambda: chg_pass(un, tk5))
    change_pass.place(x=50, y=80)

    upda_info = Button(text="Update information", bd=1, width=18,bg="cyan", font=("calibri", 10, "bold"), command=lambda: update_info(un, tk5))
    upda_info.place(x=165, y=80)

    all_data = Button(text="All data", bd=1, width=10, bg="cyan", font=("calibri", 10, "bold"), command=lambda: info(un,tk5))
    all_data.place(x=300, y=80)

    logout = Button(text="Logout", bd=1, width=9,bg="cyan", font=("calibri", 10, "bold"), command=lambda :log_out(tk5))
    logout.place(x=540, y=80)

    search_ = Button(text="Search", bd=1, width=6, bg="cyan", font=("calibri", 10, "bold"), command=lambda :search(un,tk5))
    search_.place(x=379, y=80)

    delete = Button(text="Delete Account", bd=1, width=15, bg="cyan", font=("calibri", 10, "bold"),command=lambda :delete_(un,tk5))
    delete.place(x=430, y=80)

    tk5.mainloop()


def search(un,tk3):
    tk3.destroy()
    tk6 = Tk()
    tk6.geometry("600x400+350+90")
    e = Entry()
    e.place(x=220, y=220)
    v = IntVar()

    r1 = Radiobutton(text="id",font=("calibri", 10, "bold"), variable=v, value=1)
    r2 = Radiobutton(text="User name",font=("calibri", 10, "bold"), variable=v, value=2)
    r3 = Radiobutton(text="Email",font=("calibri", 10, "bold"), variable=v, value=3)
    r4 = Radiobutton(text="Mobile",font=("calibri", 10, "bold"), variable=v, value=4)

    r1.place(x=190, y=140)
    r2.place(x=190, y=170)
    r3.place(x=320, y=140)
    r4.place(x=320, y=170)

    def result(tk3):
        r = e.get()
        value = v.get()
        tk3.destroy()
        tk4 = Tk()
        tk4.geometry("600x400+350+90")

        print("value", value)
        print("r", r)
        y3 = 140
        for i in ['id', 'name', 'father''s name', 'dob', 'Email', 'Mobile', 'Address', 'Pin code']:
            l = Label(text=i, font=("calibri", 15, "bold"))
            l.place(x=30, y=y3)
            y3 = y3 + 30

        if value == 1:
            con = pymysql.connect("localhost", "root", "root123", "student_info")
            cur = con.cursor()
            query = "select id, name_,fname,dob,email,mob,add_,pin from information where id = '%s'" %(r)
            i1 = cur.execute(query)
            record = cur.fetchall()
            print(i1)
            print(record)
            y2 = 140
            for i in record:
                for j in i:
                    l = Label(text=j, font=("calibri", 15))
                    l.place(x=180, y=y2)
                    y2 = y2 + 30

        if value == 2:
            con = pymysql.connect("localhost", "root", "root123", "student_info")
            cur = con.cursor()
            query = "select id, name_,fname,dob,email,mob,add_,pin from information where uname = '%s'" %(r)
            i1 = cur.execute(query)
            record = cur.fetchall()
            print(i1)
            print(record)
            y2 = 140
            for i in record:
                for j in i:
                    l = Label(text=j, font=("calibri", 15))
                    l.place(x=180, y=y2)
                    y2 = y2 + 30

        if value == 3:
            con = pymysql.connect("localhost", "root", "root123", "student_info")
            cur = con.cursor()
            query = "select id, name_,fname,dob,email,mob,add_,pin from information where email = '%s'" %(r)
            i1 = cur.execute(query)
            record = cur.fetchall()
            print(i1)
            print(record)
            y2 = 140
            for i in record:
                for j in i:
                    l = Label(text=j, font=("calibri", 15))
                    l.place(x=180, y=y2)
                    y2 = y2 + 30

        if value == 4:
            con = pymysql.connect("localhost", "root", "root123", "student_info")
            cur = con.cursor()
            query = "select id, name_,fname,dob,email,mob,add_,pin from information where mob = '%s'" %(r)
            i1 = cur.execute(query)
            record = cur.fetchall()
            print(i1)
            print(record)
            y2 = 140
            for i in record:
                for j in i:
                    l = Label(text=j, font=("calibri", 15))
                    l.place(x=180, y=y2)
                    y2 = y2 + 30

        about = Button(text="About", bd=1, width=6, bg="cyan", font=("calibri", 10, "bold"), command=lambda: about_own(un, tk4))
        about.place(x=0, y=80)

        change_pass = Button(text="Chang Password", bd=1, width=15, bg="cyan", font=("calibri", 10, "bold"), command=lambda: chg_pass(un, tk4))
        change_pass.place(x=50, y=80)

        upda_info = Button(text="Update information", bd=1, width=18, bg="cyan", font=("calibri", 10, "bold"), command=lambda: update_info(un, tk4))
        upda_info.place(x=165, y=80)

        all_data = Button(text="All data", bd=1, width=10, bg="cyan", font=("calibri", 10, "bold"), command=lambda: info(tk4))
        all_data.place(x=300, y=80)

        logout = Button(text="Logout", bd=1, width=6, bg="cyan", font=("calibri", 10, "bold"), command=lambda: log_out(tk4))
        logout.place(x=540, y=80)

        search_ = Button(text="Search", bd=1, width=6, bg="cyan", font=("calibri", 10, "bold"), command=lambda: search(un, tk4))
        search_.place(x=379, y=80)

        delete = Button(text="Delete Account", bd=1, width=15, bg="cyan", font=("calibri", 10, "bold"), command=lambda: delete_(un,tk4))
        delete.place(x=430, y=80)

        tk4.mainloop()

    b1 = Button(text="Search", width=10, command=lambda :result(tk6))
    b2 = Button(text="reset", width=10)
    b1.place(x=200, y=260)
    b2.place(x=300, y=260)

    about = Button(text="About", bd=1, width=6,bg="cyan", font=("calibri", 10, "bold"), command=lambda: about_own(un, tk6))
    about.place(x=0, y=80)

    change_pass = Button(text="Chang Password", bd=1, width=15,bg="cyan", font=("calibri", 10, "bold"), command=lambda: chg_pass(un, tk6))
    change_pass.place(x=50, y=80)

    upda_info = Button(text="Update information", bd=1, width=18,bg="cyan", font=("calibri", 10, "bold"), command=lambda: update_info(un, tk6))
    upda_info.place(x=165, y=80)

    all_data = Button(text="All data", bd=1, width=10, bg="cyan", font=("calibri", 10, "bold"), command=lambda: info(tk6))
    all_data.place(x=300, y=80)

    logout = Button(text="Logout", bd=1, width=6,bg="cyan", font=("calibri", 10, "bold"), command=lambda: log_out(tk6))
    logout.place(x=540, y=80)

    search_ = Button(text="Search", bd=1, width=6, bg="cyan", font=("calibri", 10, "bold"), command=lambda :search(un,tk6))
    search_.place(x=379, y=80)

    delete = Button(text="Delete Account", bd=1, width=15, bg="cyan", font=("calibri", 10, "bold"),  command=lambda: delete_(un,tk6))
    delete.place(x=430, y=80)

    tk6.mainloop()


def login():
    tk1 = Tk()
    tk1.geometry("600x400+350+90")
    tk1.resizable(0, 0)
    l = Label(text="Login", font=("calibri", 40, "bold"))
    l1 = Label(text="Username", font=80)
    l2 = Label(text="Password", font=80)

    l.pack()
    l1.place(x=170, y=90)
    l2.place(x=170, y=130)

    lun = Entry()
    lps = Entry(show="*")

    lun.place(x=270, y=90)
    lps.place(x=270, y=130)

    def register():
        tk1.destroy()
        tk2 = Tk()
        tk2.geometry("600x600+350+90")
        tk2.resizable(0, 0)
        rl = Label(text="Registration", font=("calibri", 40, "bold"))
        rid = Label(text="Enter ID", font=80)
        rname = Label(text="Name", font=80)
        rfname = Label(text="Father Name", font=80)
        rdob = Label(text="Date of birth (yyyy/mm/dd)", font=80)
        remail = Label(text="Email", font=80)
        rmob = Label(text="Mobile", font=80)
        radd = Label(text="Address", font=80)
        rpin = Label(text="pin code", font=80)
        runame = Label(text="Username", font=80)
        rpass = Label(text="Password", font=80)
        rrepass = Label(text="Reenter password", font=80)

        rl.pack()
        rid.place(x=140, y=90)
        rname.place(x=140, y=130)
        rfname.place(x=140, y=170)
        rdob.place(x=140, y=210)
        remail.place(x=140, y=250)
        rmob.place(x=140, y=290)
        radd.place(x=140, y=330)
        rpin.place(x=140, y=370)
        runame.place(x=140, y=410)
        rpass.place(x=140, y=450)
        rrepass.place(x=140, y=490)

        e1 = Entry()
        e2 = Entry()
        e3 = Entry()
        e4 = Entry()
        e5 = Entry()
        e6 = Entry()
        e7 = Entry()
        e8 = Entry()
        e9 = Entry()
        e10 = Entry(show="*")
        e11 = Entry(show="*")

        e1.place(x=330, y=90)
        e2.place(x=330, y=130)
        e3.place(x=330, y=170)
        e4.place(x=330, y=210)
        e5.place(x=330, y=250)
        e6.place(x=330, y=290)
        e7.place(x=330, y=330)
        e8.place(x=330, y=370)
        e9.place(x=330, y=410)
        e10.place(x=330, y=450)
        e11.place(x=330, y=490)

        def save():
            id = e1.get()
            name = e2.get()
            fname = e3.get()
            dob = e4.get()
            email = e5.get()
            mob = e6.get()
            add = e7.get()
            pin = e8.get()
            uname = e9.get()
            pas = e10.get()
            repass = e11.get()

            if len(id)==0  or len(name)==0 or len(fname)==0 or len(dob)==0 or len(email)==0 or len(mob)==0 or len(add)==0 or len(pin)==0 or len(uname)==0 or len(pas)==0 or len(repass) == 0:
                tkinter.messagebox.showerror("error","fill all the field")

            elif pas != repass:
                tkinter.messagebox.showinfo("error", "password and conform password are not same")
            else:
                email_check = re.fullmatch("[\w]{1,20}@[\w]{2,20}.[A-Za-z]{2,3}",email)
                if(email_check):

                    mob_check = re.search("^[0-9]{10}$",mob)
                    if mob_check:

                        pin_check = re.search("^[0-9]{6}$",pin)
                        if pin_check:

                            con = pymysql.connect("localhost", "root", "root123", "student_info")
                            cur = con.cursor()

                            query = "insert into information value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            insert_tuple = (id, name, fname, dob, email, mob, add, pin, uname, pas, repass)
                            cur.execute(query, insert_tuple)
                            con.commit()
                            cur.close()
                            tkinter.messagebox.showinfo("save", "you are successfully registered")
                        else:
                            tkinter.messagebox.showerror("error","pin code is not in correct pattern")
                    else:
                        tkinter.messagebox.showerror("error","mobile number is not correct pattern")
                else:
                    tkinter.messagebox.showerror("email","email is not correct")

        rb1 = Button(text="register", bd=3, width=10, command=save)
        rb1.place(x=200, y=530)

        def reset():
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
            e6.delete(0, END)
            e7.delete(0, END)
            e8.delete(0, END)
            e9.delete(0, END)
            e10.delete(0, END)
            e11.delete(0, END)

        rb2 = Button(text="reset", bd=3, width=10, command=reset)
        rb2.place(x=330, y=530)

        tk2.mainloop()

    b1 = Button(text="submit", bd=3, width=10, command=lambda :welcome(lun,lps,tk1))
    b1.place(x=200, y=170)
    b2 = Button(text="sign up", bd=3, width=10, command=register)
    b2.place(x=290, y=170)

    tk1.mainloop()


login()



