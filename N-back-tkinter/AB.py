import tkinter
import tkinter.messagebox
import csvfile as csvfile
import customtkinter
import csv
import random
import os
import time
import string
import datetime
import math
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from PIL import ImageTk, Image
import webbrowser
import csv
import datetime
import os
import sqlite3
from mydb import add_test

# Set up colors
black = "#000000"
white = "#FFFFFF"
yellow = "#EEEE3B"

# Set up the display window

# Global vars
lines = [None] * 20
current_index = 0
link = []
line = None
circles = []
lines_counter = 0
current_line = [[] for _ in range(100)]
line_counter = 0
circles_a = []
circles_b = []
pressings = 0
marker = 1
x1 = 0
y1 = 0
x2 = 0
y2 = 0
n = 10
last_x = 0
last_y = 0
end_x = 0
end_y = 0
coordinates = []
uppercase_letters = string.ascii_uppercase
test_duration = 0
start_test_time = 0
letter_count = 0
finish_count = n
near_circle = None
circle_signs_B = [1, "A", 2, "B", 3, "C", 4, "D", 5, "E"]
step = 1
start_x = 0
start_y = 0
current_circle = 0
init_timestamp = None
start_time = None
curr_test = None

# Getting the current working directory
current_directory = os.getcwd()


def generate_coordinates(n):
    global root, canvas
    global coordinates
    coordinates = []
    radius = min(root.winfo_width() - 150, root.winfo_height() - 150) // 2

    # Generate n coordinates evenly spaced around a circle
    for i in range(n):
        angle = 2 * math.pi * i / n
        x = int(root.winfo_width() // 2 + radius * math.cos(angle))
        y = int(root.winfo_height() // 2 + radius * math.sin(angle))
        coordinates.append((x, y))

    return coordinates


# Changing how many circles can be formed during the test
def test_settings_screen():
    global canvas
    global link
    # Remove all past widgets
    for widget in canvas.winfo_children():
        widget.destroy()
    # link.destroy()

    def set_circle_amount(num):
        global n, circle_signs_B
        n = int(num)
        if n == 10:
            circle_signs_B = [1, "A", 2, "B", 3, "C", 4, "D", 5, "E"]
        if n == 5:
            circle_signs_B = [1, "A", 2, "B", 3]
        if n == 15:
            circle_signs_B = [1, "A", 2, "B", 3, "C", 4, "D", 5, "E", 6, "F", 7, "G", 8]

    def set_test_time(num):
        global n
        n = int(num)

    # Remove all past widgets
    for widget in canvas.winfo_children():
        widget.destroy()

    # Setting the welcoming label for the test
    canvas.label = customtkinter.CTkLabel(master=canvas,
                                          text="Number of circles",
                                          width=100,
                                          height=50,
                                          fg_color=("white", "white"),
                                          text_color="black",
                                          corner_radius=10,
                                          font=("Verdana", 20))
    canvas.label.place(relx=0.5, rely=0.21, anchor=tkinter.CENTER)

    # slider for choosing how many circles we want
    slider = customtkinter.CTkSlider(master=canvas, from_=5, to=15, number_of_steps=2, height=20,
                                     command=lambda num: set_circle_amount(num))
    slider.place(relx=0.5, rely=0.32, anchor=tkinter.CENTER)

    canvas.label = customtkinter.CTkLabel(master=canvas,
                                          text="5",
                                          width=20,
                                          height=20,
                                          fg_color=("white", "white"),
                                          text_color="black",
                                          corner_radius=10)
    canvas.label.place(relx=0.424, rely=0.32, anchor=tkinter.CENTER)

    canvas.label = customtkinter.CTkLabel(master=canvas,
                                          text="10",
                                          width=20,
                                          height=20,
                                          fg_color=("white", "white"),
                                          text_color="black",
                                          corner_radius=10)
    canvas.label.place(relx=0.5, rely=0.293, anchor=tkinter.CENTER)

    canvas.label = customtkinter.CTkLabel(master=canvas,
                                          text="15",
                                          width=20,
                                          height=20,
                                          fg_color=("white", "white"),
                                          text_color="black",
                                          corner_radius=10)
    canvas.label.place(relx=0.577, rely=0.32, anchor=tkinter.CENTER)

    canvas.label = customtkinter.CTkLabel(master=canvas,
                                          text="Maximum time limit for each part",
                                          width=100,
                                          height=50,
                                          fg_color=("white", "white"),
                                          text_color="black",
                                          corner_radius=10,
                                          font=("Verdana", 20))
    canvas.label.place(relx=0.5, rely=0.43, anchor=tkinter.CENTER)

    # slider for choosing how much time we want
    slider = customtkinter.CTkSlider(master=canvas, from_=60, to=120, number_of_steps=2, height=20,
                                     command=lambda num: set_test_time(num))
    slider.place(relx=0.5, rely=0.54, anchor=tkinter.CENTER)

    canvas.label = customtkinter.CTkLabel(master=canvas,
                                          text="60",
                                          width=20,
                                          height=20,
                                          fg_color=("white", "white"),
                                          text_color="black",
                                          corner_radius=10)
    canvas.label.place(relx=0.424, rely=0.54, anchor=tkinter.CENTER)

    canvas.label = customtkinter.CTkLabel(master=canvas,
                                          text="90",
                                          width=20,
                                          height=20,
                                          fg_color=("white", "white"),
                                          text_color="black",
                                          corner_radius=10)
    canvas.label.place(relx=0.5001, rely=0.513, anchor=tkinter.CENTER)

    canvas.label = customtkinter.CTkLabel(master=canvas,
                                          text="120",
                                          width=20,
                                          height=20,
                                          fg_color=("white", "white"),
                                          text_color="black",
                                          corner_radius=10)
    canvas.label.place(relx=0.577, rely=0.54, anchor=tkinter.CENTER)

    # Back button to the start
    canvas.button = customtkinter.CTkButton(master=canvas,
                                            command=lambda: AB_start_screen(),
                                            width=220,
                                            height=64,
                                            border_width=0,
                                            corner_radius=10,
                                            text="Back to the main menu",
                                            font=("Verdana", 20))
    canvas.button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)


def instructions_screen():
    global canvas
    global link
    # Remove all past widgets
    for widget in canvas.winfo_children():
        widget.destroy()
    # link.destroy()

    # Instructions label
    canvas.label = customtkinter.CTkLabel(master=canvas,
                                          text="The test is being comprised of 2 part:\n"
                                               + "\n"
                                               + "Part A - Circles will be shown on the screen with digits "
                                                 "in their center.\n"
                                               + "You must connect all the circles by drawing a line to them according to the "
                                                 "digits in ascending order.\n"
                                               + "\n"
                                               + "1 --> 2 --> 3 --> 4 --> 5 --> 6 --> 7 --> 8 ...."
                                               + "\n"
                                               + "\n"
                                               + "Part B - Circles will be shown on the screen with digits and letters"
                                                 " in their center.\n"
                                               + "You must connect all the circles by drawing a line to them according to the "
                                                 "the following order :\n"
                                               + "\n"
                                               + "1 --> A --> 2 --> B --> 3 --> C --> 4 --> D ....",
                                          width=400,
                                          height=300,
                                          fg_color=("white", "white"),
                                          text_color="black",
                                          corner_radius=10,
                                          font=("Verdana", 20))
    canvas.label.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

    # Back button to the start
    canvas.button = customtkinter.CTkButton(master=canvas,
                                            command=lambda: AB_start_screen(),
                                            width=220,
                                            height=64,
                                            border_width=0,
                                            corner_radius=10,
                                            text="Back to the main menu",
                                            font=("Verdana", 20))
    canvas.button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)


