import math

class HTree(object):
    def __init__(self, a):
        self._h = {1: [0]}
        self._d = {0: 1}
        i = 0

        for n in range(0, len(a), 2):
            last = self._d.keys()[i]
            h = 1 + self.node_height(last * 2 + 1)

            if a[n] != -1:
                self._d[last * 2 + 1] = a[n]
                if not self._h.get(h):
                    self._h[h] = []
                self._h[h].append(last * 2 + 1)

            if a[n + 1] != -1:
                self._d[last * 2 + 2] = a[n + 1]
                if not self._h.get(h):
                    self._h[h] = []
                self._h[h].append(last * 2 + 2)

            i += 1

    def __repr__(self):
        return '{}'.format(self._d)

    def __len__(self):
        return len(self._d.keys())

    def exists(self, i):
        # return i in self._d.keys()
        return i in self._d.keys() and self._d[i] != -1

    def get_inorder_list(self, i, res):
        print 'entered: {}({})'.format(i, self.get_val(i))
        if not self.exists(i):
            return
        self.get_inorder_list(self.left(i), res)
        res.append(self.get_val(i))
        print 'appending: {}({})'.format(i, self.get_val(i))
        self.get_inorder_list(self.right(i), res)

    def get_val(self, i):
        return self._d.get(i, -1)

    def set(self, i, val):
        if val == -1:
            if self._d.get(i):
                del self._d[i]
        else:
            self._d[i] = val

    @staticmethod
    def left(i):
        return 2*i + 1

    @staticmethod
    def right(i):
        return 2*i + 2

    def swap_children(self, i):
        tmp_val = self.get_val(self.left(i))
        self.set(self.left(i), self.get_val(self.right(i)))
        self.set(self.right(i), tmp_val)

    @staticmethod
    def node_height(i):
        return int(math.log(i+1, 2))

    def height(self):
        return max(self._h.keys())

    def swap_kth(self, k):
        # print 'node indexes in height {}: {}'.format(k, self._h[k])
        for i in self._h[k]:
            # print 'swapping children for height {} index {}({})'.format(k, i, self.get_val(i))
            self.swap_children(i)

    def swap(self, ks):
        res = []
        for k in ks:
            for i in range(1, self.height()):
                if i % k == 0:
                    print 'swapping height: {}'.format(i)
                    self.swap_kth(i)
                    print 'd = {}'.format(self._d)
            k_res = []
            self.get_inorder_list(0, k_res)
            print 'inorder = {}'.format(k_res)
            res.append(k_res)
        return res


def main():
    # a = random.sample(range(1, 50), 10)
    a = [2, 3, 4, -1, 5, -1, 6, -1, 7, 8, -1, 9, -1, -1, 10, 11, -1, -1, -1, -1, -1, -1]
    t = HTree(a)
    res = []
    t.get_inorder_list(0, res)

    print 'd = {}'.format(t._d)
    # print 'h = {}'.format(t._h)
    print 'inorder = {}'.format(res)


    # t.swap_kth(2)
    res = t.swap([2, 4])


    # res = []
    # t.get_inorder_list(0, res)
    # print 'd = {}'.format(t._d)
    # print 'h = {}'.format(t._h)



if __name__ == '__main__':
    main()