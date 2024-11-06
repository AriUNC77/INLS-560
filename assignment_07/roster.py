# uses data from https://goheels.com/sports/mens-basketball/roster

import pandas as pd

roster = ['Washington', 'Brown', 'Winters','Lubin']
player = {"Last Name": roster}

data = pd.DataFrame(player)

print(data)