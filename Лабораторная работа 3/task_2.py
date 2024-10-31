# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, splitter=","):
    first = set(first.split(splitter))
    second = set(second.split(splitter))
    common = list(first.intersection(second))
    common.sort()
    return common


participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group))
