import queue
import sys


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return '{}'.format(self.value)

    def __str__(self):
        return '{}'.format(self.value)

    def is_leaf(self):
        return not self.left and not self.right

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left):
        self._left = left

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right):
        self._right = right

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class LNode(Node):
    def __init__(self, value, left=None, right=None, level=0):
        super(LNode, self).__init__(value, left, right)
        self.level = level

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        self._level = level



def height(root):
    if not root or (not root.left and not root.right):
        return 0

    lh = height(root.left)
    rh = height(root.right)

    return 1 + max(lh, rh)


def level_order_rec(root, res, h):
    if not root:
        return

    if not res.get(h):
        res[h] = []

    res.get(h).append(root)

    level_order_rec(root.left, res, h-1)
    level_order_rec(root.right, res, h-1)


def level_order(root):
    if not root:
        return
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        node = q.get()
        sys.stdout.write('{} '.format(node))
        sys.stdout.flush()
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)
    sys.stdout.write('\n')
    sys.stdout.flush()


def inorder(root, res):
    if not root:
        return
    inorder(root.left, res)
    res.append(root.value)
    inorder(root.right, res)


def inorder_norec(root):
    res = []
    q = []
    n = root
    done = False

    while not done:
        if n is not None:
            q.append(n)
            n = n.left
        else:
            if len(q) > 0:
                n = q.pop()
                res.append(n.value)
                n = n.right
            else:
                done = True

    return res


def swap_children(root):
    tmp = root.left
    root.left = root.right
    root.right = tmp


def swap_kth(root, lvl, k):
    if not root or root.is_leaf():
        return

    if lvl % k == 0:
        swap_children(root)

    swap_kth(root.left, lvl+1, k)
    swap_kth(root.right, lvl+1, k)


def swap_kth_norec(root, k):
    q = [root]
    while len(q) > 0:
        n = q.pop()
        l = n.left
        r = n.right
        if n.level % k == 0:
            swap_children(n)
        if l:
            q = [l] + q
        if r:
            q = [r] + q


def tree_from_array(a):
    root = LNode(1, level=1)
    q = [root]

    while len(a) > 0:
        # pop a node from queue
        n = q.pop()
        # pop node's left and right value
        l, r = a.pop(0)

        if l != -1:
            l = LNode(l, level=n.level+1)
            n.left = l
            q = [l] + q
        if r != -1:
            r = LNode(r, level=n.level+1)
            n.right = r
            q = [r] + q

    return root


def swap_nodes(idxs, ks):
    res = []
    n = tree_from_array(idxs)

    for k in ks:
        # swap_kth(n, 1, k)
        swap_kth_norec(n, k)

        # kres = []
        # inorder(n, kres)
        # res.append(kres)

        res.append(inorder_norec(n))

    return res


def extract_leaves(root):
    res = []
    q = []
    n = root
    visited = []
    done = False

    while not done:
        if n is not None:
            q.append(n)
            n = n.left
        else:
            if len(q) > 0:
                n = q.pop()

                if n.left and n.left.is_leaf() and n.left not in visited:
                    res.append(n.left)
                    n.left = None
                    visited.append(n)
                if n.right and n.right.is_leaf() and n.right not in visited:
                    res.append(n.right)
                    n.right = None
                    visited.append(n)
                n = n.right
            else:
                done = True

    return res



def main():

    n = Node('a', Node('b', Node('c'), Node('d')), Node('e', None, Node('z')))

    # print '{}'.format(n)
    # print 'height: {}'.format(height(n))
    #
    # lvl_order = {}
    # level_order_rec(n, lvl_order, height(n))
    # print 'Level order: {}'.format(lvl_order)
    #
    # level_order(n)

    # a = [2, 3, 4, -1, 5, -1, 6, -1, 7, 8, -1, 9, -1, -1, 10, 11, -1, -1, -1, -1, -1, -1]
    #
    # swap_nodes(a, [2,4])

    # n = tree_from_array(a)
    #
    # res = []
    # inorder(n, res)
    # print '[before] inorder: {}'.format(res)
    #
    # swap_kth(n, 1, 2)
    #
    # res = []
    # inorder(n, res)
    # print '[after] inorder: {}'.format(res)




    idxs = [[2, 3], [4, -1], [5, -1], [6, -1], [7, 8], [-1, 9], [-1, -1], [10, 11], [-1, -1], [-1, -1], [-1, -1]]
    t = tree_from_array(idxs)
    print 'inorder: {}'.format(inorder_norec(t))
    print '{}'.format(extract_leaves(t))
    print 'inorder: {}'.format(inorder_norec(t))




    # queries = [2, 4]
    # print swap_nodes(idxs, queries)



    # idxs = [[2, 3], [-1, -1], [-1, -1]]
    # queries = [1, 1]
    #
    # res = swap_nodes(idxs, queries)
    # print res

    #
    #
    #
    # import urllib2
    # link = 'https://hr-testcases-us-east-1.s3.amazonaws.com/6375/input10.txt?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1554032153&Signature=9QpdX7P6%2BUl4BMNgCEh7OA64jo0%3D&response-content-type=text%2Fplain'
    # f = urllib2.urlopen(link)
    # myfile = f.read()
    # lines = myfile.split('\n')
    # idxs = lines[1:1+int(lines[0])]
    # idxs = [map(int, x.split()) for x in idxs]
    #
    # queries = lines[2 + int(lines[0]):]
    # queries = [int(x) for x in queries]
    #
    # sys.setrecursionlimit(1500)
    # res = swap_nodes(idxs, queries)
    # print res

if __name__ == '__main__':
    main()
