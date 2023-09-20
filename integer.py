# Integer 11 Дано трехзначное число. Найти сумму и произведение его цифр

# def sum_and_product():
#     user_input = input('Введите трёхзначное число: ')
#     list_numbers = [int(i) for i in user_input]
#     result_sum = sum(list_numbers)
#     result_product = 1
#     for number in list_numbers:
#         result_product *= number
#
#     print(f'Sum of the numbers {user_input} is {result_sum}')
#     print(f'Product of the numbers {user_input} is {result_product}')
#
# sum_and_product()

# Integer 30 Дан номер некоторого года (целое положительное число).
# Определить соответствующий ему номер столетия, учитывая, что, к примеру,
# началом 20 столетия был 1901 год

# def which_centry():
#     year = int(input('Введите год: '))
#     century = (year + 99) // 100
#     print(century)
#
# which_centry()


# Integer 29 Даны целые положительные числа A, B, C. На прямоугольнике размера A × B размещено максимально возможное количество квадратов со
# стороной C (без наложений). Найти количество квадратов, размещенных
# на прямоугольнике, а также площадь незанятой части прямоугольника.


# def find_squares():
#     A = int(input('Введите сторону A (см): '))
#     B = int(input('Введите сторону B (см): '))
#     C = int(input('Введите сторону квадрата (см): '))
#     rectangle = A * B
#     squares = rectangle / C
#     left_area = (A % C) * B
#     print(round(squares))
#     print(left_area)
#
# find_squares()

# Integer 28 Дни недели пронумерованы следующим образом: 1 — понедельник, 2 — вторник, . . . , 6 — суббота, 7 — воскресенье. Дано целое число K,
# лежащее в диапазоне 1–365, и целое число N, лежащее в диапазоне 1–7.
# Определить номер дня недели для K-го дня года, если известно, что в
# этом году 1 января было днем недели с номером N


# def find_weekday_number():
#     while True:
#         K = int(input('Введите число дня в диапозане (1-365): '))
#         N = int(input('Введите число дня недели в диапозане (1-7): '))
#
#         N1 = N
#         if N1 != 7:
#             N1 += 1
#         else:
#             N1 -= 7
#
#         K1 = K % 7 + 1
#
#         day_of_week = K1
#
#         print(day_of_week - 1)
#         break
#
# find_weekday_number()






