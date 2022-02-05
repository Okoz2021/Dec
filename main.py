from dec import parametrized_decor, decorator


@decorator
@parametrized_decor('logs.txt')
def summator(a, b, c):
    return a + b + c

f = summator(2, 4, 5)
