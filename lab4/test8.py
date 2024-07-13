def find(text,char):
    for letter in text:
        if letter == char:
             return True
    return False

if __name__ == '__main__':
    s1 = 'Seneca'
    print(s1,'contains letter s? ->',find(s1,'s'))
    print(s1,'contains letter S? ->',find(s1,'S'))
