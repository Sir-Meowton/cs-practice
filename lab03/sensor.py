celsium = int(input("Введите порог тривоги в градусах Цельсия:"))
strings = int(input("Введите количество записей: "))
print("Введите записи:")
array_of_digrits = [input() for i in range(strings)]
lenght_of_array = len(array_of_digrits)
count_of_error = array_of_digrits.count("error")
[array_of_digrits.remove("error") for i in range(count_of_error)]
array_of_digrits = list(map(float, array_of_digrits))
bigger_then_celsium = 0
for x in array_of_digrits:
    if x > celsium:
        bigger_then_celsium += 1
maximum_celsium = max(array_of_digrits)
mean_of_array = sum(array_of_digrits) / len(array_of_digrits)
print(f"Количество записей = {lenght_of_array}")
print(f"Количество ошибок = {count_of_error}")
print(f"количество превышений допустимой нормы в {celsium} = {bigger_then_celsium}")
print(f"Максимальное показание = {maximum_celsium:.1f}")
print(f"Среднее значение показаний = {mean_of_array:.1f}")