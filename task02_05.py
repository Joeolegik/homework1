price_list = [57.8, 46.51, 97, 13, 17, 23.57, 64.23, 98.09, 144.35, 1250, 5499.99]
for price_tags in price_list:
    rub = int(price_tags)
    kk = (price_tags - int(price_tags)) * 100
    print(f'{rub} руб {kk:02.0f} коп', end=', ')

price_list.sort()
for price_tags in price_list[::-1][:5]:
    rub = int(price_tags)
    kk = (price_tags - int(price_tags)) * 100
    print('\n', f'{rub} руб {kk:02.0f} коп', end=', ')

