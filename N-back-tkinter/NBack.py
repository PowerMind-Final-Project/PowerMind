import sys
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from mydb import add_test, add_visit, get_visits
from PIL import ImageTk, Image
import webbrowser
import time
import random
import string
import csv
import datetime
import os
import customtkinter

import CPT as cpt
import AB as trail


# Set up colors
black = "#000000"
white = "#FFFFFF"
yellow = "#EEEE3B"

# Set up the display window
root = tk.Tk()
root.title("N-Back Test")
screen_width = 1920
screen_height = 1080

root.attributes('-fullscreen', True)
canvas = tk.Canvas(root, bg=white, width=1920, height=1080)
canvas.pack(fill="both", expand=True)

# Set up the variables for the test
n = 3
i = 0
count = 0
helper = 3
q_range = 2
stacksize = 20
test_duration = 180
stimuli_letters = list(string.ascii_uppercase)
stimuli_numbers = [str(i) for i in range(10)]
stimuli_mix = stimuli_letters + stimuli_numbers
sequence = []
end_time = 0
current_index = 3
correct_score = 0
incorrect_score = 0
test_loop = True
result = 0
timestamp = 0
time_a = 0
time_b = 0
link = []
q_list = []
x_values = []
radio_var = tk.IntVar(master=root, value=2)
gothelp = 0
expected = "a"
received = "b"
question = "q"

# Set up the font for displaying text
font_a = Font(family="Helvetica", size=100)
font_b = Font(family="Helvetica", size=40)

# Getting the current working directory
current_directory = os.getcwd()

# Creating a CSV file for the test
now = datetime.datetime.now()
timestamp_f = now.strftime('%d-%m-%Y_%H%M')
fileName = timestamp_f
#with open(os.path.join(current_directory, str(fileName) + '_N-back.csv'), mode='w', newline='') as csvfile:
#    fieldnames = ["timestamp", "result", "reaction_time", "got_help", "stack_size", "expected", "question", "received"]
#    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#    writer.writeheader()


# Define a function to generate a random sequence of stimuli


def generate_stimuli_sequence(n, sequence_length, repeat_range):
    global sequence, stimuli_numbers, stimuli_letters, stimuli_mix
    stimuli = []

    if radio_var.get() == 1:
        stimuli = stimuli_numbers
        random.shuffle(stimuli)
        sequence = [random.choice(stimuli) for _ in range(n)]
        for i in range(sequence_length):
            if i < n:
                stimulus = random.choice(stimuli)
            else:
                if random.random() < 0.5 and repeat_range > 0:
                    stimulus = sequence[random.randint(max(i - repeat_range, 0), i - 1)]
                else:
                    if repeat_range == 0:
                        stimulus = sequence[i - 1]
                    else:
                        stimulus = random.choice(stimuli)
                sequence.append(stimulus)
        return sequence

    if radio_var.get() == 2:
        stimuli = stimuli_letters
        random.shuffle(stimuli)
        sequence = [random.choice(stimuli) for _ in range(n)]
        for i in range(sequence_length):
            if i < n:
                stimulus = random.choice(stimuli)
            else:
                if random.random() < 0.5 and repeat_range > 0:
                    stimulus = sequence[random.randint(max(i - repeat_range, 0), i - 1)]
                else:
                    if repeat_range == 0:
                        stimulus = sequence[i - 1]
                    else:
                        stimulus = random.choice(stimuli)
                sequence.append(stimulus)
        return sequence

    if radio_var.get() == 3:
        stimuli = stimuli_mix
        for i in range(sequence_length):
            if i < n:
                stimulus = random.choice(stimuli)
            else:
                if random.random() < 0.5:
                    # Check if the stimulus should repeat itself
                    repeat_range = min(n - 3, i)
                    if random.random() < 0.5 and repeat_range > 0:
                        stimulus = sequence[random.randint(max(i - repeat_range, 0), i - 1)]
                    else:
                        stimulus = random.choice(stimuli)
                else:
                    repeat_range = min(n - 1, i)
                    if random.random() < 0.5 and repeat_range > 0:
                        stimulus = sequence[random.randint(max(i - repeat_range, 0), i - 1)]
                    else:
                        stimulus = random.choice(stimuli)
                sequence.append(stimulus)
        return sequence


