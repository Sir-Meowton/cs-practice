from tablestats import *
with open("events.csv", "r", encoding="utf-8") as table:
    rows = read_rows(table)
with open("summary.csv", 'w', encoding="utf-8") as out:
    try:
        out.write(f"{len(rows)} \n {len(count_types(rows))} \n {total_minutes(rows, 'ошибка')}")
    except:
        pass