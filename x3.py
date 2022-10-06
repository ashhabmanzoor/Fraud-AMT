import pandas as pd
import re
import math
data = pd.read_excel(r"C:\Users\HP\Documents\Resources\Change Negative.xlsx")
#data["X"] = data["X"].str.replace(",(\d{3})", "\\1")
#data["X"] = data["X"].str.replace(r"(\d)*,\d{3}.\d+", r"\d*,\d{3}.\d+")
print(data["X"][:])
final = []
#p = re.compile("([0-9\-][0-9,.]+)")
#p = re.compile("(\d+)(,)?(\d{3})(.\d+)?")
p = re.compile("\d+(,\d)*?[,.]?\d+[.]?(\d+)?")
#p = re.compile("\d+(,)?(\d{3,})?(\.)?(\d+)?")
#q = re.compile("[^.]")
r = re.compile("\d+(.)?(\d+)?")
for x in data["X"][:]:

    if type(x) == str:
        new = []
        a = re.split("(,)$|!|_", x)
        print(a)

        # for z in a:
        #     d = (re.sub("(\d+)?(,)?(\d+?)(,)?(\d+)?(\.)?(\d+)", r"\1\3\4", z))
        #     print(d)
        for b in a:
            if b.count(",") > 2:
                b = b.split(",")
                for z in b:
                    m = p.finditer(z)
                    if m:
                        for q in m:
                            new.append(q.group())

            else:
                m = p.finditer(b)
                for q in m:
                    z = re.match("\d+(,)\d{3}(.)?(\d+)?", q.group())
                    if z:
                        i = re.sub(
                            "^(\d+)(,)(\d+)([.]?)(\d+)?", r"\1\3\4\5", q.group())
                    new.append(q.group())
                    # if "," in q.group():
                    #     r = re.compile("\d+[,.]?\d+[.]?(\d+)?")

                    #     i = re.sub(
                    #         "^(\d+)(,)(\d+)([.]?)(\d+)?", r"\1\3\4\5", q.group())
                    #     if i:
                    #         new.append(i)
                    #     else:
                    #         e = q.group().split(",")
                    #         for stuff in e:
                    #             new.append(stuff)
                    # else:
                    #     new.append(q.group())

        if len(new) == 0:
            final.append(0)
        else:
            final.append(new)

    elif type(x) == int:
        if len(str(x)) > 8:
            x = 0
            final.append(x)
        else:
            final.append(x)

    elif math.isnan(x):
        final.append(0)

    elif type(x) == float:
        final.append(x)

    else:
        final.append(int(x))
print(final)
data["X1"] = final
final_new = []
for cell in data["X1"][:]:
    cell_count = 0
    if type(cell) == list:
        for numbers in cell:
            try:
                cell_count += int(numbers)
            except:
                cell_count = 0
        final_new.append(cell_count)

    else:
        final_new.append(cell)


print(final_new)
# for pairs in final:
#     if type(pairs) == list:
#         l = []
#         for individual in pairs[:]:

#             if "," in individual:
#                 pairs.remove(individual)
#                 individual = re.split(",", individual)
#                 for ind in individual:
#                     l.append(ind)

#             if "," not in individual:
#                 l.append(individual)

#         final_new.append(l)
#     else:
#         final_new.append(pairs)
# for pairs in final:
#     if type(pairs) == list:
#         for individuals in pairs[:]:
#             if "-" in individuals:
#                 pairs.remove(individuals)
#                 individuals = individuals.replace("-", "")
#                 pairs.append(individuals)
#             if "=" in individuals:
#                 pairs.remove(individuals)
#                 individuals = individuals.replace("=", "")
#                 pairs.append(individuals)
#             if "+" in individuals:
#                 pairs.remove(individuals)
#                 individuals = individuals.replace("+", " ")
#                 individuals = individuals.split()
#                 pairs.append(individuals)
#             if "," in individuals:
#                 pairs.remove(individuals)
#                 individuals = individuals.replace(",", " ")
#                 individuals = individuals.strip()
#                 pairs.append(individuals)

#             if ";" in individuals:
#                 pairs.remove(individuals)
#                 individuals = individuals.replace(";", " ")
#                 individuals = individuals.split()

#                 pairs.append(individuals)


#data["X1"] = final
# data.to_excel(r"C:\Users\HP\Documents\Resources\X.xlsx",
#              sheet_name='X', na_rep="NaN", index=False)
# print(final)
# print(final_new)

# for numbers in final:
#total = 0

# for number in numbers:
#total += int(number)

# final_new.append(total)

# print(final_new)
