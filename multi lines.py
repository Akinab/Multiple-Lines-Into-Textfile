def details ():
    Description = "Input Multiple lines of text into text file"
    Date = "05-16-23"
    print ("\nDescription: {}\nDate: {}".format (Description , Date))
    
details ()

def write_to_file():
    with open('random.txt', 'w') as f:
        # repeat until the user enters 'n'
        while True:
            # prompt the user to enter a line of text
            line = input("Enter line: ")
