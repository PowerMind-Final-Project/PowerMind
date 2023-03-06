import pygame
import csv
import datetime
import string
import time
import random
pygame.init()

# Set up the display window
screen_info = pygame.display.Info()
full_screen_width = screen_info.current_w
full_screen_height = screen_info.current_h
screen = pygame.display.set_mode((full_screen_width, full_screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Conors CPT")

# Set up the font for displaying text
font = pygame.font.Font(None, 50)

# Set up the boolian flag for score presentation 
final_score = True


# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the clock to control the frame rate
clock = pygame.time.Clock()

# Set up the variables for the test
correct_letter = 'X'
test_duration = 90
stimuli = list(string.ascii_uppercase)
sequence = []
correct_score = 0
incorrect_score = 0
start_time = 0
end_time = 0.0
init_counter = 0 
n = 3

# Define a function to draw text on the screen
def draw_text(text, color, x, y):
    text_surface = font.render(str(text), True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

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

# Update the correct and incorrect scores based on the user's response.
def update_score(key_press, correct_score, incorrect_score, sequence, current_index):

    # Creating a timestamp and values
    timestamp = datetime.datetime.now()
    correct = 0
    incorrect = 0

    if key_press == ' ':
        if sequence[current_index] == correct_letter:
            correct_score += 1
            correct = 1
            incorrect = 0
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
    draw_text("Press space to show the instructions of Conors CPT test.", white, full_screen_width/2, full_screen_height/2-60)
    draw_text("To end the test before the time runs out press escape.", white, full_screen_width/2, full_screen_height/2)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            start_screen = False

# Set up the instructions screen
instructions = True
while instructions:
      screen.fill(black)
      draw_text("Once this letter appears on the screen , press the space key:", white, full_screen_width/2, full_screen_height/2-80)
      draw_text('X', white, full_screen_width/2, full_screen_height/2)
      draw_text("Once memorized press space to begin the test.", white, full_screen_width/2, full_screen_height/2 + 80)
      pygame.display.flip()
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            instructions = False
            test_running = True
            start_time = time.time()

# Generate the stimuli letters and start the test
sequence = generate_stimuli_sequence(n, int(test_duration*10))
current_index = 0

# Time indicators and delays
last_update_time = 0
delay = 1500

# Test loop
while test_running:
    # Time ticking 
    current_time = pygame.time.get_ticks()
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                    correct_score, incorrect_score = update_score(' ', correct_score, incorrect_score, sequence, current_index)
                    current_index += 1
            elif event.key == pygame.K_ESCAPE:
                    test_running = False
            if event.type == pygame.QUIT:
                    test_running = False

    # Clear the screen
    screen.fill(black)

    # Draw the current stimulus
    if current_time - last_update_time > delay:
        last_update_time = current_time
        current_stimulus = sequence[current_index]
        draw_text(current_stimulus, white, full_screen_width/2, full_screen_height/2)
        current_index += 1

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
