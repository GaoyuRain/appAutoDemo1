"""
author :Rain
Date : 2019/08/03
Description :
"""


def prac01():
    try:
        a = 1 / 0
    except ZeroDivisionError as e:
        print(e)
        raise e
    finally:
        print('finally')


if __name__ == '__main__':
    prac01()