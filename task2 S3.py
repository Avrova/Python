rating = [10, 10, 5, 4, 1]
print(f"Текущий рейтинг: {rating}")

new_scores_count = int(input("Сколько вы хотите ввести новых элементов рейтинга: "))

for i in range(1, new_scores_count + 1):
    new_score = int(input("Введите новый элемент рейтинга: "))
    if new_score > 0:
        rating.append(new_score)
        rating.sort(reverse = True)
        print(f"Новый рейтинг: {rating}")
    else:
        print("Ошибка. Вы ввели не натуральное число")