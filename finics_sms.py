def decode_message(s, dictionary):
    # Сопоставление цифр буквам
    digit_to_letters = {
        '2': 'ABC',
        '3': 'DEF',
        '4': 'GHI',
        '5': 'JKL',
        '6': 'MNO',
        '7': 'PQRS',
        '8': 'TUV',
        '9': 'WXYZ'
    }

    # Преобразуем цифровую строку в буквенную
    letters = []
    i = 0
    n = len(s)
    while i < n:
        current_digit = s[i]
        count = 1
        while i + count < n and s[i + count] == current_digit:
            count += 1
        letters_group = digit_to_letters[current_digit]
        # Определяем букву: count ударов -> (count-1) индекс в letters_group
        letter = letters_group[min(count - 1, len(letters_group) - 1)]
        letters.append(letter)
        i += count
    letter_sequence = ''.join(letters)

    # Создаем префиксное дерево (Trie) для словаря
    trie = {}
    for word in dictionary:
        node = trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['#'] = word  # Маркер конца слова

    # Разбиваем буквенную строку на слова из словаря
    words = []
    current_pos = 0
    n_letters = len(letter_sequence)

    while current_pos < n_letters:
        node = trie
        end_pos = current_pos
        last_word = None
        # Ищем самое длинное слово, начиная с current_pos
        while end_pos < n_letters and letter_sequence[end_pos] in node:
            node = node[letter_sequence[end_pos]]
            end_pos += 1
            if '#' in node:
                last_word = node['#']
        if last_word is not None:
            words.append(last_word)
            current_pos += len(last_word)
        else:
            # По условию задачи разбиение существует, так что сюда не попадем
            pass

    return ' '.join(words)


# Чтение ввода
s = input().strip()
n = int(input())
dictionary = [input().strip() for _ in range(n)]

# Декодируем сообщение
print(decode_message(s, dictionary))