def all_variants(text): # Генератор возвращение последовательностей для частного случая строки из 3 символов
    text_2 = text
    while text_2 != '': # Перебор строки посимвольно
        yield text_2[0]
        text_2 = text_2[1:]
    text_2 = text
    while len(text_2) != 1: # перебор по 2 символа
        yield str(text_2[0] + text_2[1])
        text_2 = text_2[1:]
    yield text # Вывод полсной строки


a = all_variants("abc")
for i in a:
    print(i)