data = None  # Initialize data before the try block

try:
    f = open('not_a_file.txt', 'r')
    data = f.read()
    f.close()
except FileNotFoundError:
    print('File not found! Please check your spelling and try again.')

if data is not None:
    print(data)
