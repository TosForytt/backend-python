name = input("Как вас зовут? ")

name_first = name.strip().capitalize()
print(len(name_first))
if name_first[0] == "А":
    print("Имя на А")
else:
    print("Имя не на А")