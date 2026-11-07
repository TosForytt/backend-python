def is_adult(age):
    return age >= 18

def greet_adult(name, age):
    if is_adult(age):
        return f"Добрый день, {name}, вам {age} лет"
    else:
        return f"Привет, {name}, тебе {age} лет"

if __name__ == "__main__":
    print(greet_adult("Олег", 25))
    print(greet_adult("Аня", 10))