# A function for the instructions of the test

def instructions_screen():
    global link
    # Remove all past widgets
    for widget in canvas.winfo_children():
        widget.destroy()
    # link.destroy()

    # Instructions label
    text = customtkinter.CTkLabel(master=canvas,
                                  text="\n"
                                       + "The user will be presented with a randomized string that is 3 letters "
                                         "long.\n"
                                       + "This string must be memorized , for example:\n"
                                       + "\n"
                                       + " A , X , W "
                                       + "\n"
                                       + "\n"
                                       + "Once memorized a new letter will be presented to the user "
                                         ", for example:\n"
                                       + "\n"
                                       + " T "
                                       + "\n"
                                       + "\n"
                                       + "Then 2 keys on the keyboard can be pressed: \n "
                                       + "\n"
                                       + "D key - if the presented letter is different from 3 letters before.\n"
                                       + "S key - if the presented letter is the same from 3 letters before.\n"
                                       + "\n"
                                       + "If the correct key has been pressed the string changes accordingly.\n"
                                       + "\n"
                                       + " T , X , W "
                                       + "\n"
                                       + "\n"
                                       + "The process repeats itself and a new letter will be presented."
                                       + "\n",
                                  width=400,
                                  height=300,
                                  fg_color=("white", "white"),
                                  text_color="black",
                                  corner_radius=10,
                                  font=("Verdana", 18))
    text.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    # Back button to the start
    button = customtkinter.CTkButton(master=canvas,
                                     command=lambda: start_screen(),
                                     width=220,
                                     height=64,
                                     border_width=0,
                                     corner_radius=10,
                                     text="Back to the main menu",
                                     font=("Verdana", 20))
    button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)


