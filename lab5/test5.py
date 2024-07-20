abc = 'example.txt'  # Define the filename as a string

try:
    with open(abc, 'w') as file:  # Open the file in write mode
        file.write('hello world\n')
except (FileNotFoundError, PermissionError):
    print('file does not exist or wrong permissions')
except IsADirectoryError:
    print('file is a directory')
except OSError as e:
    print('unable to open file: {}'.format(e))
except Exception as e:
    print('unknown error occurred: {}'.format(e))
