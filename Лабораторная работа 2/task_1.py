money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count_month = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while True:
        money_capital += salary - spend
        spend *= 1 + increase
        if money_capital < 0:
            break
        count_month += 1
print("Количество месяцев, которое можно протянуть без долгов:", count_month)