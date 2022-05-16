# checks user choice is 'interger', 'text' or 'image'
def user_choice():

    valid = False
    while not valid:

        response = "File type (interger / text / image): ".lower()

        if response == "text" or 