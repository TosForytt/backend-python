numbers = [1, 5, 10, 20, 100]

print(len(numbers))

print(numbers[0])

print(numbers[-1])

numbers.append(500)

total = 0
for number in numbers:
    total += number

print(f"Сумма: {total}")