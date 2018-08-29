def hello(f):
    def greeting():
        print("^___^")
        f()
        print("ㅠㅠ")
    return greeting

@hello
def korean():
    print("안녕하세요")

korean()
# a = hello(korean)
# a()