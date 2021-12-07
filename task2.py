class MyZeroDivisionError(ZeroDivisionError):
    def __init__(self, txt):
        self.txt = txt


if __name__ == '__main__':
    try:
        number = int(input('Введите делитель: '))
        if number == 0:
            raise MyZeroDivisionError('На ноль делить нельзя!')
    except MyZeroDivisionError as el:
        print(el)
    else:
        result = 1 / number
        print(result)