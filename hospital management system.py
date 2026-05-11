from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql

# ---------------- DATABASE CONNECTION ---------------- #

def connect_db():
    return mysql.connect(
        host="localhost",
        database="team",
        user="root",
        password="india"
    )

# ---------------- GLOBAL VARIABLES ---------------- #

s1 = s2 = s3 = s4 = None
p1 = p2 = p3 = p4 = None

# ---------------- ROOM FUNCTIONS ---------------- #

def next1():
    global s1, s2, s3, s4

    win = Toplevel()
    win.title("Add Rooms")
    win.geometry("400x400")

    Label(win, text="Enter Room Number").place(x=20, y=30)
    s1 = Entry(win, width=30)
    s1.place(x=20, y=60)

    Label(win, text="Enter Room Category").place(x=20, y=90)
    s2 = Entry(win, width=30)
    s2.place(x=20, y=120)

    Label(win, text="Enter Room Type").place(x=20, y=150)
    s3 = Entry(win, width=30)
    s3.place(x=20, y=180)

    Label(win, text="Enter Room Cost").place(x=20, y=210)
    s4 = Entry(win, width=30)
    s4.place(x=20, y=240)

    Button(win, text="Save", command=add_rooms).place(x=20, y=280)
    Button(win, text="Clear", command=clear_rooms).place(x=80, y=280)


def add_rooms():
    try:
        rn = int(s1.get())
        category = s2.get()
        room_type = s3.get()
        cost = float(s4.get())

        q = """
        INSERT INTO Rooms VALUES
        ('true', %s, %s, %s, %s)
        """

        cn = connect_db()
        cursor = cn.cursor()
        cursor.execute(q, (rn, category, room_type, cost))
        cn.commit()
        cn.close()

        messagebox.showinfo("Success", "Room Added")

        clear_rooms()

    except Exception as e:
        messagebox.showerror("Error", str(e))


def clear_rooms():
    s1.delete(0, END)
    s2.delete(0, END)
    s3.delete(0, END)
    s4.delete(0, END)


# ---------------- EDIT ROOM ---------------- #

def next2():
    global s1, s2, s3, s4

    win = Toplevel()
    win.title("Edit Rooms")
    win.geometry("400x400")

    Label(win, text="Room Number").place(x=20, y=30)
    s1 = Entry(win, width=30)
    s1.place(x=20, y=60)

    Label(win, text="Room Category").place(x=20, y=90)
    s2 = Entry(win, width=30)
    s2.place(x=20, y=120)

    Label(win, text="Room Type").place(x=20, y=150)
    s3 = Entry(win, width=30)
    s3.place(x=20, y=180)

    Label(win, text="Room Cost").place(x=20, y=210)
    s4 = Entry(win, width=30)
    s4.place(x=20, y=240)

    Button(win, text="Update", command=edit_rooms).place(x=20, y=280)


def edit_rooms():
    try:
        rn = int(s1.get())
        category = s2.get()
        room_type = s3.get()
        cost = float(s4.get())

        q = """
        UPDATE Rooms
        SET t=%s, c=%s, cp=%s
        WHERE rn=%s
        """

        cn = connect_db()
        cursor = cn.cursor()
        cursor.execute(q, (category, room_type, cost, rn))
        cn.commit()
        cn.close()

        messagebox.showinfo("Success", "Room Updated")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------- DELETE ROOM ---------------- #

def next3():
    global s1

    win = Toplevel()
    win.title("Delete Room")
    win.geometry("300x200")

    Label(win, text="Enter Room Number").place(x=20, y=30)

    s1 = Entry(win, width=30)
    s1.place(x=20, y=60)

    Button(win, text="Delete", command=delete_rooms).place(x=20, y=100)


def delete_rooms():
    try:
        rn = int(s1.get())

        q = "DELETE FROM Rooms WHERE rn=%s"

        cn = connect_db()
        cursor = cn.cursor()
        cursor.execute(q, (rn,))
        cn.commit()
        cn.close()

        messagebox.showinfo("Success", "Room Deleted")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------- ADD PATIENT ---------------- #

def next5():
    global p1, p2, p3, p4

    win = Toplevel()
    win.title("Add Patient")
    win.geometry("400x400")

    Label(win, text="Patient ID").place(x=20, y=30)
    p1 = Entry(win, width=30)
    p1.place(x=20, y=60)

    Label(win, text="Patient Name").place(x=20, y=90)
    p2 = Entry(win, width=30)
    p2.place(x=20, y=120)

    Label(win, text="Disease").place(x=20, y=150)
    p3 = Entry(win, width=30)
    p3.place(x=20, y=180)

    Label(win, text="Medicine").place(x=20, y=210)
    p4 = Entry(win, width=30)
    p4.place(x=20, y=240)

    Button(win, text="Save", command=add_patient).place(x=20, y=280)


def add_patient():
    try:
        pid = p1.get()
        name = p2.get()
        disease = p3.get()
        medicine = p4.get()

        q = """
        INSERT INTO Patient
        VALUES (%s, %s, %s, %s)
        """

        cn = connect_db()
        cursor = cn.cursor()
        cursor.execute(q, (pid, name, disease, medicine))
        cn.commit()
        cn.close()

        messagebox.showinfo("Success", "Patient Added")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------- MAIN WINDOWS ---------------- #

def rooms():
    win = Toplevel()
    win.title("Rooms")
    win.geometry("600x400")
    win.configure(bg="royal blue")

    Button(
        win,
        text="Add Rooms",
        command=next1,
        height=2,
        width=15
    ).place(x=50, y=50)

    Button(
        win,
        text="Edit Rooms",
        command=next2,
        height=2,
        width=15
    ).place(x=300, y=50)

    Button(
        win,
        text="Delete Rooms",
        command=next3,
        height=2,
        width=15
    ).place(x=50, y=150)


def patient():
    win = Toplevel()
    win.title("Patient")
    win.geometry("600x400")
    win.configure(bg="royal blue")

    Button(
        win,
        text="Add Patient",
        command=next5,
        height=2,
        width=15
    ).place(x=50, y=50)


# ---------------- HOME PAGE ---------------- #

frame = Tk()

frame.title("Hospital Management System")
frame.geometry("1000x600")
frame.configure(bg="royal blue")

Label(
    frame,
    text="WELCOME TO HOSPITAL MANAGEMENT SYSTEM",
    bg="beige",
    font=("Courier New", 20, "bold")
).pack(pady=40)

Button(
    frame,
    text="ROOMS",
    command=rooms,
    height=3,
    width=15,
    bg="lavender"
).place(x=250, y=250)

Button(
    frame,
    text="PATIENT",
    command=patient,
    height=3,
    width=15,
    bg="lavender"
).place(x=550, y=250)

frame.mainloop()