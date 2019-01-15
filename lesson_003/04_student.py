# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
i = 0
student_income = 0
months_expenses = 0

while i < 10:
    student_income += educational_grant
    if i == 0:
        months_expenses += expenses
    elif i >= 1:
        # TODO По условию задачи расходы увеличаются каждый месяц на 3%, а судя
        # TODO по данному коду расходы увеличились на 3% только 1 раз за все
        # TODO время обучения (кроме того в данной формуле присуствует лишняя
        # TODO операция сложения).
        months_expenses += expenses + expenses * 0.03
    i += 1
    # print(months_expenses, student_income, months_expenses-student_income)

# TODO Расчет разницы необходимо производить на каждой итерации цикла
# TODO Не соблюден формат выввода из условия задачи (в формате указана необходимая точность вычислений)
print('Студенту надо попросить', months_expenses-student_income, 'рублей')