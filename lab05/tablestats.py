def read_rows(lines:list[str]) -> list[dict]:
    headers = None
    rows = []
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        fields = line.split(',')
        for i in range(len(fields)):
            fields[i] = fields[i].strip()
        if headers is None:
            headers = fields
        elif len(headers) == len(fields):
            row = {}
            for i in range(len(fields)):
                row[headers[i]] = fields[i]
            rows.append(row)
    return rows
def count_types(rows:list[dict]) -> dict:
    counts = {}
    for row in rows:
        kind = row["тип"]
        counts[kind] = counts.get(kind, 0) + 1
    return counts
def total_minutes(rows: list[dict], kind:str) -> float:
    total = 0
    for row in rows:
        if row["тип"] == kind:
            total += float(row["минуты"])
    return round(total, 2)

def to_csv(counts:dict) -> str:
    csv = "тип, количество\n"
    for kind in sorted(counts):
        csv += kind + "," + str(counts[kind]) + "\n"
    return csv
