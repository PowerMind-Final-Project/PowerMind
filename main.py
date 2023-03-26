from tkinter import *
import customtkinter
from tkinter import messagebox
import tkinter.simpledialog as sd
import datetime
# import nback as game
from tkcalendar import *
import subprocess

treament1 = (
    ('Visit 1', 'External', 'December 10, 1815', 'Delete'),
    ('Visit 2', 'Test', 'December 10, 1815', 'Delete'),
    ('Visit 3', 'Summary', 'December 10, 1815', 'Delete'),
)

treament2 = (
    ('Treatment1', 'visit1', 'December 10, 1815', 'Edit'),
    ('Treatment1', 'visit2', 'December 10, 1815', 'Edit'),
)

treament3 = (
    ('Treatment1', 'visit1', 'December 10, 1815', 'Edit'),
    ('Treatment1', 'visit2', 'December 10, 1815', 'Edit'),
)

summary = '''
Diagnosis: The patient presents with a primary diagnosis of hypertension.

Medical History: The patient has a history of high blood pressure and has been taking medication for several years. They have no known allergies and have a family history of cardiovascular disease.

Treatment Plan: The patient's current treatment plan involves taking a daily dose of lisinopril and making lifestyle modifications, such as reducing sodium intake and increasing physical activity. The patient will continue to monitor their blood pressure at home and return for regular check-ups.

Progress Notes: The patient's blood pressure has been consistently high, but there have been some improvements since starting the medication and lifestyle modifications. However, the patient reports occasional headaches and dizziness, which may be related to the medication.
'''


def open_test_window():
    subprocess.Popen(["python", "N-back-tkinter/N-back-tkinter.py"])

def new_information():
    for widgets in main_frame.winfo_children():
        widgets.destroy()

    # Back Button
    back_button = customtkinter.CTkButton(master=main_frame,
                                    text="Back",
                                    width=100,
                                    fg_color='gray',
                                    font=('consolas', 15),
                                    command=new_visit)
    back_button.place(x=10, y=20)

    # p_label = Label(main_frame,
    #                 text='Ada Lovelace',
    #                 font=("consolas", 25))
    # p_label.place(x=10, y=20)

    treat_label = Label(main_frame,
                        text='Treatment2: information from another source :',
                        font=("consolas", 15))
    treat_label.place(x=100, y=100)

    edit_butt = customtkinter.CTkButton(master=main_frame,
                                        text="Save",
                                        width=100,
                                        fg_color='gray',
                                        font=('consolas', 15),
                                        )
    edit_butt.place(x=750, y=100)

    test_sum_label = Label(main_frame,
                           text='Test Summary',
                           font=("consolas", 12))
    test_sum_label.place(x=100, y=160)

    test_entry = customtkinter.CTkEntry(master=main_frame,
                                        width=400,
                                        height=300,
                                        border_width=2)
    test_entry.place(x=100, y=190)

    attention_level_label = Label(main_frame,
                                  text='Attention Level',
                                  font=("consolas", 12))
    attention_level_label.place(x=600, y=160)

    attention_entry = customtkinter.CTkEntry(master=main_frame,
                                             width=300,
                                             height=80,
                                             border_width=2)
    attention_entry.place(x=600, y=190)

    location_label = Label(main_frame,
                           text='Location of the source',
                           font=("consolas", 12))
    location_label.place(x=600, y=280)

    location_entry = customtkinter.CTkEntry(master=main_frame,
                                            width=300,
                                            height=80,
                                            border_width=2)
    location_entry.place(x=600, y=310)

    doctor_name_label = Label(main_frame,
                              text='Name of the Doctor',
                              font=("consolas", 12, ))
    doctor_name_label.place(x=600, y=390)

    doctor_name_entry = customtkinter.CTkEntry(master=main_frame,
                                               width=300,
                                               height=80,
                                               border_width=2)
    doctor_name_entry.place(x=600, y=420)