def create_circles(n, option):
    global canvas
    global coordinates, circles
    digits = list(range(1, n + 1))
    button_size = 65
    colors = []
    iterator = 0
    count_letter = 0
    count_num = 0

    # Choosing 25 random bright hex colors for the circles
    for i in range(25):
        while True:
            red = random.randint(200, 255)
            green = random.randint(200, 255)
            blue = random.randint(200, 255)
            hex_color = '#%02x%02x%02x' % (red, green, blue)
            if int(hex_color[1:], 16) < int('F0F0F0', 16):
                break
        colors.append(hex_color)

    for i in range(n):
        digit = digits[i]
        x, y = coordinates[i]

        # Condition for choosing if we create circles for A or B
        if option == 0:
            circle_radius = button_size // 2
            circle = canvas.create_oval(x - circle_radius, y - circle_radius,
                                        x + circle_radius, y + circle_radius,
                                        width=2, fill=colors[i])
            canvas.create_text(x, y, text=str(digit), font=("Verdana", 25))
            circles.append((x, y))
        else:
            if iterator == 0:
                digit = digits[count_num]
                circle_radius = button_size // 2
                canvas.create_oval(x - circle_radius, y - circle_radius,
                                            x + circle_radius, y + circle_radius,
                                            width=2, fill=colors[i])
                canvas.create_text(x, y, text=str(digit), font=("Verdana", 25))
                iterator = 1
                count_num += 1
                circles.append((x, y))
            else:
                circle_radius = button_size // 2
                canvas.create_oval(x - circle_radius, y - circle_radius,
                                            x + circle_radius, y + circle_radius,
                                            width=2, fill=colors[count_letter])
                canvas.create_text(x, y, text=str(uppercase_letters[count_letter]), font=("Verdana", 25))
                count_letter += 1
                iterator = 0
                circles.append((x, y))

    return circles


