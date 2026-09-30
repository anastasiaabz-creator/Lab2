a1 = input("Введіть число: ")
a2 = input("Введіть число: ")
a3 = input("Введіть число: ")
a4 = input("Введіть число: ")

# Формуємо початкові частини
int_part = str(int(a1) + int(a2))
dec_part = str(int(a3) + int(a4))

# Виводимо результати обміну
print(int(dec_part) // 8)
print(int(int_part) // 15)