def new_summary():
    for widgets in main_frame.winfo_children():
        widgets.destroy()
    # Back Button
    back_button = customtkinter.CTkButton(master=main_frame,
                                    text="Back",
                                    width=100,
                                    fg_color='gray',
                                    font=('consolas', 15),
                                    command=new_visit)
    back_button.place(x=10, y=20)

    treat_label = Label(main_frame,
                        text='Treatment1: new summary:',
                        font=("consolas", 15))
    treat_label.place(x=100, y=100)

    edit_butt = customtkinter.CTkButton(master=main_frame,
                                        text="Save",
                                        width=100,
                                        fg_color='gray',
                                        font=('consolas', 15),
                                        )
    edit_butt.place(x=750, y=100)

    test_sum_label = Label(main_frame,
                           text='Test Summary',
                           font=("consolas", 12))
    test_sum_label.place(x=100, y=160)

    test_entry = customtkinter.CTkEntry(master=main_frame,
                                        width=400,
                                        height=300,
                                        border_width=2)
    test_entry.place(x=100, y=190)

    attention_level_label = Label(main_frame,
                                  text='Attention Level',
                                  font=("consolas", 12))
    attention_level_label.place(x=600, y=160)

    attention_entry = customtkinter.CTkEntry(master=main_frame,
                                             width=300,
                                             height=80,
                                             border_width=2)
    attention_entry.place(x=600, y=190)

def new_visit():
    for widgets in main_frame.winfo_children():
        widgets.destroy()

    # Back Button
    back_button = customtkinter.CTkButton(master=main_frame,
                                    text="Back",
                                    width=100,
                                    fg_color='gray',
                                    font=('consolas', 15),
                                    command=show_treatment)
    back_button.place(x=10, y=20)
    # p_label = Label(main_frame,
    #                 text='Ada Lovelace',
    #                 font=("consolas", 25))
    # p_label.place(x=10, y=20)

    treat_label = Label(main_frame,
                        text='New Visit',
                        font=("consolas", 15, "underline"))
    treat_label.place(x=450, y=70)

    butt1 = customtkinter.CTkButton(master=main_frame,
                                    text="Add new\ninformation from \n another source",
                                    height=100,
                                    fg_color='gray',
                                    font=('consolas', 15),
                                    command=new_information)
    butt1.place(x=130, y=200)

    butt2 = customtkinter.CTkButton(master=main_frame,
                                    text="Add new \n test to available \ntreatment ",
                                    height=100,
                                    fg_color='gray',
                                    font=('consolas', 15),
                                    command=start_test)
    butt2.place(x=430, y=200)

    butt3 = customtkinter.CTkButton(master=main_frame,
                                    text="Add new \nsummary",
                                    height=100,
                                    font=('consolas', 15),
                                    fg_color='gray',
                                    command=new_summary)
    butt3.place(x=730, y=200)

def close_treatment():
    patientinfo()

