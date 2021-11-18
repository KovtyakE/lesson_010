# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


class RegistrationCheck:
    def __init__(self, input_file, good_output_file, bad_output_file):
        self.file = input_file
        self.good_log = good_output_file
        self.bad_log = bad_output_file
        self.string_of_errors = ''

    def name_check(self, name):
        if name.isalpha():
            return True
        else:
            return False

    def email_check(self, email):
        if '.' in email and '@' in email:
            return True
        else:
            return False

    def age_check(self, age):
        if int(age) in range(10, 100):
            return True
        else:
            return False

    def line_check(self, line_to_check):
        name, email, age = line_to_check.split(' ')
        if not self.name_check(name):
            raise NotNameError('name is incorrect')
        elif not self.email_check(email):
            raise NotEmailError('e-mail is incorrect')
        elif not self.age_check(age):
            raise ValueError('wrong age number')

    def file_check(self):
        file_to_check = open(file=self.file, mode='r', encoding='utf8')
        good_log = open(file=self.good_log, mode='w', encoding='utf8')
        bad_log = open(file=self.bad_log, mode='w', encoding='utf8')
        for line in file_to_check:
            try:
                self.line_check(line)
            except ValueError as exc:
                if 'unpack' in exc.args[0]:
                    bad_log.write(f'Line: |{line[:-1]}|, ValueError: {exc}\n')
                elif 'wrong age number' in exc.args[0]:
                    bad_log.write(f'Line: |{line[:-1]}|, ValueError: {exc} (expected 10-99)\n')
            except NotNameError as exc:
                bad_log.write(f'Line: |{line[:-1]}|, NotNameError: {exc}\n')
            except NotEmailError as exc:
                bad_log.write(f'Line: |{line[:-1]}|, NotEmailError: {exc}\n')
            except Exception as exc:
                print(f'Something wrong with {line[:-1]}, {exc}, you must do something')
            else:
                good_log.write(line)
        file_to_check.close()
        good_log.close()
        bad_log.close()


reg_check = RegistrationCheck(input_file='registrations.txt', good_output_file='good_log.txt',
                              bad_output_file='bad_log.txt')
reg_check.file_check()
