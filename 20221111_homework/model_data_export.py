def export_data(filename):
    with open("phone_book.csv", "r", encoding="utf-8") as data_source:
        with open(filename, "w", encoding="utf-8") as data_receiver:
            for i in data_source:
                data_receiver.write(i)
