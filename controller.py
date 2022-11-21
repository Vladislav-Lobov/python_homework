import view
import model_create
import model_generator
import model_append
import model_show
import model_edit
import model_remove
import model_extra
import model_export
import model_import


def menu():

    choice = -1
    try:
        while choice != 0:
            view.get_menu_interface()
            choice = view.get_menu_choice()
            if choice == 0:
                break
            if choice == 1:
                model_show.show_database()
            if choice == 2:
                model_create.clear_database()
                model_create.create_database()
                for i in range(15):
                    new_record = model_generator.get_random_record()
                    model_append.record_append(new_record)
            if choice == 3:
                model_create.clear_database()
                model_create.create_database()
            if choice == 4:
                new_record = view.get_new_record()
                model_append.record_append(new_record)
            if choice == 5:
                id = view.get_id()
                editing_record = model_edit.get_old_record(id)
                if editing_record != -1:
                    view.show_editing_id(editing_record)
                    new_record = view.get_new_record()
                    model_edit.record_edit(new_record, id)
            if choice == 6:
                id = view.get_id()
                model_remove.record_remove(id)
            if choice == 7:
                id = view.get_id()
                position = view.get_position()
                model_extra.extra_position(position, id)
            if choice == 8:
                id = view.get_id()
                phone = view.get_phone()
                model_extra.extra_phone(phone, id)
            if choice == 9:
                filename = view.get_filename()
                model_export.export(filename)
            if choice == 10:
                filename = view.get_filename()
                model_import.import_from_file(filename)

    except ValueError:
        print("\n Произошла ошибка: ", ValueError, "\n Пожалуйста повторие ввод: ")
        menu()


