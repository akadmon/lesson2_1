from statistics import mean
school_bd = [
    {
        'school_class': '6a', 
        'scores': [3, 4, 4, 2, 4, 2, 2, 4, 3, 5]
        },
    {
        'school_class': '6b', 
        'scores': [3, 4, 5, 2, 3, 5, 5, 4, 5, 2]
        },
    {
        'school_class': '6c', 
        'scores': [2, 2, 5, 2, 5, 5, 3, 5, 3, 3]
        }
]

for i in school_bd:
    print(i)
qd = [3, 4, 4, 2, 4, 2, 2, 4, 3, 5]
za = mean(qd)
print(za)


sum = 0
kolvo = len(qd)
for i in qd:
    sum += i
    sum1 = sum * kolvo / 100
print(sum1)