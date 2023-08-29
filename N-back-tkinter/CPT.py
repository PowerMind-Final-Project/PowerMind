import tkinter as tk
from tkinter.font import Font
import time
import random
from random import randrange
import csv
import datetime
import os
import threading
import winsound
import sqlite3
from mydb import add_test

# Set up colors
black = "#000000"
white = "#FFFFFF"
yellow = "#EEEE3B"
blue = "#0847A8"
purple = "#701dA8"
green = "#20820A"
orange = "#D17F04"
red = "#910F00"
colors = [black, blue, purple, green, orange, red]

# Set up the variables for the test
correct_letter = 'X'
test_duration = 60
letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
sequence = []
current_index = 0
correct_score = 0
incorrect_score = 0
test_loop = True
result = 0
timestamp = 0
n = 3
time_a = 0
time_b = 0
counter = 0
switch_time = time.time()



# Define the cube class
class Cube:
    def __init__(self):
        self.size = 80
        self.x = randrange(self.size, root.winfo_width() - self.size, self.size)
        self.y = randrange(self.size, root.winfo_height() - self.size, self.size)
        self.z = randrange(self.size, 2 * self.size, self.size)
        self.dx = randrange(-5, 6)
        self.dy = randrange(-5, 6)
        self.speed = 10
        self.color = f'#{randrange(256):02x}{randrange(256):02x}{randrange(256):02x}'

        self.direction = [randrange(-1, 2), randrange(-1, 2), randrange(-1, 2)]
        while self.direction == [0, 0, 0]:
            self.direction = [randrange(-1, 2), randrange(-1, 2), randrange(-1, 2)]

        # Create the cube on the canvas
        self.cube = canvas.create_rectangle(self.x, self.y, self.x + self.size, self.y + self.size, fill=self.color)

    def move(self):
        # Move the cube
        self.x += self.dx
        self.y += self.dy

        # Check if the cube is hitting the edges of the canvas
        if self.x <= 0 or self.x + self.size >= canvas.winfo_width():
            self.dx = -self.dx
        if self.y <= 0 or self.y + self.size >= canvas.winfo_height():
            self.dy = -self.dy

        # Update the position of the cube on the canvas
        canvas.coords(self.cube, self.x, self.y, self.x + self.size, self.y + self.size)
        self.cube = canvas.create_rectangle(self.x, self.y, self.x + self.size, self.y + self.size, fill=self.color)


# Define a function to generate a random sequence of stimuli

def generate_sequence(n, sequence_length):
    global sequence
    sequence = []
    random_letters = random.choices(letters, k=sequence_length)
    sequence = [letter if (i + 1) % n != 0 else correct_letter for i, letter in enumerate(random_letters)]
    random.shuffle(sequence)
    return sequence

# Define a function to draw text on the canvas


def draw_text(canvas, text, color, x, y, font):
    canvas.create_text(x, y, text=str(text), fill=color, font=font)


# Update the correct and incorrect scores based on the user's response.


def update_score(key_press, correct_score, incorrect_score, sequence, current_index):
    global time_a, file_name
    global time_b
    global test_loop
    global counter, visit_id

    # Creating a timestamp and values
    timestamp = datetime.datetime.now().strftime('%d-%m-%Y_%H:%M:%S')
    if key_press == ' ':
        if sequence[current_index] == correct_letter:
            correct_score += 1
            result = 1
        else:
            incorrect_score += 1
            result = 0
    else:
        incorrect_score += 1
        result = 0

    time_diff = time_b - time_a
    # Update time_a for the next iteration
    time_a = time_b

    # Updating results
    #with open(file_name, mode='a', newline='') as file:
    #    writer = csv.writer(file)
    #    writer.writerow([timestamp, result, time_diff])
    if is_moxo:
        add_test(visit_id, timestamp, result, None, None, None, None, None, None, time_diff, None, 'MOXO CPT')
    else:
        add_test(visit_id, timestamp, result, None, None, None, None, None, None, time_diff, None, 'Conners CPT')

    return correct_score, incorrect_score


# Define a function to display the final score


