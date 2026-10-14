from tablestats import *
with open("events.csv", "r", encoding="utf-8") as table:
    rows = read_rows(table)
with open("summary.csv", 'w', encoding="utf-8") as out:
    out.write(str(len(rows)) + "\n")
    out.write(str(len(count_types(rows))) + "\n")
    out.write(str(total_minutes(rows, "ошибка")))