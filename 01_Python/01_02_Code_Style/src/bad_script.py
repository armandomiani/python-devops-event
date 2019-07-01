class myclass():
    def myFirstAndLongMethodNameIsNotThatBad(this, s, e):
        return list(range(s, e))
    def mySecondMethod(this):
        return False

class mySecondClass():
    def myFirstMethod(this):
        return False

if __name__ == '__main__':
    variableNameShouldBeSnakeCased = myclass().myFirstAndLongMethodNameIsNotThatBad(1,11)
    print(variableNameShouldBeSnakeCased)