# Changing how many circles can be formed during the test
def test_settings_screen():
    global link, radio_var

    def set_string_amount(num):
        global stacksize
        stacksize = int(num)

    def set_q_range(num):
        global q_range
        q_range = int(num)

    def radiobutton_event():
        print("radiobutton toggled, current value:", radio_var.get())

    # Remove all past widgets
    for widget in canvas.winfo_children():
        widget.destroy()
    # link.destroy()

    # Setting the welcoming label for the test
    label_1 = customtkinter.CTkLabel(master=canvas,
                                     text="Item stack size",
                                     width=100,
                                     height=50,
                                     fg_color=("white", "white"),
                                     text_color="black",
                                     corner_radius=10,
                                     font=("Verdana", 20))
    label_1.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

    # slider for choosing how many circles we want
    slider = customtkinter.CTkSlider(master=canvas, from_=10, to=30, number_of_steps=2, height=20,
                                     command=lambda num: set_string_amount(num))
    slider.place(relx=0.5, rely=0.26, anchor=tk.CENTER)

    label_2 = customtkinter.CTkLabel(master=canvas,
                                     text="10",
                                     width=20,
                                     height=20,
                                     fg_color=("white", "white"),
                                     text_color="black",
                                     corner_radius=10)
    label_2.place(relx=0.424, rely=0.26, anchor=tk.CENTER)

    label_3 = customtkinter.CTkLabel(master=canvas,
                                     text="20",
                                     width=20,
                                     height=20,
                                     fg_color=("white", "white"),
                                     text_color="black",
                                     corner_radius=10)
    label_3.place(relx=0.5, rely=0.233, anchor=tk.CENTER)

    label_4 = customtkinter.CTkLabel(master=canvas,
                                     text="30",
                                     width=20,
                                     height=20,
                                     fg_color=("white", "white"),
                                     text_color="black",
                                     corner_radius=10)
    label_4.place(relx=0.577, rely=0.26, anchor=tk.CENTER)

    label_5 = customtkinter.CTkLabel(master=canvas,
                                     text="Presentation time",
                                     width=100,
                                     height=50,
                                     fg_color=("white", "white"),
                                     text_color="black",
                                     corner_radius=10,
                                     font=("Verdana", 20))
    label_5.place(relx=0.5, rely=0.37, anchor=tk.CENTER)

    # slider for choosing how much time we want
    slider = customtkinter.CTkSlider(master=canvas, from_=1, to=3, number_of_steps=2, height=20,
                                     command=lambda num: set_q_range(num))
    slider.place(relx=0.5, rely=0.48, anchor=tk.CENTER)

    label_6 = customtkinter.CTkLabel(master=canvas,
                                     text="1",
                                     width=20,
                                     height=20,
                                     fg_color=("white", "white"),
                                     text_color="black",
                                     corner_radius=10)
    label_6.place(relx=0.424, rely=0.48, anchor=tk.CENTER)

    label_7 = customtkinter.CTkLabel(master=canvas,
                                     text="2",
                                     width=20,
                                     height=20,
                                     fg_color=("white", "white"),
                                     text_color="black",
                                     corner_radius=10)
    label_7.place(relx=0.5001, rely=0.453, anchor=tk.CENTER)

    label_8 = customtkinter.CTkLabel(master=canvas,
                                     text="3",
                                     width=20,
                                     height=20,
                                     fg_color=("white", "white"),
                                     text_color="black",
                                     corner_radius=10)
    label_8.place(relx=0.58, rely=0.48, anchor=tk.CENTER)

    label_9 = customtkinter.CTkLabel(master=canvas,
                                     text="Sequence types",
                                     width=100,
                                     height=50,
                                     fg_color=("white", "white"),
                                     text_color="black",
                                     corner_radius=10,
                                     font=("Verdana", 20))
    label_9.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    radiobutton_1 = customtkinter.CTkRadioButton(root, text="Numbers",
                                                 command=radiobutton_event, variable=radio_var, value=1,
                                                 fg_color=("white", "blue"),
                                                 text_color="black",
                                                 hover_color="blue",
                                                 font=("Verdana", 20))
    radiobutton_1.place(relx=0.35, rely=0.69, anchor=tk.CENTER)

    radiobutton_2 = customtkinter.CTkRadioButton(root, text="Letters",
                                                 command=radiobutton_event, variable=radio_var, value=2,
                                                 fg_color=("white", "blue"),
                                                 hover_color="blue",
                                                 text_color="black", font=("Verdana", 20))
    radiobutton_2.place(relx=0.5, rely=0.69, anchor=tk.CENTER)

    radiobutton_3 = customtkinter.CTkRadioButton(root, text="Numbers and letters",
                                                 command=radiobutton_event, variable=radio_var, value=3,
                                                 fg_color=("white", "blue"),
                                                 hover_color="blue",
                                                 text_color="black", font=("Verdana", 20))
    radiobutton_3.place(relx=0.65, rely=0.69, anchor=tk.CENTER)

    # Back button to the start
    button = customtkinter.CTkButton(master=canvas,
                                     command=lambda: remove_buttons(),
                                     width=220,
                                     height=64,
                                     border_width=0,
                                     corner_radius=10,
                                     text="Back to the main menu",
                                     font=("Verdana", 20))
    button.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

    def remove_buttons():
        radiobutton_1.destroy()
        radiobutton_2.destroy()
        radiobutton_3.destroy()
        start_screen()


def handle_key_press(event):
    print("")


