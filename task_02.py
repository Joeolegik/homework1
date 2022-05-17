my_list = []                      # Список всех итераций из цикла for
for cub_X in range(1, 1000, 2):   # цикл for проходит список от 1 - 1000
     my_list.append(cub_X ** 3)   # после вычисления куба из списка range добавляем в мой лист
#print(my_list)                   # Отображается список кубов нечетных чисел от 1 до 1000

# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
nums_seven_sum = 0
for number in my_list:
    item_sum = 0
    for item in str(number):
        item_sum += int(item)
    if item_sum % 7 == 0:
        nums_seven_sum += number
print(nums_seven_sum)
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
nums_seventeen_seven_sum = 0
for number in my_list:
    number += 17
    item_sum = 0
    for item in str(number):
        item_sum += int(item)
    if item_sum % 7 == 0:
        nums_seventeen_seven_sum += int(number)

print(nums_seventeen_seven_sum)

