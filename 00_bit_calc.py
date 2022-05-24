# Functions go here

# Puts series of symbles at start and end of text (for emphasis)
def statement_generator(text, decoration):

    # Make string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{}  {}  {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return""


# checks user choice is 'interger', 'text', or 'image'
def user_choice():

    # List of valid responses
    text_ok = ["text", "t", "txt"]
    integer_ok = ["integer", "int", "#", "number" ]
    image_ok = ["image", "img", "pix" "picture", "pic", "p"]

    valid = False
    while not valid:

        # ask user for choice and change response to lowercse
        response = input("File type (integer / text / image): ").lower()

        # Checks for valid response and returns text, interger or image

        if response in text_ok :
            return "text"

        elif response in integer_ok:
            return "integer"

        elif response in image_ok:
            return "image"   

        elif response == "i":
            want_integer = input("Press <enter> for an integer or any key for an image")
            if want_integer == "":
                return "integer"
            else:
                return "image"    

        else:
            # if response is not valid, output an error
            print("Sorry, please choose integer, text or image")
            print()


# Main Routine goes here

# Heading
statement_generator("Bit Calculator for intergers, Text & Images", "-")

# Display instructions if iser has not used the program before

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    #Ask the user for the file type
    data

    # For integers, ask for integer
    # (must be an integer more than / equal to 0)

    # For images, ask for width and height
    # (must be integers more than / equal to 1)