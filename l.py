from itertools import count
import math
import re
import pandas as pd
import json

data = pd.read_excel(r"C:\Users\HP\Documents\Resources\Change Negative.xlsx")
#data["X"] = data["X"].str.replace(",(\d{3})", "\\1")
#data["X"] = data["X"].str.replace("\d*,\d{3}.\d+", "\d*,\d{3}.\d+")
# print(data["X"][:])
final = []
#p = re.compile("([0-9\-][0-9,.]+)")
#p = re.compile("(\d+)(,)?(\d{3})(.\d+)?")
#p = re.compile("(\d+)?(,)?(\d+)(,)?(\d+)([.]?)(\d+)?")
#p = re.compile("(\d+)?(,)?(\d+)?[,]?(\d+)[.]?\d+?")
p = re.compile("(\d+)?(" ")?(,)?(" ")?(\d+)?(" ")?[,]?(" ")?(\d+)[.]?(\d+)?")
q = re.compile("[^.]")
for x in data["X"][:]:

    if type(x) == str:
        new = []
        a = re.split("-|!|_| ", x)

        # print(a)

        for b in a:

            if b.count("=") >= 1:
                if b.endswith("="):
                    b = b.replace("=", "")
                    if b == "":
                        continue
                    else:
                        new.append(b)
                elif b.endswith("=") == False:
                    try:
                        a[-2] == "="
                        a = a[-1]
                        a = re.sub("\D", "", a)
                        new.append(a)
                    except:
                        b = b.split("=")
                        b = b[-1]
                        b = re.sub("\D", "", b)
                        new.append(b)
                else:
                    continue

            elif b.count(",") > 2:
                if len(a) == 1:
                    z = b.split(",")
                    for things in z:
                        m = p.finditer(things)
                        if m:
                            for q in m:
                                new.append(q.group())
                else:
                    i = re.sub(
                        "(\d+)[,](\d{3})(.)?(\d+)?(,)(\d+)[,](\d+)(.)?(\d+)?", r"\1\2\3\4\5\6\7\8\9", b)
                    m = p.finditer(i)
                    for q in m:
                        z = re.match(
                            "\d+(,)\d{3}(.)?(\d+)?", q.group())
                        w = re.match(
                            "(\d+)[,](\d+)[,](\d+)(\.\d+)?", q.group())
                        r = re.match(
                            "(,)(\d+)?(,)?(\d+)?(.)?(\d+)?", q.group())
                        if z:
                            i = re.sub(
                                "^(\d+)?[,](\d+)?(.)?(\d+)?", r"\1\2\3\4", q.group())
                            new.append(i)
                        elif w:
                            i = re.sub(
                                "(\d+)[,](\d+)[,](\d+)(\.\d+)?", r"\1\2\3\4", q.group())
                            new.append(i)

                        elif r:
                            i = re.sub("(,)(\d+)?[,]?(\d+)?(.)?(\d+)?",
                                       r"\2\3\4\5", q.group())
                            new.append(i)
                        else:
                            new.append(q.group())

            elif b.count(",") == 1:
                m = p.finditer(b)
                for q in m:
                    o = re.match(
                        "(\d)(,)\d{3}(.)?(\d+)?", q.group())
                    if o:
                        i = re.sub(
                            "(\d)[,](\d{3})(.)?(\d+)?", r"\1\2\3\4", q.group())
                        new.append(i)
                        break
                    c = re.match(
                        "(\d+)(,)\d{3}(.)?(\d+)?", q.group())
                    if c:
                        i = re.sub(
                            "(\d+)[,](\d{3})(.)?(\d+)?", r"\1\2\3\4", q.group())
                        new.append(i)
                        break
                    d = re.match(
                        "(\d)(,)(\d+)(.)?(\d+)?", q.group())
                    if d:
                        i = re.sub(
                            "(\d)[,](\d{3})(.)?(\d+)?", r"\1\2\3\4", q.group())
                        new.append(i)
                        break
                    e = re.match(
                        "(,)(\d+)?(.)?(\d+)?", q.group())
                    if e:
                        i = re.sub("[,](\d+)?(.)?(\d+)?", r"\1\2\3", q.group())
                        new.append(i)
                        break

                else:
                    i = re.sub(
                        "(\d+)[,](\d{3})(.)?(\d+)?(,)(\d+)[,](\d+)(.)?(\d+)?", r"\1\2\3\4\5\6\7\8\9", b)
                    m = p.finditer(i)
                    for q in m:
                        z = re.match(
                            "\d+(,)\d{3}(.)?(\d+)?", q.group())
                        w = re.match(
                            "(\d+)[,](\d+)[,](\d+)(\.\d+)?", q.group())
                        r = re.match(
                            "(,)(\d+)?(,)?(\d+)?(.)?(\d+)?", q.group())
                        if z:
                            i = re.sub(
                                "^(\d+)?[,](\d+)?(.)?(\d+)?", r"\1\2\3\4", q.group())
                            new.append(i)
                        elif w:
                            i = re.sub(
                                "(\d+)[,](\d+)[,](\d+)(\.\d+)?", r"\1\2\3\4", q.group())
                            new.append(i)

                        elif r:
                            i = re.sub("(,)(\d+)?[,]?(\d+)?(.)?(\d+)?",
                                       r"\2\3\4\5", q.group())
                            new.append(i)
                        else:
                            new.append(q.group())

                    # new.append(i)
                    # e = re.match(
                    #     "\d+(,)\d{3}(.)?(\d+)?(,)(\d+)(,)(\d+)(.)?(\d+)?", b)
                    # if e:
                    #     i = re.sub(
                    #         "(\d+)[,](\d{3})(.)?(\d+)?(,)(\d+)[,](\d+)(.)?(\d+)?", r"\1\2\3\4\5\6\7\8\9", b)
                    #     new.append(i)
                # except:

                #     z = b.split(",")
                #     for things in z:
                #         m = p.finditer(things)
                #         if m:
                #             for q in m:
                #                 new.append(q.group())

            else:
                m = p.finditer(b)

                if m:
                    for q in m:
                        z = re.match(
                            "\d+(,)\d{3}(.)?(\d+)?", q.group())
                        w = re.match(
                            "(\d+)[,](\d+)[,](\d+)(\.\d+)?", q.group())
                        r = re.match(
                            "(,)(\d+)?(,)?(\d+)?(.)?(\d+)?", q.group())
                        if z:
                            i = re.sub(
                                "^(\d+)?[,](\d+)?(.)?(\d+)?", r"\1\2\3\4", q.group())
                            new.append(i)
                        elif w:
                            i = re.sub(
                                "(\d+)[,](\d+)[,](\d+)(\.\d+)?", r"\1\2\3\4", q.group())
                            new.append(i)

                        elif r:
                            o = re.match(
                                "(^,)(\d+)?[, ]?(\d+)?(.)?(\d+)?", q.group())
                            if o:

                                i = re.sub("(,)(\d+)?[,]?(\d+)?(.)?(\d+)?",
                                           r"\2\3\4\5", q.group())
                                new.append(i)
                        else:
                            new.append(q.group())

        sum = 0
        if len(new) == 0:
            final.append(0)

        elif "+" in a:
            for x in range(len(new)-1):
                sum += int(float(new[x]))
            if int(sum) == int(float(new[-1])):
                final.append([new[-1]])
            else:
                final.append(new)
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

data["Z"] = final
print(final)
# z = data.to_excel(
#     r"C:\Users\HP\Documents\Resources\Change Negative.xlsx", index=False)
# print(z)
