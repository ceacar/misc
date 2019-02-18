import heapq

class HeapImpl:
    def __init__(self, list_input: [int]):
        self.cache_list = list_input
        heapq.heapify(self.cache_list)
        self.length = 0

    def insert(self, num: int):
        heapq.heappush(self.cache_list, num)
        self.length += 1

    def extract_min(self) -> int:
        self.length -= 1
        return heapq.heappop(self.cache_list)

    def extract_max(self) -> int:
        res = self.cache_list[self.length - 1]
        self.length -= 1
        del self.cache_list[self.length - 1]
        return res

    def get_min(self) -> int:
        return self.cache_list[0]

    def get_max(self) -> int:
        return self.cache_list[self.length - 1]

    def get_length(self):
        return self.length


#class MaximumHeap:
#    def __init__(self, list_input: [int]):
#        self.cache_list = list_input
#        heapq.heapify(self.cache_list)
#        self.length = 0
#
#    def insert(self, num: int):
#        self.length += 1
#        heapq.heappush(self.cache_list, -num)
#
#    def extract_max(self) -> int:
#        self.length -= 1
#        res = -heapq.heappop(self.cache_list)
#        return res
#
#    def extract_min(self) -> int:
#        res = self.cache_list[self.length - 1]
#        self.length -= 1
#        del self.cache_list[self.length - 1]
#        return res
#
#    def get_max(self) -> int:
#        return -self.cache_list[0]
#
#    def get_min(self) -> int:
#        return -self.cache_list[self.length - 1]
#
#    def get_length(self) -> int:
#        return self.length

class MedianTracker:
    def __init__(self):
        self.min_heap_list = []
        self.max_heap_list = []
        self.max_heap = HeapImpl(self.max_heap_list)
        self.min_heap = HeapImpl(self.min_heap_list)
        self.median = None

    def track_median(self, num: int) -> int:
        if self.min_heap.get_length() == 0 and self.max_heap.get_length() == 0:
            #initial state
            self.min_heap.insert(num)
            self.median = num
            return self.median

        if self.median <= num:
            self.max_heap.insert(num)
        else:
            self.min_heap.insert(num)

        self.rebalance_two_heaps()
        import pdb

        if self.min_heap.get_length() > self.max_heap.get_length():
            self.median = self.min_heap.get_max()
        elif self.min_heap.get_length() < self.max_heap.get_length():
            self.median = self.max_heap.get_min()
        else:
            return (self.min_heap.get_max() + self.max_heap.get_min())/2

        return self.median

    def rebalance_two_heaps(self):
        length_min_heap = self.min_heap.get_length()
        length_max_heap = self.max_heap.get_length()
        if length_min_heap - length_max_heap > 1:
            self.max_heap.insert(self.min_heap.extract_max())
        elif length_max_heap - length_min_heap > 1:
            self.min_heap.insert(self.max_heap.extract_min())

        print("rebalanced two heap")
        print("min heap", self.min_heap.cache_list)
        print("max heap", self.max_heap.cache_list)
        return



if __name__ == '__main__':
    """
    output should have 
    """
    input_int_list = [1,2,3,18,10,12,15,9,8]
    mt = MedianTracker()
    for i in range(len(input_int_list)):
        print(input_int_list[:i + 1])
        ele = input_int_list[i]
        res = mt.track_median(ele)
        print("median is", res)

