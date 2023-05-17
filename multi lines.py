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
            # write the line to the file
            f.write(line + '\n')
            # prompt the user to enter more lines or not
            answer = input("Are there more lines y/n? ")
            # if the answer is 'n', break out of the loop
            if answer.lower() == 'n':
                break
