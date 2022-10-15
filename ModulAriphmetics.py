import random

m = int(input("Введіть значення m.\nm = "))

a = int(input("\nВведіть значення а.\na  = "))
print("a mod m = ", a % m)

b = int(input("\nВведіть значення b.\nb = "))
print("a^b mod m = ", (a ** b) % m)

x = (b % m) / a
print("\nb mod m = a * x\nx = ", x, "\nb mod m = ", a * x)


#Згенерувати просте число у діапазоні від A до B.
print("Генерація простого числа в діапазоні [A, B]")
a = int(input("A = "))
b = int(input("B = "))
lst = [2]
for i in range(3, b + 1, 2):
	if (i > 10) and (i % 10 == 5):
		continue
	for j in lst:
		if j * j - 1 > i:
			lst.append(i)
			break
		if (i % j == 0):
			break
	else:
		lst.append(i)
new_lst = []
for i in lst:
    if i >= a:
        new_lst.append(i)
print(new_lst)
