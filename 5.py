import csv

def hash_c(s):
    alpabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
    '''print(alpabet)
    alpabet = alpabet + alpabet.upper + ' '
    print(alpabet)'''
    p, m = 67, 10**9 + 9
    hash = 0
    slovar = {alpabet[i]:(i + 1) for i in range(len(alpabet))}
    for i in range(len(s)):
        hash += slovar[s[i]] * (i + 1)**2
    hash = hash * (p ** len(s) - 1) + p
    return hash % m


with open('q.csv', encoding='cp1251') as file:
    data = list(csv.DictReader(file, delimiter=';'))
    for member in data:
        member['id'] =  hash_c(member['Full_Name'])

with open('q_with_hash.csv', 'w', encoding='cp1251') as file:
    writer = csv.DictWriter(file, delimiter=';', fieldnames=['id', 'Full_Name', 'Project_id',\
                                                              'Nomination', 'Prize'])
    writer.writeheader()
    writer.writerows(data)

