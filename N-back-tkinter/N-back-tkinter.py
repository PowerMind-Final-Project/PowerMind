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

# Set up the display window
root = tk.Tk()
root.attributes('-fullscreen', True)
root.title("N-Back Test")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
canvas = tk.Canvas(root, bg=white, width=screen_width, height=screen_height)
canvas.pack(fill="both", expand=True)

# Set up the variables for the test
n = 3
test_duration = 90
stimuli = list(string.ascii_uppercase)
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


# Set up the font for displaying text
font_a = Font(family="Helvetica", size=100)
font_b = Font(family="Helvetica", size=40)

# Getting the current working directory
current_directory = os.getcwd()

# Creating a CSV file for the test
init_timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%H%M")
with open(os.path.join(current_directory, init_timestamp+'_N-Back.csv'), mode='w', newline='') as csvfile:
    fieldnames = ["timestamp", "result", "reaction_time"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
# Define a function to generate a random sequence of stimuli


def generate_stimuli_sequence(n, sequence_length):
    global sequence
    sequence = []
    random.shuffle(stimuli)
    for i in range(sequence_length):
        if i < n:
            stimulus = random.choice(stimuli)
        else:
            if random.random() < 0.5:
                stimulus = sequence[i-n]
            else:
                stimulus = random.choice(stimuli)
        sequence.append(stimulus)
    return sequence

# Define a function to draw text on the canvas


def draw_text(canvas, text, color, x, y, font):
    canvas.create_text(x, y, text=str(text), fill=color, font=font)


# Update the correct and incorrect scores based on the user's response.

def update_score(key_press, correct_score, incorrect_score, sequence, current_index):
    # Creating a timestamp and values
    global result
    global timestamp
    global time_a
    global time_b

    timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%H:%M:%S")

    if key_press == 's':
        if sequence[current_index] == sequence[current_index - 3]:
            correct_score += 1
            result = 1
        else:
            incorrect_score += 1
            result = 0
    elif key_press == 'd':
        if sequence[current_index] != sequence[current_index - 3]:
            correct_score += 1
            result = 1
        else:
            incorrect_score += 1
            result = 0

    if current_index == 3:
        time_diff = time_b - time_a
        # Update time_a for the next iteration
        time_a = time_b
    else:
        time_diff = time_b - time_a
        # Update time_a for the next iteration
        time_a = time_b

    # Updating results
    with open(init_timestamp+'_N-Back.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, result, time_diff])

    return correct_score, incorrect_score


# Define a function to display the final score
def display_final_score(correct_score, incorrect_score):
    # clear the canvas
    canvas.delete("all")

    # Display the final score
    final_score = "Final score: {} correct, {} incorrect".format(
        correct_score, incorrect_score)
    draw_text(final_score, black, screen_width/2, screen_height/2)

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

    # Printing instructions
    draw_text(canvas, "Press space to begin the N-back test.",
              black, screen_width/2, screen_height/2-60, font_b)
    draw_text(canvas, "To end the test before the time runs out enter escape.",
              black, screen_width/2, screen_height/2, font_b)

    global space_pressed

    # Bind the space key to handle_key_press function
    root.bind("<KeyPress>", handle_key_press)

    # Loop until space key is pressed
    space_pressed = False
    while not space_pressed:
        root.update()

    root.unbind("<KeyPress>")

# A function for the starting stimuli of the test


def first_stimuli():

    # Clearing the screen
    canvas.delete("all")

    # Printing instructions
    draw_text(canvas, "These are the first 3 letters you must remember at the start:",
              black, screen_width/2, screen_height/2-80, font_b)
    draw_text(canvas, sequence[0:3], black,
              screen_width/2, screen_height/2, font_b)
    draw_text(canvas, "Once memorized press space to begin the test.",
              black, screen_width/2, screen_height/2 + 80, font_b)

    global space_pressed

    # Bind the space key to handle_key_press function
    root.bind("<KeyPress>", handle_key_press)

    # Loop until space key is pressed
    space_pressed = False
    while not space_pressed:
        root.update()

    root.unbind("<KeyPress>")

# Event handle for test screen


def handle_test_key_press(event):

    global test_loop
    global correct_score
    global incorrect_score
    global current_index
    global time_b

    if event.keysym == "Escape":
        test_loop = False
    elif event.keysym == "d":
        time_b = time.time()
        correct_score, incorrect_score = update_score(
            'd', correct_score, incorrect_score, sequence, current_index)
        current_index += 1
    elif event.keysym == "s":
        time_b = time.time()
        correct_score, incorrect_score = update_score(
            's', correct_score, incorrect_score, sequence, current_index)
        current_index += 1


# A function for creating the testing loop
def test_running():

    # Creation of the time variable
    global start_time
    global end_time
    global time_a
    time_a = time.time()

    # Setting the time
    start_time = time.time()

    global test_loop
    while test_loop:

        # Clear the canvas
        canvas.delete("all")

        # Draw the current stimulus
        current_stimulus = sequence[current_index]
        draw_text(canvas, current_stimulus, yellow,
                  screen_width/2, screen_height/2, font_a)

        # Draw the instructions
        draw_text(canvas, "Press the 'S' key if the letter is the same.",
                  black, screen_width/2, screen_height/2-210, font_b)
        draw_text(canvas, "Press the 'D' key if the letter is different.",
                  black, screen_width/2, screen_height/2-140, font_b)

        # Draw the time remaining
        time_remaining = max(0, test_duration - (time.time() - start_time))
        draw_text(canvas, "Time: {:.1f}".format(
            time_remaining), black, 165, 50, font_b)

        # Draw the current score
        draw_text(canvas, "Correct: " + str(correct_score),
                  black, 145, screen_height - 110, font_b)
        draw_text(canvas, "Incorrect: " + str(incorrect_score),
                  black, 175, screen_height - 50, font_b)

        # Bind the space key to handle_key_press function
        root.bind("<KeyPress>", handle_test_key_press)

        # Check if the test is finished
        if current_index == len(sequence):
            test_loop = False

        # Check if the time has run out
        elif time_remaining == 0:
            test_loop = False

        # update the display
        root.update()

    # unbind the key press event outside of the while loop
    root.unbind("<KeyPress>")


def stop_mainloop():
    root.quit()  # Stop the mainloop


def final_screen():

    # Printing instructions
    draw_text(canvas, "The test has been completed.", black,
              screen_width/2, screen_height/2-60, font_b)
    draw_text(canvas, "Results have been saved successfully.",
              black, screen_width/2, screen_height/2, font_b)

    root.after(2500, stop_mainloop)


# The actual running of the program

# The first screen is shown
start_screen()
# Clearing the screen
canvas.delete("all")

# Once we finish watching the first screen we generate a sequence
sequence = generate_stimuli_sequence(n, int(test_duration*10))

# We present the sequence on the next screen
first_stimuli()
# Clearing the screen
canvas.delete("all")

# Once memorized the sequance we start the actual test
test_running()
# Clearing the screen
canvas.delete("all")

# When the test is done the final screen wil be shown
final_screen()

# The final running phase of all functions
root.mainloop()