# Define a function to display the final score
def display_final_score(correct_score, incorrect_score):
    global root, canvas, font_a, font_b
    # clear the canvas
    canvas.delete("all")

    # Display the final score
    final_score = "Final score: {} correct, {} incorrect".format(
        correct_score, incorrect_score)
    draw_text(canvas, final_score, black, root.winfo_width() / 2, root.winfo_height() / 2)

    # Update the display
    canvas.update()

    # Wait for 2.5 seconds
    root.after(2500, root.destroy)


# Event handle for start screen and first_stimuli screen


def handle_key_press(event):
    global space_pressed
    if event.keysym == "space":
        space_pressed = True


# A function for the starting screen of the test


def start_screen():
    global root, canvas, font_a, font_b, is_moxo
    # Printing instructions
    if is_moxo:
        first_text = "Press space to show the instructions of MOXO CPT test."
    else:
        first_text = "Press space to show the instructions of Connors CPT test."
    canvas.create_text(root.winfo_width() / 2,
                       root.winfo_height() / 2 - 60,
                        text=first_text,
                        fill=black,
                        font=font_b)
    canvas.create_text(root.winfo_width() / 2,
                       root.winfo_height() / 2,
                        text="To end the test before the time runs out press escape.",
                        fill=black,
                        font=font_b)

    global space_pressed

    # Bind the space key to handle_key_press function
    root.bind("<KeyPress>", handle_key_press)

    # Loop until space key is pressed
    space_pressed = False
    while not space_pressed:
        root.update()

    root.unbind("<KeyPress>")


def first_stimuli():
    global root, canvas, font_a, font_b
    global space_pressed
    # Clearing the screen
    canvas.delete("all")

    # Printing instructions
    canvas.create_text(root.winfo_width() / 2,
                       root.winfo_height() / 2 - 120,
                        text="Once this letter appears on the screen , press the space key:",
                        fill=black,
                        font=font_b)
    canvas.create_text(root.winfo_width() / 2,
                       root.winfo_height() / 2,
                        text=correct_letter,
                        fill=black,
                        font=font_a)
    canvas.create_text(root.winfo_width() / 2,
                       root.winfo_height() / 2 + 120,
                        text="Once memorized press space to begin the test.",
                        fill=black,
                        font=font_b)

    # Bind the space key to handle_key_press function
    root.bind("<KeyPress>", handle_key_press)

    # Loop until space key is pressed
    space_pressed = False
    while not space_pressed:
        root.update()

    root.unbind("<KeyPress>")


def handle_test_key_press(event):
    global test_loop
    global correct_score
    global incorrect_score
    global current_index
    global time_b
    global switch_time
    global color_index, color, beep

    if event.keysym == "Escape":
        test_loop = False

    if event.keysym == "space":
        beep = True
        color = colors[color_index]
        color_index += 1
        color_index %= 6
        time_b = time.time()
        correct_score, incorrect_score = update_score(
            ' ', correct_score, incorrect_score, sequence, current_index)
        current_index += 1
        switch_time = time.time()
    # else:
    #     time_b = time.time()
    #     correct_score, incorrect_score = update_score(
    #         '', correct_score, incorrect_score, sequence, current_index)
    #     current_index += 1
    #     switch_time = time.time()


def animate_cubes(cubes, animate):
    if not animate:
        return
    for cube in cubes:
        cube.move()


