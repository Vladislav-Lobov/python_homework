def adding_phone(id, phone_number):
    with open("phone_book.csv", "r", encoding="utf-8") as source_data:
        new_book = []
        for i in source_data:
            new_book.append(i)
            if i.startswith(id):
                new_book.append(i.rpartition(",")[0] + ", " + phone_number + "\n")

    # переиндексация после добавления:
    new_index = 0
    reindex_book = []
    for i in new_book:
        result = str(new_index) + "," + i.split(",", 1)[1]
        reindex_book.append(result)
        new_index += 1

    with open("phone_book.csv", "w", encoding="utf-8") as reciever_data:
        for i in reindex_book:
            reciever_data.write(i)
