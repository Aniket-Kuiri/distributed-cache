import random
from cache import Cache
import bisect
class ConsistentHashing():
    def __init__(self, num_caches, dup_factor, num_keys):
        self.num_caches = num_caches
        self.dup_factor = dup_factor
        self.num_keys = num_keys
        self.num_instances = self.num_caches * self.dup_factor
        self.cache_obj = Cache(self.num_caches, self.num_keys)
        self.cache_obj.build_cache()
        self.cache_instance_list = {i: 0 for i in range(self.num_caches)}
        self.hash_table = []
        self.cache_allocation = []

    def get_rand_cache_id(self):
        return random.randint(0, self.num_caches - 1)
        

    def get_cache_instance_list(self):
        rand_cache_id = -1
        while(True):
            rand_cache_id = self.get_rand_cache_id()
            if self.cache_instance_list[rand_cache_id] == self.dup_factor:
                continue
            if len(self.cache_allocation) == 0:
                self.cache_instance_list[rand_cache_id] += 1
                self.cache_allocation.append(rand_cache_id)
                break
            if rand_cache_id != self.cache_allocation[-1]:
                self.cache_instance_list[rand_cache_id] += 1
                self.cache_allocation.append(rand_cache_id)
                break
        return rand_cache_id

    def build_hash_table(self):
        gap = self.num_keys // self.num_instances
        i = 0
        while (i < self.num_keys):
            self.hash_table.append([i, self.get_cache_instance_list()])
            i = i + gap
            #print("hashtable: "+ str(self.hash_table))
        print("hashtable: "+ str(self.hash_table))

    def get_cache_id(self, key):
        length = len(self.hash_table)
        lower , upper = 0, length - 1
        while( lower < upper ):
            mid = (lower + upper) // 2
            if self.hash_table[mid][0] < key: lower = mid + 1
            elif self.hash_table[mid][0] >= key: upper = mid
        if lower == length:
            print("query cache: "+str(self.hash_table[0][1]))
            return self.hash_table[0][1]
        elif lower == upper:
            print("query cache: "+str(self.hash_table[lower][1]))
            return self.hash_table[lower][1]
        return self.hash_table[0][1]
        # need to add state and if state is not healthy we move to next cache
        # in line
        

    def get_data(self, key):
        cache_id = self.get_cache_id(key)
        v = self.cache_obj.get_data(cache_id, key)
        return v


def main():
    consistent_hashing = ConsistentHashing(5, 4, 10000)
    consistent_hashing.build_hash_table()
    x = consistent_hashing.get_data(3459)
    print(x)
    x = consistent_hashing.get_data(1234)
    print(x)
    x = consistent_hashing.get_data(1234)
    print(x)

if __name__ == "__main__":
    main()

    
        
