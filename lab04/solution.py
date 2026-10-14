def winner(names: list[str], scores:list[float]):
    return scores.index(max(scores))

def average(scores: list[float]):
    return round(sum(scores) / len(scores), 2)

def ranking(names: list[str], scores: list[float]):
    rev_sort_names = []
    for i in range(len(scores)):
        maximum = scores.index(max(scores))
        rev_sort_names.append(names[maximum])
        scores[maximum] = 0
    return rev_sort_names

def above_average(names: list[str], scores: list[float]):
    mean = sum(scores) / len(scores)
    bigger_then_mean = []
    for index in range(len(scores)):
        if scores[index] > mean:
            bigger_then_mean.append(names[index])
    return bigger_then_mean
