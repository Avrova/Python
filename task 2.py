print("Введите время в секундах: ")
time_sek = int(input())
hours = time_sek / 3600
minutes = time_sek / 60
print(f"Время в формате ч:м:с :- {round(hours, 1)}:{round(minutes, 1)}:"
      f"{time_sek}")