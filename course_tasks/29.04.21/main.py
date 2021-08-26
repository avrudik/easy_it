from re import sub


def var1(wordlist):
    vowels_list = ["а", "и", "о", "у", "э", "я", "ё", "ю", "ы"]
    consonants = 0
    vowels = 0
    for item in wordlist:
        if item[0] in vowels_list:
            vowels += 1
        else:
            consonants += 1
    return {'Гласные': vowels, 'Согласные': consonants}


def var2(text):
    special_symbols = ['.', ',', ':', '-', '"', "'", "»", '«', '?', ';', '(', ')', '\t', '\n', ';', ':']
    num_of_sp_symbols = 0
    for item in text:
        if item in special_symbols:
            num_of_sp_symbols += 1
    return f'Кол-во знаков препинания: {num_of_sp_symbols}'


def var3(some_list):
    some_dict = {}
    for item in some_list:
        some_dict[item[0]] = some_dict[item[0]] + 1 if item[0] in some_dict else 1
    return some_dict


def var4(word_list):
    some_dict = {}
    for item in word_list:
        some_dict[len(item)] = some_dict[len(item)] + 1 if len(item) in some_dict else 1
    return some_dict


def var5(text):
    k = 0
    for item in text:
        if item.isupper():
            k += 1
    return f'Кол-во слов, начинающихся с заглавной буквы: {k}'


def var6(some_lst):
    return f'Кол-во чисел: {len([int(k) for k in some_lst if k.isdigit()])}'


def var7(words_dict):
    list_d = list(words_dict.items())
    list_d.sort(key=lambda i: i[1], reverse=True)
    return f'Самое используемое слово - {list_d[0][0]} - {list_d[0][1]} раз'


def write_file(some_dictionary):
    with open('results.txt', 'w', encoding='UTF-8') as file:
        for i, k in some_dictionary.items():
            file.write(f'Слово "{i}" встречается в тексте {k} раз.\n')


with open('random.txt', 'r', encoding='UTF-8') as file:
    s = file.read()

my_str = ''

for i in s:
    if i.isalpha() or i.isdigit() or i == ' ':
        my_str += i

my_str = my_str.lower()
my_lst = my_str.split(' ')
my_lst = [i for i in my_lst if i != '']

my_dict = {}

for i in my_lst:
    my_dict[i] = my_dict[i] + 1 if i in my_dict else 1

print(var1(my_lst))
print(var2(s))
print(var3(my_lst))
print(var4(my_lst))
print(var5(s))
print(var6(my_lst))
print(var7(my_dict))
print(my_dict)
write_file(my_dict)
