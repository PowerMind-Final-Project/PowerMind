import tkinter as tk
from tkinter.font import Font
import time
import random
import string
import csv
import datetime
import os


# Set up colors
black = "#000000"
white = "#FFFFFF"
yellow = "#EEEE3B"

# Set up the variables for the test
correct_letter = 'X'
test_duration = 90
letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
sequence = []
current_index = 0
correct_score = 0
incorrect_score = 0
test_loop = True
result = 0
timestamp = 0
time_a = 0
time_b = 0
counter = 0
switch_time = time.time()


# Getting the current working directory
current_directory = os.getcwd()
init_timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%H:%M:%S")

# Creating a CSV file for the test 
with open(os.path.join(current_directory, init_timestamp + 'conors.csv'), mode='w', newline='') as csvfile:
    fieldnames = ["timestamp", "result", "reaction_time"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

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
    global root
    canvas.create_text(x, y, text=str(text), fill=color, font=font)


# Update the correct and incorrect scores based on the user's response.


def update_score(key_press, correct_score, incorrect_score, sequence, current_index):
    global root, canvas
    global time_a
    global time_b
    global test_loop
    global counter

    # Creating a timestamp and values
    timestamp = datetime.datetime.now().strftime('%d-%m-%y_%H:%M:%S')
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
    with open(os.path.join(current_directory, init_timestamp + 'conors.csv'), mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, result, time_diff])

    return correct_score, incorrect_score


# Define a function to display the final score


# Define a function to display the final score
def display_final_score(correct_score, incorrect_score):
    global root, canvas
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
    global root, canvas
    global space_pressed
    if event.keysym == "space":
        space_pressed = True


# A function for the starting screen of the test


def start_screen():
    global root, canvas, font_a, font_b
    # Printing instructions
    draw_text(canvas, "Press space to show the instructions of Conors CPT test.",
              black, root.winfo_width() / 2, root.winfo_height() / 2 - 60, font_b)
    draw_text(canvas, "To end the test before the time runs out press escape.",
              black, root.winfo_width() / 2, root.winfo_height() / 2, font_b)

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
    # Clearing the screen
    canvas.delete("all")

    # Printing instructions
    draw_text(canvas, "Once this letter appears on the screen , press the space key:",
              black, root.winfo_width() / 2, root.winfo_height() / 2 - 120, font_b)
    draw_text(canvas, 'X', yellow,
              root.winfo_width() / 2, root.winfo_height() / 2, font_a)
    draw_text(canvas, "Once memorized press space to begin the test.",
              black, root.winfo_width() / 2, root.winfo_height() / 2 + 120, font_b)

    global space_pressed

    # Bind the space key to handle_key_press function
    root.bind("<KeyPress>", handle_key_press)

    # Loop until space key is pressed
    space_pressed = False
    while not space_pressed:
        root.update()

    root.unbind("<KeyPress>")


def handle_test_key_press(event):
    global root, canvas
    global test_loop
    global correct_score
    global incorrect_score
    global current_index
    global time_b
    global switch_time

    if event.keysym == "Escape":
        test_loop = False

    if event.keysym == "space":
        time_b = time.time()
        correct_score, incorrect_score = update_score(
            ' ', correct_score, incorrect_score, sequence, current_index)
        current_index += 1
        switch_time = time.time()
    else:
        time_b = time.time()
        correct_score, incorrect_score = update_score(
            '', correct_score, incorrect_score, sequence, current_index)
        current_index += 1
        switch_time = time.time()


def test_running():
    global root, canvas, start_time, time_a, correct_score, current_index, incorrect_score
    global time_a, time_b, test_loop, switch_time, font_a, font_b
    time_a = time.time()
    switch_time = time.time()

    # Setting the time
    start_time = time.time()

    while test_loop:

        # Getting the current time when the loop is activated
        now_time = time.time()

        # calculate elapsed time
        elapsed_time = (now_time - switch_time)

        # check if 1 seconds have passed without pressing any key when a "X" is shown
        if elapsed_time >= 1 and sequence[current_index] == "X":
            time_b = time.time()
            correct_score, incorrect_score = update_score(
                '', correct_score, incorrect_score, sequence, current_index)
            current_index += 1
            switch_time = time.time()

        # check if 1 seconds have passed without pressing any key when a letter is shown
        elif elapsed_time >= 1 and sequence[current_index] != "X":
            current_index += 1
            switch_time = time.time()

        # Clear the canvas
        canvas.delete("all")

        # Draw the instructions
        draw_text(canvas, "Keep track of the presented letters on the screen",
                  black, root.winfo_width() / 2, root.winfo_height() / 2 - 210, font_b)

        # Draw the time remaining
        time_remaining = max(0, test_duration - (time.time() - start_time))
        draw_text(canvas, "Time: {:.1f}".format(
            time_remaining), black, 165, 50, font_b)

        # Draw the current score
        draw_text(canvas, "Correct: " + str(correct_score),
                  black, 145, root.winfo_height() - 110, font_b)
        draw_text(canvas, "Incorrect: " + str(incorrect_score),
                  black, 175, root.winfo_height() - 50, font_b)

        # Draw the current stimulus
        current_stimulus = sequence[current_index]
        draw_text(canvas, current_stimulus, yellow,
                  root.winfo_width() / 2, root.winfo_height() / 2, font_a)

        # Bind the space key to handle_key_press function
        root.bind("<KeyPress>", handle_test_key_press)

        # update the display
        root.update()

        # Check if the test is finished
        if current_index == len(sequence):
            test_loop = False

        # Check if the time has run out
        elif time_remaining == 0:
            test_loop = False

    # unbind the key press event outside of the while loop
    root.unbind("<KeyPress>")


def stop_mainloop():
    global root
    root.quit()  # Stop the mainloop


def final_screen():
    global root, canvas, font_a, font_b
    # Printing instructions
    draw_text(canvas, "The test has been completed.", black,
              root.winfo_width() / 2, root.winfo_height() / 2 - 60, font_b)
    draw_text(canvas, "Results have been saved successfully.",
              black, root.winfo_width() / 2, root.winfo_height() / 2, font_b)

    root.after(2500, stop_mainloop)

def main(ex_root, ex_canvas):
    global sequence, root, canvas, font_a, font_b

    root, canvas = ex_root, ex_canvas
    for widget in canvas.winfo_children():
        widget.destroy()
    # Set up the font for displaying text
    font_a = Font(family="Helvetica", size=100)
    font_b = Font(family="Helvetica", size=40)
    # The first screen is shown
    start_screen()
    # Clearing the screen
    canvas.delete("all")

    # Once we finish watching the first screen we generate a sequence
    sequence = generate_sequence(10, int(test_duration * 10))

    # We present the sequence on the next screen
    first_stimuli()
    # Clearing the screen
    canvas.delete("all")

    # Once memorized the sequance we start the actual test
    test_running()
    # Clearing the screen
    canvas.delete("all")

    # When the test is done the final screen wil be shown
    # final_screen()

