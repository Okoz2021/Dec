from datetime import datetime

def decorator(old_f):
    def new_f(*args, **kwargs):
        print(f'Вызвана функция {old_f.__name__}, с аргументами {args}, {kwargs}')
        result = old_f(*args, **kwargs)
        print(f'Итог {result}')
        return result
    return new_f


def parametrized_decor(path):
    def decorator(old_f):
        def new_f(*args, **kwargs):
            with open('logs.txt', 'w', encoding='utf-8') as file:
                t = str(datetime.now())
                result = old_f(*args,)
                string = f'функция {old_f.__name__}, вызвана в {t}, с следующими аргументами {args},'\
                f'результат работы функции равен {result}'
                file.write(string)
                return result
        return new_f
    return decorator

