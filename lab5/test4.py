try:
    f = open('data', 'r')
    data = f.read()
    f.close()
    print(data)
except FileNotFoundError:
    print('File not found.')
except Exception as e:
    print('Some other problem occurred:', e)