# A function for handling the pressing during test B , gathers x/y cords
def handle_circle_press_part_B(num, current_line):
    global canvas
    global pressings, x1, y1, x2, y2, marker, time_a, time_b, test_duration, start_test_time, uppercase_letters \
        , letter_count, step, circle_signs_B
    timestamp = datetime.datetime.now()
    if pressings == 0:
        if num == 1:
            print("Circle number " + str(num) + " has been drawn upon")
            time_a = timestamp
            pressings += 1
            marker += 1
        else:
            print("Start from digit number 1 !")
            pressings = 0
            result = 0
            # Updating results
            #with open(init_timestamp + 'Part_B.csv', mode='a', newline='') as file:
            #    writer = csv.writer(file)
            #    writer.writerow([timestamp.strftime("%d-%m-%Y_%H:%M"), result, 0])
            add_test(visit_id, timestamp.strftime("%d-%m-%Y_%H:%M:%S"), result, None, None, None, None, None, None, None, 0, 'Trail part B')
            canvas.after(100, show_label, marker, current_line)
    else:
        if num == circle_signs_B[step]:
            print("Correct !")
            result = 1
            step += 1
            time_b = timestamp
            time_diff = time_b - time_a

            # Updating results
            #with open(init_timestamp + 'Part_B.csv', mode='a', newline='') as file:
            #    writer = csv.writer(file)
            #    writer.writerow([timestamp.strftime("%d-%m-%Y_%H:%M"), result, str(time_diff)])
            add_test(visit_id, timestamp.strftime("%d-%m-%Y_%H:%M"), result, None, None, None, None, None, None, None, time_diff, 'Trail part B')
            # Update time_a for the next iteration
            time_a = time_b
        else:
            print("Inorrect !")
            result = 0
            time_b = timestamp
            time_diff = time_b - time_a

            # Updating results
            #with open(init_timestamp + 'Part_B.csv', mode='a', newline='') as file:
            #    writer = csv.writer(file)
            #    writer.writerow([timestamp.strftime("%d-%m-%Y_%H:%M"), result, str(time_diff)])
            add_test(visit_id, timestamp.strftime("%d-%m-%Y_%H:%M:%S"), result, None, None, None, None, None, None, None, time_diff, 'Trail part B')
            # Update time_a for the next iteration
            time_a = time_b
            canvas.after(100, show_label, circle_signs_B[step], current_line)

        # The test has ended , moving to final_screen
        if step == n:
            print("The limit has been reached")
            pressings = 0
            final_screen()


