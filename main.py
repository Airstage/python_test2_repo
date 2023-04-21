from datetime import datetime as dt


def what_time_is_now():
    print(dt.now())


def till_midnight():
    midnight = dt.now()
    midnight.minutes = 59
    midnight.hours = 23
    print(midnight - dt.now())

print('Привет, мир!')

print('Меня зовут Кирилл.')
print('В этом проекте я тестирую возможности VCS.')
print('В дальнейшем добавлю несколько функций.')

print('Конец.')

what_time_is_now()
till_midnight()