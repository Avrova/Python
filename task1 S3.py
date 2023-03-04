month = int(input("Введите номер календарного месяца: "))
seasons_dict = {12:'зима',1:'зима',2:'зима', 3:'весна', 4:'весна', 5:'весна', 6: 'лето',7: 'лето', 8: 'лето', 9:'осень', 10:'осень',11:'осень'}
print(f'Словарь:время года - {seasons_dict.get(month)}')
seasons_list = list(seasons_dict.values())
print(f'Список:время года - {seasons_list[month-1]}')