def test_running():
    global sequence, root, canvas, font_a, font_b, is_moxo
    # Creation of the time variables
    global start_time
    global time_a
    global correct_score
    global current_index
    global incorrect_score
    global time_a
    global time_b
    global test_loop
    global switch_time
    global color_index, color, beep
    time_a = time.time()
    switch_time = time.time()

    # Setting the time
    start_time = time.time()

    color = random.choice(colors)
    # Create 15 cubes
    beep = True
    if is_moxo:
        cubes = [Cube() for i in range(15)]
        # Start the animation
        animate = True
        random_divider = random.choice([5,7,11,13])
    color_index = 0
    beeps_count = 0
    while test_loop:
        if is_moxo: animate_cubes(cubes, animate)
        # Getting the current time when the loop is activated
        now_time = time.time()

        # calculate elapsed time
        elapsed_time = (now_time - switch_time)

        # Update the state of the animation
        if test_loop:
            animate = True
        else:
            False
        if sequence[current_index] == correct_letter:
            if beep and beeps_count < 5 :
                threading.Thread(target=winsound.Beep, args=(500, 250)).start()
                # winsound.Beep(500, 10)
                beep = False
                beeps_count += 1
        else:
            beep = True
        if is_moxo and beeps_count == 5 :
            if current_index % random_divider == 0:
                threading.Thread(target=winsound.Beep, args=(500, 250)).start()
                random_divider = random.choice([5,7,11,13])
        # check if 1 seconds have passed without pressing any key when a "X" is shown
        if elapsed_time >= 1 and sequence[current_index] == correct_letter:
            color = colors[color_index]
            color_index += 1
            color_index %= 6
            time_b = time.time()
            correct_score, incorrect_score = update_score(
                '', correct_score, incorrect_score, sequence, current_index)
            current_index += 1
            switch_time = time.time()

        # check if 1 seconds have passed without pressing any key when a letter is shown
        elif elapsed_time >= 1 and sequence[current_index] != correct_letter:
            color = colors[color_index]
            color_index += 1
            color_index %= 6
            current_index += 1
            switch_time = time.time()

        # Draw the instructions
        # canvas.create_text(root.winfo_width() / 2,
        #                    root.winfo_height() / 2 - 210,
        #                     text="Keep track of the presented letters on the screen",
        #                     fill=black,
        #                     font=font_b)

        # Draw the time remaining
        time_remaining = max(0, test_duration - (time.time() - start_time))
        canvas.create_text(165, 50,
                           text="Time: {:.1f}".format(time_remaining),
                            fill=black,
                            font=font_b)

        # Draw the current stimulus
        current_stimulus = sequence[current_index]
        canvas.create_text(root.winfo_width() / 2,
                           root.winfo_height() / 2,
                           text=current_stimulus,
                            fill=color,
                            font=font_a)

        # Check if the test is finished
        if current_index == len(sequence):
            test_loop = False

        # Check if the time has run out
        elif time_remaining == 0:
            test_loop = False

        # Bind the space key to handle_key_press function
        root.bind("<KeyPress>", handle_test_key_press)

        # update the display
        root.update()
        canvas.update()
        canvas.delete("all")

    # unbind the key press event outside of the while loop
    root.unbind("<KeyPress>")


def stop_mainloop():
    root.quit()  # Stop the mainloop


def final_screen():
    # Printing instructions
    draw_text(canvas, "The test has been completed.", black,
              root.winfo_width() / 2, root.winfo_height() / 2 - 60, font_b)
    draw_text(canvas, "Results have been saved successfully.",
              black, root.winfo_width() / 2, root.winfo_height() / 2, font_b)

    root.after(2500, stop_mainloop)

visit_id = None
def main(ex_root, ex_canvas, visit_id_, moxo=False):
    global sequence, root, canvas, font_a, font_b, is_moxo, file_name, visit_id
    visit_id = visit_id_
    is_moxo = moxo
    root, canvas = ex_root, ex_canvas
    for widget in canvas.winfo_children():
        widget.destroy()
    current_directory = os.getcwd()
    init_timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
    suffix = '_conners.csv'
    if is_moxo:
        suffix = '_moxo.csv'
    file_name = init_timestamp + suffix
    # Creating a CSV file for the test
    #with open(os.path.join(current_directory, file_name ), mode='w', newline='') as csvfile:
    #    fieldnames = ["timestamp", "result", "reaction_time"]
    #    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #    writer.writeheader()

    # Set up the font for displaying text
    font_a = Font(family="Helvetica", size=80)
    font_b = Font(family="Helvetica", size=30)
    # The first screen is shown
    start_screen()
    # Clearing the screen
    canvas.delete("all")

    # Once we finish watching the first screen we generate a sequence
    sequence = generate_sequence(7, int(test_duration * 10))

    # We present the sequence on the next screen
    first_stimuli()
    # Clearing the screen
    canvas.delete("all")

    # Once memorized the sequence we start the actual test
    test_running()
    # Clearing the screen
    canvas.delete("all")