class Square:
    def __init__(self, canvas, x, y, size, color):
        self.canvas = canvas
        self.rect = canvas.create_rectangle(x, y, x + size, y + size, fill=color, outline='black')
        self.text = None  # initialize text object to None

    def set_text(self, text, font_size=20):
        if not self.text:
            # create text object if it doesn't exist
            x1, y1, x2, y2 = self.canvas.bbox(self.rect)
            width = x2 - x1
            height = y2 - y1
            self.text = self.canvas.create_text(
                x1 + width / 2,
                y1 + height / 2,
                text=text,
                font=("Verdana", font_size)
            )
        else:
            # update existing text object
            self.canvas.itemconfig(self.text, text=text)


# A function for the starting stimuli of the test

def first_stimuli_setup():
    global link, n, test_duration, stacksize, sequence, q_list, x_values, start_time, \
        test_loop, end_time, time_a, i

    # Once we finish watching the first screen we generate a sequence
    sequence = generate_stimuli_sequence(n, int(test_duration * 10), 3)

    for i in range(stacksize):
        x = random.randint(1, 3)
        x_values.append(x)
        q_list.append("n - " + str(x))
    q_tuple = tuple(q_list)
    x_tuple = tuple(x_values)

    # Remove all past widgets
    for widget in canvas.winfo_children():
        widget.destroy()
    # link.destroy()

    # Button creation for starting the test
    button_begin = customtkinter.CTkButton(master=canvas,
                                           command=lambda: begin_stimuli(),
                                           width=220,
                                           height=64,
                                           border_width=0,
                                           corner_radius=10,
                                           text="Begin test",
                                           font=("Verdana", 20))
    button_begin.place(relx=0.5, rely=0.13, anchor=tk.CENTER)

    # get screen width and height
    screen_width = canvas.winfo_screenwidth()
    screen_height = canvas.winfo_screenheight()

    # calculate square positions based on screen width and height
    square_1_x = int(screen_width * 0.36)
    square_1_y = int(screen_height * 0.44)
    square_2_x = int(screen_width * 0.64)
    square_2_y = int(screen_height * 0.44)

    # draw a square on the canvas
    square_1 = canvas.create_rectangle(square_1_x - 200, square_1_y - 170, square_1_x + 200, square_1_y + 170,
                                       outline='black', fill='#F5DEB3')
    square_2 = canvas.create_rectangle(square_2_x - 200, square_2_y - 170, square_2_x + 200, square_2_y + 170,
                                       outline='black', fill='#F5DEB3')

    # get the coordinates of the top line of the first rectangle
    x1, y1, x2, y2 = canvas.coords(square_1)
    topline_x1 = (x1 + x2) / 2
    topline_y1 = y1

    # get the coordinates of the top line of the second rectangle
    x1, y1, x2, y2 = canvas.coords(square_2)
    topline_x2 = (x1 + x2) / 2
    topline_y2 = y1

    # create the labels and place them at the middle point of the top line of the rectangles
    label1 = customtkinter.CTkLabel(master=canvas,
                                    text="Next item",
                                    width=100,
                                    height=50,
                                    fg_color=("white", "white"),
                                    text_color="black",
                                    corner_radius=10,
                                    font=("Verdana", 20))
    label1.place(x=topline_x1, y=topline_y1 - 25, anchor=tk.CENTER)

    label2 = customtkinter.CTkLabel(master=canvas,
                                    text="Question",
                                    width=100,
                                    height=50,
                                    fg_color=("white", "white"),
                                    text_color="black",
                                    corner_radius=10,
                                    font=("Verdana", 20))
    label2.place(x=topline_x2, y=topline_y2 - 25, anchor=tk.CENTER)

    if stacksize == 20:
        distance_x = 180
        x_start = topline_x1 - 90
        y_start = topline_y1 + 360
    elif stacksize == 30:
        distance_x = 360
        x_start = topline_x1 - 270
        y_start = topline_y1 + 360
    elif stacksize == 10:
        distance_x = 0
        x_start = topline_x1 + 100
        y_start = topline_y1 + 360
    label3 = customtkinter.CTkLabel(master=canvas,
                                    text="Stack of itmes :",
                                    width=100,
                                    height=50,
                                    fg_color=("white", "white"),
                                    text_color="black",
                                    corner_radius=10,
                                    font=("Verdana", 20))
    label3.place(x=topline_x1 - distance_x, y=topline_y1 + 380, anchor=tk.CENTER)
    size = 40
    color = 'white'
    squares = []  # list to store Square objects

    for i in range(stacksize):
        x = x_start + i * size
        y = y_start
        square = Square(canvas, x, y, size, color)
        squares.append(square)

    button_yes = customtkinter.CTkButton(master=canvas,
                                         width=220,
                                         height=64,
                                         border_width=0,
                                         corner_radius=10,
                                         text="Yes",
                                         font=("Verdana", 30))
    button_yes.place(relx=0.42, rely=0.85, anchor=tk.CENTER)

    button_no = customtkinter.CTkButton(master=canvas,
                                        width=220,
                                        height=64,
                                        border_width=0,
                                        corner_radius=10,
                                        text="No",
                                        font=("Verdana", 30))
    button_no.place(relx=0.58, rely=0.85, anchor=tk.CENTER)

    def begin_stimuli():

        global time_a, start_time, i, count, current_index, helper

        # Setting the time
        start_time = time.time()
        button_yes = customtkinter.CTkButton(master=canvas,
                                             command=lambda answer="Yes",: handle_test_key_press(
                                                 answer),
                                             width=220,
                                             height=64,
                                             border_width=0,
                                             corner_radius=10,
                                             text="Yes",
                                             font=("Verdana", 30))
        button_yes.place(relx=0.42, rely=0.85, anchor=tk.CENTER)

        button_no = customtkinter.CTkButton(master=canvas,
                                            command=lambda answer="No": handle_test_key_press(
                                                answer),
                                            width=220,
                                            height=64,
                                            border_width=0,
                                            corner_radius=10,
                                            text="No",
                                            font=("Verdana", 30))
        button_no.place(relx=0.58, rely=0.85, anchor=tk.CENTER)

        label_4 = customtkinter.CTkLabel(master=canvas,
                                         text="The first 3 items are displayed , each card is displayed for \n" +
                                              "2.5 seconds. The test begins when the forth item is displayed.",
                                         width=100,
                                         height=50,
                                         text_color="red",
                                         fg_color=("white", "white"),
                                         corner_radius=10,
                                         font=("Verdana", 20))
        label_4.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

        text_x_1 = square_1_x
        text_y_1 = square_1_y
        text_obj_1 = canvas.create_text(text_x_1, text_y_1, text='', font=("Arial", 70), fill="black", anchor="center")

        text_x_2 = square_2_x
        text_y_2 = square_2_y
        text_obj_2 = canvas.create_text(text_x_2, text_y_2, text='', font=("Arial", 70), fill="black", anchor="center")

        button_show = customtkinter.CTkButton(master=canvas,
                                              command=lambda index=helper: show_letter_string_help(sequence,
                                                                                                   squares, index),
                                              width=220,
                                              height=64,
                                              border_width=0,
                                              corner_radius=10,
                                              text="Show items",
                                              font=("Verdana", 30))
        button_show.place(relx=0.82, rely=0.85, anchor=tk.CENTER)

        def end_screen():
            print("Test complete")
            final_screen()

        def remove_letter_string(sequence, squares, i):
            canvas.itemconfig(text_obj_1, text="")
            for j in range(i):
                squares[j].set_text("", font_size=22)

        def show_letter_string_help(sequence, squares, index):
            global gothelp, helper
            gothelp = 1
            for j in range(helper):
                squares[j].set_text(sequence[j], font_size=20)

        def show_letter_string(sequence, squares, index):
            print("needs to give back " + str(index) + " letters")
            for j in range(index):
                squares[j].set_text(sequence[j], font_size=22)
            canvas.itemconfig(text_obj_2, text="")

        def question_time(sequence, squares, i):

            global time_a, count, q_range, stacksize, question

            if i == 4:
                time_a = time.time()
            count = i
            label_4.destroy()
            canvas.itemconfig(text_obj_1, text=sequence[i])
            canvas.itemconfig(text_obj_2, text=q_tuple[i])
            squares[i].set_text(sequence[i], font_size=22)
            label_q = customtkinter.CTkLabel(master=canvas,
                                             text="The item is " + str(sequence[i]) + "  " + ", the question " + str(
                                                 q_tuple[i]) + " asks if this card is\n" +
                                                  "the same as " + str(x_tuple[i]) + " items ago.",
                                             width=100,
                                             height=50,
                                             text_color="red",
                                             fg_color=("white", "white"),
                                             corner_radius=10,
                                             font=("Verdana", 20))
            label_q.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
            question = str(q_tuple[i])
            canvas.after(q_range * 1000, remove_letter_string, sequence, squares, i)

        def test_loop(i):
            if i < stacksize:
                canvas.itemconfig(text_obj_1, text=sequence[i])
                squares[i].set_text(sequence[i], font_size=22)
                canvas.after(2500, question_time, sequence, squares, i)
            else:
                final_screen()

        def show_letter(sequence, squares, i=0):
            if i < 3:
                canvas.itemconfig(text_obj_1, text=sequence[i])
                squares[i].set_text(sequence[i], font_size=22)
                canvas.after(2500, show_letter, sequence, squares, i + 1)
            else:
                test_loop(i)

        # Event handle for test screen
        def handle_test_key_press(answer):

            global time_b, sequence, count, x_values
            if answer == "Yes":
                time_b = time.time()
                update_score('Yes', sequence, x_values[count])
            elif answer == "No":
                time_b = time.time()
                update_score('No', sequence, x_values[count])

        # Update the correct and incorrect scores based on the user's response.

        def update_score(answer, sequence, number):

            # Creating a timestamp and values
            global result, timestamp, time_a, time_b, current_index, count, gothelp, helper, expected, received , \
                question

            timestamp = datetime.datetime.now().strftime('%d-%m-%Y_%H:%M:%S')
            if answer == 'Yes':
                if sequence[current_index] == sequence[current_index - number]:
                    result = 1
                    print(str(sequence[current_index]) + " " + str(sequence[current_index - number]) + " ")
                    print("Correct")
                else:
                    result = 0
                    print(str(sequence[current_index]) + " " + str(sequence[current_index - number]) + " ")
                    print("Incorrect")
            elif answer == 'No':
                if sequence[current_index] != sequence[current_index - number]:
                    result = 1
                    print(str(sequence[current_index]) + " " + str(sequence[current_index - number]) + " ")
                    print("Correct")
                else:
                    result = 0
                    print(str(sequence[current_index]) + " " + str(sequence[current_index - number]) + " ")
                    print("Incorrect")

            expected = str(sequence[current_index])
            received = str(sequence[current_index - number])
            time_diff = time_b - time_a
            # Update time_a for the next iteration
            time_a = time_b

            # Updating results
            #with open(str(fileName) + '_N-back.csv', mode='a', newline='') as file:
            #    writer = csv.writer(file)
            #    writer.writerow([timestamp, result, time_diff, gothelp, stacksize , expected , question , received])
            add_test(visit_id, timestamp, result, time_diff, gothelp, stacksize , expected , question , received, None, None, 'NBack')

            show_letter_string(sequence, squares, current_index)
            gothelp = 0
            count += 1
            current_index += 1
            helper = current_index
            test_loop(current_index)

        # call the show_letter function to display each letter one after another
        canvas.after(0, show_letter, sequence, squares)

        def final_screen():
            canvas.delete("all")
            # Remove all past widgets
            for widget in canvas.winfo_children():
                widget.destroy()
            label_end = customtkinter.CTkLabel(master=canvas,
                                               text="Test results have been saved \n" +
                                                    "Thank you for youre time.",
                                               width=100,
                                               height=50,
                                               text_color="black",
                                               fg_color=("white", "white"),
                                               corner_radius=10,
                                               font=("Verdana", 30))
            label_end.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

            button_show = customtkinter.CTkButton(master=canvas,
                                                  command=lambda: root.destroy(),
                                                  width=220,
                                                  height=64,
                                                  border_width=0,
                                                  corner_radius=10,
                                                  text="Exit program",
                                                  font=("Verdana", 20))
            button_show.place(relx=0.5, rely=0.55, anchor=tk.CENTER)


