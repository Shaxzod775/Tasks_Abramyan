# If5. Даны три целых числа. Найти количество положительных и количество
# отрицательных чисел в исходном наборе.


# def pos_neg_numbers():
#     user_input = input('Введите три числа (Пример 4,5,6): ')
#     positive_numbers = 0
#     negative_numbers = 0
#     for number in user_input.split(','):
#         if int(number) > 0:
#             positive_numbers += 1
#         elif int(number) < 0:
#             negative_numbers += 1
#
#     print(positive_numbers)
#     print(negative_numbers)
#
#
# pos_neg_numbers()


# If20. На числовой оси расположены три точки: A, B, C. Определить, какая из
# двух последних точек (B или C) расположена ближе к A, и вывести эту
# точку и ее расстояние от точки A.


# def find_nearest_point():
#     A = int(input('Введите точку A: '))
#     B = int(input('Введите точку B: '))
#     C = int(input('Введите точку C: '))
#
#     if B > C:
#         print(f'B ближе к A чем C, и находится в {B - A} см')
#     elif C > B:
#         print(f'C ближе к A чем B, и находится в {C - A} см')
#     elif B == C:
#         print(f'C и B находятся на равном расстояние от точки A, и находится в {C - A} см')
#
# find_nearest_point()

# If30. Дано целое число, лежащее в диапазоне 1–999.
# Вывести его строкуописание вида «четное двузначное число»,
# «нечетное трехзначное число» и т. д.

# def number_description():
#     number = input('Введите целое число, лежащее в диапазоне 1–999: ')
#     if int(number) % 2 == 0:
#         even_odd = 'чётное'
#     else:
#         even_odd = 'нечётное'
#
#     if len(number) == 1:
#         digits_description = 'однозначное'
#     elif len(number) == 2:
#         digits_description = 'двухзначное'
#     elif len(number) == 3:
#         digits_description = 'трёхзначное'
#
#     print(f'{number} это {even_odd} {digits_description} число')
#
#
# number_description()









