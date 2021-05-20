def qood_question ():
    while True:
        user_say = input('Как дела?\n')
        if user_say == 'Хорошо':
            return f'И ответ "{user_say}" это правильный ответ!'    
            break
        else:
            print('Подумай и ответь снова!')
print(qood_question())