# Матрица первоначальной подготовки ключа
CP_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

# Матрица завершающей обработки ключа
CP_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]

# Матрица сдвигов для вычисления ключа
SHIFT = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# Матрица начальной перестановки IP
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]
# Матрица обратной перестановки IP(-1)
IP_1 = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]
# Матрица расширения
E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

# S-боксы
S_BOX = [

    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
     ],

    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
     ],

    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
     ],

    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
     ],

    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
     ],

    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
     ],

    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
     ],

    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
     ]
]

# P-бокс
P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]


# Функция добавления пустых байт, если сообщение не кратно 64 бит
def padding(data):
    while len(data) % 8 != 0:
        data += b' '
    return data


# Функция перобразования массива байт в массив бит
def byte_to_bit(data_byte):
    bit_array = []
    for byte in data_byte:
        l = list("{0:08b}".format(byte))
        for i in range(len(l)):
            bit_array.append(int(l[i]))
    return bit_array


# Функция перобразования массива бит в массив символов
def bit_to_char(data_bit):
    char_array = []
    data_bit = [str(data_bit[i]) for i in range(len(data_bit))]
    for i in range(len(data_bit) // 8):
        char_array.append(chr(int(''.join(data_bit[8 * i:8 * (i + 1)]), 2)))
    return char_array


# Функция разделения массива на 2 массива длинной n
def nsplit(s, n):
    return [s[k:k + n] for k in range(0, len(s), n)]


# Функция сложения по модулю 2
def xor(t1, t2):
    return [x ^ y for x, y in zip(t1, t2)]


# Функция перестановки
def permut(block, table):
    return [block[x - 1] for x in table]


# Функции подстановки
def substitute(R):
    subblocks = nsplit(R, 6)
    res = []
    for i in range(8):
        block = subblocks[i]
        row = int(str(block[0]) + str(block[5]), 2)  # номер строки по первому и последнему биту
        column = int(''.join([str(x) for x in block[1:][:-1]]), 2)  # номер столбца 2,3,4 и 5 битам
        val = S_BOX[i][row][column]  # значение из S-бокса
        l = list("{0:04b}".format(val))
        for i in range(len(l)):
            res.append(int(l[i]))
    return res


# Функция генерации подключей
def generate_keys(key):
    keys = []
    key_bit = byte_to_bit(key)
    key_bit = permut(key_bit, CP_1)
    g, d = nsplit(key_bit, 28)
    for i in range(16):
        g, d = g[SHIFT[i]:] + g[:SHIFT[i]], d[SHIFT[i]:] + d[:SHIFT[i]]
        temp = g + d
        keys.append(permut(temp, CP_2))
    return keys


# Функция шифрования
def encrypt(data_bit, keys):
    encrypt_data = []
    for block in range(0, len(data_bit) // 64):
        temp = data_bit[64 * block:64 * (block + 1)]
        # Начальная перестановка
        temp = permut(temp, IP)
        # Цикл шифрования
        L, R = nsplit(temp, 32)  # разделение блока на подблоки L0 и R0
        for i in range(16):
            temp = permut(R, E)  # расширение 32-битового блока до 48 бит
            temp = xor(temp, keys[i])  # сложение по модулю 2 подблока с подключом
            temp = substitute(temp)  # подстановка S
            temp = permut(temp, P)  # перестановка P
            temp = xor(temp, L)
            L = R  # L[i] = R[i-1]
            R = temp  # R[i] = L[i-1] XOR f(R[i-1], keys[i])
        # Конечная перестановка
        encrypt_data += permut(L + R, IP_1)
    return encrypt_data


# Функция шифрования
def decrypt(data_bit, keys):
    decrypt_data = []
    for block in range(0, len(data_bit) // 64):
        temp = data_bit[64 * block:64 * (block + 1)]
        # Начальная перестановка
        temp = permut(temp, IP)
        # Цикл шифрования
        L, R = nsplit(temp, 32)  # разделение блока на подблоки L0 и R0
        for i in range(16):
            temp = permut(L, E)  # расширение 32-битового блока до 48 бит
            temp = xor(temp, keys[15 - i])  # сложение по модулю 2 подблока с подключом
            temp = substitute(temp)  # подстановка S
            temp = permut(temp, P)  # перестановка P
            temp = xor(temp, R)
            R = L  # L[i] = R[i-1]
            L = temp  # R[i] = L[i-1] XOR f(R[i-1], keys[i])
        # Конечная перестановка
        decrypt_data += permut(L + R, IP_1)
    return decrypt_data


# Ввод сообщения для шифрования
data = input('Введите любой набор символов: ').encode()
data_padding = padding(data)
data_bit = byte_to_bit(data_padding)

# Ввод ключа с проверкой длинны в 8 символов
while True:
    key = input('Введите пароль: ').encode()
    if len(key) == 8:
        break
    else:
        print('Пароль должен быть минимум из 8 символов!')

keys = generate_keys(key)

data_enc = encrypt(data_bit, keys)
print('Зашифрованный текст: ' + ''.join(bit_to_char(data_enc)))

data_dec = decrypt(data_enc, keys)
print('Расшифрованный текст: ' + ''.join(bit_to_char(data_dec)))