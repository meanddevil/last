# 1. Показать все контакты
# 2. Добавить контакт
# 3. Найти контакт
# 4. Изменить контакт
# 5. Удалить контак
# 6. Скопировать контакт в другой файл

# формат : Имя Номер Комментарий


my_dict = []
with open('people.txt', 'r+') as file:
    for i in file:
        my_list= i.split()
        my_dict.append({'№':my_list[0],'Имя':my_list[1], 'Телефон':my_list[2], 'Комментарий':my_list[3]})

# print(*my_dict)


def show_all(my_dict):
    print("Все значения из справочника:")
    for i in my_dict:
        for key in i:
            print(f"{key}: {str(i[key]).replace('{', '').replace('}', '')}", end=' ')
        print()
    print()


def add_contact(my_dict):
    name = input("Введите имя контакта\n")
    phone_number = input("Введите номер телефона контакта\n")
    comment = input("Введите комментарий контакта\n")
    num_of_per = len(my_dict)+1
    new_person = f'{num_of_per} {name} {phone_number} {comment}'
    my_dict.append({'№':len(my_dict)+1,'Имя':name, 'Телефон':phone_number, 'Комментарий':comment})
    with open("people.txt",'a+') as file:
        file.write(new_person + '\n')
        show_all(my_dict)


def find_person(my_dict):
    information = input("Введите информацию для поиска\n")
    k = False
    for item in my_dict:
        for i in item.values():
            if information == str(i):
                for j in item:
                    print(f"{j}: {str(item[j]).replace('{', '').replace('}', '')}", end=' ')
                    k = True
                print()
            print()
    if k == False:
        print("Контакт не найден\n")
        return k
    return information


def change_contact(my_dict):
    num = int(input("Введите номер контакта\n"))
    if num-1 > len(my_dict):
        print("Контакт не найден\n")
        return
    what_inf = input("Что меняем? Имя/Телефон/Комментарий\n")
    new_inf = input("Внесите новую информацию\n")
    my_dict[num-1][what_inf] = new_inf
    show_all(my_dict)
    with open('people.txt', 'w') as file:
        for i in my_dict:
            file.write(f'{i["№"]} {i["Имя"]} {i["Телефон"]} {i["Комментарий"]}'+ "\n")

def delete_contact(my_dict):
    num = int(input("Введите номер контакта для удаления\n"))
    if len(my_dict) == 0:
        print("Справочник уже пустой.\n")
        return
    if num > len(my_dict):
        print("Контакт не найден\n")
        return

    my_dict.pop(num-1)
    for i in range(len(my_dict)):
        my_dict[i]['№'] = str(i+1)

    with open('people.txt', 'w') as file:
        for i in my_dict:
            file.write(f'{i["№"]} {i["Имя"]} {i["Телефон"]} {i["Комментарий"]}'+ "\n")
    print()

def cope_contact(my_dict):
    num = int(input("Введите номер контакта для копирования\n"))
    if num > len(my_dict):
        print("Контакт не найден\n")
        return
    with open('people_cope.txt', 'a+') as file:
        file.write(f'{my_dict[num-1]["Имя"]} {my_dict[num-1]["Телефон"]} {my_dict[num-1]["Комментарий"]}' + "\n")

print("""Выберите необходимый пункт:
 1. Показать все контакты
 2. Добавить контакт
 3. Найти контакт
 4. Изменить контакт
 5. Удалить контак
 6. Скопировать контакт в другой файл
 7. Выход из программы""")

while True:
    try:
        menu_item = int(input())
        break
    except ValueError:
        print("Неверно введен номер меню. Попробуйте снова.")
        next

while menu_item != 7:
    if menu_item == 1:
        show_all(my_dict)
    elif menu_item == 2:
        add_contact(my_dict)
    elif menu_item == 3:
        find_person(my_dict)
    elif menu_item == 4:
         change_contact(my_dict)
    elif menu_item == 5:
        delete_contact(my_dict)
    elif menu_item == 6:
        cope_contact(my_dict)
    else:
        print("Такой команды нет!")
    menu_item = int(input("Введите команду: "))


