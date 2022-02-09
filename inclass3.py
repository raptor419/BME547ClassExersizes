def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return (a/abs(a))*float('inf')


def main():
    divide(2,0)


if __name__=="__main__":
    main()
