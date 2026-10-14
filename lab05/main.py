from tablestats import *
filename = input()
with open(filename, "r", encoding="utf-8") as table:
    rows = read_rows(table)
with open("summary.csv", 'w', encoding="utf-8") as out:
    out.write(str(len(rows)) + "\n" + str(len(count_types(rows))) + "\n" + str(total_minutes(rows, "ошибка")))