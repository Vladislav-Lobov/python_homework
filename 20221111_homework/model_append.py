def finding_previvios_id():
    with open("phone_book.csv", "r", encoding="utf-8") as data:
        for line in data:
            pass
    return int(line.split(",")[0])


def append_new_record(new_record, id):
    id = str(id) + ","
    with open("phone_book.csv", "a", encoding="utf-8") as data:
        data.write("{0} {1}\n".format(id, new_record))


def clear_phone_book():
    with open("phone_book.csv", "w", encoding="utf-8") as data:
        data.write("")
