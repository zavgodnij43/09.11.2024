with open("quotes.txt", "r", encoding="utf-8") as Harri:
    data = Harri.read()

print(data)

answer = input("Прізвище")

with open("quotes.txt", "a", encoding="utf-8") as Harri:
    Harri.write("\n" + answer)

with open("quotes.txt", "r", encoding="utf-8") as Harri:
    data = Harri.read()

print(data)