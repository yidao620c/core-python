class Father:
    def __init__(self, choose_dir: str):
        print(choose_dir)
        self.choose_dir = choose_dir


class Son:
    def execute(self):
        f = Father("ddd")

if __name__ == '__main__':
    son = Son()
    son.execute()
    print(222)