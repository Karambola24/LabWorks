numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
not_number_index = 4
not_number = 0
numbers[not_number_index] = not_number
average = (sum(numbers[:not_number_index]) + sum(numbers[not_number_index+1:])) / len(numbers)
numbers[not_number_index] = average
print("Измененный список:", numbers)
