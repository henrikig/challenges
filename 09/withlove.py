class Writer:
    def __init__(self, name):
        self.name = name
        self.level = 0

    def __enter__(self):
        self.level += 1
        self.file = open(self.name, 'a')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

    def writing(self, text):
        with Writer(self.name) as f:
            f.write('   '*self.level + text)


if __name__ == "__main__":
    my_class = Writer("hello.txt")
    my_class.writing("hello\n")
    my_class.writing("hello\n")
    my_class.writing("hello\n")
    my_class.writing("hello\n")
    my_class.writing("hello\n")
