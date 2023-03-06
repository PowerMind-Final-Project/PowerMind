import pygame
import time
import random
import string
import csv
import datetime

pygame.init()


# Set up the display window
screen_info = pygame.display.Info()
full_screen_width = screen_info.current_w
full_screen_height = screen_info.current_h
screen = pygame.display.set_mode((full_screen_width, full_screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("N-Back Test")

# Set up the boolian flag for score presentation 
final_score = True

# Set up the font for displaying text
font = pygame.font.Font(None, 50)

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the clock to control the frame rate
clock = pygame.time.Clock()

# Set up the variables for the test
n = 3
test_duration = 90
stimuli = list(string.ascii_uppercase)
sequence = []
correct_score = 0
incorrect_score = 0
start_time = 0
end_time = 0.0
init_counter = 0 

# Define a function to generate a random sequence of stimuli
def generate_stimuli_sequence(n, sequence_length):
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

# Define a function to draw text on the screen
def draw_text(text, color, x, y):
    text_surface = font.render(str(text), True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

# Update the correct and incorrect scores based on the user's response.
def update_score(key_press, correct_score, incorrect_score, sequence, current_index):

    # Creating a timestamp and values
    timestamp = datetime.datetime.now()
    correct = 0
    incorrect = 0

    if key_press == 's':
        if sequence[current_index] == sequence[current_index - 3]:
            correct_score += 1
            correct = 1
            incorrect = 0
        else:
            incorrect_score += 1
    elif key_press == 'd':
        if sequence[current_index] != sequence[current_index - 3]:
            correct_score += 1
            correct = 0
            incorrect = 1
        else:
            incorrect_score += 1
            correct = 0
            incorrect = 1

    # Updating results 
    with open('data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, correct, incorrect])

    return correct_score, incorrect_score

# Display the final score to the user.
def display_final_score(correct_score, incorrect_score):
    screen.fill(black)

    # Display the final score
    final_score = "Final score: {} correct, {} incorrect".format(correct_score, incorrect_score)
    draw_text(final_score, white, full_screen_width/2, full_screen_height/2)

    # Update the display
    pygame.display.flip()

    # Wait for 2.5 seconds
    pygame.time.wait(2500)

# Set up the start screen
start_screen = True
while start_screen:
    screen.fill(black)
    draw_text("Press space to begin the N-back test.", white, full_screen_width/2, full_screen_height/2-60)
    draw_text("To end the test before the time runs out press escape.", white, full_screen_width/2, full_screen_height/2)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            start_screen = False

# Generate the stimuli letters and start the test
sequence = generate_stimuli_sequence(n, int(test_duration*10))
current_index = 3

# Set up the first stimuli sequence screen
first_stimuli = True
while first_stimuli:
      screen.fill(black)
      draw_text("These are the first 3 letters you must remember at the start:", white, full_screen_width/2, full_screen_height/2-80)
      draw_text(sequence[0:3], white, full_screen_width/2, full_screen_height/2)
      draw_text("Once memorized press space to begin the test.", white, full_screen_width/2, full_screen_height/2 + 80)
      pygame.display.flip()
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            first_stimuli = False
            test_running = True
            start_time = time.time()

# Test loop
while test_running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                    correct_score, incorrect_score = update_score('s', correct_score, incorrect_score, sequence, current_index)
                    current_index += 1
            elif event.key == pygame.K_d:
                    correct_score, incorrect_score = update_score('d', correct_score, incorrect_score, sequence, current_index)
                    current_index += 1
            elif event.key == pygame.K_ESCAPE:
                    test_running = False
            if event.type == pygame.QUIT:
                    test_running = False
    # Clear the screen
    screen.fill(black)

    # Draw the current stimulus
    current_stimulus = sequence[current_index]
    draw_text(current_stimulus, white, full_screen_width/2, full_screen_height/2)

    # Draw the instructions 
    draw_text("Press the 'S' key if the letter is the same like 3 letters ago.", white, full_screen_width/2, full_screen_height/2-180)
    draw_text("Press the 'D' key if the letter is different from 3 letters ago.", white, full_screen_width/2, full_screen_height/2-120)

    # Draw the time remaining
    time_remaining = max(0, test_duration - (time.time() - start_time))
    draw_text("Time: {:.1f}".format(time_remaining), white, 90, 50)

    # Draw the current score
    draw_text("Correct: " + str(correct_score), white, 90, full_screen_height - 100)
    draw_text("Incorrect: " + str(incorrect_score), white, 110, full_screen_height - 50)

    # Check if the test is finished
    if current_index == len(sequence):
        end_time = time_remaining
        test_running = False
    
    # Check if the time has run out
    if end_time == time_remaining:      
        test_running = False 

    # Update the display
    pygame.display.flip()

    # Wait for the next frame
    clock.tick(10)

while final_score:
    display_final_score(correct_score,incorrect_score)
    final_score = False