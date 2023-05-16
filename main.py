from tkinter import *
from PIL import Image
import customtkinter
from tkinter import messagebox
import datetime
import data_controller as dc
# import nback as game

import numpy as np
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from tkcalendar import *
import subprocess
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import numpy as np

# from Alfa.Data.BCI_data import TimeAxis, df, ratio




treatment1 = (
    ('Visit 1', 'External', 'December 10, 1815', 'Delete'),
    ('Visit 2', 'Test', 'December 10, 1815', 'Delete'),
    ('Visit 3', 'Summary', 'December 10, 1815', 'Delete'),
)

treatment2 = (
    ('Treatment1', 'visit1', 'December 10, 1815', 'Edit'),
    ('Treatment1', 'visit2', 'December 10, 1815', 'Edit'),
)

treatment3 = (
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


def open_result_window():
    subprocess.Popen(["python", "Data/BCI_data.py"])


def save_source(test_summary, attention_level, external_source, doctor_name):
    visit_type = 'from another source'
    today = datetime.datetime.today().strftime("%m/%d/%Y")
    dc.add_visit(treatment_id, today, visit_type, test_summary, attention_level, external_source, doctor_name)
    show_treatment(treatment_id)


"""
    page **** External Source ****
"""
def new_information(visit_id = None, edit = False, skip = False):
    
    for widgets in main_frame.winfo_children():
        widgets.destroy()

    if not skip:
        l = customtkinter.CTkLabel(frame_breadcrumbs, text=' External Source >', font=("consolas", breadcrumbs_size))
        l.pack(side='left')
        l.bind('<Button-1>', lambda e: new_information(skip=True))
        l.bind('<Enter>', lambda e, labels=[l]: on_enter(labels))
        l.bind('<Leave>', lambda e, labels=[l]: on_leave(labels))
    page_found = False
    for widget in frame_breadcrumbs.winfo_children():
        if page_found:
            widget.destroy()
        if ' External Source >' == widget.cget('text'):
            page_found = True

    main_frame.grid_rowconfigure((0,1,2,4), weight=0)
    main_frame.grid_rowconfigure(3, weight=1)
    main_frame.grid_columnconfigure((0,1), weight=1)
    main_frame.grid_columnconfigure((2,3,4), weight=0)

    # Back Button
    back_button = customtkinter.CTkButton(master=main_frame,
                                          text="Back",
                                          width=100,
                                          font=('consolas', 15),
                                          command=new_visit)
    back_button.grid(row=0, column=0, sticky='W', padx=(20,0), pady=(20,0))

    # p_label = Label(main_frame,
    #                 text='Ada Lovelace',
    #                 font=("consolas", 25))
    # p_label.place(x=10, y=20)

    frame = customtkinter.CTkFrame(main_frame, fg_color='#2b2b2b')
    frame.grid(row=1, column=0, columnspan=2, sticky='EW', padx=50, pady=20)
    treat_label = customtkinter.CTkLabel(frame,
                        text='information from another source :',
                        font=("consolas", 15))
    treat_label.pack(side='left')

    edit_butt = customtkinter.CTkButton(master=frame,
                                        text="Save",
                                        width=100,
                                        font=('consolas', 15)
                                        )
    edit_butt.pack(side='right')

    test_sum_label = customtkinter.CTkLabel(main_frame,
                           text='Test Summary',
                           font=("consolas", 12))
    test_sum_label.grid(row=2, column=0, padx=50, sticky='W')

    test_entry = customtkinter.CTkTextbox(master=main_frame,
                                        border_width=2)
    test_entry.grid(row=3, column=0, sticky='NSEW', padx=50, pady=(0,75))

    attention_level_label = customtkinter.CTkLabel(main_frame,
                                  text='Attention Level',
                                  font=("consolas", 12))
    attention_level_label.grid(row=2, column=1, sticky='W', padx=50)

    frame = customtkinter.CTkFrame(main_frame, fg_color='#2b2b2b')
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure((0,2,4), weight=1)
    frame.grid(row=3, column=1, sticky='NSEW', padx=(50,20), pady=(0,75))
    attention_entry = customtkinter.CTkTextbox(master=frame,
                                             border_width=2)
    attention_entry.grid(row=0, column=0, sticky='NSEW')

    location_label = customtkinter.CTkLabel(frame,
                           text='Location of the source',
                           font=("consolas", 12))
    location_label.grid(row=1, column=0, sticky='W')

    location_entry = customtkinter.CTkTextbox(master=frame,
                                            border_width=2)
    location_entry.grid(row=2, column=0, sticky='NSEW')

    doctor_name_label = customtkinter.CTkLabel(frame,
                              text='Name of the Doctor',
                              font=("consolas", 12,))
    doctor_name_label.grid(row=3, column=0, sticky='W')

    doctor_name_entry = customtkinter.CTkTextbox(master=frame,
                                               border_width=2)
    doctor_name_entry.grid(row=4, column=0, sticky='NSEW')
    edit_butt.configure(command=lambda:save_source(
        test_entry.get("1.0", END).rstrip('\n'),
        attention_entry.get("1.0", END).rstrip('\n'),
        location_entry.get("1.0", END).rstrip('\n'),
        doctor_name_entry.get("1.0", END).rstrip('\n'),
        ))
    if visit_id:
        visit = dc.get_visit_by_id(visit_id)
        back_button.configure(command=lambda:show_treatment(treatment_id))
        try:
            test_entry.insert("1.0", visit[4])
        except:
            pass
        try:
            attention_entry.insert("1.0", visit[5])
        except:
            pass
        try:
            location_entry.insert("1.0", visit[6])
        except:
            pass
        try:
            doctor_name_entry.insert("1.0", visit[8])
        except:
            pass
        if not edit:
            test_entry.configure(state='disabled')
            attention_entry.configure(state='disabled')
            location_entry.configure(state='disabled')
            doctor_name_entry.configure(state='disabled')
            edit_butt.pack_forget()
        else:
            edit_butt.configure(command=lambda:(dc.update_visit(
                visit[0], 
                test_entry.get("1.0", END).rstrip('\n'), 
                attention_entry.get("1.0", END).rstrip('\n'),
                location_entry.get("1.0", END).rstrip('\n'),
                doctor_name_entry.get("1.0", END).rstrip('\n')),
                show_treatment(treatment_id)))


"""
    page **** Summary ****
"""
def new_summary(visit_id=None, edit = False, skip = False):
    for widgets in main_frame.winfo_children():
        widgets.destroy()

    if not skip:
        l = customtkinter.CTkLabel(frame_breadcrumbs, text=' Summary >', font=("consolas", breadcrumbs_size))
        l.pack(side='left')
        l.bind('<Button-1>', lambda e: new_summary(skip=True))
        l.bind('<Enter>', lambda e, labels=[l]: on_enter(labels))
        l.bind('<Leave>', lambda e, labels=[l]: on_leave(labels))
    page_found = False
    for widget in frame_breadcrumbs.winfo_children():
        if page_found:
            widget.destroy()
        if ' Summary >' == widget.cget('text'):
            page_found = True

    main_frame.grid_rowconfigure((0,1,2,4), weight=0)
    main_frame.grid_rowconfigure(3, weight=1)
    main_frame.grid_columnconfigure((0,1), weight=1)
    main_frame.grid_columnconfigure((2,3,4), weight=0)

    # Back Button
    back_button = customtkinter.CTkButton(master=main_frame,
                                          text="Back",
                                          width=100,
                                          font=('consolas', 15),
                                          command=new_visit)
    back_button.grid(row=0, column=0, sticky='W', padx=(20,0), pady=(20,0))
    frame = customtkinter.CTkFrame(main_frame, fg_color='#2b2b2b')
    frame.grid(row=1, column=0, columnspan=2, sticky='EW', padx=50, pady=20)

    treat_label = customtkinter.CTkLabel(frame,
                        text='new summary:',
                        font=("consolas", 15))
    treat_label.pack(side='left')

    edit_butt = customtkinter.CTkButton(master=frame,
                                        text="Save",
                                        width=100,
                                        font=('consolas', 15)
                                        )
    edit_butt.pack(side='right')

    test_sum_label = customtkinter.CTkLabel(main_frame,
                           text='Test Summary', 
                           anchor='w',
                           font=("consolas", 12))
    test_sum_label.grid(row=2, column=0, sticky='EW', padx=50)

    test_entry = customtkinter.CTkTextbox(master=main_frame,
                                        border_width=2)
    test_entry.grid(row=3, column=0, padx=50, pady=(0,75), sticky='NSEW')

    attention_level_label = customtkinter.CTkLabel(main_frame,
                                  text='Attention Level', 
                                  anchor='w',
                                  font=("consolas", 12))
    attention_level_label.grid(row=2, column=1, sticky='EW')

    attention_entry = customtkinter.CTkTextbox(master=main_frame,
                                             border_width=2)
    attention_entry.grid(row=3, column=1, pady=(0,75), sticky='NSEW', padx=(0,50))
    edit_butt.configure(command=lambda:save_summary(test_entry.get("1.0", END).rstrip('\n'), attention_entry.get("1.0", END).rstrip('\n')))
    if visit_id:
        back_button.configure(command=lambda:show_treatment(treatment_id))
        visit = dc.get_visit_by_id(visit_id)
        try:
            test_entry.insert("1.0", visit[4])
        except:
            pass
        try:
            attention_entry.insert("1.0", visit[5])
        except:
            pass
        if not edit:
            attention_entry.configure(state='disabled')
            test_entry.configure(state='disabled')
            edit_butt.pack_forget()
        else:
            edit_butt.configure(command=lambda:(dc.update_visit(
                visit[0],
                test_entry.get("1.0", END).rstrip('\n'),
                attention_entry.get("1.0", END).rstrip('\n'),
                '',
                ''),
                show_treatment(treatment_id)
                )
            )



def save_summary(summary, attention_level):
    visit_type = 'summary'
    today = datetime.datetime.today().strftime("%m/%d/%Y")
    dc.add_visit(treatment_id, today, visit_type, summary, attention_level, '', '')
    show_treatment(treatment_id)


"""
    page **** new visit ****
"""
def new_visit(skip = False):
    for widgets in main_frame.winfo_children():
        widgets.destroy()
    if not skip:
        l = customtkinter.CTkLabel(frame_breadcrumbs, text=' New Visit >', font=("consolas", breadcrumbs_size))
        l.pack(side='left')
        l.bind('<Button-1>', lambda e: new_visit(True))
        l.bind('<Enter>', lambda e, labels=[l]: on_enter(labels))
        l.bind('<Leave>', lambda e, labels=[l]: on_leave(labels))
    page_found = False
    for widget in frame_breadcrumbs.winfo_children():
        if page_found:
            widget.destroy()
        if ' New Visit >' == widget.cget('text'):
            page_found = True
    # Back Button
    main_frame.grid_columnconfigure((0,1), weight=1)
    main_frame.grid_columnconfigure((2,3,4), weight=0)
    main_frame.grid_rowconfigure(1, weight=1)
    main_frame.grid_rowconfigure((0,2,3,4), weight=0)
    back_button = customtkinter.CTkButton(master=main_frame,
                                          text="Back",
                                          width=100,
                                          font=('consolas', 15),
                                          command=lambda: show_treatment(treatment_id, True))
    back_button.grid(row=0, column=0, sticky='W', padx=(20,0), pady=(20,0))
    # p_label = Label(main_frame,
    #                 text='Ada Lovelace',
    #                 font=("consolas", 25))
    # p_label.place(x=10, y=20)

    left_frame = customtkinter.CTkFrame(main_frame, fg_color='#2b2b2b')
    left_frame.grid(row=1, column=0, sticky='NSEW', padx=30, pady=30)
    treat_label = customtkinter.CTkLabel(left_frame,
                        text='New Visit',
                        font=("consolas", 15, "underline"))
    treat_label.pack()
    image = Image.open('images/icon.png')
    image_label = customtkinter.CTkLabel(left_frame, text='',
                        image=customtkinter.CTkImage(light_image=image, size=(370,290)))
    image_label.pack(expand=True, fill='both')
    image_label.image = image

    right_frame = customtkinter.CTkFrame(main_frame, fg_color='#2b2b2b')
    right_frame.grid(row=1, column=1, sticky='NSEW', padx=30, pady=30)

    butt1 = customtkinter.CTkButton(master=right_frame,
                                    text="Add new\ninformation from \n another source",
                                    height=100,
                                    width=200,
                                    font=('consolas', 15),
                                    command=new_information)
    butt1.pack(expand=True, pady=20)

    butt2 = customtkinter.CTkButton(master=right_frame,
                                    text="Add new \n test to available \ntreatment ",
                                    height=100,
                                    font=('consolas', 15),
                                    width=200,
                                    command=start_test)
    butt2.pack(expand=True, pady=20)

    butt3 = customtkinter.CTkButton(master=right_frame,
                                    text="Add new \nsummary",
                                    height=100,
                                    width=200,
                                    font=('consolas', 15),
                                    command=new_summary)
    butt3.pack(expand=True, pady=(20,0))


def close_treatment():
    patientinfo()

def on_row_edit_visit(event):
    global visit_id
    row_index = event.widget.grid_info()['row']
    visit_id = int(data[row_index-1][0])
    visit = dc.get_visit_by_id(visit_id)
    open_edit_visit(visit)

def fill_visit(table, data):
    for child in table.winfo_children():
        child.grid_forget()
    column = ("ID", "treatment_id", "Date", "Visit Type", "Attention Level", "Edit")
    for i in range(len(data)):
        new_row = list(data[i])
        new_row.append("Edit Visit")
        data[i] = new_row
    for col, heading in enumerate(column):
        Label(table, text=heading,
              bg="#808080",
              fg='white',
              border=2,
              padx=10,
              pady=10,
              relief="solid",
              highlightbackground='black',
              font=('Orega One', text_size+3)).grid(row=0, column=col, sticky="nsew")
        table.grid_columnconfigure(col, weight=1)

    for row, record in enumerate(data, start=1):
        labels = []
        for col, value in enumerate(record):
            if col == 3:
                l = Label(table,
                        text=value,
                        padx=5,
                        pady=20,
                        borderwidth=2,
                        font=('Orega One', text_size, 'underline'),
                        relief="solid",
                        highlightbackground='black',
                        fg='white',
                        bg='#242424')
                l.grid(row=row, column=col, sticky="nsew")
                l.bind('<Button-1>', on_row_click_visit)
            elif col == 5:
                l = Label(table,
                        text=value,
                        padx=5,
                        pady=20,
                        borderwidth=2,
                        font=('Orega One', text_size, 'underline'),
                        relief="solid",
                        highlightbackground='black',
                        fg='white',
                        bg='#242424')
                l.grid(row=row, column=col, sticky="nsew")
                l.bind('<Button-1>', on_row_edit_visit)
            else:
                l = Label(table,
                        text=value,
                        padx=5,
                        pady=20,
                        borderwidth=2,
                        font=('Orega One', text_size),
                        relief="solid",
                        highlightbackground='black',
                        fg='white',
                        bg='#242424')
                l.grid(row=row, column=col, sticky="nsew")
            labels.append(l)
            if col == 5 or col == 3:
                l.bind('<Enter>', lambda e, labels=labels: on_enter(labels))
                l.bind('<Leave>', lambda e, labels=labels: on_leave(labels))

def on_row_click_visit(event):
    global visit_id, visit_data
    # Get the index of the clicked row
    row_index = event.widget.grid_info()['row']
    visit_id = visit_data[row_index-1][0]
    visit_type = dc.get_visit_by_id(visit_id)[7]
    if visit_type == 'from another source':
        new_information(visit_id)
    elif visit_type == 'summary':
        new_summary(visit_id)


def filter_visit(*args):
    global treatment_id, visit_data
    visit_data = dc.get_visits(treatment_id=treatment_id, filter=var_visitfilter.get(), 
        col_filter=var_visitoption.get(), sort=var_visitsort.get())
    fill_visit(table_visit, visit_data)


def test1_page(skip = False):
    for widgets in main_frame.winfo_children():
        widgets.destroy()
    scroll_frame = customtkinter.CTkScrollableFrame(main_frame)
    scroll_frame.grid(row=0, column=0, sticky='NSEW')
    main_frame.grid_columnconfigure((1,2,3,4), weight=0)
    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_rowconfigure((1,2,3,4), weight=0)
    main_frame.grid_rowconfigure(0, weight=1)
    customtkinter.CTkButton(main_frame, text='Back', font=('consolas', 20), command=results_page).grid(row=1, column=0, pady=15)
    if not skip:
        l = customtkinter.CTkLabel(frame_breadcrumbs, text=' Test 1 >', font=("consolas", breadcrumbs_size))
        l.pack(side='left')
        l.bind('<Button-1>', lambda e: test1_page(True))
        l.bind('<Enter>', lambda e, labels=[l]: on_enter(labels))
        l.bind('<Leave>', lambda e, labels=[l]: on_leave(labels))
    """window = customtkinter.CTkToplevel()
    window.geometry("500x500")
    window.title('Test 1')
    frm = customtkinter.CTkScrollableFrame(window)
    frm.pack(expand=True, fill='both')
    window.after(100, window.focus)"""


def test2_page(skip = False):
    for widgets in main_frame.winfo_children():
        widgets.destroy()
    scroll_frame = customtkinter.CTkScrollableFrame(main_frame)
    scroll_frame.grid(row=0, column=0, sticky='NSEW')
    main_frame.grid_columnconfigure((1,2,3,4), weight=0)
    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_rowconfigure((1,2,3,4), weight=0)
    main_frame.grid_rowconfigure(0, weight=1)
    customtkinter.CTkButton(main_frame, text='Back', font=('consolas', 20), command=results_page).grid(row=1, column=0, pady=15)
    if not skip:
        l = customtkinter.CTkLabel(frame_breadcrumbs, text=' Test 2 >', font=("consolas", breadcrumbs_size))
        l.pack(side='left')
        l.bind('<Button-1>', lambda e: test2_page(True))
        l.bind('<Enter>', lambda e, labels=[l]: on_enter(labels))
        l.bind('<Leave>', lambda e, labels=[l]: on_leave(labels))
    """window = customtkinter.CTkToplevel()
    window.geometry("500x500")
    window.title('Test 2')
    frm = customtkinter.CTkScrollableFrame(window)
    frm.pack(expand=True, fill='both')
    window.after(100, window.focus)"""


def test3_page(skip = False):
    for widgets in main_frame.winfo_children():
        widgets.destroy()
    scroll_frame = customtkinter.CTkScrollableFrame(main_frame)
    scroll_frame.grid(row=0, column=0, sticky='NSEW')
    main_frame.grid_columnconfigure((1,2,3,4), weight=0)
    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_rowconfigure((1,2,3,4), weight=0)
    main_frame.grid_rowconfigure(0, weight=1)
    customtkinter.CTkButton(main_frame, text='Back', font=('consolas', 20), command=results_page).grid(row=1, column=0, pady=15)
    if not skip:
        l = customtkinter.CTkLabel(frame_breadcrumbs, text=' Test 3 >', font=("consolas", breadcrumbs_size))
        l.pack(side='left')
        l.bind('<Button-1>', lambda e: test3_page(True))
        l.bind('<Enter>', lambda e, labels=[l]: on_enter(labels))
        l.bind('<Leave>', lambda e, labels=[l]: on_leave(labels))
    """window = customtkinter.CTkToplevel()
    window.geometry("500x500")
    window.title('Test 3')
    frm = customtkinter.CTkScrollableFrame(window)
    frm.pack(expand=True, fill='both')
    window.after(100, window.focus)"""


def test4_page(skip = False):
    for widgets in main_frame.winfo_children():
        widgets.destroy()
    scroll_frame = customtkinter.CTkScrollableFrame(main_frame)
    scroll_frame.grid(row=0, column=0, sticky='NSEW')
    main_frame.grid_columnconfigure((1,2,3,4), weight=0)
    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_rowconfigure((1,2,3,4), weight=0)
    main_frame.grid_rowconfigure(0, weight=1)
    customtkinter.CTkButton(main_frame, text='Back', font=('consolas', 20), command=results_page).grid(row=1, column=0, pady=15)
    if not skip:
        l = customtkinter.CTkLabel(frame_breadcrumbs, text=' Test 4 >', font=("consolas", breadcrumbs_size))
        l.pack(side='left')
        l.bind('<Button-1>', lambda e: test4_page(True))
        l.bind('<Enter>', lambda e, labels=[l]: on_enter(labels))
        l.bind('<Leave>', lambda e, labels=[l]: on_leave(labels))
    """window = customtkinter.CTkToplevel()
    window.geometry("500x500")
    window.title('Test 4')
    frm = customtkinter.CTkScrollableFrame(window)
    frm.pack(expand=True, fill='both')
    window.after(100, window.focus)"""

"""
    page **** Summary Results ****
"""
def results_page(skip = False):
    global treatment_id
    for widgets in main_frame.winfo_children():
        widgets.destroy()
    if not skip:
        l = customtkinter.CTkLabel(frame_breadcrumbs, text=' Tests >', font=("consolas", breadcrumbs_size))
        l.pack(side='left')
        l.bind('<Button-1>', lambda e: results_page(True))
        l.bind('<Enter>', lambda e, labels=[l]: on_enter(labels))
        l.bind('<Leave>', lambda e, labels=[l]: on_leave(labels))
    page_found = False
    for widget in frame_breadcrumbs.winfo_children():
        if page_found:
            widget.destroy()
        if ' Tests >' == widget.cget('text'):
            page_found = True
    main_frame.grid_columnconfigure((2,3,4), weight=0)
    main_frame.grid_columnconfigure((0, 1), weight=1)
    main_frame.grid_rowconfigure((0,3,4), weight=0)
    main_frame.grid_rowconfigure((1,2), weight=1)
    customtkinter.CTkLabel(main_frame, text='Summary results', font=("consolas", 25, "underline")).grid(row=0, column=0, columnspan=2, sticky='EW', pady=10)
    customtkinter.CTkButton(main_frame, text='Test 1', font=("consolas bold", 25), command=test1_page).grid(row=1, column=0, ipadx=50, ipady=50)
    customtkinter.CTkButton(main_frame, text='Test 2', font=("consolas bold", 25), command=test2_page).grid(row=1, column=1, ipadx=50, ipady=50)
    customtkinter.CTkButton(main_frame, text='Test 3', font=("consolas bold", 25), command=test3_page).grid(row=2, column=0, ipadx=50, ipady=50)
    customtkinter.CTkButton(main_frame, text='Test 4', font=("consolas bold", 25), command=test4_page).grid(row=2, column=1, ipadx=50, ipady=50)
    customtkinter.CTkButton(main_frame, text='Back', font=("consolas bold", 25), command=lambda:show_treatment(treatment_id)).grid(row=3, column=0, columnspan=2, pady=15)

"""
    page **** Visit ****
"""
def show_treatment(treatment_id, skip = False):
    global start_date_open, end_date_open, table_visit, visit_data
    for widgets in main_frame.winfo_children():
        widgets.destroy()

    if not skip:
        l = customtkinter.CTkLabel(frame_breadcrumbs, text=' Treatment >', font=("consolas", breadcrumbs_size))
        l.pack(side='left')
        l.bind('<Button-1>', lambda e: show_treatment(treatment_id, True))
        l.bind('<Enter>', lambda e, labels=[l]: on_enter(labels))
        l.bind('<Leave>', lambda e, labels=[l]: on_leave(labels))
    page_found = False
    for widget in frame_breadcrumbs.winfo_children():
        if page_found:
            widget.destroy()
        if ' Treatment >' == widget.cget('text'):
            page_found = True
    
    main_frame.grid_columnconfigure((0,2,3,4), weight=0)
    main_frame.grid_columnconfigure(1, weight=1)
    main_frame.grid_rowconfigure((0,1,2,3), weight=0)
    main_frame.grid_rowconfigure(4, weight=1)
    current_treatment = dc.get_treatment_by_id(treatment_id)
    patient_id = int(current_treatment[2])
    current_patient = dc.get_patient_by_id(patient_id)

    p_label = customtkinter.CTkLabel(main_frame,
                    text=current_patient[1] + " " + current_patient[2],
                    font=("consolas", 25))
    p_label.grid(row=0, column=0, padx=(25,0), sticky='W', pady=(25,5))

    treat_label = customtkinter.CTkLabel(main_frame,
                    text=current_treatment[1],
                    font=("consolas", 20))
    treat_label.grid(row=1, column=0, padx=(80,0), sticky='W', pady=(0,25))

    customtkinter.CTkButton(main_frame, text='results', font=("consolas", 20), command=results_page).grid(row=0, rowspan=2, column=1, padx=(0,60), sticky='E')

    # treat_label = Label(main_frame,
    #                     text=treatment_id,
    #                     font=("consolas", 15, "underline"))
    # treat_label.place(x=420, y=70)

    p_label = customtkinter.CTkLabel(main_frame,
                    text='Visits Summary',
                    font=("consolas", 15))
    p_label.grid(row=2, column=1, sticky='W', padx=(25,0))

    frm = customtkinter.CTkFrame(main_frame, fg_color='#2b2b2b')
    frm.grid(row=3, column=1, pady=(20,10), padx=(0, 50), sticky='EW')
    customtkinter.CTkLabel(frm, text='Search', font=('consolas', 20))
    customtkinter.CTkEntry(frm, textvariable=var_visitfilter, width=200).pack(side='left', padx=10)
    var_visitfilter.trace_add('write', filter_visit)
    customtkinter.CTkOptionMenu(frm, values=["ID", "Date", "Visit Type", "Attention Level"], variable=var_visitoption, command=filter_visit).pack(side='left', padx=10)
    customtkinter.CTkOptionMenu(frm, values=["ID", "Date", "Visit Type", "Attention Level"], variable=var_visitsort, command=filter_visit).pack(side='right', padx=10)
    customtkinter.CTkLabel(frm, text='Sort by', font=('consolas', 20)).pack(side='right', padx=10)
    visit_data = dc.get_visits(treatment_id, sort=var_visitsort.get())
    # new_id, name, treatment_id, date, summary, attention_level, external_source
    table_visit = customtkinter.CTkScrollableFrame(main_frame, orientation='vertical', fg_color='#2b2b2b')
    table_visit.grid(row=4, column=1, sticky='NSEW', padx=(0,50), pady=(0,20))
    #table_visit.grid_columnconfigure((0,1,2,3,4,5), weight=1)
    fill_visit(table_visit, visit_data)
    
    def pick_start_date(event):
        global start_date_open, cal_frame
        def cancel():
            cal_frame.destroy()

        def select():
            cal_frame.destroy()
            date = cal.get_date()
            start_date_label.config(text=f'{date}\t\t\t')

        if start_date_open:
            start_date_open = False
            cal_frame.destroy()
            return
        else:
            start_date_open = True

        cal_frame = customtkinter.CTkFrame(start_frame, fg_color='#2b2b2b')
        cal_frame.pack(pady=(5,0), fill='both', expand=True)
        cal = Calendar(cal_frame, selectmode="day", year=2023, month=3, day=20, font='consolas 15')
        cal.pack(fill='both', expand=True, padx=20, pady=10)

        select_butt = customtkinter.CTkButton(master=cal_frame,
                                              text="Select",
                                              width=100,
                                              command=select)
        select_butt.pack(pady=10)
        """cancel_butt = customtkinter.CTkButton(master=cal_frame,
                                              text="Cancel",
                                              width=100,
                                              command=cancel)
        cancel_butt.pack(pady=10, side="right")"""

    def pick_end_date(event):
        global end_date_open, cal_frame
        def cancel():
            cal_frame.destroy()

        def select():
            cal_frame.destroy()
            date = cal.get_date()
            end_date_label.config(text=f'{date}\t\t\t')

        if end_date_open:
            end_date_open = False
            cal_frame.destroy()
            return
        else:
            end_date_open = True

        cal_frame = customtkinter.CTkFrame(end_frame, fg_color='#2b2b2b')
        cal_frame.pack(pady=(5,0), fill='both', expand=True)
        cal = Calendar(cal_frame, selectmode="day", year=2023, month=3, day=20, font='consolas 15')
        cal.pack(fill='both', expand=True, padx=20, pady=10)

        select_butt = customtkinter.CTkButton(master=cal_frame,
                                              text="Select",
                                              width=100,
                                              command=select)
        select_butt.pack(pady=10)
        """cancel_butt = customtkinter.CTkButton(master=cal_frame,
                                              text="Cancel",
                                              width=100,
                                              command=cancel)
        cancel_butt.pack(pady=10, side="right")"""

    start_date_open = False
    end_date_open = False

    left_frame = customtkinter.CTkFrame(main_frame, fg_color='#2b2b2b')
    left_frame.grid(row=3, rowspan=2, column=0, sticky='NS', padx=(15,15))
    start_frame = customtkinter.CTkFrame(left_frame, fg_color='#2b2b2b')
    start_frame.pack()
    start_label = customtkinter.CTkLabel(start_frame,
                        text='Start Treatment',
                        font=("consolas", 25))
    start_label.pack()

    date_img = PhotoImage(file="images/dateicon.png")

    start_date_label = tk.Label(start_frame,
                            text="d/mm/yy\t\t\t",
                            image=date_img,
                            compound="right",
                            font=('Orega One', 25),
                            fg='white',
                            bg='#242424',
                            anchor="w",
                            borderwidth=4,
                            relief="groove")
    start_date_label.pack(fill='x')
    start_date_label.image = date_img
    start_date_label.bind("<Button-1>", pick_start_date)

    start_date_label.config(text=f'{current_treatment[3]}\t\t\t')

    end_frame = customtkinter.CTkFrame(left_frame, fg_color='#2b2b2b')
    end_frame.pack()

    end_label = customtkinter.CTkLabel(end_frame,
                      text='End Treatment',
                      font=("consolas", 25))
    end_label.pack()

    end_date_label = Label(end_frame,
                           text="d/mm/yy\t\t\t",
                           image=date_img,
                           compound="right",
                           font=('Orega One', 25),
                           fg='white',
                           bg='#242424',
                           anchor="w",
                           borderwidth=4,
                           relief="groove")
    end_date_label.pack(fill='x')
    end_date_label.image = date_img
    end_date_label.image = date_img
    end_date_label.bind("<Button-1>", pick_end_date)

    end_date_label.config(text=f'{current_treatment[4]}\t\t\t')
    summary_label = customtkinter.CTkLabel(left_frame,
                          text='Summary',
                          font=("consolas", 25))
    summary_label.pack()

    summary_text_area = customtkinter.CTkTextbox(master=left_frame,
                                                 border_width=2)
    summary_text_area.pack(fill='x')
    summary_text_area.insert("1.0", current_treatment[-1])

    bottom_frame = customtkinter.CTkFrame(master=main_frame, fg_color='#2b2b2b')
    bottom_frame.grid(row=5, column=0, columnspan=2, pady=(15, 15), sticky='EW')

    new_visit_butt = customtkinter.CTkButton(master=bottom_frame,
                                             text="New Visit",
                                             height=50,
                                             command=new_visit)
    new_visit_butt.pack(expand=True, side='left')

    """
    edit_visit_butt = customtkinter.CTkButton(master=bottom_frame,
                                             text="Edit Visit",
                                             height=50,
                                             command=edit_visit)
    edit_visit_butt.pack(expand=True, side='left')
    """

    delete_visit_butt = customtkinter.CTkButton(master=bottom_frame,
                                             text="Delete Visit",
                                             height=50,
                                             command=delete_visit)
    delete_visit_butt.pack(expand=True, side='left')    

    close_treatment_butt = customtkinter.CTkButton(master=bottom_frame,
                                                   text="Close treatment",
                                                   height=50,
                                                   command=close_treatment)
    close_treatment_butt.pack(expand=True, side='left')


def delete_visit():
    dialog = customtkinter.CTkInputDialog(text="Type ID of visit to be deleted:", title="Delete visit")
    text = dialog.get_input()  # waits for input
    if not text.isdigit():
        messagebox.showerror('Error', 'ID must be a number.')
    else:
        visits = dc.get_visits(treatment_id, sort=var_visitsort.get())
        name = ''
        for item in visits:
            if item[0] == int(text) and item[1] == treatment_id:
                name = f"{item[3]}"
                break
        if not name:
            messagebox.showerror('Error', 'ID of Visit not found.')
        elif messagebox.askyesno('Delete Visit', f'Are you sure you want to delete the visit with type {name}?') and dc.remove_visit(int(text)):
            show_treatment(treatment_id)


def update_visit(visit_id, visit_name, visit_date, summary, attention_level, external_source):
    if not visit_name:
        messagebox.showerror('Error', 'No visit name found.')
    else:
        new_date = datetime.datetime.strptime(visit_date, "%m/%d/%y").strftime("%m/%d/%Y")
        dc.update_visit(visit_id, visit_name, new_date, summary, attention_level, external_source)
        close_visit()
        show_treatment(treatment_id)

def close_visit():
    global edit_visit_visible
    edit_visit_visible = False
    edit_visit_window.destroy()

def edit_visit():
    global edit_visit_visible, edit_visit_window
    dialog = customtkinter.CTkInputDialog(text="Type ID of visit to be edited:", title="Edit visit")
    text = dialog.get_input()  # waits for input
    if not text.isdigit():
        messagebox.showerror('Error', 'ID must be a number.')
    else:
        visit = dc.get_visit_by_id(int(text))
        if not visit:
            messagebox.showerror('Error', 'ID of visit not found.')
        else:
            open_edit_visit(visit)
            #window.after(100, edit_visit_window.focus)

def open_edit_visit(visit):
    if visit[7] == 'from another source':
        new_information(visit[0], True)
    elif visit[7] == 'summary':
        new_summary(visit_id, True)

"""
edit_visit_visible = False
def open_edit_visit(visit):
    global edit_visit_visible, edit_visit_window
    if not edit_visit_visible:
        edit_visit_visible = True
        edit_visit_window = customtkinter.CTkToplevel()
        edit_visit_window.title('Visit')
        edit_visit_window.resizable(False, False)
        customtkinter.CTkLabel(edit_visit_window, text="Visit Name:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        entry_visit_name = customtkinter.CTkEntry(edit_visit_window)
        entry_visit_name.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        entry_visit_name.insert(0, visit[1])
        customtkinter.CTkLabel(edit_visit_window, text="Date:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        cal = Calendar(edit_visit_window, selectmode="day", year=2023, month=1, day=1)
        cal.grid(row=1, column=1, padx=10, pady=10, sticky="e")
        cal.selection_set(visit[3])
        customtkinter.CTkLabel(edit_visit_window, text="Summary:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        summary = customtkinter.CTkTextbox(edit_visit_window)
        summary.grid(row=2, column=1, padx=10, pady=10, sticky="e")
        summary.insert("1.0", visit[4])
        customtkinter.CTkLabel(edit_visit_window, text="Attention Level:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        entry_attention_level = customtkinter.CTkEntry(edit_visit_window)
        entry_attention_level.grid(row=3, column=1, padx=10, pady=10, sticky="ew")
        entry_attention_level.insert(0, visit[5])
        customtkinter.CTkLabel(edit_visit_window, text="External Source:").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        entry_external_source = customtkinter.CTkEntry(edit_visit_window)
        entry_external_source.grid(row=4, column=1, padx=10, pady=10, sticky="ew")
        entry_external_source.insert(0, visit[6])
        submit_button = customtkinter.CTkButton(edit_visit_window, 
            text='Submit',
            command=lambda:update_visit(
                visit[0],
                entry_visit_name.get(), 
                cal.get_date(), 
                summary.get("1.0", END).rstrip('\n'), 
                entry_attention_level.get(), 
                entry_external_source.get()
            )
        )
        edit_visit_window.protocol("WM_DELETE_WINDOW", close_visit) 
        submit_button.grid(row=5, column=0, columnspan=2, padx=20, pady=15, sticky="s")
"""

def on_row_click_patient(event):
    global patient_id
    # Get the index of the clicked row
    row_index = event.widget.grid_info()['row']
    patient_id = int(data[row_index-1][0])
    patientinfo_click()
    # patientinfo()

def on_row_edit_patient(event):
    global edit_patient_window
    row_index = event.widget.grid_info()['row']
    patient_id = int(data[row_index-1][0])
    patient = dc.get_patient_by_id(patient_id)
    if not add_patient_opened:
        edit_patient_opened = True
        edit_patient_window = PatientWindow(patient_id=patient[0], first_name=patient[1], last_name=patient[2], birth_date=patient[3], phone=patient[4], email=patient[5], mode='edit')
    window.after(100, edit_patient_window.focus)


def on_row_click_treatment(event):
    global treatment_id
    # Get the index of the clicked row
    row_index = event.widget.grid_info()['row']
    treatment_id = treatment_data[row_index-1][0]
    show_treatment(treatment_id)




"""
# New treatment button
def new_treatment(patient_id):
    for widgets in main_frame.winfo_children():
        widgets.destroy()

    p_label = customtkinter.CTkLabel(main_frame,
                    text='Ada Lovelace',
                    font=("consolas", 25))
    p_label.place(x=10, y=20)

    newtreat_label = customtkinter.CTkLabel(main_frame,
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

        cal_frame = customtkinter.CTkFrame(main_frame, borderwidth=4)
        cal_frame.place(x=290, y=160)
        cal = Calendar(cal_frame, selectmode="day", year=2023, month=3, day=20)
        cal.pack()

        select_butt = customtkinter.CTkButton(master=cal_frame,
                                              text="Select",
                                              width=100,
                                              command=select)
        select_butt.pack(pady=10, side="left")
        cancel_butt = customtkinter.CTkButton(master=cal_frame,
                                              text="Cancel",
                                              width=100,
                                              command=cancel)
        cancel_butt.pack(pady=10, side="right")

    def pick_end_date(event):
        def cancel():
            cal_frame.destroy()

        def select():
            cal_frame.destroy()
            date = cal.get_date()
            end_date_label.config(text=f'{date}\t\t\t')

        cal_frame = customtkinter.CTkFrame(main_frame, borderwidth=4)
        cal_frame.place(x=290, y=260)
        cal = Calendar(cal_frame, selectmode="day", year=2023, month=3, day=20)
        cal.pack()

        select_butt = customtkinter.CTkButton(master=cal_frame,
                                              text="Select",
                                              width=100,
                                              command=select)
        select_butt.pack(pady=10, side="left")
        cancel_butt = customtkinter.CTkButton(master=cal_frame,
                                              text="Cancel",
                                              width=100,
                                              command=cancel)
        cancel_butt.pack(pady=10, side="right")

    start_label = customtkinter.CTkLabel(main_frame,
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

    end_label = customtkinter.CTkLabel(main_frame,
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

    summary_label = customtkinter.CTkLabel(main_frame,
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
                                                  command=lambda:
                                                  add_treatment("New_treatment_"+str(patient_id),
                                                                patient_id,
                                                                start_date_label['text'][:-len("\t\t\t")],
                                                                end_date_label['text'][:-len("\t\t\t")],
                                                                summary_text_area.get('1.0', END)[:-len("\n")])
                                                  )
    start_new_treatment.place(x=750, y=270)
"""


"""
    page **** Test ****
"""
def start_test(skip = False):

    subprocess.Popen(["BrainLinkConnect/bin/Release/BrainLinkConnect.exe"])
    # Clear
    for widgets in main_frame.winfo_children():
        widgets.destroy()

    if not skip:
        l = customtkinter.CTkLabel(frame_breadcrumbs, text=' Test >', font=("consolas", breadcrumbs_size))
        l.pack(side='left')
        l.bind('<Button-1>', lambda e: start_test(skip=True))
        l.bind('<Enter>', lambda e, labels=[l]: on_enter(labels))
        l.bind('<Leave>', lambda e, labels=[l]: on_leave(labels))
    page_found = False
    for widget in frame_breadcrumbs.winfo_children():
        if page_found:
            widget.destroy()
        if ' Test >' == widget.cget('text'):
            page_found = True
    
    main_frame.grid_columnconfigure((0), weight=1)
    main_frame.grid_columnconfigure((1,2,3,4), weight=0)
    main_frame.grid_rowconfigure(2, weight=1)
    main_frame.grid_rowconfigure((0,1,3,4), weight=0)
    # Back Button
    back_button = customtkinter.CTkButton(master=main_frame,
                                          text="Back",
                                          width=100,
                                          font=('consolas', 15),
                                          command=new_visit)
    back_button.grid(row=0, column=0, sticky='W', padx=(20,0), pady=(20,0))

    p_label2 = customtkinter.CTkLabel(main_frame,
                     text='Conor CPT test:', anchor='w',
                     font=("consolas", 25))
    p_label2.grid(row=1, column=0, padx=50, pady=(25,0), sticky='W')

    start_frame = customtkinter.CTkFrame(main_frame)
    start_frame.grid(row=2, column=0, sticky='NSEW', padx=50, pady=(0,50))

    start_butt = customtkinter.CTkButton(master=start_frame,
                                         text="Start Test",
                                         font=("consolas", 20),
                                         command=open_test_window)
    start_butt.pack(expand=True)

    frm = customtkinter.CTkFrame(main_frame, fg_color='#2b2b2b')
    frm.grid(row=2, column=1, sticky='NSEW', padx=(0,20), pady=(0,50))
    inst_frame = customtkinter.CTkFrame(frm, fg_color='#242424', corner_radius=15)
    inst_frame.pack(expand=True, fill='x')

    inst_text1 = customtkinter.CTkLabel(inst_frame,
                       text="Instructions:",
                       font=("consolas", 15, "bold", "underline"), anchor='w')
    inst_text1.pack(fill='x', pady=(15,0), padx=20)

    inst_text2 = customtkinter.CTkLabel(inst_frame,
                       text="Press Space \n when the \n correct\n shape appears",
                       font=("consolas", 15))
    inst_text2.pack(expand=True, pady=(0,15), padx=20)

    end_butt = customtkinter.CTkButton(master=frm,
                                       text="Show BCI Results",
                                       font=("consolas", 20),
                                       command=test_results)
    end_butt.pack(side='bottom')
    #
    # toggle_text = Label(main_frame,
    #                     text="Connect to BCI kit",
    #                     font=("consolas", 15, "bold"))
    # toggle_text.place(x=750, y=90)
    #
    # def on_on(event):
    #     global off_label
    #
    #     on_label.destroy()
    #     off_label = Label(main_frame,
    #                       image=off)
    #     off_label.place(x=820, y=120)
    #     off_label.image = off
    #     off_label.bind("<Button-1>", on_off)
    #
    # def on_off(event):
    #     global on_label
    #
    #     off_label.destroy()
    #     on_label = Label(main_frame,
    #                      image=on)
    #     on_label.place(x=820, y=120)
    #     on_label.image = on
    #     on_label.bind("<Button-1>", on_on)
    #
    # on = PhotoImage(file='images/on.png')
    # off = PhotoImage(file='images/off.png')
    #
    # off_label = Label(main_frame,
    #                   image=off)
    # off_label.place(x=820, y=120)
    #
    # off_label.image = off
    #
    # off_label.bind("<Button-1>", on_off)



"""
    page **** home *****
"""
def home(event = None):
    create_menu('home')
    try:
        label_menu.destroy()
    except:
        pass
    for widgets in frame_breadcrumbs.winfo_children():
        widgets.destroy()
    for widgets in main_frame.winfo_children():
        widgets.destroy()

    l = customtkinter.CTkLabel(frame_breadcrumbs, text=' Home >', font=("consolas", breadcrumbs_size))
    l.pack(side='left')
    l.bind('<Button-1>', home_click)
    l.bind('<Enter>', lambda e, labels=[l]: on_enter(labels))
    l.bind('<Leave>', lambda e, labels=[l]: on_leave(labels))
    doc = dc.get_doctor()
    f = customtkinter.CTkFrame(main_frame)
    f.pack(fill='x')
    customtkinter.CTkLabel(f, text=f'Hello Doctor {doc[1]}', font=('consolas', 20)).grid(row=0, column=0, padx=15, pady=5)
    text = '''
Nowadays we can see that there are various methods for conducting a preliminary diagnosis in order to identify ADHD, \n such as cognitive tests, testing biological measures and using brain wave technologies such as BCI.

Due to the fact that there are many methods for diagnosing ADHD it can be argued that there is no unequivocal method \nfor diagnosing the issue.

In parallel with the methods of preliminary diagnosis, it can be seen that there are a large number of means to indicate \n and monitor the severity of the ADHD phenomenon during the existence of therapy which again indicates a lack of insignificance regarding \n the use of existing auditing tools.

In addition to the current issues that have been mentioned there is another problem when it comes to the different \n treatment methods that every medical institute or therapist offers. Treatment methods can be through medications, physical training,\n cognitive therapy and more.

'''
    text_label = customtkinter.CTkLabel(main_frame,
                       text=text,
                       font=("consolas", 10))
    text_label.pack(fill='both', expand=True)
    image = Image.open('images/icon.png')
    image_label = customtkinter.CTkLabel(main_frame, text='',
                        image=customtkinter.CTkImage(light_image=image, size=(370,290)))
    image_label.pack(fill='both', expand=True, side='bottom')
    image_label.image = image


def filter_patient(*args):
    data = dc.get_patients(filter=var_filter.get(), col_filter=var_patientoption.get(), sort=var_patientsort.get())
    fill_patients(table_patient, data)

def on_enter(labels):
    for label in labels:
        try:
            label.configure(bg="#2752D6")
        except:
            label.configure(bg_color="#2752D6")

def on_leave(labels):
    for label in labels:
        try:
            label.configure(bg='#242424')
        except:
            label.configure(bg_color="#242424")

def fill_patients(table, data):
    for child in table.winfo_children():
        child.grid_forget()
    column = ("ID", "First Name", "Last Name", "Date of Birth", "Edit")
    for i in range(len(data)):
        new_row = list(data[i])
        new_row.pop()
        new_row.pop()
        new_row.append('Edit Patient')
        data[i] = new_row
    for col, heading in enumerate(column):
        Label(table,
              text=heading,
              bg="#808080",
              fg='white',
              border=2,
              padx=40,
              pady=10,
              relief="solid",
              highlightbackground='black',
              font=('Orega One', text_size+3)).grid(row=0, column=col, sticky="nsew")

    for row, record in enumerate(data, start=1):
        labels = []
        record = list(record)
        for col, value in enumerate(record):
            if col == 4 or col == 1:
                label = Label(table,
                    text=value,
                    padx=40,
                    pady=30,
                    borderwidth=2,
                    font=('Orega One', text_size, 'underline'),
                    relief="solid",
                    highlightbackground='black',
                    fg='white',
                    bg='#242424')

                table.grid_columnconfigure(col, weight=1)
                table.grid_rowconfigure(row, weight=1)
                label.grid(row=row, column=col, sticky="nsew")
                label.bind("<Button-1>", on_row_click_patient)
            else:
                label = Label(table,
                text=value,
                padx=40,
                pady=30,
                borderwidth=2,
                font=('Orega One', text_size),
                relief="solid",
                highlightbackground='black',
                fg='white',
                bg='#242424')

                table.grid_columnconfigure(col, weight=1)
                table.grid_rowconfigure(row, weight=1)
                label.grid(row=row, column=col, sticky="nsew")
                label.bind("<Button-1>", on_row_click_patient)
            labels.append(label)
            if col == 4 or col == 1:
                label.bind('<Enter>', lambda e, labels=labels:on_enter(labels))
                label.bind('<Leave>', lambda e, labels=labels:on_leave(labels))
            if col == 4:
                label.bind("<Button-1>", on_row_edit_patient)


menu_opened = False
def open_menu(label_menu):
    global menu_opened
    menu_opened = True
    label_menu.configure(image=customtkinter.CTkImage(light_image=Image.open('images/close.png')))
    label_menu.bind('<Button-1>', lambda e: close_menu(label_menu))
    frm_menu.grid(row=1, rowspan=3, column=0, sticky='NSEW', padx=20, pady=20)

def close_menu(label_menu):
    global menu_opened
    menu_opened = False
    label_menu.configure(image=customtkinter.CTkImage(light_image=Image.open('images/menu.png')))
    label_menu.bind('<Button-1>', lambda e: open_menu(label_menu))
    frm_menu.grid_forget()

"""
    page **** Patient ****
"""
def patient(event = None):
    global data, var_filter, var_patientoption, table_patient, label_home, label_menu, menu_opened
    for widgets in main_frame.winfo_children():
        widgets.destroy()
    create_menu('patient')
    try:
        label_menu.destroy()
    except:
        pass
    if not menu_opened:
        label_menu = customtkinter.CTkLabel(window, image=customtkinter.CTkImage(light_image=Image.open('images/menu.png'), 
                size=(25,25)), text='')
        label_menu.bind('<Button-1>', lambda e: open_menu(label_menu))
    else:
        label_menu = customtkinter.CTkLabel(window, image=customtkinter.CTkImage(light_image=Image.open('images/close.png'), 
                size=(25,25)), text='')
        label_menu.bind('<Button-1>', lambda e: close_menu(label_menu))
    label_menu.grid(row=0, column=0, padx=(15,0), pady=5, sticky='W')
    l = customtkinter.CTkLabel(frame_breadcrumbs, text=' Patient >', font=("consolas", breadcrumbs_size))
    l.pack(side='left')
    l.bind('<Button-1>', patient_click)
    l.bind('<Enter>', lambda e, labels=[l]: on_enter(labels))
    l.bind('<Leave>', lambda e, labels=[l]: on_leave(labels))

    page_found = False
    for widget in frame_breadcrumbs.winfo_children():
        if page_found:
            widget.destroy()
        if ' Patient >' == widget.cget('text'):
            page_found = True

    data = dc.get_patients(sort=var_patientsort.get())
    frm = customtkinter.CTkFrame(main_frame, fg_color='#2b2b2b')
    frm.pack(pady=(50,10), padx=50, fill='x')
    customtkinter.CTkLabel(frm, text='Search', font=('consolas', 20)).pack(side='left', padx=10)
    customtkinter.CTkEntry(frm, textvariable=var_filter, width=200).pack(side='left', padx=10)
    var_filter.trace_add('write', filter_patient)
    customtkinter.CTkOptionMenu(frm, values=['ID', 'First Name', 'Last Name', 'Date of Birth'], variable=var_patientoption, command=filter_patient).pack(side='left', padx=10)
    customtkinter.CTkOptionMenu(frm, values=['ID', 'First Name', 'Last Name', 'Date of Birth'], variable=var_patientsort, command=filter_patient).pack(side='right', padx=10)
    customtkinter.CTkLabel(frm, text='Sort by', font=('consolas', 20)).pack(side='right', padx=10)
    table_patient = customtkinter.CTkScrollableFrame(main_frame)
    table_patient.pack(expand=True, fill='both', padx=50, pady=(0,50))

    fill_patients(table_patient, data)

    frm = customtkinter.CTkFrame(master=main_frame, fg_color='#2b2b2b')
    frm.pack(side='bottom', pady=15, fill='x')

    new_patient_button = customtkinter.CTkButton(master=frm,
                                                 text='New Patient',
                                                 font=("consolas",
                                                       15, "bold"),
                                                 height=50,
                                                 command=add_patient)
    new_patient_button.pack(expand=True, side='left')

    delete_patient_button = customtkinter.CTkButton(master=frm,
                                                 text='Delete Patient',
                                                 font=("consolas",
                                                       15, "bold"),
                                                 height=50,
                                                 command=delete_patient)
    delete_patient_button.pack(expand=True, side='left')

    """
    edit_patient_button = customtkinter.CTkButton(master=frm,
                                                 text='Edit Patient',
                                                 font=("consolas",
                                                       15, "bold"),
                                                 height=50,
                                                 command=edit_patient)
    edit_patient_button.pack(expand=True, side='left')
    """

def edit_patient():
    global edit_patient_opened, edit_patient_window
    dialog = customtkinter.CTkInputDialog(text="Type ID of patient to be edited:", title="Edit patient")
    text = dialog.get_input()  # waits for input
    if not text.isdigit():
        messagebox.showerror('Error', 'ID must be a number.')
    else:
        patient = dc.get_patient_by_id(int(text))
        if not patient:
            messagebox.showerror('Error', 'ID of patient not found.')
        else:
            if not add_patient_opened:
                edit_patient_opened = True
                edit_patient_window = PatientWindow(patient_id=patient[0], first_name=patient[1], last_name=patient[2], birth_date=patient[3], mode='edit')
            window.after(100, edit_patient_window.focus)

def confirm_edit_patient(patient_id, first_name, last_name, phone, email, birth_date):
    global edit_patient_window
    if not first_name or not last_name:
        messagebox.showerror('Error', 'Please enter all the information of the patient.', master=edit_patient_window)
        edit_patient_window.focus()
    else:
        new_date = datetime.datetime.strptime(birth_date, "%m/%d/%y").strftime("%m/%d/%Y")
        dc.update_patient(patient_id, first_name, last_name, phone, email, new_date)
        close_patient(edit_patient_window, 'edit')
        patient()

def delete_patient():
    dialog = customtkinter.CTkInputDialog(text="Type ID of patient to be deleted:", title="Delete patient")
    text = dialog.get_input()  # waits for input
    if not text.isdigit():
        messagebox.showerror('Error', 'ID must be a number.')
    else:
        patients = dc.get_patients(sort=var_patientsort.get())
        name = ''
        for item in patients:
            if item[0] == int(text):
                name = f"{item[1]} {item[2]}"
                break
        if not name:
            messagebox.showerror('Error', 'ID of patient not found.')
        elif messagebox.askyesno('Delete Patient', f'Are you sure you want to delete the patient {name}?') and dc.remove_patient(int(text)):
            patient()

def close_patient(window, mode = 'add'):
    global add_patient_opened, edit_patient_opened
    if mode == 'add':
        add_patient_opened = False
    elif mode == 'edit':
        edit_patient_opened = False
    window.destroy()

class PatientWindow(customtkinter.CTkToplevel):
    def __init__(self, first_name = None, last_name = None, phone = None, email = None, birth_date = None, mode = 'add', patient_id = None,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Patient')
        self.protocol("WM_DELETE_WINDOW", lambda:close_patient(self, mode))
        self.geometry("500x450")
        self.resizable(False, False)  
        label_first_name = customtkinter.CTkLabel(self, text="First Name:")
        label_first_name.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.entry_first_name = customtkinter.CTkEntry(self)
        self.entry_first_name.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        # create a label and entry for the last name
        label_last_name = customtkinter.CTkLabel(self, text="Last Name:")
        label_last_name.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.entry_last_name = customtkinter.CTkEntry(self)
        self.entry_last_name.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        label_phone = customtkinter.CTkLabel(self, text="Phone Number:")
        label_phone.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.entry_phone = customtkinter.CTkEntry(self)
        self.entry_phone.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        label_email = customtkinter.CTkLabel(self, text="Email:")
        label_email.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.entry_email = customtkinter.CTkEntry(self)
        self.entry_email.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

        # create a label and entry for the date of birth
        label_dob = customtkinter.CTkLabel(self, text="Date of Birth:")
        label_dob.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.cal = Calendar(self, selectmode="day", year=2000, month=1, day=1, font='consolas 15')
        self.cal.grid(row=4, column=1, padx=10, pady=10, sticky="NSEW")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(4, weight=1)
        if first_name:
            self.entry_first_name.insert(0, first_name)
            self.entry_last_name.insert(0, last_name)
            if phone:
                self.entry_phone.insert(0, phone)
            if email:
                self.entry_email.insert(0, email)
            self.cal.selection_set(birth_date)
        self.submit_button = customtkinter.CTkButton(self, 
            text='Submit', 
            command=lambda:submit_patient(
                self.entry_first_name.get(), 
                self.entry_last_name.get(),
                self.entry_phone.get(),
                self.entry_email.get(),
                self.cal.get_date()
            ))
        if mode == 'edit':
            self.submit_button.configure(command=lambda:confirm_edit_patient(
                patient_id=patient_id,
                first_name=self.entry_first_name.get(),
                last_name=self.entry_last_name.get(),
                phone=self.entry_phone.get(),
                email=self.entry_email.get(),
                birth_date=self.cal.get_date()
            ))
        self.submit_button.grid(row=5, column=0, columnspan=2, padx=20, pady=15, sticky="s")


add_patient_opened = add_patient_window = edit_patient_opened = edit_patient_window = False
def add_patient():
    global add_patient_opened, add_patient_window
    if not add_patient_opened:
        add_patient_opened = True
        add_patient_window = PatientWindow()
    window.after(100, add_patient_window.focus)


def submit_patient(first_name, last_name, phone, email, birth_date):
    global add_patient_window
    if not first_name or not last_name:
        messagebox.showerror('Error', 'Please enter all the information of the patient.', master=add_patient_window)
        add_patient_window.focus()
    else:
        new_date = datetime.datetime.strptime(birth_date, "%m/%d/%y").strftime("%m/%d/%Y")
        dc.add_patient(first_name, last_name, phone, email, new_date)
        close_patient(add_patient_window)
        patient()

def filter_treatment(*args):
    global patient_id
    data = dc.get_treatments(patient_id=patient_id, filter=var_treatmentfilter.get(), 
        col_filter=var_treatmentoption.get(), sort=var_treatmentsort.get())
    fill_treatments(table_treatment, data)

def fill_treatments(table, data):
    for child in table.winfo_children():
        child.grid_forget()
    column = ("Treatment ID", "Treatment Name", "Patient ID", "Start Date", "End Date", "Summary", "Edit")
    for i in range(len(data)):
        new_row = list(data[i])
        new_row.append('Edit Treatment')
        data[i] = new_row
    for col, heading in enumerate(column):
        Label(table,
              text=heading,
              bg="#808080",
              fg='white',
              border=2,
              padx=40,
              pady=10,
              relief="solid",
              highlightbackground='black',
              font=('Orega One', text_size+3)).grid(row=0, column=col, sticky="nsew")
        table.grid_columnconfigure(col, weight=1)

    for row, record in enumerate(data, start=1):
        labels = []
        table.grid_rowconfigure(row, weight=1)
        for col, value in enumerate(record):
            # If name of treatment (col 0)
            if col == 6:
                info = Label(table,
              text=value,
              padx=40,
              pady=30,
              borderwidth=2,
              font=('Orega One', text_size, "underline"),
              relief="solid",
              highlightbackground='black',
              fg='white',
              bg='#242424')
                info.grid(row=row, column=col, sticky="nsew")
                info.bind("<Button-1>", on_row_edit_treatment)
            elif col == 1:
                info = Label(table,
              text=value,
              padx=40,
              pady=30,
              borderwidth=2,
              font=('Orega One', text_size, "underline"),
              relief="solid",
              highlightbackground='black',
              fg='white',
              bg='#242424')
                info.grid(row=row, column=col, sticky="nsew")
                info.bind('<Button-1>', on_row_click_treatment)
            else:
                info = Label(table,
              text=value,
              padx=40,
              pady=30,
              borderwidth=2,
              font=('Orega One', text_size),
              relief="solid",
              highlightbackground='black',
              fg='white',
              bg='#242424')
                info.grid(row=row, column=col, sticky="nsew")
            labels.append(info)
            if col == 1 or col == 6:
                info.bind('<Enter>', lambda e, labels=labels:on_enter(labels))
                info.bind('<Leave>', lambda e, labels=labels:on_leave(labels))

def on_row_edit_treatment(event):
    global edit_treatment_window, add_treatment_opened
    row_index = event.widget.grid_info()['row']
    treatment_id = int(data[row_index-1][0])
    treatment = dc.get_treatment_by_id(treatment_id)
    edit_treatment_window = TreatmentWindow(treatment_id=treatment[0], patient_id=treatment[2], treatment_name=treatment[1], 
                start_date=treatment[3], end_date=treatment[4], summary=treatment[5])
    window.after(100, edit_treatment_window.focus)


def calculate_age(birth_date):
    today = datetime.date.today()
    age = today.year - birth_date.year
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1
    return age

"""
    page **** Treatment ****
"""
def patientinfo(event = None):
    global treatment_data, patient_id, var_treatmentfilter, var_treatmentoption, table_treatment, label_menu, menu_opened
    current_patient = dc.get_patient_by_id(patient_id)
    if not current_patient:
        messagebox.showerror('Error', 'No patient selected')
        return
    for widgets in main_frame.winfo_children():
        widgets.destroy()
    try:
        label_menu.destroy()
    except:
        pass
    if not menu_opened:
        label_menu = customtkinter.CTkLabel(window, image=customtkinter.CTkImage(light_image=Image.open('images/menu.png'), 
                size=(25,25)), text='')
        label_menu.bind('<Button-1>', lambda e: open_menu(label_menu))
    else:
        label_menu = customtkinter.CTkLabel(window, image=customtkinter.CTkImage(light_image=Image.open('images/close.png'), 
                size=(25,25)), text='')
        label_menu.bind('<Button-1>', lambda e: close_menu(label_menu))
    label_menu.grid(row=0, column=0, padx=(15,0), pady=5, sticky='W')
    create_menu('patient_info')
    l = customtkinter.CTkLabel(frame_breadcrumbs, text=' Patient Info >', font=("consolas", breadcrumbs_size))
    l.pack(side='left')
    l.bind('<Button-1>', patientinfo_click)
    l.bind('<Enter>', lambda e, labels=[l]: on_enter(labels))
    l.bind('<Leave>', lambda e, labels=[l]: on_leave(labels))
    page_found = False
    for widget in frame_breadcrumbs.winfo_children():
        if page_found:
            widget.destroy()
        if ' Patient Info >' == widget.cget('text'):
            page_found = True
    main_frame.grid_columnconfigure(1, weight=1)
    main_frame.grid_columnconfigure((0,2,3,4), weight=0)
    main_frame.grid_rowconfigure(2, weight=1)
    main_frame.grid_rowconfigure((0,1,3,4), weight=0)
    p_label = customtkinter.CTkLabel(main_frame,
                    # fullname
                    text=current_patient[1] + " " + current_patient[2],
                    font=("consolas", 25))
    p_label.grid(row=0, column=0, columnspan=2, padx=(25, 0), sticky='W', pady=(25,5))
    frame_info = customtkinter.CTkFrame(main_frame, corner_radius=20)
    frame_info.grid(row=2, column=0, sticky='NS', padx=(10,0), pady=(0,50))
    frame_info.grid_columnconfigure((0,1), weight=1)
    frame_info.grid_rowconfigure((0,1,2,3,4,5), weight=1)
    customtkinter.CTkLabel(frame_info, text='First Name:', font=('consolas', 20), anchor='w').grid(row=0, column=0, sticky='NSEW', padx=5, pady=5)
    customtkinter.CTkLabel(frame_info, text='Last Name:', font=('consolas', 20), anchor='w').grid(row=1, column=0, sticky='NSEW', padx=5, pady=5)
    customtkinter.CTkLabel(frame_info, text='Birth Date:', font=('consolas', 20), anchor='w').grid(row=2, column=0, sticky='NSEW', padx=5, pady=5)
    customtkinter.CTkLabel(frame_info, text='Phone Number:', font=('consolas', 20), anchor='w').grid(row=3, column=0, sticky='NSEW', padx=5, pady=5)
    customtkinter.CTkLabel(frame_info, text='Email:', font=('consolas', 20), anchor='w').grid(row=4, column=0, sticky='NSEW', padx=5, pady=5)
    customtkinter.CTkLabel(frame_info, text='Age:', font=('consolas', 20), anchor='w').grid(row=5, column=0, sticky='NSEW', padx=5, pady=5)
    for i in range(5):
        en = customtkinter.CTkEntry(frame_info, font=('consolas', 20), justify='center')
        en.grid(row=i, column=1, sticky='NSEW', padx=5, pady=5)
        if current_patient[1+i]:
            en.insert(0, current_patient[1+i])
        en.configure(state='disabled')
    en = customtkinter.CTkEntry(frame_info, font=('consolas', 20), justify='center')
    en.grid(row=5, column=1, sticky='NSEW', padx=5, pady=5)
    try:
        age = calculate_age(datetime.datetime.strptime(current_patient[3], '%m/%d/%Y').date())
        en.insert(0, age)
    except Exception as e:
        print(e)
    en.configure(state='disabled')
    treatment_data = dc.get_treatments(patient_id, sort=var_treatmentsort.get())
    frm = customtkinter.CTkFrame(main_frame, fg_color='#2b2b2b')
    frm.grid(row=1, column=1, pady=(20,10), padx=(0,50), sticky='EW')
    customtkinter.CTkLabel(frm, text='Search', font=('consolas', 20)).pack(side='left', padx=10)
    customtkinter.CTkEntry(frm, textvariable=var_treatmentfilter, width=200).pack(side='left', padx=10)
    var_treatmentfilter.trace_add('write', filter_treatment)
    customtkinter.CTkOptionMenu(frm, values=["Treatment ID", "Treatment Name", "Start Date", "End Date", "Summary"], variable=var_treatmentoption, command=filter_treatment).pack(side='left', padx=10)
    customtkinter.CTkOptionMenu(frm, values=["Treatment ID", "Treatment Name", "Start Date", "End Date", "Summary"], variable=var_treatmentsort, command=filter_treatment).pack(side='right', padx=10)
    customtkinter.CTkLabel(frm, text='Sort by', font=('consolas', 20)).pack(side='right', padx=10)
    table_treatment = customtkinter.CTkScrollableFrame(main_frame)
    table_treatment.grid(row=2, column=1, sticky='NSEW', padx=(10, 50), pady=(0,50))
    table_treatment.grid_rowconfigure(0, weight=1)
    fill_treatments(table_treatment, treatment_data)
    frm = customtkinter.CTkFrame(master=main_frame, fg_color='#2b2b2b')
    frm.grid(row=3, column=0, columnspan=2, pady=15, sticky='EW')

    new_treatment_button = customtkinter.CTkButton(master=frm,
                                                   text='New Treatment',
                                                   font=("consolas",
                                                         15, "bold"),
                                                   height=50,
                                                   command=lambda: new_treatment(patient_id))
    new_treatment_button.pack(expand=True, side='left')

    delete_treatment_button = customtkinter.CTkButton(master=frm,
                                                 text='Delete Treatment',
                                                 font=("consolas",
                                                       15, "bold"),
                                                 height=50,
                                                 command=delete_treatment)
    delete_treatment_button.pack(expand=True, side='left')

    """
    edit_treatment_button = customtkinter.CTkButton(master=frm,
                                                 text='Edit Treatment',
                                                 font=("consolas",
                                                       15, "bold"),
                                                 height=50,
                                                 command=edit_treatment)
    edit_treatment_button.pack(expand=True, side='left')
    """


def add_treatment(treatment_name, patient_id, start_date, end_date, summary):
    start_date = datetime.datetime.strptime(start_date, "%m/%d/%y").strftime("%d/%m/%Y")
    end_date = datetime.datetime.strptime(end_date, "%m/%d/%y").strftime("%d/%m/%Y")
    dc.add_treatment(treatment_name, patient_id, start_date, end_date, summary)
    patientinfo(patient_id)

class TreatmentWindow(customtkinter.CTkToplevel):
    def __init__(self, patient_id, treatment_id = None, treatment_name = None, start_date = None, end_date = None, summary = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.treatment_id = treatment_id
        self.title('Treatment')
        self.patient_id = patient_id
        self.resizable(False, False)
        self.var_startD = StringVar(value='1/1/23')
        self.var_endD = StringVar(value='1/10/23')
        customtkinter.CTkLabel(self, text="Treatment Name:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_treatment_name = customtkinter.CTkEntry(self)
        self.entry_treatment_name.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        customtkinter.CTkLabel(self, text="Start Date:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.calstart = Calendar(self, selectmode="day", year=2023, month=1, day=1, font='consolas 15')
        self.calstart.grid(row=1, column=1, padx=10, pady=(10, 0), sticky="NSEW")
        customtkinter.CTkEntry(self, textvariable=self.var_startD).grid(row=2, column=1, padx=10, pady=(5, 10), sticky="EW")
        customtkinter.CTkLabel(self, text="End Date:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.calend = Calendar(self, selectmode="day", year=2023, month=1, day=10, font='consolas 15')
        self.calend.grid(row=3, column=1, padx=10, pady=10, sticky="NSEW")
        customtkinter.CTkEntry(self, textvariable=self.var_endD).grid(row=4, column=1, padx=10, pady=(5, 10), sticky="EW")
        self.calstart.bind('<<CalendarSelected>>', self.update_treatmentdate)
        self.calend.bind('<<CalendarSelected>>', self.update_treatmentdate)
        customtkinter.CTkLabel(self, text="Summary:").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.summary = customtkinter.CTkTextbox(self, border_color='#4d5254', fg_color='#343638', border_width=2)
        self.summary.grid(row=5, column=1, padx=10, pady=10, sticky="NSEW")
        self.submit_button = customtkinter.CTkButton(self, 
            text='Submit',
            command=self.add_treatment
        )
        self.protocol("WM_DELETE_WINDOW", lambda:self.close_treatment("add")) 
        if treatment_name:
            self.protocol("WM_DELETE_WINDOW", lambda:self.close_treatment("edit")) 
            self.entry_treatment_name.insert(0, treatment_name)
            self.calstart.selection_set(start_date)
            self.calend.selection_set(end_date)
            self.summary.insert("1.0", summary)
            self.submit_button.configure(command=self.edit_treatment)
        self.submit_button.grid(row=6, column=0, columnspan=2, padx=20, pady=15, sticky="s")

    
    def update_treatmentdate(self, e):
        self.var_startD.set(self.calstart.get_date())
        self.var_endD.set(self.calend.get_date())


    def close_treatment(self, mode):
        global treatment_window_visible, edit_treatment_visible
        if mode == 'add':
            treatment_window_visible = False
        elif mode == 'edit':
            edit_treatment_visible = False
        self.destroy()


    def edit_treatment(self):
        global edit_treatment_visible
        treatment_name = self.entry_treatment_name.get()
        calstart = self.calstart.get_date()
        calend = self.calend.get_date()
        summary = self.summary.get("1.0", END).rstrip('\n')
        if not treatment_name:
            messagebox.showerror('Error', 'No treatment name was given')
        else:
            new_start = datetime.datetime.strptime(calstart, "%m/%d/%y").strftime("%m/%d/%Y")
            new_end = datetime.datetime.strptime(calend, "%m/%d/%y").strftime("%m/%d/%Y")
            dc.update_treatment(self.treatment_id, treatment_name, new_start, new_end, summary)
            self.destroy()
            edit_treatment_visible = False
            patientinfo()


    def add_treatment(self):
        global treatment_window_visible
        treatment_name = self.entry_treatment_name.get()
        calstart = self.calstart.get_date()
        calend = self.calend.get_date()
        summary = self.summary.get("1.0", END).rstrip('\n')
        if not treatment_name:
            messagebox.showerror('Error', 'No treatment name was given')
        else:
            try:
                new_start = datetime.datetime.strptime(self.var_startD.get(), "%m/%d/%y").strftime("%m/%d/%Y")
                new_end = datetime.datetime.strptime(self.var_endD.get(), "%m/%d/%y").strftime("%m/%d/%Y")
            except:
                messagebox.showerror('Error', 'Please enter the date in the correct format such as: 1/20/23')
                return
            dc.add_treatment(treatment_name, self.patient_id, new_start, new_end, summary)
            self.destroy()
            treatment_window_visible = False
            patientinfo()
        

treatment_window_visible = False
def new_treatment(patient_id):
    global treatment_window_visible, treatment_window
    if not treatment_window_visible:
        treatment_window = TreatmentWindow(patient_id)
        treatment_window_visible = True
    window.after(100, treatment_window.focus)

def delete_treatment():
    dialog = customtkinter.CTkInputDialog(text="Type ID of treatment to be deleted:", title="Delete treatment")
    text = dialog.get_input()  # waits for input
    if not text.isdigit():
        messagebox.showerror('Error', 'ID must be a number.')
    else:
        treatments = dc.get_treatments(patient_id, sort=var_treatmentsort.get())
        name = ''
        for item in treatments:
            if item[0] == int(text) and item[2] == patient_id:
                name = f"{item[1]}"
                break
        if not name:
            messagebox.showerror('Error', 'ID of treatment not found.')
        elif messagebox.askyesno('Delete Treatment', f'Are you sure you want to delete the treatment {name}?') and dc.remove_treatment(int(text)):
            patientinfo()


edit_treatment_visible = False
def edit_treatment():
    global edit_treatment_visible, edit_treatment_window
    dialog = customtkinter.CTkInputDialog(text="Type ID of treatment to be edited:", title="Edit treatment")
    text = dialog.get_input()  # waits for input
    if not text.isdigit():
        messagebox.showerror('Error', 'ID must be a number.')
    else:
        treatment = dc.get_treatment_by_id(int(text))
        if not treatment:
            messagebox.showerror('Error', 'ID of treatment not found.')
        else:
            if not edit_treatment_visible:
                edit_treatment_visible = True
                edit_treatment_window = TreatmentWindow(treatment_id=treatment[0], patient_id=treatment[2], treatment_name=treatment[1], 
                    start_date=treatment[3], end_date=treatment[4], summary=treatment[5])
            window.after(100, edit_treatment_window.focus)


def BCI_data():

    df = pd.read_csv("test.csv")
    df.head()
    # df.info()
    copy_df = df.copy()

    Timestamp = df["Timestamp"]
    meanAttention = df["Attention"].mean()
    meanMeditation = df["Meditation"].mean()
    meanTheta = df["Theta"].mean()
    meanLowBeta = df["LowBeta"].mean()
    # meanHighBeta= df["HighBeta"].mean()

    # df["Timestamp"].fillna(meanTimestamp,inplace=True)
    df["Attention"].fillna(meanAttention, inplace=True)
    df["Meditation"].fillna(meanMeditation, inplace=True)
    df["Theta"].fillna(meanTheta, inplace=True)
    df["LowBeta"].fillna(meanLowBeta, inplace=True)
    # df["HighBeta"].fillna(meanHighBeta,inplace=True)


    # delete rows
    df.drop('Delta', inplace=True, axis=1)
    df.drop('LowAlpha', inplace=True, axis=1)
    df.drop('HighAlpha', inplace=True, axis=1)
    df.drop('HighBeta', inplace=True, axis=1)
    df.drop('LowGamma', inplace=True, axis=1)
    df.drop('HighGamma', inplace=True, axis=1)

    # Updated the data form
    cleaned_df = df

    # Define a Series of timestamps as strings
    timestamp_series_str = pd.Series(df["Timestamp"])

    # Convert the timestamp Series to a datetime Series
    timestamp_series_dt = pd.to_datetime(timestamp_series_str, format='%d-%m-%Y_%H:%M:%S')

    # Convert the datetime Series to Unix timestamps in seconds
    timestamp_series_sec = timestamp_series_dt.astype('int64') // 10**9

    # Print the Unix timestamp Series in seconds
    # print(timestamp_series_sec)

    TimeAxis = timestamp_series_sec-timestamp_series_sec.iloc[0]
    # print(TimeAxis)

    # calculates ratio
    print("Theta mean:", np.mean(cleaned_df['Theta']))
    print("LowBeta mean:", np.mean(cleaned_df['LowBeta']))
    print("The ratio between Theta and LowBeta is:")
    print(np.divide(np.mean(cleaned_df['Theta']), np.mean(cleaned_df['LowBeta'])))
    print("Attention mean:", np.mean(cleaned_df['Attention']))

    df['Theta-Beta Ratio'] = (cleaned_df['Theta']) / (cleaned_df['LowBeta'])

    ratio = np.divide(np.mean(cleaned_df['Theta']), np.mean(cleaned_df['LowBeta']))
    # Create the ratio graph
    plt.plot(TimeAxis / 60, df['Theta-Beta Ratio'], linestyle='-.', linewidth=0.1, marker='o', color='b')

    # Add title and axis labels
    plt.title(f'Theta/LowBeta = {round(ratio, 4)}')
    plt.xlabel('Time (min)')
    plt.ylabel('Theta/LowBeta')

    # Show the graph
    # plt.show()

    """# **Exploratory Data Analysis**
    Each feature analysis
    """

    df['AttentionMean'] = (cleaned_df['Attention'])
    mean = np.mean(cleaned_df['Attention'])
    plt.plot(TimeAxis / 60, df['AttentionMean'], linestyle='-.', linewidth=0.1, marker='o', color='g')

    # Add title and axis labels
    plt.title(f'AttentionMean = {round(mean, 3)}')
    plt.xlabel('Time (min)')
    plt.ylabel('Attention')

    # Show the graph
    # plt.show()

    df['MeditationMean'] = (cleaned_df['Meditation'])
    mean = np.mean(cleaned_df['Meditation'])
    plt.plot(TimeAxis / 60, df['MeditationMean'], linestyle='-.', linewidth=0.1, marker='o', color='c')

    # Add title and axis labels
    plt.title(f'MeditationMean = {round(mean, 3)}')
    plt.xlabel('Time (min)')
    plt.ylabel('Meditation')

    # Show the graph
    # plt.show()


import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import glob


def test_results():
    # Clear
    for widgets in main_frame.winfo_children():
        widgets.destroy()

    main_frame.grid_columnconfigure((0), weight=1)
    main_frame.grid_columnconfigure((1,2,3,4), weight=0)
    main_frame.grid_rowconfigure(2, weight=1)
    main_frame.grid_rowconfigure((0,1,3,4), weight=0)
    # Back Button
    back_button = customtkinter.CTkButton(master=main_frame,
                                          text="Back",
                                          width=100,
                                          font=('consolas', 15),
                                          command=start_test)
    back_button.grid(row=0, column=0, sticky='W', padx=(20,0), pady=(20,0))

    # Create Matplotlib figure and canvas
    fig, ((ax1, ax2), (ax3,ax4)) = plt.subplots(2, 2, figsize=(10, 6))
    fig.delaxes(ax4)
    today = datetime.datetime.now().strftime("%d-%m-%Y")
    targetPattern = r""+today+"*test.csv"
    test_file = glob.glob(targetPattern)[-1]
    df = pd.read_csv(test_file)
    df.head()
    df.info()
    copy_df = df.copy()

    Timestamp = df["Timestamp"]
    meanAttention = df["Attention"].mean()
    meanMeditation = df["Meditation"].mean()
    meanTheta = df["Theta"].mean()
    meanLowBeta = df["LowBeta"].mean()
    # meanHighBeta= df["HighBeta"].mean()

    # df["Timestamp"].fillna(meanTimestamp,inplace=True)
    df["Attention"].fillna(meanAttention, inplace=True)
    df["Meditation"].fillna(meanMeditation, inplace=True)
    df["Theta"].fillna(meanTheta, inplace=True)
    df["LowBeta"].fillna(meanLowBeta, inplace=True)
    # df["HighBeta"].fillna(meanHighBeta,inplace=True)

    # delete rows
    df.drop('Delta', inplace=True, axis=1)
    df.drop('LowAlpha', inplace=True, axis=1)
    df.drop('HighAlpha', inplace=True, axis=1)
    df.drop('HighBeta', inplace=True, axis=1)
    df.drop('LowGamma', inplace=True, axis=1)
    df.drop('HighGamma', inplace=True, axis=1)

    # Updated the data form
    cleaned_df = df

    # Define a Series of timestamps as strings
    timestamp_series_str = pd.Series(df["Timestamp"])

    # Convert the timestamp Series to a datetime Series
    timestamp_series_dt = pd.to_datetime(timestamp_series_str, format='%d-%m-%Y_%H:%M:%S')

    # Convert the datetime Series to Unix timestamps in seconds
    timestamp_series_sec = timestamp_series_dt.astype('int64') // 10 ** 9

    # Print the Unix timestamp Series in seconds
    # print(timestamp_series_sec)

    TimeAxis = timestamp_series_sec - timestamp_series_sec.iloc[0]
    # print(TimeAxis)

    # calculates ratio
    # print("Theta mean:", np.mean(cleaned_df['Theta']))
    # print("LowBeta mean:", np.mean(cleaned_df['LowBeta']))
    # print("The ratio between Theta and LowBeta is:")
    # print(np.divide(np.mean(cleaned_df['Theta']), np.mean(cleaned_df['LowBeta'])))
    # print("Attention mean:", np.mean(cleaned_df['Attention']))

    df['Theta-Beta Ratio'] = (cleaned_df['Theta']) / (cleaned_df['LowBeta'])

    ratio = np.divide(np.mean(cleaned_df['Theta']), np.mean(cleaned_df['LowBeta']))
    # Create the ratio graph
    # plt.plot(TimeAxis / 60, df['Theta-Beta Ratio'], linestyle='-.', linewidth=0.1, marker='o', color='b')

    # Add title and axis labels
    plt.title(f'Theta/LowBeta = {round(ratio, 4)}')
    plt.xlabel('Time (min)')
    plt.ylabel('Theta/LowBeta')

    # Show the graph
    # plt.show()

    """# **Exploratory Data Analysis**
    Each feature analysis
    """

    df['AttentionMean'] = (cleaned_df['Attention'])
    mean = np.mean(cleaned_df['Attention'])
    # plt.plot(TimeAxis / 60, df['AttentionMean'], linestyle='-.', linewidth=0.1, marker='o', color='g')

    # Add title and axis labels
    plt.title(f'AttentionMean = {round(mean, 3)}')
    plt.xlabel('Time (min)')
    plt.ylabel('Attention')

    # Show the graph
    # plt.show()

    df['MeditationMean'] = (cleaned_df['Meditation'])
    mean = np.mean(cleaned_df['Meditation'])
    # plt.plot(TimeAxis / 60, df['MeditationMean'], linestyle='-.', linewidth=0.1, marker='o', color='c')

    # Add title and axis labels
    plt.title(f'MeditationMean = {round(mean, 3)}')
    plt.xlabel('Time (min)')
    plt.ylabel('Meditation')

    # Show the graph
    # plt.show()


    ax1.plot(TimeAxis / 60, df['Theta-Beta Ratio'], linestyle='-.', linewidth=0.1, marker='o',markersize=2, color='b')
    ax1.set_title(f'Theta/LowBeta = {round(ratio, 4)}')
    ax1.set_xlabel('Time (min)')
    ax1.set_ylabel('Theta/LowBeta')

    mean1 = np.mean(df['Meditation'])
    mean2 = np.mean(df['Attention'])
    # Add second plot
    ax2.plot(TimeAxis / 60, df['MeditationMean'], linestyle='-.', linewidth=0.1, marker='o',markersize=2, color='c')
    ax2.set_title(f'MeditationMean = {round(mean1, 3)}')
    ax2.set_xlabel('Time (min)')
    ax2.set_ylabel('Meditation')

    # Add third plot
    ax3.plot(TimeAxis / 60, df['AttentionMean'], linestyle='-.', linewidth=0.1, marker='o',markersize=2, color='g')
    ax3.set_title(f'AttentionMean = {round(mean2, 3)}')
    ax3.set_xlabel('Time (min)')
    ax3.set_ylabel('Attention')

    fig.subplots_adjust(wspace=0.3, hspace=0.4)  # Adjust space between axes

    canvas = FigureCanvasTkAgg(fig, master=main_frame)
    canvas.draw()

    # Add toolbar above the first and second plot
    toolbar = NavigationToolbar2Tk(canvas, main_frame)
    toolbar.update()
    toolbar.pack(side=tk.TOP, fill=tk.X)

    # Place the canvas below the toolbar
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


# ////////////////////////////////////////////////DATA///////////////////////////////////////////////////7/
window = customtkinter.CTk()
window.title("PowerMind")
var_filter = StringVar()
var_patientoption = customtkinter.StringVar(value="ID")
var_patientsort = customtkinter.StringVar(value="ID")
var_treatmentfilter = StringVar()
var_treatmentoption = customtkinter.StringVar(value="Treatment ID")
var_treatmentsort = customtkinter.StringVar(value="Treatment ID")
var_visitfilter = customtkinter.StringVar()
var_visitoption = customtkinter.StringVar(value="ID")
var_visitsort = customtkinter.StringVar(value="ID")
# Set the width and height of the window
window_width = 1100
window_height = 770

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the x and y coordinates to center the window
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the position of the window
window.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))


def home_click(event = None):
    home_tab.configure(fg_color="#2752D6", state='disabled')
    patient_tab.configure(fg_color="#1f6aa5", state='normal')
    patientinfo_tab.configure(fg_color="#1f6aa5", state='normal')
    home()


def patient_click(event = None):
    home_tab.configure(fg_color="#1f6aa5", state='normal')
    patient_tab.configure(fg_color="#2752D6", state='disabled')
    patientinfo_tab.configure(fg_color="#1f6aa5", state='normal')
    patient()


def patientinfo_click(event = None):
    global patient_id
    if not patient_id:
        messagebox.showerror('Error', 'No patient selected. Please select a patient from the table first.')
        return
    home_tab.configure(fg_color="#1f6aa5", state='normal')
    patient_tab.configure(fg_color="#1f6aa5", state='normal')
    patientinfo_tab.configure(fg_color="#2752D6", state='disabled')
    patientinfo()

def on_enterMenu(label, frame):
    frame.configure(fg_color="#2752D6")
    label.configure(bg_color="#2752D6")

def on_leaveMenu(label, frame, leave_color='#2b2b2b'):
    frame.configure(fg_color=leave_color)
    label.configure(bg_color=leave_color)


def show_appointments(e):
    global app_calendar
    date_selected = datetime.datetime.strptime(app_calendar.get_date(), "%m/%d/%y").strftime("%m/%d/%Y")
    appointment_list = dc.get_appointments()
    found = False
    selected_apps = []
    for a in appointment_list:
        if a[1] == date_selected:
            found = True
            selected_apps.append(a)
    if found:
        window_showapp = customtkinter.CTkToplevel(window)
        window_showapp.resizable(False, False)
        window_showapp.title('Selected Appointments')
        window_showapp.grid_columnconfigure(0, weight=1)
        customtkinter.CTkLabel(window_showapp, text=date_selected, font=('consolas', 25)).grid(row=0, column=0, padx=25, pady=15)
        checkboxes = []
        for i in range(len(selected_apps)):
            formated_str = f"{selected_apps[i][0]}. {selected_apps[i][4]}\t{selected_apps[i][2]}:{selected_apps[i][3]} {selected_apps[i][5]}"
            c = customtkinter.CTkCheckBox(window_showapp, text=formated_str, font=('consolas', 20), onvalue=selected_apps[i][0], offvalue=False)
            c.grid(row=i+1, column=0, padx=40, pady=15, sticky='EW')
            checkboxes.append(c)
        customtkinter.CTkButton(window_showapp, text='Delete Appointments', font=('consolas', 20), command=lambda:delete_appointment(checkboxes, window_showapp)).grid(row=i+3, column=0, pady=10, padx=15, sticky='EW')
        window_showapp.after(100, window_showapp.focus)

def delete_appointment(checkboxes, window_showapp):
    delete = False
    for c in checkboxes:
        if c.get():
            dc.delete_appointment(c.get())
            delete = True
    if delete:
        appointment_list = dc.get_appointments()
        for a in appointment_list:
            app_calendar.calevent_create(datetime.datetime.strptime(a[1], '%m/%d/%Y'), "", tags="app")
        window_showapp.destroy()

appointment_window = None
def appointments(e):
    global appointment_window, app_calendar
    if not appointment_window:
        appointment_list = dc.get_appointments()
        appointment_window = customtkinter.CTkToplevel(window)
        appointment_window.resizable(False, False)
        appointment_window.title('My Appointments')
        appointment_window.geometry('650x600')
        appointment_window.grid_columnconfigure(0, weight=1)
        appointment_window.grid_rowconfigure(0, weight=1)
        app_calendar = Calendar(appointment_window, selectmode="day", year=2023, month=6, day=20, font='consolas 25')
        for a in appointment_list:
            app_calendar.calevent_create(datetime.datetime.strptime(a[1], '%m/%d/%Y'), "", tags="app")
        app_calendar.tag_config("app", foreground="black", background='green')
        app_calendar.bind('<<CalendarSelected>>', show_appointments)
        app_calendar.grid(row=0, column=0, sticky='NSEW', padx=45, pady=40)
        #frm_bottom = customtkinter.CTkFrame(appointment_window, corner_radius=15)
        ##frm_bottom.grid(row=1, column=0, sticky='EWS', padx=15, pady=10)
        #frm_bottom.grid_columnconfigure((0,1), weight=1)
        #customtkinter.CTkButton(frm_bottom, text='Delete Appointment', font=('consolas', 20)).grid(row=0, column=0, pady=10, padx=15)
        customtkinter.CTkButton(appointment_window, text='New Appointment', font=('consolas', 20), command=new_appointment).grid(row=1, column=0, sticky='EWS', padx=15, pady=10)
    appointment_window.protocol("WM_DELETE_WINDOW",  close_appointment)
    appointment_window.after(100, appointment_window.focus)

def new_appointment():
    new_app = customtkinter.CTkToplevel(window)
    new_app.resizable(False, False)
    new_app.title('New Appointment')
    new_app.geometry('400x450')
    new_app.grid_columnconfigure((0,1), weight=1)
    new_app.grid_rowconfigure((0,1,2), weight=1)
    var_am = StringVar()
    var_am.set('AM')
    customtkinter.CTkLabel(new_app, text='Date:', font=('consolas', 20)).grid(row=0, column=0, sticky='W', padx=15)
    customtkinter.CTkLabel(new_app, text='Time:', font=('consolas', 20)).grid(row=1, column=0, sticky='W', padx=15)
    customtkinter.CTkLabel(new_app, text='Name:', font=('consolas', 20)).grid(row=2, column=0, sticky='W', padx=15)
    new_date = Calendar(new_app, selectmode="day", year=2023, month=6, day=20, font='consolas 15')
    new_date.grid(row=0, column=1, sticky='NSEW', padx=15, pady=(15,0))
    frm = customtkinter.CTkFrame(new_app)
    frm.grid(row=1, column=1, padx=15)
    entry_hours = customtkinter.CTkEntry(frm, width=40, font=('consolas', 20))
    entry_hours.pack(side='left')
    customtkinter.CTkLabel(frm, text=':').pack(side='left')
    entry_minutes = customtkinter.CTkEntry(frm, width=40, font=('consolas', 20))
    entry_minutes.pack(side='left')
    customtkinter.CTkOptionMenu(frm, values=['AM', 'PM'], variable=var_am, width=100).pack(side='left')
    entry_name = customtkinter.CTkEntry(new_app, font=('consolas', 20))
    entry_name.grid(row=2, column=1, sticky='EW', padx=15)
    customtkinter.CTkButton(new_app, text='Save', font=('consolas', 20), command=lambda:add_appointment(
        date=datetime.datetime.strptime(new_date.get_date(), "%m/%d/%y").strftime("%m/%d/%Y"),
        time=(entry_hours.get(), entry_minutes.get()),
        name=entry_name.get(),
        new_app=new_app,
        am=var_am.get()
    )
        ).grid(row=3, column=0, columnspan=2, pady=10, padx=15)
    new_app.after(100, new_app.focus)

def add_appointment(date, time, name, new_app, am):
    if not time or not date or not name:
        messagebox.showerror('Error', 'Please provide all the information')
        new_app.focus()
        return
    dc.add_appointment(date, time, name, am)
    appointment_list = dc.get_appointments()
    for a in appointment_list:
        app_calendar.calevent_create(datetime.datetime.strptime(a[1], '%m/%d/%Y'), "", tags="app")
    new_app.destroy()

def close_appointment():
    global appointment_window
    appointment_window.destroy()
    appointment_window = None

doctor_window = None

def close_doctor():
    global doctor_window
    doctor_window.destroy()
    doctor_window = None

def save_doctor(first_name, last_name, country, phone):
    global doctor_window
    dc.save_doctor(first_name=first_name, last_name=last_name, country=country, phone=phone)
    close_doctor()

def doctor(e):
    global doctor_window
    if not doctor_window:
        doctor_window = customtkinter.CTkToplevel(window)
        doctor_window.resizable(False, False)
        doctor_window.title('Doctor Profile')
        doctor_window.geometry('500x450')
        var_country = StringVar()
        doctor_window.grid_columnconfigure((0,1), weight=1)
        doctor_window.grid_rowconfigure((0,1,2,3,4), weight=1)
        customtkinter.CTkLabel(doctor_window, text='First Name:', font=('consolas', 20)).grid(row=0, column=0, sticky='W', padx=15)
        customtkinter.CTkLabel(doctor_window, text='Last Name:', font=('consolas', 20)).grid(row=1, column=0, sticky='W', padx=15)
        customtkinter.CTkLabel(doctor_window, text='Country:', font=('consolas', 20)).grid(row=2, column=0, sticky='W', padx=15)
        customtkinter.CTkLabel(doctor_window, text='Phone Number:', font=('consolas', 20)).grid(row=3, column=0, sticky='W', padx=15)
        doctor_info = dc.get_doctor()
        doctor_fname = customtkinter.CTkEntry(doctor_window, font=('consolas', 20))
        doctor_fname.grid(row=0, column=1, sticky='EW', padx=15)
        if doctor_info[1]:
            doctor_fname.insert(0, doctor_info[1])
        doctor_lname = customtkinter.CTkEntry(doctor_window, font=('consolas', 20))
        doctor_lname.grid(row=1, column=1, sticky='EW', padx=15)
        if doctor_info[2]:
            doctor_fname.insert(0, doctor_info[2])
        countries = ['USA', 'UK', 'Germany', 'France', 'Canada']
        doctor_country = customtkinter.CTkComboBox(doctor_window, font=('consolas', 20), values=countries, variable=var_country)
        doctor_country.grid(row=2, column=1, sticky='EW', padx=15)
        if doctor_info[3]:
            var_country.set(doctor_info[3])
        doctor_number = customtkinter.CTkEntry(doctor_window, font=('consolas', 20))
        doctor_number.grid(row=3, column=1, sticky='EW', padx=15)
        if doctor_info[4]:
            doctor_number.insert(0, doctor_info[4])
        frm = customtkinter.CTkFrame(doctor_window, corner_radius=15)
        frm.grid(row=4, column=0, columnspan=2, pady=10, sticky='EWS', padx=15)
        frm.grid_columnconfigure((0,1), weight=1)
        customtkinter.CTkButton(frm, text='Close', command=close_doctor).grid(row=0, column=0, pady=10)
        customtkinter.CTkButton(frm, text='Save', command=lambda:save_doctor(
            first_name=doctor_fname.get(),
            last_name=doctor_lname.get(),
            country=doctor_country.get(),
            phone=doctor_number.get()
        )).grid(row=0, column=1, pady=10)
    doctor_window.protocol("WM_DELETE_WINDOW",  close_doctor)
    doctor_window.after(100, doctor_window.focus)

def create_menu(page):
    global label_home, label_patient, label_patientinfo, frm_menu, menu_opened
    frm_menu.destroy()
    frm_menu = customtkinter.CTkFrame(window, corner_radius=20)
    if page == 'home' or menu_opened:
        frm_menu.grid(row=1, rowspan=4, column=0, sticky='NSEW', padx=20, pady=20)
    frm_homemenu =customtkinter.CTkFrame(frm_menu, corner_radius=0, fg_color='#2b2b2b')
    frm_homemenu.pack(fill='x', pady=20, ipady=1, ipadx=1)
    label_home = customtkinter.CTkLabel(frm_homemenu, text=' Home', font=('Consolas', 25), anchor='w',
        image=customtkinter.CTkImage(light_image=Image.open('images/home.png'), size=(30,30)), compound='left', text_color='white')
    label_home.pack(fill='x', ipadx=30, ipady=10, padx=(15,0))
    frm_patientmenu =customtkinter.CTkFrame(frm_menu, corner_radius=0, fg_color='#2b2b2b')
    frm_patientmenu.pack(fill='x', pady=20, ipady=1, ipadx=1)
    label_patient = customtkinter.CTkLabel(frm_patientmenu, text=' Patient', font=('Consolas', 25), anchor='w',
        image=customtkinter.CTkImage(light_image=Image.open('images/patient.png'), size=(30,30)), compound='left', text_color='white')
    label_patient.pack(fill='x', ipadx=30, ipady=10, padx=(15,0))
    frm_patientinfomenu =customtkinter.CTkFrame(frm_menu, corner_radius=0, fg_color='#2b2b2b')
    frm_patientinfomenu.pack(fill='x', pady=20, ipady=1, ipadx=1)
    label_patientinfo = customtkinter.CTkLabel(frm_patientinfomenu, text=' Patient Info', font=('Consolas', 25), anchor='w',
        image=customtkinter.CTkImage(light_image=Image.open('images/info.png'), size=(30,30)), compound='left', text_color='white')
    label_patientinfo.pack(fill='x', ipadx=30, ipady=10, padx=(15,0))
    frm_appmenu =customtkinter.CTkFrame(frm_menu, corner_radius=0, fg_color='#2b2b2b')
    frm_appmenu.pack(fill='x', pady=20, ipady=1, ipadx=1)
    label_app = customtkinter.CTkLabel(frm_appmenu, text=' My Appointments', font=('Consolas', 25), anchor='w',
        image=customtkinter.CTkImage(light_image=Image.open('images/app.png'), size=(30,30)), compound='left', text_color='white')
    label_app.pack(fill='x', ipadx=30, ipady=10, padx=(15,0))
    frm_profilemenu =customtkinter.CTkFrame(frm_menu, corner_radius=0, fg_color='#2b2b2b')
    frm_profilemenu.pack(fill='x', pady=20, ipady=1, ipadx=1, side='bottom')
    label_profile = customtkinter.CTkLabel(frm_profilemenu, text=' My Profile', font=('Consolas', 25), anchor='w',
        image=customtkinter.CTkImage(light_image=Image.open('images/user.png'), size=(30,30)), compound='left', text_color='white')
    label_profile.pack(fill='x', ipadx=30, ipady=10, padx=(15,0))
    if page == 'home':
        main_label = label_home
        main_frame = frm_homemenu
    elif page == 'patient':
        main_label = label_patient
        main_frame = frm_patientmenu
    elif page == 'patient_info':
        main_label = label_patientinfo
        main_frame = frm_patientinfomenu
    main_label.configure(bg_color='white', text_color='black')
    main_frame.configure(fg_color='white')
    label_home.bind('<Button-1>', home)
    label_patient.bind('<Button-1>', patient)
    label_patientinfo.bind('<Button-1>', patientinfo)
    label_app.bind('<Button-1>', appointments)
    label_profile.bind('<Button-1>', doctor)
    for widgets in [(label_home, frm_homemenu), (label_patient, frm_patientmenu), (label_patientinfo, frm_patientinfomenu),
        (label_profile, frm_profilemenu), (label_app, frm_appmenu)]:
        widgets[0].bind('<Enter>', lambda e, label=widgets[0], frame=widgets[1]: on_enterMenu(label, frame))
        if widgets[0] == main_label:
            widgets[0].bind('<Leave>', lambda e, label=widgets[0], frame=widgets[1]: on_leaveMenu(label, frame, 'white'))
        else:
            widgets[0].bind('<Leave>', lambda e, label=widgets[0], frame=widgets[1]: on_leaveMenu(label, frame))

def update_date():
    date_day.configure(state='normal')
    date_day.delete(0, END)
    date_day.insert(0, datetime.date.today().strftime("%d"))
    date_day.configure(state='disabled')
    date_month.configure(state='normal')
    date_month.delete(0, END)
    date_month.insert(0, datetime.date.today().strftime("%m"))
    date_month.configure(state='disabled')
    date_year.configure(state='normal')
    date_year.delete(0, END)
    date_year.insert(0, datetime.date.today().strftime("%Y"))
    date_year.configure(state='disabled')
    time_hour.configure(state='normal')
    time_hour.delete(0, END)
    time_hour.insert(0, datetime.datetime.now().strftime("%H"))
    time_hour.configure(state='disabled')
    time_minute.configure(state='normal')
    time_minute.delete(0, END)
    time_minute.insert(0, datetime.datetime.now().strftime("%M"))
    time_minute.configure(state='disabled')
    window.after(1000, update_date)

window.grid_columnconfigure((1,2), weight=1)
window.grid_rowconfigure(3, weight=1)

frm_menu = customtkinter.CTkFrame(window, corner_radius=20)
frm_menu.grid(row=1, rowspan=4, column=0, sticky='NSEW', padx=20, pady=20)
create_menu('home')
customtkinter.set_appearance_mode('dark') # set theme to dark regardless of system preferences
patient_id = None
image = Image.open('images/icon.png')
frm_top = customtkinter.CTkFrame(window)
frm_top.grid(row=0, column=0, columnspan=3, sticky='EW')
frm_top.grid_columnconfigure(0, weight=1)
powermind_label = customtkinter.CTkLabel(frm_top,
                        compound='left',
                        text="PowerMind",
                        font=("consolas", 20),
                        image=customtkinter.CTkImage(light_image=image, size=(70,50)))
powermind_label.grid(row=0, column=0, sticky='EW')
frm_date = customtkinter.CTkFrame(frm_top, corner_radius=20)
frm_date.grid(row=0, column=1, sticky='E', padx=15, pady=5)
today_label = customtkinter.CTkLabel(frm_date, text="Today's Date:", font=('consolas', 15))
today_label.grid(row=0, column=0, columnspan=3, sticky='w', padx=(10,15), pady=(5,0))
time_label = customtkinter.CTkLabel(frm_date, text="Time:", font=('consolas', 15))
time_label.grid(row=0, column=3, columnspan=2, sticky='w', pady=(5,0))
date_day = customtkinter.CTkEntry(frm_date, width=30, justify='center')
date_day.insert(0, datetime.date.today().strftime("%d"))
date_day.configure(state='disabled')
date_day.grid(row=1, column=0, sticky='w', padx=(10,0), pady=(0,5))
date_month = customtkinter.CTkEntry(frm_date, width=30, justify='center')
date_month.insert(0, datetime.date.today().strftime("%m"))
date_month.configure(state='disabled')
date_month.grid(row=1, column=1, sticky='w', pady=(0,5))
date_year = customtkinter.CTkEntry(frm_date, width=50, justify='center')
date_year.insert(0, datetime.date.today().strftime("%Y"))
date_year.configure(state='disabled')
date_year.grid(row=1, column=2, sticky='w', pady=(0,5), padx=(0, 15))
time_hour = customtkinter.CTkEntry(frm_date, width=30)
time_hour.grid(row=1, column=3, sticky='w', pady=(0,5))
time_hour.insert(0, datetime.datetime.now().strftime("%H"))
time_hour.configure(state='disabled')
time_minute = customtkinter.CTkEntry(frm_date, width=30)
time_minute.grid(row=1, column=4, sticky='w', pady=(0,5), padx=(0,10))
time_minute.insert(0, datetime.datetime.now().strftime("%M"))
time_minute.configure(state='disabled')
window.after(1000, update_date)
tab_width = int(window_width / 3)
home_tab = customtkinter.CTkButton(window,
                 text="Home",
                    state='disabled',
                 fg_color="#2752D6",
                 text_color_disabled='white',
                 font=("consolas", 20),
                 command=home_click)
#home_tab.grid(row=1, column=0, sticky='EW', padx=15, pady=5)

patient_tab = customtkinter.CTkButton(window,
                    text="Patient",
                    #bg="#BEBABA",
                    text_color_disabled='white',
                    font=("consolas", 20),
                    command=patient_click)
#patient_tab.grid(row=1, column=1, sticky='EW', padx=15, pady=5)

patientinfo_tab = customtkinter.CTkButton(window,
                        text="Patient Info",
                        #bg="#BEBABA",
                        font=("consolas", 20),
                        text_color_disabled='white',
                        command=patientinfo_click)
#patientinfo_tab.grid(row=1, column=2, sticky='EW', padx=15, pady=5)

frame_breadcrumbs = customtkinter.CTkFrame(window, fg_color='#242424',
                   )
frame_breadcrumbs.grid(row=2, column=1, columnspan=2, pady=10, sticky='W', padx=30)
breadcrumbs_size = 20

main_frame = customtkinter.CTkFrame(window
                   )
main_frame.grid(row=3, column=1, columnspan=2, sticky='NSEW')

text_size = 22
home()

window.mainloop()