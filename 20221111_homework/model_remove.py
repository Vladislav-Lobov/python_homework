def removing_record(id):
    new_book = []
    with open("phone_book.csv", "r", encoding="utf-8") as data:
        for i in data:
            if not i.startswith(id):
                new_book.append(i)

    # переиндексация после удаления:
    new_index = 0
    reindex_book = []
    for i in new_book:
        result = str(new_index) + "," + i.split(",", 1)[1]
        reindex_book.append(result)
        new_index += 1

    with open("phone_book.csv", "w", encoding="utf-8") as data:
        for i in reindex_book:
            data.write(i)
