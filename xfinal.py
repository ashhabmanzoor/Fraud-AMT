import math
import re
import pandas as pd


data = pd.read_excel(
    r"C:\Users\HP\Documents\Resources\X.xlsx")
#
final_new = []
wrong = []
# data["Z"] = data["Z"].apply(eval)
# print(data["X1"])
# data["X1"] = pd.Series(data["X1"])
# print(data["X1"])

for idx, cell in enumerate(data["New_3"][:]):
    try:
        # data.loc[data.index[idx],
        #          "Z"]
        cell = eval(cell)
        # dfd.loc[dfd.index[[0, 2]], 'A']
    except:
        # data.loc[data.index[idx],
        #          "Z"]
        cell = cell

    cell_count = 0

    if type(cell) == list:
        for numbers in cell:
            try:
                numbers = float(numbers)
            except:
                # print(cell)
                wrong.append(cell)

            try:
                cell_count += float(numbers)
            except:
                cell_count = 0
        final_new.append(cell_count)
    else:
        final_new.append(cell)
data["SUM_3"] = final_new
z = data.to_excel(
    r"C:\Users\HP\Documents\Resources\X.xlsx", index=False)

# q = data.loc[data['Z'].isin(wrong)]
# print(q.shape)


# new = pd.DataFrame()
# for rows in data["Z"][:]:
#     for things in wrong:
#         try:
#             new_rows = eval(rows)

#             if new_rows == things:
#                 new.append(rows)
#             else:
#                 continue

#         except:
#             continue
# print(new.head())
for things in wrong:
    print(things)
