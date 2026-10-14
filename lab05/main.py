from tablestats import *
with open("events.csv", "r", encoding="utf-8") as table:
    rows = read_rows(table)
with open("summary.csv", 'w', encoding="utf-8") as out:
    out.writeln(str(len(rows)))
    out.writeln(str(len(count_types(rows))))
    out.writeln(str(total_minutes(rows, "ошибка")))