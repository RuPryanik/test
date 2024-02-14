import csv

with open('q.csv', encoding='cp1251') as file:
    data = list(csv.DictReader(file, delimiter=';'))
    for member in data:
        if 'Агафья' in member['Full_Name'] and 'Ершова' in member['Full_Name']:
            print(f'Вы получили {member["Prize"]} рублей в конкурсе {member["Nomination"]} с номером заявки {member["Project_id"]}.')
            break
        
    counts, summ = {}, {}
    for member in data:
        if member['Prize'] != 'NULL':
            summ[member['Nomination']] = summ.get(member['Nomination'], 0) + int(member['Prize'])
            counts[member['Nomination']] = counts.get(member['Nomination'], 0) + 1
    for member in data:
        if member['Prize'] == 'NULL':
            member['Prize'] = round(summ[member['Nomination']] // counts[member['Nomination']], -3)

with open('q_fix.csv', 'w', encoding='cp1251') as file:
    writer = csv.DictWriter(file, delimiter=';', fieldnames=['id', 'Full_Name', 'Project_id',\
                                                              'Nomination', 'Prize'])
    writer.writeheader()
    writer.writerows(data)