# URL open for the image
def callback(url):
    webbrowser.open_new(url)


def trail_making_call():
    today = datetime.datetime.today().strftime("%m/%d/%Y")
    visit_id = add_visit(treatment_id, today, f'Trail Making {get_visits(treatment_id, "Trail Making")}', None, None, None, None, None, None, None, None)
    trail.main(root, canvas, visit_id)


def cpt_call(moxo=False):
    today = datetime.datetime.today().strftime("%m/%d/%Y")
    if moxo:
        visit_id = add_visit(treatment_id, today, f'MOXO CPT {get_visits(treatment_id, "MOXO CPT")}', None, None, None, None, None, None, None, None)
    else:
        visit_id = add_visit(treatment_id, today, f'Conners CPT {get_visits(treatment_id, "Conners CPT")}', None, None, None, None, None, None, None, None)
    cpt.main(root, canvas, visit_id_=visit_id, moxo=moxo)
    for widget in canvas.winfo_children():
        widget.destroy()
    start_screen()

# The home page
def start_screen():
    global link

    # Remove all past widgets
    for widget in canvas.winfo_children():
        widget.destroy()

    # load the PNG image using PhotoImage
    # image = Image.open('N-back-tkinter-1/N-back-tkinter/Image/man.png')
    # image_label = customtkinter.CTkLabel(master=canvas, text='',
    #                                      image=customtkinter.CTkImage(light_image=image, size=(650, 650)))
    # image_label.place(relx=0.35, rely=0.55, anchor=tk.CENTER)
    # image_label.image = image

    label = customtkinter.CTkLabel(master=canvas,
                                   text="Test Selection",
                                   width=400,
                                   height=200,
                                   text_color="black",
                                   fg_color=("white", "white"),
                                   corner_radius=10,
                                   font=("Verdana", 50))
    label.place(relx=0.5, rely=0.12, anchor=tk.CENTER)

    style = ttk.Style()
    style.configure("Link.TLabel", background="white")
    # link = ttk.Label(root, text="A png from pngtree.com", foreground="blue", style="Link.TLabel", font=("Verdana", 16),cursor="hand2")
    # link.place(relx=0.35, rely=0.9, anchor=tk.CENTER)
    # link.bind("<Button-1>", lambda e: callback(link["text"]))

    # Create the first button
    button1 = customtkinter.CTkButton(master=canvas,
                                      command= cpt_call,
                                      width=220,
                                                                       height=65,
                                      border_width=0,
                                      corner_radius=10,
                                      text="Conners CPT",
                                      font=("Verdana", 20))
    button1.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

    # Create the second button
    button2 = customtkinter.CTkButton(master=canvas,
                                      command=lambda: cpt_call(True),
                                      width=220,
                                                                       height=65,
                                      border_width=0,
                                      corner_radius=10,
                                      text="MOXO CPT",
                                      font=("Verdana", 20))
    button2.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

    # Create the third button
    button3 = customtkinter.CTkButton(master=canvas,
                                      command= n_back_menu,
                                      width=220,
                                                                       height=65,
                                      border_width=0,
                                      corner_radius=10,
                                      text="N-Back",
                                      font=("Verdana", 20))
    button3.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

    # Create the forth button
    button4 = customtkinter.CTkButton(master=canvas,
                                      command= trail_making_call,
                                      width=220,
                                                                       height=65,
                                      border_width=0,
                                      corner_radius=10,
                                      text="Trail Making",
                                      font=("Verdana", 20))
    button4.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

    # Create the forth button
    button5 = customtkinter.CTkButton(master=canvas,
                                      command= root.destroy,
                                      width=220,
                                                                       height=65,
                                      border_width=0,
                                      corner_radius=10,
                                      text="Exit",
                                      font=("Verdana", 20))
    button5.place(relx=0.5, rely=0.75, anchor=tk.CENTER)




