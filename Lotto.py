# I step import libraries
# II step made GUI
# III write logic-functions

# I)
import random
from tkinter import *


# III)
def make_unique_numbers():
    unique_numbers = []
    while len(unique_numbers) < 7:
        rand = random.randint(1, 39)
        if rand not in unique_numbers:
            unique_numbers.append(rand)

    return unique_numbers


def guess_combination():
    guess_numbers = []
    counter = 0

    while counter < 7:
        user_input = int(input('Enter guess number: '))
        if user_input > 39 or user_input < 1:
            print('Number cant be less than 1 or bigger than 39 Enter again')
            continue
        if user_input in guess_numbers:
            print('You already said that number. Enter some other number')
            continue
        guess_numbers.append(user_input)
        counter += 1
    return guess_numbers


def compare_combinations(winning_combination, user_combination):
    number_of_initial_hits = 0
    for number in winning_combination:
        for user_number in user_combination:
            if int(user_number) == number:
                number_of_initial_hits += 1
                break

    return number_of_initial_hits


def play_game():
    winning_combination1 = make_unique_numbers()
    user_combination = user_combination_entry.get()
    user_combination_list = user_combination.split(",")
    score = compare_combinations(winning_combination1, user_combination_list)
    winning_text_combination_label.config(text=f'The winning combination is: {winning_combination1} ')
    guessed_label.config(text=f'You guessed: {score}')


# II)
root = Tk()
root.title("Lotto")
root.geometry("410x400")
root.resizable(0, 0)


root.configure(bg="white smoke")
user_combination_label = Label(root, text="Enter your combination: ", font="Roboto", fg="SlateGray", bg="white smoke",
                               anchor="center")  # Label=text
winning_text_combination_label = Label(root, text="The winning combination is: ", font="Roboto", fg="SlateGray",
                                        bg="white smoke")
guessed_label = Label(root, text="You guessed: ", font="Roboto", fg="SlateGray", bg="white smoke")

user_combination_entry = Entry(root, width=22)
button = Button(root, text="Play", bg="white smoke", fg="SlateGray", command=play_game, font="Roboto")



user_combination_label.place(x=20, y=35)
winning_text_combination_label.place(x=20, y=105)
guessed_label.place(x=20, y=175)
user_combination_entry.place(x=210, y=37)
button.place(x=350, y=30)

root.mainloop()
