import sys # do not use quit() or exit(), use sys.exit

# Makes the program repeat
while True:

# Get user input    
    file_variable =input('''
    Which file of genre novel do you want to search in? 
    a) fantasy novels file
    b) sci-fi novels file
    x) exits program
    
    Please type your selection here: ''')
# Different options for the user to select
    if file_variable == 'x':
        print("Goodbye, have a good one!")
        sys.exit()
    elif file_variable == 'a':
        file_variable = 'fantasy_novels.csv'
    elif file_variable == 'b':
        file_variable = 'scifi_novels.csv'
    else:
        print("The letter you chose is an invalid option. Please type a, b, or x.")
        continue

    # Input for entering a search term
    search_variable = input(f'Enter the search term for the {file_variable} file: ')
    search_variable = search_variable.title() # Makes it so that searching is not case sensitive

    def find(file_variable, search_variable):
        with open(file_variable, 'r') as file:
            content = file.read()
            # File is now in memory buffer as content
    
    # See if search_variable is in content buffer
        if search_variable in content:
        # User sees if the content is in the file and is asked if they
        # want to see the entries.
            print(f'Your term {search_variable} was found in the {file_variable} file.')
            see_entries = input(f'Would you like to see the entries found in {file_variable}? (y or n): ')

# If y, run this code to show the entries.
            if see_entries.lower() == 'y':
                print(f"Here are all the entries that include the term {search_variable}:")
                with open(file_variable, 'r') as file:
                    for line in file:
                        if search_variable in line:
                            print(line.strip())

# If n, run this code to end the program.
            elif see_entries.lower() == 'n':
                print(f'Goodbye. I hope this program was helpful in your search for a good book!')
                sys.exit()

            else:
                print("Invalid selection. Please type y or n.")
        # If the searched term was not found:
        else:
            print(f"{search_variable} was not found in {file_variable}.")
    
    # Call the function.
    find(file_variable, search_variable)

    