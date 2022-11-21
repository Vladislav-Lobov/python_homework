def show():
    with open("phone_book.csv", "r", encoding="utf-8") as data:
        for i in data:
            print(i, end="")
