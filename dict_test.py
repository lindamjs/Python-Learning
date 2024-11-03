def print_dict(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)


#input = {"name":["John", "Smith", "Alice","Bob"], "age":[20, 30, 40, 50]}
#input = ('John', 1, 'Alice', 2)
print_dict(name='Leo', age='20')

#print_dict(first='Geeks', mid='for', last='Geeks')