def test_loop_part_B():
    global canvas
    # Remove all past widgets
    global coordinates, start_time, init_timestamp, circles
    for widget in canvas.winfo_children():
        widget.destroy()
    # link.destroy()

    # Binding the mouse for drawing the line and creating a set of circles
    canvas.bind("<Button-1>", start_drawing)
    canvas.bind("<B1-Motion>", end_drawing)
    canvas.bind("<ButtonRelease-1>", check_current_line)
    coordinates = []
    coordinates = generate_coordinates(n)
    circles = create_circles(n, 1)

    start_time = time.time()
    #with open(os.path.join(current_directory, init_timestamp + '_Part_B.csv'), mode='w',
    #          newline='') as csvfile:
    #    fieldnames = ["Timestamp", "result", "elapsed_time"]
    #    writer_a = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #    writer_a.writeheader()

    canvas.button = customtkinter.CTkButton(master=canvas,
                                            command=lambda: final_screen(),
                                            width=50,
                                            height=50,
                                            border_width=0,
                                            corner_radius=10,
                                            text="End part B",
                                            font=("Verdana", 20))
    canvas.button.place(relx=0.02, rely=0.05, anchor='w')


def start_test_B():
    global canvas
    global coordinates, circles, curr_test
    curr_test = 1
    for widget in canvas.winfo_children():
        widget.destroy()
    canvas.delete("all")
    canvas.unbind("<Button-1>")
    canvas.unbind("<B1-Motion>")
    canvas.unbind("<ButtonRelease-1>")
    canvas.label = customtkinter.CTkLabel(master=canvas,
                                          text="Remember prevent from drawing lines\n"
                                               + "that collide with each other as much as you can !",
                                          width=20,
                                          height=20,
                                          fg_color=("white", "white"),
                                          text_color="black",
                                          font=("Verdana", 30),
                                          corner_radius=10)
    canvas.label.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

    canvas.button = customtkinter.CTkButton(master=canvas,
                                            command=lambda: test_loop_part_B(),
                                            width=220,
                                            height=64,
                                            border_width=0,
                                            corner_radius=10,
                                            text="Press to start part B",
                                            font=("Verdana", 20))
    canvas.button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)


# The actual loop of the test
def test_loop_part_A():
    global canvas
    global link, circles_a, coordinates, pressings, pressed_circles_a, current_directory, start_time, init_timestamp
    # Remove all past widgets
    for widget in canvas.winfo_children():
        widget.destroy()
    # link.destroy()

    init_timestamp = datetime.datetime.now().strftime('%d-%m-%Y_%H:%M:%S')
    start_time = time.time()
    #with open(os.path.join(current_directory, init_timestamp + '_Part_A.csv'), mode='w',
    #          newline='') as csvfile:
    #    fieldnames = ["Timestamp", "result", "elapsed_time"]
    #    writer_a = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #    writer_a.writeheader()

    # Binding the mouse for drawing the line and creating a set of circles
    canvas.bind("<Button-1>", start_drawing)
    canvas.bind("<B1-Motion>", end_drawing)
    canvas.bind("<ButtonRelease-1>", check_current_line)
    coordinates = []
    coordinates = generate_coordinates(n)
    circles_a = create_circles(n, 0)
    canvas.button = customtkinter.CTkButton(master=canvas,
                                            command=lambda: start_test_B(),
                                            width=50,
                                            height=50,
                                            border_width=0,
                                            corner_radius=10,
                                            text="End part A",
                                            font=("Verdana", 20))
    canvas.button.place(relx=0.02, rely=0.05, anchor='w')


