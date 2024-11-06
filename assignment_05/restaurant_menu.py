menu_option = ''

while menu_option != 'q':
    print(f'''
          Dante'/s Restaurant menu:
          
          -a NYU Flank Steak ($30)
          -b Seared Salmon ($28)
          -c Almond and Mint Salad ($26)
          -d Sherbert ($12)
          -q Quit the menu
          
          Please enter a letter to choose:
          ''')
    
    menu_option = input("> ")
    
    if menu_option == 'a':
        print("You have ordered the steak.")
    
    elif menu_option == 'b':
        print("Looks like you have chosen the salmon.")
    
    elif menu_option == 'c':
        salad_choice = input('Do you have a nut allergy? y or n: ')
        if salad_choice == 'n':
            print('Please enjoy the salad.')
        else:
            print("We will remove the nuts.")
    
    elif menu_option == 'd':
        sherbert_choice = input("Would you like orange (o) or strawberry (s): ")
        if sherbert_choice == 'o':
            print("You chose the orange sherbert.")
        elif sherbert_choice == 's':
            print("You got the strawberry sherbert.")
    else:
        print('Please ask about our specials.')
