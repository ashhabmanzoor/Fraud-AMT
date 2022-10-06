import math
import re
import pandas as pd


data = pd.read_excel(
    r"C:\Users\HP\Documents\Resources\Change_Negative_2.xlsx", sheet_name=0)
final = []
final_2 = []

p = re.compile("(\d+)?(" ")?(,)?(" ")?(\d+)?(" ")?[,]?(" ")?(\d+)[.]?(\d+)?")
l = re.compile(
    "(\d+)|(\d\,\d{3})|(\d\,\d{3}\.\d+)|(\d\d\,\d{3})|(\d\d\,\d{3}\.\d+)")
t = re.compile("(\d+)(,)?(\d+)?[.]?(\d+)?")
for x in data["X"][:]:

    if type(x) == str:
        new = []
        split_cell = re.split("-|!|_| ", x)
        for b in split_cell:
            if b.count("=") >= 1:
                if b.endswith("="):
                    b = b.replace("=", "")
                    if b == "":
                        continue
                    else:
                        m = p.finditer(b)
                        if m:
                            for q in m:
                                new.append(q.group())

                elif b.endswith("=") == False:
                    if len(split_cell) == 1:

                        b = b.split("=")
                        b = b[-1]
                        b = re.sub("\D", "", b)
                        new.append(b)

                    else:
                        if split_cell[-2] == "=":

                            split_cell = split_cell[-1]
                            split_cell = re.sub("\D", "", split_cell)
                            new.append(split_cell)
                        else:
                            b = b.split("=")
                            b = b[-1]
                            b = re.sub("\D", "", b)
                            new.append(b)
                else:
                    continue
            elif b.count(",") > 2:
                if len(split_cell) == 1:
                    z = b.split(",")
                    for things in z:
                        m = p.finditer(things)
                        if m:
                            for q in m:
                                new.append(q.group())

                else:
                    # i = re.sub(
                    #     "(\d+)[,](\d{3})(.)?(\d+)?(,)(\d+)[,](\d+)(.)?(\d+)?", r"\1\2\3\4\5\6\7\8\9", b)
                    morethantwo_comma_count_m = p.finditer(b)
                    for q in morethantwo_comma_count_m:
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
                one_comma_count_m = p.finditer(b)
                for q in one_comma_count_m:
                    one_comma_first = re.match(
                        "(\d)(,)\d{3}(.)?(\d+)?", q.group())
                    if one_comma_first:
                        i = re.sub(
                            "(\d)[,](\d{3})(.)?(\d+)?", r"\1\2\3\4", q.group())
                        new.append(i)
                        break
                    one_comma_second = re.match(
                        "(\d)(\d)(\,)(\d{3})(\.)?(\d+)?", q.group())
                    if one_comma_second:
                        i = re.sub(
                            "(\d)(\d)[\,](\d+)(\.)?(\d+)?", r"\1\2\3\4\5", q.group())
                        new.append(i)
                        break
                    comma_between_numbers = re.match(
                        "(\d+)(\.)?(\d+)?(\,)(\d+)?(\.)?(\d+)?", q.group())
                    if comma_between_numbers:
                        i = re.finditer(
                            r"\d*?(.)?\d+", q.group())
                        for find in i:
                            find = re.sub(
                                "[^ 0-9a-zA-Z](?!(?<=\d\.)\d)", "", find.group())
                            new.append(find)
                        break

                    comma_first = re.match(
                        "(,)(\d+)?(.)?(\d+)?", q.group())
                    if comma_first:
                        i = re.sub("[,](\d+)?(.)?(\d+)?", r"\1\2\3", q.group())
                        new.append(i)
                        break
                    only_number = re.match("\d+(,)?\d{3}(.)?(\d+)?", q.group())
                    if only_number:
                        i = re.sub(
                            "^(\d+)?[,](\d+)?(.)?(\d+)?", r"\1\2\3\4", q.group())
                        new.append(i)
                        continue
                    comma_last = re.match("(\d+)?(.)?(\d+)?[,]", q.group())
                    if comma_last:
                        i = re.sub("(\d+)?(.)?(\d+)?[,]", r"\1\2\3", q.group())
                        new.append(i)
                        break
                    else:
                        new.append(q.group())
            else:
                m = p.finditer(b)

                if m:
                    for q in m:
                        # z = re.match(
                        #     "\d+(,)\d{3}(.)?(\d+)?", q.group())
                        twc_cf = re.match(
                            "(,)(\d+)?(,)?(\d+)?(.)?(\d+)?", q.group())

                        if twc_cf:
                            o = str(q.group())
                            o = o[1:]

                            twc_cf_one_comma_first = re.match(
                                "(\d)(,)\d{3}(.)?(\d+)?", o)
                            if twc_cf_one_comma_first:
                                i = re.sub(
                                    "(\d)[,](\d{3})(.)?(\d+)?", r"\1\2\3\4", o)
                                new.append(i)
                                break
                            twc_cf_one_comma_second = re.match(
                                "(\d)(\d)(\,)(\d+)(\.)?(\d+)?", o)
                            if twc_cf_one_comma_second:
                                i = re.sub(
                                    "(\d)(\d)[\,](\d+)(\.)?(\d+)?", r"\1\2\3\4\5", o)
                                new.append(i)
                                continue
                            twc_cf_comma_between_numbers = re.match(
                                "(\d+)(\.)?(\d+)?(\,)(\d+)?(\.)?(\d+)?", o)
                            if twc_cf_comma_between_numbers:
                                i = re.finditer(
                                    r"\d+?(.)?\d+", q.group())
                                for find in i:
                                    new.append(find.group())
                                break
                            else:
                                new.append(o)
                                continue

                        twc_one_comma_first = re.match(
                            "(\d)(,)\d{3}(.)?(\d+)?", q.group())
                        if twc_one_comma_first:
                            i = re.sub(
                                "(\d)[,](\d{3})(.)?(\d+)?", r"\1\2\3\4", q.group())
                            new.append(i)
                            continue
                            # break
                        twc_one_comma_second = re.match(
                            "(\d)(\d)(\,)(\d+)(\.)?(\d+)?", q.group())
                        if twc_one_comma_second:
                            i = re.sub(
                                "(\d)(\d)[\,](\d+)(\.)?(\d+)?", r"\1\2\3\4\5", q.group())
                            new.append(i)
                            continue

                        # 4200,6200
                        number_divider = re.match(
                            "(\d+)(.)?(\d+)?(,)(\d+)(.)?(\d+)?", q.group())

                        if number_divider:
                            i = re.finditer(
                                r"\d+?(.)?\d+", q.group())
                            for find in i:
                                find_1 = find.group()
                                find_1 = re.sub(
                                    "[^ 0-9a-zA-Z](?!(?<=\d\.)\d)", "", find_1)
                                new.append(find_1)
                            break

                        w = re.match(
                            "(\d+)[,](\d+)[,](\d+)(\.\d+)?", q.group())

                        # if z:
                        #     i = re.sub(
                        #         "^(\d+)?[,](\d+)?(.)?(\d+)?", r"\1\2\3\4", q.group())
                        #     new.append(i)
                        if w:

                            # i = re.sub(
                            #     "(\d+)[,](\d+)[,](\d+)(\.\d+)?", new.append(r"\1", r"\2"), q.group())
                            for matches in w.groups()[:-1]:
                                new.append(matches)

                            # op = re.match(
                            #     "(\d+)?[,]?(\d+)?(.)?(\d+)?", o)
                            # if op:
                            #     i = re.sub("(,)(\d+)?[,]?(\d+)?(.)?(\d+)?",
                            #                r"\2\3\4\5", o)
                            #     new.append(i)
                        else:
                            i = re.sub(
                                "^(\d+)?[,](\d+)?(.)?(\d+)?", r"\1\2\3\4", q.group())
                            i = re.sub("[^ 0-9a-zA-Z](?!(?<=\d\.)\d)", "", i)
                            new.append(i)

        sum = 0

        if len(new) == 0:
            final.append(0)
        elif "+" in split_cell:
            for x in range(len(new)-1):
                try:
                    sum += int(float(new[x]))
                except:
                    final_2.append(x)
            if int(sum) == int(float(new[-1])):
                final.append([new[-1]])
            else:
                final.append(new)

        elif "=" in split_cell:
            for x in range(len(new)-1):
                try:
                    sum += int(float(new[x]))
                except:
                    final_2.append(x)
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

# data["New_4"] = final
for v in final:
    print(v)
# z = data.to_excel(
#     r"C:\Users\HP\Documents\Resources\X.xlsx", index=False)
# # print(z)
print(final_2)