def start_test_A():
    global canvas
    global link, curr_test
    # Remove all past widgets
    for widget in canvas.winfo_children():
        widget.destroy()
    # link.destroy()
    curr_test = 0
    canvas.label = customtkinter.CTkLabel(master=canvas,
                                          text="Remember prevent from drawing lines\n"
                                               + "that collide with each other as much as you can !",
                                          width=20,
                                          height=20,
                                          fg_color=("white", "white"),
                                          text_color="black",
                                          font=("Verdana", 30),
                                          corner_radius=10)
    canvas.label.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

    canvas.button = customtkinter.CTkButton(master=canvas,
                                            command=lambda: test_loop_part_A(),
                                            width=220,
                                            height=64,
                                            border_width=0,
                                            corner_radius=10,
                                            text="Press to start part A",
                                            font=("Verdana", 20))
    canvas.button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)


# Once a mistake has been made a label will be shown
def show_label(num, current_line):
    global canvas
    def paint_line(coords_list):
        # create the line
        canvas.create_line(coords_list, fill="white", width=8, tags="line")

        # add the points to the "line" tag on the canvas
        for coords in coords_list:
            x, y = coords
            canvas.addtag_withtag("line", canvas.find_closest(x, y)[0])

    paint_line(current_line)
    canvas.label = customtkinter.CTkLabel(master=canvas,
                                          text=("Incorrect pick, you need to draw a line to circle with the sign "
                                                + str(num)),
                                          fg_color=("white", "white"),
                                          text_color="red",
                                          corner_radius=10,
                                          font=("Verdana", 30))
    canvas.label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    canvas.after(1500, lambda: canvas.label.destroy())


# A function to send the user to the website of the picture
def callback(url):
    webbrowser.open_new(url)


