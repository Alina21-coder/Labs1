# TODO Напишите функцию find_common_participants

def find_common_participants(group1,group2, S=','):
    # Разделим строки на участников
    participants1 = set(group1.split(S))
    participants2 = set(group2.split(S))

    # Находим общих участников
    common_participants = participants1.intersection(participants2)
    # Сортируем общий список
    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
common = find_common_participants(participants_first_group, participants_second_group, S='|')
print(common)
# TODO Провеьте работу функции с разделителем отличным от запятой
