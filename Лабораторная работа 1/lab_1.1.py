numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

list_num1 = numbers[:4]
list_num2 = numbers[5:]
sum_num = list_num1 + list_num2
average = round(sum(sum_num) / len(numbers), 2)
numbers[4] = average

print("Измененный список:", numbers)
