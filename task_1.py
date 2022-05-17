seconds = int(input('Введите секунды для расчёта точного времени: '))
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
    print('За гранью моего понимания')