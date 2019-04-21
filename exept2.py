import shutil

def recordSprav():# добавление нового предприятия  перечень организаций и вывод на экран всех предприятий
    str=input('Введите название предприятия,адрес, сотрудника, телефон: ')
    str=str.title()
    str += '\n'
    f = open('text.txt', 'at')
    f.write(str)
    f = open('text.txt', 'rt')
    print('Предприятие добавленно в список: \n')
    return  f.read()
    f.close()



def printSprav():#вывести на экран все предприятия
    f = open('text.txt', 'rt')
    return f.read()
    f.close()




def recordsearchSprav():#поиск предприятия
    a=input('Введите названние предприятия: ')
    a=a.title()
    old_file = open('text.txt', 'rt')
    new_file = open('text2.txt', 'wt')
    for line in old_file:
       if a in line:
           new_file.write(line)
    old_file = open('text.txt', 'rt')
    text=old_file.read()
    if not a in text:
        print('Предприятия в списке нет')
    new_file = open('text2.txt', 'rt')
    return new_file.read()
    new_file.close()
    old_file.close()



def delSprav():#удаление предприятия
    bad_company = input('Введите информацию о предприятии которое нужно удалить:')
    bad_company=bad_company.title()
    old_file = open('text.txt', 'rt')
    new_file = open('text3.txt', 'wt')
    for line in old_file:
        if not bad_company in line:
            new_file.write(line)
    old_file = open('text.txt', 'rt')
    text = old_file.read()
    if not bad_company in text:
        print('Предприятия в списке нет. Список предприятий:\n')
    new_file = open('text3.txt', 'rt')
    shutil.copyfile('text3.txt', 'text.txt')
    old_file = open('text.txt', 'rt')
    return old_file.read()
    new_file.close()
    old_file.close()






while True:
    try:
        a=int(input('1-Список предприятий\n'
               '2-Добавить предприятие\n'
                '3-Поиск предприятия\n'
                '4-Удалить предприятие\n'
                '0-завершить работу с программой\n'
                'Введите Ваш выбор\n\v'))

        while a!=0:
            if a==1:
                print('Список предприятий:\n', printSprav(),'\n')
                a = int(input('1-Список предприятий\n'
                              '2-Добавить предприятие\n'
                              '3-Поиск предприятия\n'
                              '4-Удалить предприятие\n'
                              '0-завершить работу с программой\n'
                              'Введите Ваш выбор\n\v'))
            elif a==2:
                print(recordSprav(), '\n')
                a = int(input('1-Список предприятий\n'
                              '2-Добавить предприятие\n'
                              '3-Поиск предприятия\n'
                              '4-Удалить предприятие\n'
                              '0-завершить работу с программой\n'
                              'Введите Ваш выбор\n\v'))
            elif a==3:
                print(recordsearchSprav(),'\n')
                a = int(input('1-Список предприятий\n'
                              '2-Добавить предприятие\n'
                              '3-Поиск предприятия\n'
                              '4-Удалить предприятие\n'
                              '0-завершить работу с программой\n'
                              'Введите Ваш выбор\n\v'))
            elif a==4:
                print(delSprav(),'\n')
                a = int(input('1-Список предприятий\n'
                              '2-Добавить предприятие\n'
                              '3-Поиск предприятия\n'
                              '4-Удалить предприятие\n'
                              '0-завершить работу с программой\n'
                              'Введите Ваш выбор\n\v'))
            else:
                print('Вы ввели не корректное значение, пожалуйста сделайте Ваш выбор!')
                a = int(input('1-Список предприятий\n'
                              '2-Добавить предприятие\n'
                              '3-Поиск предприятия\n'
                              '4-Удалить предприятие\n'
                              '0-завершить работу с программой\n'
                              'Введите Ваш выбор\n\v'))
        print('Программа завершила работу')
        break
    except ValueError:
        print('Вы ввели текстовое значение,пожалуйста сделайте Ваш выбор!')
        continue




