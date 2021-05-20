
try:
    def compare_string (first, second):
        if type(first) == str and type(second) == str: 
            if len(first) != len(second) and second == 'learn':
                return '3' 
            elif len(first) > len(second):
                return '1'
            elif len(first) == len(second):
                return '2'
            else:
                return 'Не подходит ни под один необходимый параметр'
        else:
            return '0'
    
    result_1 = compare_string('same', 'same')
    result_2 = compare_string('longest', 'short')
    result_3 = compare_string('nolearn', 'learn')
    result_4 = compare_string('short', 'longest')
    result_5 = compare_string(10, 333)
    print (result_1)
    print (result_2)
    print (result_3)
    print (result_4)
    print (result_5)
except ValueError:
    print ('Черт знает, что вы могли внести! Может клингонский?')