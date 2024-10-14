#Variable for priming the while loop
menu_option = ''

#Loop that infinitely runs until menu_option is 'q'
while menu_option != 'q':
    print("Menu", 'a: Roasted Salmon', "b: NYC Steak", 
          "c: Spring Salad", "q: Quit", sep="\n")
    # Sets menu_option variable to user's input
    menu_option = input("""Please type a, b, or c to select your dish, or q to quit: """)
    if menu_option == 'a':
        print("It's a great season for seafood.")

    elif menu_option == 'b':
        print("Steak's always a classic.")
        
    elif menu_option == 'c':
        print("Sometimes all you want is a salad.")
        


