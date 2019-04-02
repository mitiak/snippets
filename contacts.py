class CNode(object):
    def __init__(self, val):
        self.val = val
        self.children = dict()
        self.score = 0


class Contacts(object):
    def __init__(self):
        self.contacts = CNode(None)

    def __len__(self):
        return self.contacts.score

    def add(self, name):
        root = self.contacts
        root.score += 1
        for i in name:
            if i not in root.children:
                root.children[i] = CNode(i)
            root = root.children[i]
            root.score += 1

    def find(self, name_part):
        if len(self) == 0:
            return 0

        root = self.contacts
        for i in name_part:
            if i not in root.children:
                return 0
            root = root.children[i]
        return root.score


def contacts(queries):
    c = {
        'val': None,
        'children': dict(),
        'score': 0
    }

    for q in queries:
        cmd = q[0]
        param = q[1]

        if cmd == 'add':
            name = param
            root = c
            root['score'] += 1
            for i in name:
                if i not in root['children']:
                    root['children'][i] = {
                        'val': i,
                        'children': dict(),
                        'score': 0
                    }
                root = root['children'][i]
                root['score'] += 1

        elif cmd == 'find':
            part = param
            root = c
            res = 0
            for i in part:
                if i not in root['children']:
                    res = 0
                    break
                else:
                    root = root['children'][i]
                    res = root['score']
            yield res









def main():
    c = Contacts()
    names = ['david', 'dasha', 'darth', 'dad', 'abc']
    parts = ['d', 'das', 'dad', 'a', 'vas']

    # print names
    print 'names: {}'.format(names)

    # add names
    for name in names:
        c.add(name)

    # find names by parts
    for part in parts:
        print 'found {} contacts matching {}'\
            .format(c.find(part), part)


if __name__ == '__main__':
    main()
