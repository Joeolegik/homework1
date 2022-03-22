my_list = ['в', '5', 'часов', '17', 'минут',
           'температура', 'воздуха',
           'была', '+5', 'градусов']
new_list = []
for element in my_list:
    if element.isdigit():
        new_list.append(f'"{int(element):02}"')
    elif (element.startswith('+') or element.startswith('-')) and element[1:].isdigit():
        new_list.append(f'"{element[0]}{int(element[1:])}"')
    else:
        new_list.append(element)
print(new_list)
out_info = ' '.join(new_list)
print(out_info)