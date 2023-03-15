from tkinter import *
import customtkinter
from tkinter import messagebox
import tkinter.simpledialog as sd
import datetime


def start_test():
    for widgets in main_frame.winfo_children():
        widgets.destroy()

    p_label = Label(main_frame,
                    text='Ada Lovelace',
                    font=("consolas", 25))
    p_label.place(x=10, y=20)

    p_label2 = Label(main_frame,
                     text='Conor CPT test:',
                     font=("consolas", 25))
    p_label2.place(x=150, y=90)

    start_frame = Frame(main_frame,
                        width=550,
                        height=400,
                        borderwidth=4,
                        relief="groove")
    start_frame.place(x=150, y=150)

    start_butt = customtkinter.CTkButton(master=start_frame,
                                         text="Start Test",
                                         font=("consolas", 20),
                                         fg_color='grey')
    start_butt.place(relx=0.5, rely=0.5, anchor=CENTER)

    inst_frame = Frame(main_frame,
                       width=200,
                       height=200,
                       borderwidth=4,
                       relief="groove")
    inst_frame.place(x=750, y=250)

    inst_text1 = Label(inst_frame,
                       text="Instructions:",
                       font=("consolas", 15, "bold", "underline"))
    inst_text1.place(x=5, y=5)

    inst_text2 = Label(inst_frame,
                       text="Press Space \n when the \n correct\n shape appears",
                       font=("consolas", 15))
    inst_text2.place(x=5, y=70)

    end_butt = customtkinter.CTkButton(master=main_frame,
                                       text="End Test",
                                       font=("consolas", 20),
                                       fg_color='grey')
    end_butt.place(x=780, y=510)

    toggle_text = Label(main_frame,
                        text="Connect to BCI kit",
                        font=("consolas", 15, "bold"))
    toggle_text.place(x=750, y=90)

    bci_butt = customtkinter.CTkButton(master=start_frame,
                                         text="Start BCI",
                                         font=("consolas", 20),
                                         fg_color='grey')
    bci_butt.place(x=750, y=130)

    def on_on(event):
        global off_label

        on_label.destroy()
        off_label = Label(main_frame,
                          image=off)
        off_label.place(x=820, y=120)
        off_label.image = off
        off_label.bind("<Button-1>", on_off)

    def on_off(event):
        global on_label

        off_label.destroy()
        on_label = Label(main_frame,
                         image=on)
        on_label.place(x=820, y=120)
        on_label.image = on
        on_label.bind("<Button-1>", on_on)

    on = PhotoImage(file='images/on.png')
    off = PhotoImage(file='images/of.png')

    off_label = Label(main_frame,
                      image=off)
    off_label.place(x=820, y=120)

    off_label.image = off

    off_label.bind("<Button-1>", on_off)


def home():
    for widgets in main_frame.winfo_children():
        widgets.destroy()

    text = '''
Nowadays we can see that there are various methods for conducting a preliminary diagnosis in order to identify ADHD, \n such as cognitive tests, testing biological measures and using brain wave technologies such as BCI.

Due to the fact that there are many methods for diagnosing ADHD it can be argued that there is no unequivocal method \nfor diagnosing the issue.

In parallel with the methods of preliminary diagnosis, it can be seen that there are a large number of means to indicate \n and monitor the severity of the ADHD phenomenon during the existence of therapy which again indicates a lack of insignificance regarding \n the use of existing auditing tools.

In addition to the current issues that have been mentioned there is another problem when it comes to the different \n treatment methods that every medical institute or therapist offers. Treatment methods can be through medications, physical training,\n cognitive therapy and more.

'''
    text_label = Label(main_frame,
                       text=text,
                       font=("consolas", 10))
    text_label.place(x=20, y=20)
    image = PhotoImage(file='./images/head.png')
    image_label = Label(main_frame,
                        image=image)
    image_label.place(x=330, y=280)
    image_label.image = image


def patient():
    for widgets in main_frame.winfo_children():
        widgets.destroy()

    column = ("Patient Name", "Date of Birth", "Action")

    data = (
        ('Ada Lovelace', 'December 10, 1815', 'Edit'),
        ('Bill Gate', 'December 21, 1915', 'Edit'),
        ('Jace Norman', 'October 15, 1815', 'Edit')
    )
    table = Frame(main_frame)
    table.place(x=270, y=50)

    for col, heading in enumerate(column):
        Label(table,
              text=heading,
              bg="grey",
              border=2,
              padx=40,
              pady=10,
              borderwidth=2,
              relief="groove").grid(row=0, column=col, sticky="nsew")

    for row, record in enumerate(data, start=1):
        for col, value in enumerate(record):
            Label(table,
                  text=value,
                  padx=40,
                  pady=30,
                  borderwidth=2,
                  relief="groove").grid(row=row, column=col, sticky="nsew")


