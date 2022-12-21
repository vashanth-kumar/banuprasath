import csv
import pandas as pd

file = open('new_file.csv', mode='r')
lst = list(csv.reader(file))
for i in lst:
    if i[0] == "kadi":
        print(i)
        indx=lst.index(i) - 1



df = pd.read_csv("new_file.csv")
df.loc[indx, 'Name'] = "vk"
df.to_csv("new_file.csv", index=False)
log = pd.read_csv("new_file.csv")
log.loc[indx, "Name"] = "vk"
log.to_csv("new_file.csv", index=False)