def show_treatment(treatment, treat_no):
    for widgets in main_frame.winfo_children():
        widgets.destroy()

    p_label = Label(main_frame,
                    text='Ada Lovelace',
                    font=("consolas", 25))
    p_label.place(x=10, y=20)

    treat_label = Label(main_frame,
                        text=treat_no,
                        font=("consolas", 15, "underline"))
    treat_label.place(x=420, y=70)

    p_label = Label(main_frame,
                    text='Visits Summary',
                    font=("consolas", 15))
    p_label.place(x=500, y=130)

    column = ("Visit", "Type", "Date", "Action")

    table = customtkinter.CTkScrollableFrame(main_frame,
                                             height=50,
                                             width=410)
    table.place(x=500, y=155)

    for col, heading in enumerate(column):
        Label(table, text=heading,
              bg="grey",
              padx=20,
              pady=5,
              borderwidth=2,
              relief="groove").grid(row=0, column=col, sticky="nsew")

    for row, record in enumerate(treatment, start=1):
        for col, value in enumerate(record):
            if value == "Delete":
                Label(table,
                    text=value,
                    font=("consolas", 15, "underline"),
                    cursor="hand2",
                    padx=20,
                    pady=15,
                    borderwidth=2,
                    relief="groove").grid(row=row, column=col, sticky="nsew")
            elif value == "Visit 2":
                test = Label(table,
                    text=value,
                    font=("consolas", 15, "underline"),
                    cursor="hand2",
                    padx=20,
                    pady=15,
                    borderwidth=2,
                    relief="groove",
                    )
                test.grid(row=row, column=col, sticky="nsew")
                test.bind("<Button-1>", test_results)
            else:
                Label(table,
                    text=value,
                    padx=20,
                    pady=15,
                    borderwidth=2,
                    relief="groove").grid(row=row, column=col, sticky="nsew")

    def pick_start_date(event):
        def cancel():
            cal_frame.destroy()

        def select():
            cal_frame.destroy()
            date = cal.get_date()
            start_date_label.config(text=f'{date}\t\t\t')

        cal_frame = Frame(main_frame, borderwidth=4)
        cal_frame.place(x=290, y=160)
        cal = Calendar(cal_frame, selectmode="day", year=2023, month=3, day=20)
        cal.pack()

        select_butt = customtkinter.CTkButton(master=cal_frame,
                                              text="Select",
                                              width=100,
                                              fg_color='gray',
                                              command=select)
        select_butt.pack(pady=10, side="left")
        cancel_butt = customtkinter.CTkButton(master=cal_frame,
                                              text="Cancel",
                                              width=100,
                                              fg_color='gray',
                                              command=cancel)
        cancel_butt.pack(pady=10, side="right")

    def pick_end_date(event):
        def cancel():
            cal_frame.destroy()

        def select():
            cal_frame.destroy()
            date = cal.get_date()
            end_date_label.config(text=f'{date}\t\t\t')

        cal_frame = Frame(main_frame, borderwidth=4)
        cal_frame.place(x=290, y=260)
        cal = Calendar(cal_frame, selectmode="day", year=2023, month=3, day=20)
        cal.pack()

        select_butt = customtkinter.CTkButton(master=cal_frame,
                                              text="Select",
                                              width=100,
                                              fg_color='gray',
                                              command=select)
        select_butt.pack(pady=10, side="left")
        cancel_butt = customtkinter.CTkButton(master=cal_frame,
                                              text="Cancel",
                                              width=100,
                                              fg_color='gray',
                                              command=cancel)
        cancel_butt.pack(pady=10, side="right")

    start_label = Label(main_frame,
                        text='Start Treatment',
                        font=("consolas", 15))
    start_label.place(x=60, y=130)

    date_img = PhotoImage(file="images/dateicon.png")
    start_date_label = Label(main_frame,
                             text="d/mm/yy\t\t\t",
                             image=date_img,
                             compound="right",
                             anchor="w",
                             borderwidth=4,
                             relief="groove")
    start_date_label.place(x=60, y=160)
    start_date_label.image = date_img
    start_date_label.bind("<Button-1>", pick_start_date)

    end_label = Label(main_frame,
                      text='End Treatment',
                      font=("consolas", 15))
    end_label.place(x=60, y=230)

    end_date_label = Label(main_frame,
                           text="d/mm/yy\t\t\t",
                           image=date_img,
                           compound="right",
                           anchor="w",
                           borderwidth=4,
                           relief="groove")
    end_date_label.place(x=60, y=260)
    end_date_label.image = date_img
    end_date_label.image = date_img
    end_date_label.bind("<Button-1>", pick_end_date)

    summary_label = Label(main_frame,
                          text='Summary',
                          font=("consolas", 15))
    summary_label.place(x=60, y=330)

    summary_text_area = customtkinter.CTkTextbox(master=main_frame,
                                                 width=400,
                                                 height=200,
                                                 border_width=2)
    summary_text_area.place(x=60, y=370)
    summary_text_area.insert("1.0", summary)

    new_visit_butt = customtkinter.CTkButton(master=main_frame,
                                             text="New Visit",
                                             height=50,
                                             fg_color='gray',
                                             command=new_visit)
    new_visit_butt.place(x=550, y=500)

    close_treatment_butt = customtkinter.CTkButton(master=main_frame,
                                                   text="Close Treament",
                                                   height=50,
                                                   fg_color='gray',
                                                   command=close_treatment)
    close_treatment_butt.place(x=700, y=500)

def on_row_click(event):
    # Get the index of the clicked row
    row_index = event.widget.grid_info()['row']
    # Get the first item in the tuple for the clicked row
    first_item = data[row_index - 1][0]
    print(first_item)
    if first_item == 'Treatment1':
        show_treatment(treament1, 'Treament1')
    if first_item == 'Treatment2':
        show_treatment(treament2, 'Treament2')
    if first_item == 'Treatment3':
        show_treatment(treament3, 'Treament3')

