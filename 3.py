import csv

with open('q.csv', 'r', encoding='cp1251') as file:
    data = list(csv.DictReader(file, delimiter=';'))
    #id;Full_Name;Project_id;Nomination;Prize
    data = sorted(data, key=lambda member: member['Project_id'])
    zayavka = input()
    while zayavka != 'СТОП' and zayavka != 'стоп' and zayavka != '':
        zayavka = int(zayavka)
        for member in data:
            if int(member['Project_id']) == zayavka:
                sername, name, otch = member['Full_Name'].split()
                print(f'Заявка № {member["Project_id"]} Автор: {sername} {name[0]}.{otch[0]} Сумма – {int(member["Prize"])/1000} тыс. руб.')
                break
        else:
            print('kui')
        zayavka = input()
