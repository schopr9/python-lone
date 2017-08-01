"S is an integer store object"


class S:
    "integer store object"

    def __init__(self):
        "initialization"
        self.int_obj = []

    def create_object(self, inp):
        "create object"
        if isinstance(inp, int):
            self.int_obj.append(inp)
        else:
            raise "input is not integer"

    def empty_object(self):
        "check object"
        return len(self.int_obj) == 0

    def list_object(self):
        "list object"
        return self.int_obj

a = S()
a.create_object(5)
a.create_object(9)
a.create_object(10)
print a
print a.empty_object()
print a.list_object()
