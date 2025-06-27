class myclass:
    __privateV=27;
    def __privmeth(self):
        print("I'm inside class myclass")

    def hello(self):
        print("private variable value: ", myclass.__privateV)


foo=myclass()
foo.hello()
foo.__privmeth