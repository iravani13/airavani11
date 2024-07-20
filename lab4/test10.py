def is_vowel(char):
    if char in 'aeiou':
        return True
    return False
      
if __name__ == '__main__':
    text = 'Seneca'
    vowel_count = 0
    for char in text:
        if is_vowel(char):
             vowel_count = vowel_count + 1
    print('There are',vowel_count,'vowel(s) in',text)
