first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

#first_result = (len(x[0])-len(x[1]) for x in zip(first, second) if len(x[0]) != len(x[1]))
first_result = (len(x)-len(y) for x,y in zip(first, second) if len(x) != len(y))
print(list(first_result))
second_result = (len(x) == len (y) for x in first for y in second if first.index(x) == second.index(y))
print(list(second_result))
