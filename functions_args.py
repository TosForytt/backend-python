def area(width, height):
    S = width * height
    return S

def describe(name, age= 18):
    return f"Имя: {name}, возраст: {age}"

print(area(5,4))
print(describe("Анна", 20))