import lab4c

dict_york = {
    'Address': '70 The Pond Rd',
    'City': 'Toronto',
    'Country': 'Canada',
    'Postal Code': 'M3J3M6',
    'Province': 'ON'
}
dict_newnham = {
    'Address': '1750 Finch Ave E',
    'City': 'Toronto',
    'Country': 'Canada',
    'Postal Code': 'M2J2X5',
    'Province': 'ON'
}
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

york = lab4c.create_dictionary(list_keys, list_values)

print(york)
# Will print: {'Address': '70 The Pond Rd',
#              'City': 'Toronto',
#              'Country': 'Canada',
#              'Postal Code': 'M3J3M6',
#              'Province': 'ON'}

common = lab4c.shared_values(dict_york, dict_newnham)

print(common)
# Will print: {'Canada', 'ON', 'Toronto'}

