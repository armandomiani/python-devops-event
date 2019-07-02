class MyClass():
    def first_method(self, start, end):
        return list(range(start, end))

    def second_method(self):
        return False


class SecondClass():
    def first_method(self):
        return False


if __name__ == '__main__':
    print(MyClass().first_method(1, 11))
