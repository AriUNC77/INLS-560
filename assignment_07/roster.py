# uses data from https://goheels.com/sports/mens-basketball/roster

import pandas as pd

roster = ['Washington', 'Brown', 'Winters']
player = {"Last Name": roster,
          "First Name": ['Jalen', 'James',"Jae'Lyn"],
          'Height':[70, 70, 69],
          'Weight':[235, 215, 220]}

data = pd.DataFrame(player)

print(data)