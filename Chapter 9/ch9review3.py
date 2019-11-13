__author__ = 'andydelso'

if __name__ == '__main__':
    birthdays = {}

    birthdays['Luke Skywalker'] = '5/24/19'
    birthdays['Obi-Wan Kenobi'] = '3/11/57'
    birthdays['Darth Vader'] = '4/1/41'

    if 'Yoda' not in birthdays:
        birthdays['Yoda'] = 'unknown'

    if 'Darth Vader' not in birthdays:
        birthdays['Darth Vader'] = 'unknown'

    for each in birthdays:
        print each, birthdays[each]

    del(birthdays['Darth Vader'])

    for each in birthdays:
        print each, birthdays[each]

    birthdays2 = dict([('Luke Skywalker','5/24/19'),('Obi-Wan Kenobi','3/11/57'),\
                       ('Darth Vader','4/1/41'),('Yoda','unknown')])

    for each in birthdays2:
        print each, birthdays2[each]