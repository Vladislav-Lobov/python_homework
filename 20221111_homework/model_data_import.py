def import_data(filename, id):
    #переиндексация базы, которая будет добавленна
    with open(filename, "r", encoding="utf-8") as data_source:
        appending_book = []
        new_index = id
        for i in data_source:
            result = str(new_index) + "," + i.split(",", 1)[1]
            appending_book.append(result)
            new_index += 1

    with open("phone_book.csv", "a", encoding="utf-8") as data_receiver:
        for i in appending_book:
            data_receiver.write(i)