def n_back_menu():
    global link, visit_id
    today = datetime.datetime.today().strftime("%m/%d/%Y")
    visit_id = add_visit(treatment_id, today, f'N-Back {get_visits(treatment_id, "N-Back")}', None, None, None, None, None, None, None, None)
    # Remove all past widgets
    for widget in canvas.winfo_children():
        widget.destroy()

    # load the PNG image using PhotoImage
    image = Image.open('N-back-tkinter/Image/man.png')
    image_label = customtkinter.CTkLabel(canvas, text='',
                                         image=customtkinter.CTkImage(light_image=image, size=(650, 650)))
    image_label.place(relx=0.35, rely=0.55, anchor=tk.CENTER)
    image_label.image = image

    label = customtkinter.CTkLabel(master=canvas,
                                   text="Welcome to the N-Back test",
                                   width=400,
                                   height=200,
                                   text_color="black",
                                   fg_color=("white", "white"),
                                   corner_radius=10,
                                   font=("Verdana", 50))
    label.place(relx=0.35, rely=0.12, anchor=tk.CENTER)

    # style = ttk.Style()
    # style.configure("Link.TLabel", background="white")
    # link = ttk.Label(root, text="A png from pngtree.com", foreground="blue", style="Link.TLabel", font=("Verdana", 16),
    #                  cursor="hand2")
    # link.place(relx=0.35, rely=0.9, anchor=tk.CENTER)
    # link.bind("<Button-1>", lambda e: callback(link["text"]))

    # Create the first button
    button1 = customtkinter.CTkButton(master=canvas,
                                      command=lambda: first_stimuli_setup(),
                                      width=220,
                                      height=64,
                                      border_width=0,
                                      corner_radius=10,
                                      text="Test screen",
                                      font=("Verdana", 20))
    button1.place(relx=0.57, rely=0.30, anchor=tk.CENTER)

    # Create the second button
    button2 = customtkinter.CTkButton(master=canvas,
                                      command=lambda: instructions_screen(),
                                      width=220,
                                      height=64,
                                      border_width=0,
                                      corner_radius=10,
                                      text="Test instructions",
                                      font=("Verdana", 20))
    button2.place(relx=0.57, rely=0.45, anchor=tk.CENTER)

    # Create the third button
    button3 = customtkinter.CTkButton(master=canvas,
                                      command=lambda: test_settings_screen(),
                                      width=220,
                                      height=64,
                                      border_width=0,
                                      corner_radius=10,
                                      text="Test settings",
                                      font=("Verdana", 20))
    button3.place(relx=0.57, rely=0.6, anchor=tk.CENTER)

    # Create the forth button
    button4 = customtkinter.CTkButton(master=canvas,
                                      command=lambda: root.destroy(),
                                      width=220,
                                      height=64,
                                      border_width=0,
                                      corner_radius=10,
                                      text="Exit",
                                      font=("Verdana", 20))
    button4.place(relx=0.57, rely=0.75, anchor=tk.CENTER)

    global space_pressed

    # Bind the space key to handle_key_press function
    # root.bind("<KeyPress>", handle_key_press)

    # # Loop until space key is pressed
    # space_pressed = False
    # while not space_pressed:
    #     root.update()

    # root.unbind("<KeyPress>")



# The actual running of the program
treatment_id = int(sys.argv[1])
if __name__ == "__main__":
    # The first screen is shown
    start_screen()

    # The final running phase of all functions
    root.mainloop()