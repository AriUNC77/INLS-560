#Constants for UNC SILS graduation requirements
MIN_HOURS = 48
MIN_CAPSTONES = 1
COMP_EXAM = 1

academic_hours = int(input('Enter how your completed class hours here: '))
capstones = int(input('Enter how many capstone projects you have completed: '))
comp_passes = int(input('Enter how many times you have passed the comp exam: '))

if academic_hours >= MIN_HOURS and capstones >= MIN_CAPSTONES and comp_passes >= COMP_EXAM:
    print("Congratulations! You are ready to graduate!")
else:
    #Multi-line with f-string
    print(f'''
          I am sorry, you do not meet the requirements to graduate.
          
          You need at least
          -{MIN_HOURS} academic hours completed as a SILS student.
          -{MIN_CAPSTONES} thesis or practicum completed.
          -{COMP_EXAM} passing grade for the comprehensive exam.
          ''')