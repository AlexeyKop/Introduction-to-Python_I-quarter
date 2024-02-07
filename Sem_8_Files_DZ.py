'''
Задача No49. Решение в группах
Создать     телефонный     справочник     с возможностью  импорта  и  экспорта  данных  в формате  .txt.  
Фамилия,  имя,  отчество,  номер телефона - данные, которые должны находиться в файле.
1.Программа должна выводить данные 
2.Программа  должна  сохранять  данные  в текстовом файле 
3.Пользователь  может  ввести  одну  из характеристик  для  поиска  определенной записи
(Например   имя   или   фамилию человека) 
4.Использование  функций.  Ваша  программа не должна быть линейной

ДЗ:
Дополнить справочник возможностью копирования данных из одного файла в другой. 
Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.
'''

def input_lastname():
    return input('Введите Фамилию контакта: ').title()

def input_name():
    return input('Введите Имя контакта: ').title()

def input_patronymic():
    return input('Введите Отчество контакта: ').title()

def input_phone():
    return input('Введите Телефон контакта: ')

def input_address():
    return input('Введите Адрес(город) контакта: ').title()

def create_contact():
    lastname = input_lastname()
    name = input_name()
    patronomic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f'{lastname} {name} {patronomic}: {phone}\n{address}\n\n'


def add_contact():
    contact_str = create_contact()
    with open('phonebook.txt', 'a', encoding='UTF-8') as file:
        file.write(contact_str)

def print_contacts():
    with open ('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_str = file.read()
    # print([contacts_ctr])
    contacts_list = contacts_str.rstrip().split('\n\n')
    for n, contact in enumerate(contacts_list, 1):
        print(n, contact)

def search_contact():
    print(
            'Возможные варианты поиска:\n'
            '1. По Фамилии\n'
            '2. По Имени\n'
            '3. По Отчеству\n'
            '4. По телефону\n'
            '5. По адресу(город)'
            )
    var = input('Выберите вариант поиска: ')
    while var not in ('1', '2', '3', '4', '5'):
        print('Некорректный ввод')
        var = input('Выберите вариант поиска: ')
    i_var = int(var) - 1

    search = input('Введите данные для поиска: ').title()
    with open ('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_str = file.read()
    # print('contacts_str = file.read()'[contacts_str])
    contacts_list = contacts_str.rstrip().split('\n\n')
    # print(contacts_list)
    for str_contact in contacts_list:
        # print(str_contact)
        lst_contact = str_contact.replace(':', '').split()
        if search in lst_contact[i_var]:
            print()          
            print(str_contact)


def copy_contact(contact_number):
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts = file.read().rstrip().split('\n\n')

    if 1 <= contact_number <= len(contacts):
        contact = contacts[contact_number - 1]
        with open('phonebook_copy.txt', 'a', encoding='UTF-8') as copy_file:
            copy_file.write(contact + '\n\n')
        print(f"Контакт номер {contact_number} скопирован в phonebook_copy.txt.")
    else:
        print("Некорректный номер контакта.")

# def interfaice():
#     with open('phonebook.txt', 'a', encoding='UTF-8'):
#         pass
    
#     var = 0
#     while var != '5':
#         print(
#             'Возможные действия:\n'
#             '1. Добавить контакт\n'
#             '2. Вывести на экран\n'
#             '3. Поиск контакта\n'
#             '4. Копировать контакт в другой файл\n'
#             '5. Выход'
#             )
#         print()
#         var = input('Выберите действие: ')
#         while var not in ('1', '2', '3', '4', '5'):
#             print('Некорректный ввод')
#             var = input('Выберите действие: ')
        
#         print()
#         match var:
#             case '1':
#                 add_contact()
#             case '2':
#                 print_contacts()
#             case '3':
#                 search_contact()
#             case '4':
#                 contact_number = int(input("Введите номер контакта для копирования: "))
#                 copy_contact(contact_number)
#             case '5':
#                 print('Good luck!')
#         print()


# if __name__ == '__main__':
#     interfaice()

def print_copy_contacts():    
    with open('phonebook_copy.txt', 'r', encoding='UTF-8') as copy_file:
        copy_contacts_str = copy_file.read()        
    copy_contacts_list = copy_contacts_str.rstrip().split('\n\n')
    for n, contact in enumerate(copy_contacts_list, 1):
        print(n, contact)


def interfaice():
    with open('phonebook.txt', 'a', encoding='UTF-8'):
        pass
    
    var = 0
    while var != '6':
        print(
            'Возможные действия:\n'
            '1. Добавить контакт\n'
            '2. Вывести контакты из phonebook.txt на экран\n'
            '3. Поиск контакта\n'
            '4. Копировать контакт в другой файл\n'
            '5. Вывести контакты из phonebook_copy.txt на экран\n'
            '6. Выход'
            )
        print()
        var = input('Выберите действие: ')
        while var not in ('1', '2', '3', '4', '5', '6'):
            print('Некорректный ввод')
            var = input('Выберите действие: ')
        
        print()
        match var:
            case '1':
                add_contact()
            case '2':
                print_contacts()
            case '3':
                search_contact()
            case '4':
                contact_number = int(input("Введите номер контакта для копирования: "))
                copy_contact(contact_number)
            case '5':
                print_copy_contacts()
            case '6':
                print('Good luck!')
        print()


if __name__ == '__main__':
    interfaice()
