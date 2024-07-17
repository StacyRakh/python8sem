# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 18:34:56 2024

@author: Анастасия Рахманина
"""

from csv import DictWriter, DictReader
from os.path import exists

class NameError(Exception):
    def _init_(self,txt):
        self.txt = txt

def get_data():
    flag = False
    while not flag:
        try:
            first_name = input('Введите имя:')
            if len(first_name) <2:
                raise NameError ("Слишком короткое имя")
            last_name = input('Введите фамилию:')
            if len(last_name) <5:
                raise NameError ("Слишком короткая фамилия")
            phone = input('Введите номер телефона после +')
            if len (phone)<11:
                raise NameError ("Слишком короткий телефон")
        except NameError as err:
            print ('Слишком короткое значение')
        else: 
            flag = True
    
    return [first_name, last_name, phone]

def create_file (file_name):
    with open (file_name, 'w', encoding= 'utf-8') as data:
        f_w = DictWriter(data, fieldnames = ['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()


def read_file (file_name):
    with open (file_name, 'r', encoding= 'utf-8') as data:
        f_r = DictReader(data)
        return list (f_r)

def write_file(file_name, lst):
    res = read_file(file_name) 
    obj = {'Имя':lst[0], 'Фамилия':lst[1], 'Телефон': lst [2]} 
    res.append(obj)     
    with open (file_name, 'w', encoding= 'utf-8') as data:
        f_w = DictWriter(data, fieldnames = ['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()
        f_w.writerows(res)

def row_search(file_name):
    last_name = input("Введите фамилию:")
    res = read_file(file_name)
    for row in res:
        if last_name == row['Фамилия']:
            return row
    return "Запись не найдена"

def delete_row(file_name):
    row_number = input("Введите номер строки:")
    res = read_file(file_name)
    res.pop(row_number-1)
    standart_write(file_name,res)
     
def standart_write(file_name,res):
    with open(file_name, 'w', encoding='utf-8') as data:
        res = read_file(file_name)
        f_w = DictWriter(data, fieldnames = ['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()
        f_w.writerows(res)
        
def change_row(file_name):
    row_number = int(input("Введите номер строки:"))
    res = read_file(file_name)
    data = get_data()
    res[row_number-1]['Имя'] = data[0]
    res[row_number-1]['Фамилия'] = data[1]   
    res[row_number-1]['Телефон'] = data[2]  
    standart_write(file_name,res)
def copy_paste(file_name,other_file):
    res = read_file(file_name)
    row_number = int(input('Введите номер строки'))
    need_number = res[row_number-1]
    copying = list(need_number.values())
    re1 = read_file(other_file) 
    obj = {'Имя':copying[0], 'Фамилия':copying[1], 'Телефон': copying[2]} 
    re1.append(obj)     
    with open (other_file, 'w', encoding= 'utf-8') as data:
        f_w = DictWriter(data, fieldnames = ['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()
        f_w.writerows(re1)
    
    
file_name = 'phone.csv'   
other_file = 'all_phones.csv'
    
 
def main():
    while True:
        command = input ("Введите команду:")
        if command == "q":
            break
        elif command == "w":
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_data())
        elif command =='r':
            if not exists(file_name):
                print ("Файл не сушествует, создайте его")
                continue
            print(read_file(file_name))
        elif command == "f":
            if not exists(file_name):
                print ("Файл не сушествует, создайте его")
                continue
            print (row_search(file_name))
        elif command == "d":
            if not exists(file_name):
                print ("Файл не сушествует, создайте его")
                continue
            delete_row(file_name)
        elif command == "c":
            if not exists(file_name):
                print ("Файл не сушествует, создайте его")
                continue
            change_row(file_name)
        elif command == 'cp':
            if not exists(file_name):
                print ("Файл не сушествует, создайте его")
                continue
            if not exists(other_file):
                print ("Файл не сушествует, создайте его")
                continue
            copy_paste(file_name,other_file)
    
              
      
            
#создадим новый файл для копирования
#file_name = 'all_phones.csv'
#main()
#Далее я ввела комманду w и добавила в нее запись 
#была создана функция cp для копирования, но чувствую, что можно было 
#обойтись меньшим количеством строк через другие функции, пока дается тяжело
main()

