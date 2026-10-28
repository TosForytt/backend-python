grade = int(input("Укажите ваши баллы: "))

if grade < 0 or grade > 100:
    print("Ошибка ввода")
elif grade >= 90:
    print("Ваша оценка: A")
elif grade >= 80:
    print("Ваша оценка: B")
elif grade >= 70:
    print("Ваша оценка: C")
else:
    print("Ваша оценка: F")