import csv
import string
import random


def create_login(fio):
    sername, name, otch = fio.split()
    return f'{name[0]}{otch[0]}{sername}'


def password_create():
    alphabet = string.ascii_lowercase + string.ascii_lowercase
    chisl = '0123456789'
    spec_sim = '!?.()'
    pas_sim = alphabet + chisl + spec_sim
    password = ''
    while True:
        al = 0
        ch = 0
        sp = 0
        for _ in password:
            if _ in alphabet:
                al = 1
            if _ in chisl:
                ch = 1
            if _ in spec_sim:
                sp = 1
        if al + ch + sp > 1:
            return password
        else:
            password = ''
            for q in range(10):
                password += random.choice(pas_sim)
        
    

with open('q.csv', 'r', encoding='cp1251') as file:
    data = list(csv.DictReader(file, delimiter=';'))
    #id;Full_Name;Project_id;Nomination;Prize
    for member in data:
        member['Login'] = create_login(member['Full_Name'])
        member['Password'] = password_create()
    

with open('q_new.csv', 'w', encoding='cp1251') as file:
    writer = csv.DictWriter(file, delimiter=';', fieldnames=['id', 'Full_Name', 'Project_id',\
                                                              'Nomination', 'Prize', 'Login', 'Password'])
    writer.writeheader()
    writer.writerows(data)
    
    