def new_treatment():
    for widgets in main_frame.winfo_children():
        widgets.destroy()

    p_label = Label(main_frame,
                    text='Ada Lovelace',
                    font=("consolas", 25))
    p_label.place(x=10, y=20)

    newtreat_label = Label(main_frame,
                           text='New Treatment',
                           font=("consolas", 15, "underline"))
    newtreat_label.place(x=465, y=70)

    def pick_start_date(event):
        def cancel():
            cal_frame.destroy()

        def select():
            cal_frame.destroy()
            date = cal.get_date()
            start_date_label.config(text=f'{date}\t\t\t')

        cal_frame = Frame(main_frame, borderwidth=4)
        cal_frame.place(x=290, y=160)
        cal = Calendar(cal_frame, selectmode="day", year=2023, month=3, day=20)
        cal.pack()

        select_butt = customtkinter.CTkButton(master=cal_frame,
                                              text="Select",
                                              width=100,
                                              fg_color='gray',
                                              command=select)
        select_butt.pack(pady=10, side="left")
        cancel_butt = customtkinter.CTkButton(master=cal_frame,
                                              text="Cancel",
                                              width=100,
                                              fg_color='gray',
                                              command=cancel)
        cancel_butt.pack(pady=10, side="right")

    def pick_end_date(event):
        def cancel():
            cal_frame.destroy()

        def select():
            cal_frame.destroy()
            date = cal.get_date()
            end_date_label.config(text=f'{date}\t\t\t')

        cal_frame = Frame(main_frame, borderwidth=4)
        cal_frame.place(x=290, y=260)
        cal = Calendar(cal_frame, selectmode="day", year=2023, month=3, day=20)
        cal.pack()

        select_butt = customtkinter.CTkButton(master=cal_frame,
                                              text="Select",
                                              width=100,
                                              fg_color='gray',
                                              command=select)
        select_butt.pack(pady=10, side="left")
        cancel_butt = customtkinter.CTkButton(master=cal_frame,
                                              text="Cancel",
                                              width=100,
                                              fg_color='gray',
                                              command=cancel)
        cancel_butt.pack(pady=10, side="right")

    start_label = Label(main_frame,
                        text='Start Treatment',
                        font=("consolas", 15))
    start_label.place(x=60, y=130)

    date_img = PhotoImage(file="images/dateicon.png")
    start_date_label = Label(main_frame,
                             text="d/mm/yy\t\t\t",
                             image=date_img,
                             compound="right",
                             anchor="w",
                             borderwidth=4,
                             relief="groove")
    start_date_label.place(x=60, y=160)
    start_date_label.image = date_img
    start_date_label.bind("<Button-1>", pick_start_date)

    end_label = Label(main_frame,
                      text='End Treatment',
                      font=("consolas", 15))
    end_label.place(x=60, y=230)

    end_date_label = Label(main_frame,
                           text="d/mm/yy\t\t\t",
                           image=date_img,
                           compound="right",
                           anchor="w",
                           borderwidth=4,
                           relief="groove")
    end_date_label.place(x=60, y=260)
    end_date_label.image = date_img
    end_date_label.image = date_img
    end_date_label.bind("<Button-1>", pick_end_date)

    summary_label = Label(main_frame,
                          text='Summary',
                          font=("consolas", 15))
    summary_label.place(x=60, y=330)

    summary_text_area = customtkinter.CTkTextbox(master=main_frame,
                                                 width=400,
                                                 height=200,
                                                 border_width=2)
    summary_text_area.place(x=60, y=370)

    start_new_treatment = customtkinter.CTkButton(master=main_frame,
                                                  text="Start New Treatment",
                                                  height=50,
                                                  fg_color='gray',
                                                  )
    start_new_treatment.place(x=750, y=270)

def start_test():
    # Clear
    for widgets in main_frame.winfo_children():
        widgets.destroy()
    # Back Button
    back_button = customtkinter.CTkButton(master=main_frame,
                                    text="Back",
                                    width=100,
                                    fg_color='gray',
                                    font=('consolas', 15),
                                    command=new_visit)
    back_button.place(x=10, y=20)

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
                                         fg_color='grey',
                                         command=open_test_window)
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
    off = PhotoImage(file='images/off.png')

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
    image = PhotoImage(file='images/head.png')
    image_label = Label(main_frame,
                        image=image)
    image_label.place(x=330, y=280)
    image_label.image = image

