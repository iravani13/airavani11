
list_of_numbers = [ 1, 5, 2, 6, 8, 5, 10, 2 ]
def delete_numbers(numbers):
    numbers.remove(5)
    numbers.remove(6)
    numbers.remove(8)
    numbers.remove(5)
delete_numbers(list_of_numbers)
print(list_of_numbers)
