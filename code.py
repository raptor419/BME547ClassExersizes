def take_input():
    try:
        inp = int(input("Enter your input"))
        return inp
    except:
        print("Invalid Input, Enter again")
        return take_input()

def check_HDL(hdl):
    if hdl>=60:
        print("Normal")
    elif hdl>=40:
        print("Borderline Low")
    elif hdl<40:
        print("Low")
        
def driver(what):
    print("Enter",what)
    hdl = take_input()
    if what=="HDL":
        check_HDL(hdl)
    
def interface():
    while True:
        print("My Program")
        print("Options:")
        print("1 - Check HDL")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice=='9':
            return
        elif choice=='1':
            driver("HDL")
        else:
            print("Invalid Option, Try again")