def patient():
    for widgets in main_frame.winfo_children():
        widgets.destroy()

    column = ("Patient Name", "Date of Birth", "Edit", "Delete")

    data = (
        ('Ada Lovelace', 'December 10, 1815', 'Edit', 'Delete'),
        ('Bill Gate', 'December 21, 1915', 'Edit', 'Delete'),
        ('Jace Norman', 'October 15, 1815', 'Edit', 'Delete')
    )

    table = Frame(main_frame)
    table.place(x=200, y=50)

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
            if value == "Edit" or value == "Delete":
                label = Label(table,
                    text=value,
                    font="consolas 15 underline",
                    padx=40,
                    pady=30,
                    borderwidth=2,
                    relief="groove")
                label.grid(row=row, column=col, sticky="nsew")
                label.bind("<Button-1>", lambda e: print(e))
            else:
                Label(table,
                    text=value,
                    padx=40,
                    pady=30,
                    borderwidth=2,
                    relief="groove").grid(row=row, column=col, sticky="nsew")

    new_patient_button = customtkinter.CTkButton(master=main_frame,
                                                 text='New Patient',
                                                 fg_color='gray',
                                                 font=("consolas",
                                                       15, "bold"),
                                                 height=50,
                                                 )
                                                # command = new_treatment)
    new_patient_button.place(x=650, y=400)

def patientinfo():
    global data
    for widgets in main_frame.winfo_children():
        widgets.destroy()
    main_frame.config(width=1000,
                      height=600)

    p_label = Label(main_frame,
                    text='Ada Lovelace',
                    font=("consolas", 25))
    p_label.place(x=10, y=20)

    p_label = Label(main_frame,
                    text='Visits Summary',
                    font=("consolas", 15))
    p_label.place(x=80, y=70)
    column = ('Treatment', "Visits", "Date", "Delete")

    data = (
        ('Treatment1', '3 Visits', 'December 10, 1815', 'Delete'),
        ('Treatment2', '2 Visits', 'December 10, 1915', 'Delete'),
        ('Treatment3', '0 Visits', 'December 10, 1815', 'Delete'),
    )

    table = customtkinter.CTkScrollableFrame(main_frame,
                                             height=50,
                                             width=410)
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
            # If name of treatment (col 0)
            if col == 0:
                info = Label(table,
                            text=value,
                            font=("consolas", 15, "underline"),
                            padx=20,
                            pady=15,
                            borderwidth=2,
                            relief="groove",
                            cursor="hand2"
                            )
                info.grid(row=row, column=col, sticky="nsew")
                info.bind('<Button-1>', on_row_click)
            # Delete
            elif value == "Delete":
                info = Label(table,
                            text=value,
                            font=("consolas", 15, "underline"),
                            padx=20,
                            pady=15,
                            borderwidth=2,
                            relief="groove",
                            cursor="hand2"
                            )
                info.grid(row=row, column=col, sticky="nsew")
                # bind Delete Button
                # info.bind('<Button-1>', on_row_click)
            else:
                info = Label(table,
                             text=value,
                             padx=20,
                             pady=15,
                             borderwidth=2,
                             relief="groove"
                             )
                info.grid(row=row, column=col, sticky="nsew")

    new_treatment_button = customtkinter.CTkButton(master=main_frame,
                                                   text='New Treatment',
                                                   fg_color='gray',
                                                   font=("consolas",
                                                         15, "bold"),
                                                   height=50,
                                                   command=new_treatment)
    new_treatment_button.place(x=650, y=400)

    '''newtest_frame = Frame(main_frame,
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
    date_img = PhotoImage(file="images/dateicon.png")
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
    '''

def test_results(event):
    # Clear
    for widgets in main_frame.winfo_children():
        widgets.destroy()
    # Back Button
    back_button = customtkinter.CTkButton(master=main_frame,
                                          text="Back",
                                          width=100,
                                          fg_color='gray',
                                          font=('consolas', 15),
                                          )
                                    # command=new_visit)
    back_button.place(x=10, y=20)

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
                        font=("consolas", 20))
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
