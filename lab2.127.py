# Вводимо дані
day = int(input("Введіть день: "))
month = int(input("Введіть місяць: "))
year = int(input("Введіть останні дві цифри року: "))

# Перевіряємо, чи введено "магічну" дату (02.10.20)
if day == 2 and month == 10 and year == 20:
   print (" The date is magic! ")
else:
    print (" This is a normal date ")

