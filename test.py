from typing import Callable


class Father:
    def __init__(self, choose_dir: str):
        print(choose_dir)
        self.choose_dir = choose_dir

    def choose(self, val):
        print(val)


class Son(Father):
    def __init__(self, d):
        super().__init__(d)

    def execute(self):
        f = Father("ddd")

def swap():
    pass

if __name__ == '__main__':
    son = Son('dd')
    son.choose('a')
    print(type(swap))
    print(isinstance(son, Son))
    print(isinstance(swap, Callable))
    print(isinstance(son.choose, Callable))
    print(callable(son.choose))

    print(type(son))
    print(type(Son))
    print(type(type))
