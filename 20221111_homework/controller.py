import view
import model_show
import model_append
import model_generator
import model_remove
import model_data_import
import model_data_export
import model_extra_phone


def menu():
    choice = -1

    while choice != 0:
        view.show_main_menu()
        choice = view.get_menu_item()

        if choice == 1:
            model_show.show()
        elif choice == 2:
            id = model_append.finding_previvios_id()
            id += 1
            new_record = view.get_new_record()
            model_append.append_new_record(new_record, id)
        elif choice == 3:
            id_removing = view.get_id_removing()
            model_remove.removing_record(id_removing)
        elif choice == 4:
            model_append.clear_phone_book()
            for i in range(15):
                model_append.append_new_record(model_generator.get_random_record(), i)
        elif choice == 5:
            filename = view.get_import_filename()
            id = model_append.finding_previvios_id()
            id += 1
            model_data_import.import_data(filename, id)
        elif choice == 6:
            filename = view.get_export_filename()
            model_data_export.export_data(filename)
        elif choice == 7:
            id = view.get_extra_id()
            phone_number = view.get_extra_phone()
            model_extra_phone.adding_phone(id, phone_number)
        else:
            print("Пожалуйста, ведите цифру от 0 до 7...")
