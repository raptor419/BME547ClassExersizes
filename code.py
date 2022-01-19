def take_input():
    inp = input("Enter your input")
    return inp

def interface():
    while True:
        print("My Program")
        print("Options:")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice=='9':
            return choice
