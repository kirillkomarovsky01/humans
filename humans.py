def spisok():
    for name,vk in persons.items():
        print('Контакт: {0}, vk: {1}'.format(name,vk))

def dobavit():
    name_1 = input('Введите имя: ')
    vk_1 = input('Введите его vk: ')
    persons[name_1] = vk_1
    print('Обновленный список: ')
    
persons = { 'Кирилл Наметкин': 'https://vk.com/nametkinkirill',
            'Никита Азаренков': 'https://vk.com/frishaa',
            'Егор Нощенко': 'https://vk.com/id339682102'}
slovo = input('Введите, что вам нужно: добавить, удалить, изменить, показать --> ')

if (slovo == 'показать'):
    spisok()
elif (slovo == 'добавить'):
    dobavit()
    spisok()
elif (slovo == 'удалить'):
    lox = input('Введите имя человека, которого нужно удалить: ')
    del persons[lox]
    print('Обновленный список: ')
    spisok()
