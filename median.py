import bisect
import random
import time
import heapq


# insertion sort method - sucks
def running_med(a):
    l = []
    m = []
    r = []

    for n in a:

        # insert a value
        if len(m) == 0 or min(m) <= n <= max(m):
            m.append(n)
        elif n > max(m):
            bisect.insort(r, n)
        else:
            bisect.insort(l, n)

        if len(m) == 1:
            if not len(l) == len(r) == 0:
                if len(l) > len(r):
                    m.insert(0, l.pop(len(l) - 1))
                else:
                    m.append(r.pop(0))
        elif len(m) == 2:
            if len(l) > len(r):
                r.insert(0, m.pop(1))
            else:
                l.append(m.pop(0))
        else:
            l.append(m.pop(0))
            r.insert(0, m.pop(1))

        med = round(float(sum(m))/float(len(m)), 1)

        # print the median
        print 'adding {}. l={}, m={}, r={}, median={}'.format(n, l, m, r, med)


# min-heap and max-heap method - cool
def median_heaps(a):
    l = []
    r = []
    m = 0

    for n in a:
        if len(l) > len(r):
            if n < m:
                heapq.heappush(r, abs(heapq.heappop(l)))
                heapq.heappush(l, -n)
            else:
                heapq.heappush(r, n)
            m = float((abs(l[0]) + r[0])) / 2
        elif len(r) > len(l):
            if n > m:
                heapq.heappush(l, -heapq.heappop(r))
                heapq.heappush(r, n)
            else:
                heapq.heappush(l, -n)
            m = float((abs(l[0]) + r[0])) / 2
        else:
            if n < m:
                heapq.heappush(l, -n)
                m = abs(l[0])
            else:
                heapq.heappush(r, n)
                m = r[0]
        yield float(m)


def main():
    n = 10
    a = [random.choice(range(20)) for _ in range(n)]

    t0 = time.time()
    # running_med(a)
    median_heaps(a)
    dt = time.time() - t0

    print 'took {:.3f} sec'.format(dt)


if __name__ == '__main__':
    main()
