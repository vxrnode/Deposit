per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = round(float(input('Введите сумму вклада: ')), 2)
deposit = []

for count in per_cent:
    deposit.append(round((per_cent[count] * money / 100), 2))

    # Округлегние до целых, как описано непосредственно в задании
    # deposit.append(round((per_cent[count] * money / 100))) #

print(deposit)
print("Максимальная сумма, которую вы можете заработать = " + str(max(deposit)))
