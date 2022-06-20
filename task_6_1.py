# Не используя библиотеки для парсинга,
# распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
#— получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).

with open('nginx_logs.txt') as f:
    data = []
    for line in f:
        splitted = line.split()
        data.append((splitted[0],splitted[5].replace('"', ''), splitted[6]))
print(data)