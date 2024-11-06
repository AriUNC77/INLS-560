# uses data from https://goheels.com/sports/mens-basketball/roster

import pandas as pd
print("The following is a list of the top ten tallest UNC basketball players:\n")
player = {"First Name": ['Jalen', 'James',"Jae'Lyn", 'Ven-Allen', "John",
                         "Cade", "Ty", "Drake", "Ian", "Seth"],
          "Last Name": ['Washington', 'Brown', 'Winters', "Lubin", 'Holbrook',
                        'Tyson','Claude', "Powell", "Jackson", "Trimble"],
          'Height':[70, 70, 69, 68, 68, 67, 67, 66, 64, 63],
          'Weight':[235, 215, 220, 230, 230, 200, 230, 195, 190, 195]}

data = pd.DataFrame(player)

# bmi is height in kg/weight in meters squared
data["BMI"] = round((data["Weight"]/2.205)/((data["Height"]/39.37)**2), 2)

print(data)

data.to_csv("bmi.csv")