import sys


class LeastRecentUsedCache():

    cache = {}
    lru = []
    max_size = 0

    def __init__(self, max_size = 0):
        self.max_size = max_size

    def get(self, key):
        """
        retrieve content
        update lru(swap order)
        """

        if key in self.cache:
            self.update_lru(key)
            return self.cache[key]

        return None

    def set(self, key, value):
        """
        set cache
        update lru
        """
        #if new key value pair insert into cache, need to check the length first
        if key not in self.cache and len(self.lru) >= self.max_size:
            self.drop_leaset_used_cache()

        self.update_lru(key)
        self.cache[key] = value

    def swap_key_to_lru_first(self, key):
        index_key = self.lru.index(key)
        self.lru.pop(index_key)
        self.lru.append(key)

    def update_lru(self, key):
        """
        move key to the top
        """
        if key in self.lru:
            self.swap_key_to_lru_first(key)

        if key not in self.lru:
            self.lru.append(key)

    def drop_leaset_used_cache(self):
        """
        drops first element
        """
        key_to_drop = self.lru.pop(0)
        del self.cache[key_to_drop]



if __name__ == '__main__':
    #in python list appends right ways, so lru will looked reversed
    #it will pop first element instead of last
    lru = LeastRecentUsedCache(max_size=3)
    lru.set("a", 1)
    lru.set("b", 2)
    lru.set("c", 3)
    #[a,b,c]
    lru.set('d',4)
    #[b,c,d] <-- first element is poped
    print('popped frist element', lru.lru)
    lru.get('b')
    #[c,d,b]
    print('final_cache', lru.lru)
    assert lru.lru == ['c', 'd', 'b']




