
seconds = int(input('Введите секунды для расчёта времени: '))
if seconds <= 60:
    print(seconds, 'сек')
elif 60 < seconds < 3600:
    m = seconds // 60
    s = seconds % 60
    print(m, 'мин', s, 'сек')
elif 3600 < seconds < 86400:
    h = seconds // 3600
    m = seconds % 3600 // 60
    s = seconds % 60
    print(h, 'час', m, 'мин', s, 'сек')
elif 86400 < seconds < 2629743:
    d = seconds // 86400
    h = seconds % 86400 // 3600
    m = seconds % 3600 // 60
    s = seconds % 60
    print(d, ' дн', h, 'час', m, 'мин', s, 'сек')
else:
    seconds >= 2629743
    print('За гранью понимания')

'''
#1 ВАРИАНТ ленивый

duration = (53, 153, 4153, 5000065323)
s = duration[0]
print(s, 'сек')
m = duration[1] // 60
s = duration[1] % 60
print(m, 'мин', s, 'сек')
h = duration[2] // 3600
m = duration[2] % 3600 // 60
s = duration[2] % 60
print(h, 'час', m, 'мин',  s, 'сек')
d = duration[3] // 86400
h = duration[3] % 86400 // 3600
m = duration[3] % 3600 // 60
s = duration[3] % 60
print(d,' дн', h, 'час', m, 'мин',  s, 'сек')

'''