# End screen to the test
def final_screen():
    global canvas
    canvas.delete("all")
    # Remove all past widgets
    for widget in canvas.winfo_children():
        widget.destroy()
    canvas.unbind("<B1-Motion>")
    canvas.unbind("<ButtonRelease-1>")
    label_end = customtkinter.CTkLabel(master=canvas,
                                       text="Test results of both tests have been saved \n" +
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


def check_current_line(event):
    global canvas
    global line, lines, circles, current_circle, start_x, start_y, end_x, end_y, n, init_timestamp, start_time
    circle_center_x = circles[current_circle][0]
    circle_center_y = circles[current_circle][1]
    circle_radius = 20
    result = 0
    distance_1 = ((start_x - circle_center_x) ** 2 + (start_y - circle_center_y) ** 2) ** 0.5
    if distance_1 <= circle_radius:
        # if the line started in the current circle
        circle_center_x = circles[current_circle + 1][0]
        circle_center_y = circles[current_circle + 1][1]
        distance_2 = ((end_x - circle_center_x) ** 2 + (end_y - circle_center_y) ** 2) ** 0.5
        if distance_2 <= circle_radius:
            # and if the line ended in the next circle
            # insert to csv result 1
            result = 1
            lines.append([start_x, start_y, end_x, end_y])
            line = None
            current_circle += 1
            if current_circle == n - 1:
                if curr_test == 0:
                    current_circle = 0
                    circles = []
                    lines = []
                    start_test_B()
                else:
                    return
                    final_screen()
        else:
            # Start OK end No
            canvas.delete(line)
    else:
        # Not Ok
        canvas.delete(line)

    timestamp = datetime.datetime.now()
    curr_time = time.time()
    elapsed_time = curr_time - start_time
    if curr_test == 0:
        #with open(init_timestamp + '_Part_A.csv', mode='a', newline='') as file:
        #    writer = csv.writer(file)
        #    writer.writerow([timestamp.strftime('%d-%m-%Y_%H:%M:%S'), result, elapsed_time])
        add_test(visit_id, timestamp.strftime("%d-%m-%Y_%H:%M:%S"), result, None, None, None, None, None, None, None, elapsed_time, 'Trail part A')
    else:
        #with open(init_timestamp + '_Part_B.csv', mode='a', newline='') as file:
        #    writer = csv.writer(file)
        #    writer.writerow([timestamp.strftime('%d-%m-%Y_%H:%M:%S'), result, elapsed_time])
        add_test(visit_id, timestamp.strftime("%d-%m-%Y_%H:%M:%S"), result, None, None, None, None, None, None, None, elapsed_time, 'Trail part A')


def start_drawing(event):
    global start_x, start_y
    start_x = event.x
    start_y = event.y


def end_drawing(event):
    global canvas
    global end_x, end_y, lines, current_index
    end_x = event.x
    end_y = event.y
    if line is not None:
        canvas.delete(line)
    draw_line(start_x, start_y, end_x, end_y)
    # save_line(start_x, start_y, end_x, end_y)


def save_line(x1, y1, x2, y2):
    # Create a line dictionary and add it to the lines list
    current_index += 1
    line = {
        "start_x": x1,
        "start_y": y1,
        "end_x": x2,
        "end_y": y2
    }
    lines.append(line)


def draw_line(x1, y1, x2, y2):
    global canvas
    global line
    line = canvas.create_line(x1, y1, x2, y2, width=8, fill="#701dA8")
    lines.append(line)



def handle_key_press(event):
    global mouse_clicked
    mouse_clicked = True


def AB_start_screen():
    global root, canvas
    global link

    # Remove all past widgets
    for widget in canvas.winfo_children():
        widget.destroy()

    # load the PNG image using PhotoImage
    # image = Image.open('Image/map.png')
    # image_label = customtkinter.CTkLabel(canvas, text='',
    #                                      image=customtkinter.CTkImage(light_image=image, size=(650, 650)))
    # image_label.place(relx=0.35, rely=0.55, anchor=tk.CENTER)
    # image_label.image = image

    label = customtkinter.CTkLabel(master=canvas,
                                   text="Welcome to the trail making A & B test",
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
                                      command=lambda: start_test_A(),
                                      width=220,
                                      height=64,
                                      border_width=0,
                                      corner_radius=10,
                                      text="Test screen",
                                      font=("Verdana", 20))
    button1.place(relx=0.77, rely=0.30, anchor=tk.CENTER)

    # Create the second button
    button2 = customtkinter.CTkButton(master=canvas,
                                      command=lambda: instructions_screen(),
                                      width=220,
                                      height=64,
                                      border_width=0,
                                      corner_radius=10,
                                      text="Test instructions",
                                      font=("Verdana", 20))
    button2.place(relx=0.77, rely=0.45, anchor=tk.CENTER)

    # Create the third button
    button3 = customtkinter.CTkButton(master=canvas,
                                      command=lambda: test_settings_screen(),
                                      width=220,
                                      height=64,
                                      border_width=0,
                                      corner_radius=10,
                                      text="Test settings",
                                      font=("Verdana", 20))
    button3.place(relx=0.77, rely=0.6, anchor=tk.CENTER)

    # Create the forth button
    button3 = customtkinter.CTkButton(master=canvas,
                                      command=lambda: root.destroy(),
                                      width=220,
                                      height=64,
                                      border_width=0,
                                      corner_radius=10,
                                      text="Exit",
                                      font=("Verdana", 20))
    button3.place(relx=0.77, rely=0.75, anchor=tk.CENTER)

    
    # Bind the space key to handle_key_press function
    # root.bind("<Button-1>", handle_key_press)

    # # Loop until space key is pressed
    
    # mouse_clicked = False
    # while not mouse_clicked:
    #     root.update()

    # root.unbind("<Button-1>")


# The actual running of the program
visit_id = None
def main(ex_root, ex_canvas, visit_id_):
    global root, canvas, visit_id
    visit_id = visit_id_
    root, canvas = ex_root, ex_canvas
    for widget in canvas.winfo_children():
        widget.destroy()
    canvas.delete("all")
    # The first screen is shown
    AB_start_screen()
