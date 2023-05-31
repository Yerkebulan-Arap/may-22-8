price = float(input("Введите стоимость покупки:"))
discount = float(input("Введите размер скидки:"))
sum = "%#10.2f" %(price-(price*discount/100))
print("Итоговая стоимость покупки со скидкой:", sum)