def patientinfo():
    for widgets in main_frame.winfo_children():
        widgets.destroy()
    main_frame.config(width=1000,
                      height=600)

    p_label = Label(main_frame,
                    text='Ada Lovelace',
                    font=("consolas", 25))
    p_label.place(x=10, y=20)

    p_label = Label(main_frame,
                    text='Treatment Summary',
                    font=("consolas", 15))
    p_label.place(x=80, y=70)
    column = ("Visit", "Date", "Summarry")

    data = (
        ('Ada Lovelace', 'December 10, 1815', 'Edit'),
        ('Ada Lovelace', 'December 21, 1915', 'Edit'),
        ('Ada Lovelace', 'October 15, 1815', 'Edit')
    )
    table = Frame(main_frame)
    table.place(x=80, y=100)

    for col, heading in enumerate(column):
        Label(table, text=heading,
              bg="grey",
              padx=20,
              pady=5,
              borderwidth=2,
              relief="groove").grid(row=0, column=col, sticky="nsew")

    for row, record in enumerate(data, start=1):
        for col, value in enumerate(record):
            Label(table,
                  text=value,
                  padx=20,
                  pady=15,
                  borderwidth=2,
                  relief="groove").grid(row=row, column=col, sticky="nsew")

    newtest_frame = Frame(main_frame,
                          width=250,
                          height=300,
                          borderwidth=4,
                          relief="groove")
    newtest_frame.place(x=650, y=280)

    new_text = Label(newtest_frame,
                     width=245,
                     font=("consolas", 20),
                     bg="grey")
    new_text.place(x=-5, y=-4)

    new_text = Label(newtest_frame,
                     text="New Test",

                     font=("consolas", 15),
                     bg="grey")
    new_text.place(x=75, y=0)

    ass_text = Label(newtest_frame,
                     text="Association Treatment:",

                     font=("consolas", 13),
                     )
    ass_text.place(x=15, y=55)

    ass_treatment = ["treatment1", "treatment2"]
    ass_treatment_var = StringVar()
    ass_treatment_var.set("Select")

    ass_dropdown = customtkinter.CTkOptionMenu(master=newtest_frame,
                                               values=ass_treatment,
                                               variable=ass_treatment_var,
                                               fg_color="grey",
                                               width=200,
                                               font=("consolas", 13))
    ass_dropdown.place(x=15, y=85)

    def show_datepicker(event):
        date_str = sd.askstring(
            "Select Date", "Enter date in YYYY-MM-DD format:")
        if date_str is not None:
            try:
                date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
                date_label.config(text=date)
            except ValueError:
                messagebox.showerror("Invalid Date",
                                     "The date you entered is invalid. Please enter a date in DD-MM-YYYY format.")

    date_text = Label(newtest_frame,
                      text="Date:",
                      font=("consolas", 11),
                      )
    date_text.place(x=15, y=120)
    date_img = PhotoImage(file="images/dateicon.PNG")
    date_label = Label(newtest_frame,
                       text="dd/mm/yyyy             ",
                       image=date_img,
                       compound="right",
                       anchor="w",
                       borderwidth=4,
                       relief="groove")
    date_label.place(x=15, y=145)
    date_label.image = date_img
    date_label.bind("<Button-1>", show_datepicker)

    type_text = Label(newtest_frame,
                      text="Test Type:",
                      font=("consolas", 11),
                      )
    type_text.place(x=15, y=185)

    test_type = ["type1", "type2"]
    test_type_var = StringVar()
    test_type_var.set("Select")

    ass_dropdown = customtkinter.CTkOptionMenu(master=newtest_frame,
                                               values=test_type,
                                               variable=test_type_var,
                                               fg_color="grey",
                                               width=200,
                                               font=("consolas", 13))
    ass_dropdown.place(x=15, y=210)

    start_butt = customtkinter.CTkButton(master=newtest_frame,
                                         text="Start Test",
                                         font=("consolas", 15),
                                         fg_color="grey",
                                         command=start_test)
    start_butt.place(x=50, y=250)


window = Tk()
window.title("PowerMind")
# Set the width and height of the window
window_width = 1000
window_height = 680

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the x and y coordinates to center the window
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the position of the window
window.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))


def home_click(event):
    home_tab.config(bg="#F6F6F6")
    patient_tab.config(bg="#BEBABA")
    patientinfo_tab.config(bg="#BEBABA")
    home()


def patient_click(event):
    home_tab.config(bg="#BEBABA")
    patient_tab.config(bg="#F6F6F6")
    patientinfo_tab.config(bg="#BEBABA")
    patient()


def patientinfo_click(event):
    home_tab.configure(bg="#BEBABA")
    patient_tab.configure(bg="#BEBABA")
    patientinfo_tab.configure(bg="#F6F6F6")
    patientinfo()


powermind_label = Label(window,
                        text="PowerMind",
                        bg="#A8A09E",
                        width=window_width,
                        font=("consolas", 20)
                        )
powermind_label.pack()

tab_width = int(window_width/3)
home_tab = Label(window,
                 text="Home",
                 bg="#F6F6F6",
                 font=("consolas", 20),
                 padx=133)
home_tab.place(x=0, y=40)

patient_tab = Label(window,
                    text="Patient",
                    bg="#BEBABA",
                    font=("consolas", 20),
                    padx=110)
patient_tab.place(x=tab_width, y=40)

patientinfo_tab = Label(window,
                        text="Patient Info",
                        bg="#BEBABA",
                        font=("consolas", 20),
                        padx=80)
patientinfo_tab.place(x=tab_width+tab_width, y=40)

home_tab.bind("<Button-1>", home_click)
patient_tab.bind("<Button-1>", patient_click)
patientinfo_tab.bind("<Button-1>", patientinfo_click)

main_frame = Frame(window,
                   width=1000,
                   height=600,
                   )
main_frame.place(x=0, y=80)
home()


window.mainloop()
