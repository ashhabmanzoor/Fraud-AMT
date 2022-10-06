import pandas as pd
import re
import math
data = pd.read_excel(r"C:\Users\HP\Documents\Resources\X.xlsx")
p = re.compile("(\d+)?(,)?(\d+?)[,]?\d+[.]?\d+?")
new = []
for x in data["Fraud Amount"][:]:

    if type(x) == str:

        # a = re.split("-|!|_| ", x)

        if x.count("=") >= 1:
            new.append(x)

    elif type(x) == int:
        continue

    else:
        continue

column = ["TICKET ID", "Channel Type", "Fraud Amount", "X", "Fraudster-1"]
z = data[data['Fraud Amount'].isin(new)]
r = z.to_excel(r"C:\Users\HP\Documents\Resources\Y.xlsx",
               columns=column, index=False)
# print(z)
# print(new)
