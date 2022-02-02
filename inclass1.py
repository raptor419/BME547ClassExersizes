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
        
def check_LDL(ldl):
    if ldl>=190:
        print("Very High")
    elif ldl>=130 and ldl<160:
        print("Borderline High")
    elif ldl>=160 and ldl<190:
        print("Normal")
    elif ldl>-190:
        print("Very High")
        
        
def driver(what):
    print("Enter",what)
    inp = take_input()
    if what=="HDL":
        check_HDL(inp)
    elif what=="LDL":
        check_LDL(inp)
    
def interface():
    while True:
        print("My Program")
        print("Options:")
        print("1 - Check HDL")
        print("1 - Check LDL")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice=='9':
            return
        elif choice=='1':
            driver("HDL")
        elif choice=='1':
            driver("LDL")
        else:
            print("Invalid Option, Try again")
