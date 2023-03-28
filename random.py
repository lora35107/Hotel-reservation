import random

# Define a dictionary of questions with unique identifier numbers
questions = {
    1: "What is your favorite color?",
    2: "What is your favorite animal?",
    3: "What is your favorite food?",
    4: "What is your favorite movie?",
    5: "What is your favorite hobby?",
    6: "What is your favorite book?",
    7: "What is your favorite place to travel?",
    8: "What is your favorite type of music?",
    9: "What is your favorite outdoor activity?",
    10: "What is your favorite indoor activity?"
}

# Define a list of available question numbers
available_numbers = list(questions.keys())

# Calculate the number of rows and columns for displaying the question numbers
num_questions = len(questions)
num_cols = 2
num_rows = (num_questions + num_cols - 1) // num_cols

# Display the list of question numbers in rows and columns
def display_question_numbers():
    print("Choose a number from the following list:")
    for i in range(num_rows):
        for j in range(num_cols):
            number = i * num_cols + j + 1
            if number in available_numbers:
                print("{:<2}".format(number), end=" ")
        print("")

# Function to prompt the user to select a number and display the corresponding question
def ask_question():
    selected_number = int(input("Enter a number: "))
    if selected_number in available_numbers:
        selected_question = questions[selected_number]
        print("Your selected question is:", selected_question)
        available_numbers.remove(selected_number)  # remove selected number from available numbers
        return True
    else:
        print("Invalid number entered.")
        return False

# Main loop to repeatedly prompt the user to select a question or reset
while True:
    display_question_numbers()
    if not available_numbers:
        print("No more questions available.")
        break
    reset_selected = False
    while not reset_selected:
        selected = ask_question()
        if selected:
            if not available_numbers:
                print("No more questions available.")
                break
            reset_selected = input("Press 'r' to select another question or any other key to exit: ").lower() == 'r'
        else:
            reset_selected = input("Press 'r' to try again or any other key to exit: ").lower() == 'r'
    print("")
