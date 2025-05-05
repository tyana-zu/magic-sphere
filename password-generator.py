import random
import time

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"

chars = ''

has_digits = False
has_lowercase = False
has_uppercase = False
has_punct = False

# описание функций


def check_input(answer):
    return answer.strip().isdigit()

def ask_and_add_symbols(prompt, symbols, chars):
    while True:
        print(prompt)
        answer = input()
        if answer.strip().lower() == "да":
            chars += symbols
            return chars, True
        elif answer.strip().lower() == "нет":
            return chars, False
        else:
            print('Пожалуйста, введи "да" или "нет".')

def check_strong(password):
    if has_digits and not any(c in digits for c in password):
        return False
    if has_uppercase and not any(c in uppercase_letters for c in password):
        return False
    if has_lowercase and not any(c in lowercase_letters for c in password):
        return False
    if has_punct and not any(c in punctuation for c in password):
        return False
    return True


def generate_password(chars, length):
    while True:
        password = ''.join(random.sample(chars, length))
        if check_strong(password):
            print(password)
            break


# основная программа

print("Привет! Я генератор паролей - могу сгенерировать тебе надёжные пароли.")
time.sleep(2)
print("Сначала я задам тебе несколько вопросов.")
time.sleep(1)

print("Сколько паролей ты хочешь получить? Введи число.")

while True:
    answer = input()
    if check_input(answer):
        number = int(answer)
        break
    else:
        print("Пожалуйста, введи число.")

time.sleep(1)

print("Какой длины должны быть пароли? Введи число.")

while True:
    answer = input()
    if check_input(answer):
        length = int(answer)
        break
    else:
        print("Пожалуйста, введи число.")

time.sleep(1)

chars, has_digits = ask_and_add_symbols('Должен ли пароль содержать цифры - 0123456789? Введи "да" или "нет".', digits, chars)

time.sleep(1)

chars, has_uppercase = ask_and_add_symbols('Должен ли пароль содержать прописные буквы - ABCDEFGHIJKLMNOPQRSTUVWXYZ? Введи "да" или "нет".', uppercase_letters, chars)

time.sleep(1)

chars, has_lowercase = ask_and_add_symbols('Должен ли пароль содержать строчные буквы - abcdefghijklmnopqrstuvwxyz? Введи "да" или "нет".', lowercase_letters, chars)

time.sleep(1)

chars, has_punct = ask_and_add_symbols('Должен ли пароль содержать символы - !#$%&*+-=?@^_? Введи "да" или "нет".', punctuation, chars)

time.sleep(1)

if not chars:
    print("Ошибка: ты не выбрал ни одного типа символов. Генерация невозможна.")
    exit()

print("Отлично! Я получил всю необходимую информацию.")
print("Начинаю генерацию паролей...")
time.sleep(3)


for _ in range(number):
    generate_password(chars, length)
    time.sleep(1)

print("Пароли сгенерированы!")