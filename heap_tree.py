class HTree(object):
    """
    Heap tree
    """
    def __init__(self, sort_key=None):
        self.sort_key = sort_key
        self.a = []

    def __len__(self):
        return len(self.a)

    def exists(self, i):
        return True if i < len(self) else False

    def val(self, i):
        return self.a[i] if self.exists(i) else None

    @staticmethod
    def left(i):
        return 2 * i + 1

    @staticmethod
    def right(i):
        return 2 * i + 2

    @staticmethod
    def parent(i):
        return i / 2

    def push(self, val):
        self.a.append(val)

