'''
Задача No49. Решение в группах
Создать     телефонный     справочник     с возможностью  импорта  и  экспорта  данных  в формате  .txt.  
Фамилия,  имя,  отчество,  номер телефона - данные, которые должны находиться в файле.
1.Программа должна выводить данные 
2.Программа  должна  сохранять  данные  в текстовом файле 
3.Пользователь  может  ввести  одну  из характеристик  для  поиска  определенной записи
(Например   имя   или   фамилию человека) 
4.Использование  функций.  Ваша  программа не должна быть линейной

Алгоритм:
1. Создание файла:  +++
    - открываем файл на дозапись ( а )  +++
2. Добавление контакта:
    - запросить у пользователя новый контакт
    - открыть файл на дозапись ( а )
    - добавиь новый контакт
3. Вывод данных на экран:
    - открыть файл на чтение ( r )
    - считать файл
    - вывод данных на экран
4. Поиск контакта:
    - выбор варианта поиска
    - запросить данные для поиска
    - открыть файл на чтение
    - считываем данные с файла, сохранить их в переменную
    - поиск контакта с переменной
    - выввести на экран найденный контакт
5. Создание UI (User Interfeice):
    - вывести меню на экран +++
    - запросить у пользователя вариант действия +++
    - запустить соответствующую функцию +++
    - осуществить возможность выхода из программы   +++
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
    # print([contacts_ctr])
    contacts_list = contacts_str.rstrip().split('\n\n')
    # print(contacts_list)
    for str_contact in contacts_list:
        # print(str_contact)
        lst_contact = str_contact.replace(':', '').split()
        if search in lst_contact[i_var]:            
            print(str_contact)


def interfaice():
    with open ('phonebook.txt', 'a', encoding='UTF-8'):
        pass
    
    var = 0
    while var != '4':
        print(
            'Возможные варианты:\n'
            '1. Добавит контакт\n'
            '2. Вывести на экран\n'
            '3. Поиск контакта\n'
            '4. Выход'
            )
        print()
        var = input('Выберите вариант действия: ')
        while var not in ('1', '2', '3', '4'):
            print('Некорректный ввод')
            var = input('Выберите вариант действия: ')
        
        print()
        match var:
            case '1':
                add_contact()
            case '2':
                print_contacts()
            case '3':
                search_contact()
            case '4':
                print('Good luck!')
        print()


if __name__ == '__main__':
    interfaice()


def add_contact(contact_info, phonebook):
    contact_number = len(phonebook) + 1
    phonebook[contact_number] = contact_info

def copy_contact(contact_number, phonebook):
    if 1 <= contact_number <= len(phonebook):
        contact_info = phonebook[contact_number]
        with open('phonebook_copy.txt', 'a', encoding='UTF-8') as copy_file:
            copy_file.write(contact_info + '\n')
        print(f"Контакт номер {contact_number} успешно скопирован в другой файл.")
    else:
        print("Некорректный номер контакта.")

def interfaice():
    phonebook = {}
    var = 0
    while var != '5':
        print(
            'Возможные действия:\n'
            '1. Добавить контакт\n'
            '2. Вывести на экран\n'
            '3. Поиск контакта\n'
            '4. Копировать контакт в другой файл\n'
            '5. Выход'
            )
        print()
        var = input('Выберите действие: ')
        while var not in ('1', '2', '3', '4', '5'):
            print('Некорректный ввод')
            var = input('Выберите действие: ')
        
        print()
        match var:
            case '1':
                lastname = input_lastname()
                name = input_name()
                patronomic = input_patronymic()
                phone = input_phone()
                address = input_address()
                contact_info = f'{lastname} {name} {patronomic}: {phone}\n{address}\n'
                add_contact(contact_info, phonebook)
            case '2':
                print_contacts(phonebook)
            case '3':
                search_contact(phonebook)
            case '4':
                contact_number = int(input("Введите номер контакта для копирования: "))
                copy_contact(contact_number, phonebook)
            case '5':
                print('До свидания!')
        print()

def print_contacts(phonebook):
    for contact_number, contact_info in phonebook.items():
        print(contact_number, contact_info)

def search_contact(phonebook):
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
    for contact_number, contact_info in phonebook.items():
        lst_contact = contact_info.replace(':', '').split()
        if search in lst_contact[i_var]:            
            print(contact_number, contact_info)


if __name__ == '__main__':
    interfaice()
