# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.


from random import randint

ENLIGHTENMENT_CARMA_LEVEL = 777


class IAmGodError(Exception):
    def __str__(self):
        return ' IAmGodError: He is got crazy again...'


class DrunkError(Exception):
    def __str__(self):
        return 'DrunkError: He is drunken...'


class CarCrashError(Exception):
    def __str__(self):
        return 'CarCrashError: He is crashed by car...'


class GluttonyError(Exception):
    def __str__(self):
        return 'GluttonyError: No, he is not drunken... he is glutted...'


class DepressionError(Exception):
    def __str__(self):
        return 'DepressionError: He is in depression...'


class SuicideError(Exception):
    def __str__(self):
        return 'SuicideError: He is committed suicide...'


def one_day():
    day = 0
    carma = 0
    log_file = open(file='groundhog_log.txt', mode='w', encoding='utf8')
    while carma < ENLIGHTENMENT_CARMA_LEVEL:
        try:
            day += 1
            carma += randint(1, 7)
            log_file.write(f'Day {day}:')
            if carma >= 777:
                break
            dice = randint(1, 13)
            if dice == 1:
                raise IAmGodError
            elif dice == 2:
                raise DrunkError
            elif dice == 3:
                raise CarCrashError
            elif dice == 4:
                raise GluttonyError
            elif dice == 5:
                raise DepressionError
            elif dice == 6:
                raise SuicideError
            else:
                log_file.write('Today there is nothing happened\n')
        except IAmGodError as exc:
            log_file.write(f'{exc}\n')
        except DrunkError as exc:
            log_file.write(f'{exc}\n')
        except CarCrashError as exc:
            log_file.write(f'{exc}\n')
        except GluttonyError as exc:
            log_file.write(f'{exc}\n')
        except DepressionError as exc:
            log_file.write(f'{exc}\n')
        except SuicideError as exc:
            log_file.write(f'{exc}\n')
    log_file.write('Groundhog day is over!!!')
    log_file.close()
    with open(file='groundhog_log.txt', mode='r', encoding='utf8') as file:
        for line in file:
            print(line, end='')


one_day()
