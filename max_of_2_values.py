# 12 Maximum of Two Values

# Helper function, takes in 2 parameters
def max(val_1, val_2):
    if val_1 > val_2:
        return val_1     
    else:
        return val_2

# Main function, asks for 2 user inputs
def main():
    val_1 = int(input('Enter an integer value: '))
    val_2 = int(input('Enter another integer value: '))

    which_one = max(val_1, val_2)

    print(f'The greater integer is: {which_one}')

# While loop that runs the program as long as the user wants to keep playing
again = 'y'.lower()
while again == 'Y'.lower():
    main()
    again = input('Do you want to play again? y/n: ')
