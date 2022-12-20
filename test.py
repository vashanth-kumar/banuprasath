import csv
import pandas as pd
df = pd.read_csv("new_file.csv")
df.loc[indx, 'MOBILE'] = new_mob
df.to_csv("user_details.csv", index=False)
log = pd.read_csv("login_details.csv")
log.loc[indx, "MOBILE"] = new_mob
log.to_csv("login_details.csv", index=False)