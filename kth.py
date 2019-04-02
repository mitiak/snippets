# amcat
# 23280720684104

# 23280666189043

import heapq
import random


class TopK(object):
    def __init__(self):
        self._data = {}

    def update_data(self, arr):
        for val in arr:
            self._data[val] = 1 + self._data[val] if val in self._data else 1

    def _build_min_heap(self):
        h = []
        for val, freq in self._data.iteritems():
            heapq.heappush(h, (-freq, val))

        return h

    def get_top_k(self, k):
        topk = []
        h = self._build_min_heap()
        for _ in range(min(k, len(h))):
            topk.append(heapq.heappop(h)[1])

        return topk

    def print_data(self):
        print 'data: {}'.format(self._data)


# deprecated
class TopKOLD(object):
    def __init__(self):
        self.top = []
        self.top_max_size = k
        self.frequencies = {}
        self.dfrequencies = {}

    def __len__(self):
        return len(self.top)

    def update_dist_freq(self, val):
        new_freq = self.freq(val)
        old_freq = new_freq - 1

        # add new freq
        if new_freq in self.dfrequencies:
            heapq.heappush(self.dfrequencies[new_freq], val)
        else:
            self.dfrequencies[new_freq] = [val]

        # delete old freq
        if old_freq:
            if len(self.dfrequencies[old_freq]) == 1:
                del self.dfrequencies[old_freq]
            else:
                self.dfrequencies[old_freq].remove(val)
                heapq.heapify(self.dfrequencies[old_freq])

    def update_freq(self, val):
        if val in self.frequencies.keys():
            self.frequencies[val] += 1
        else:
            self.frequencies[val] = 1

    def freq(self, val):
        return self.frequencies.get(val, 0)

    def top_min(self):
        return self.top[0]

    def is_top_full(self):
        return len(self) == self.top_max_size

    def top_sort(self):
        self.top = sorted(self.top, key=lambda x: (self.freq(x), x))

    def top_push(self, val):
        if val not in self.top:
            self.top.append(val)

    def is_top_contains(self, val):
        return val in self.top

    def top_remove_min(self):
        self.top.pop(0)

    def is_top_candidate(self, val):
        if not self.is_top_full():
            return True
        else:
            # Top is full. Need to check the frequencies
            if self.freq(val) > self.freq(self.top_min()):
                return True
            elif self.freq(val) == self.freq(self.top_min()):
                if val <= self.top_min():
                    return True
        return False

    def update_k_max(self, a):
        for val in a:
            self.update_freq(val)
            self.update_dist_freq(val)

            # if not self.is_top_candidate(val):
            #     continue
            #
            # if not self.is_top_contains(val):
            #     if self.is_top_full():
            #         self.top_remove_min()
            #     self.top_push(val)
            # self.top_sort()

    def get_top(self):
        return self.top

    def get_kth_freq(self, k):
        if k > len(self):
            return 0
        else:
            return self.top[len(self) - k]

    def get_kth_freq_distinct(self, k):
        freqs = sorted(self.dfrequencies.keys(), reverse=True)

        if k > len(freqs):
            return 0
        else:
            return self.dfrequencies[freqs[k - 1]][0]


if __name__ == '__main__':
    a = [random.choice(range(10)) for _ in range(30)]
    print 'input: {}'.format(a)

    t = TopK()
    t.update_data(a)
    t.print_data()
    print 'top k: {}'.format(t.get_top_k(5))
