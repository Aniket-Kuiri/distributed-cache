#from ..database.query_database import QueryDatabase

from query_database import QueryDatabase


class Cache():
    def __init__(self, count_cache, key_count):
        self.count_cache = count_cache
        self.key_count = key_count

    def build_cache(self):
        self.cache_list = []
        self.cache_capacity = self.key_count // self.count_cache
        for i in range(self.count_cache):
            data = []
            for j in range(self.cache_capacity):
                data.append(None)
            self.cache_list.append(data)

    def get_data(self, cache_id, key):
        position = key % self.cache_capacity
        data = self.cache_list[cache_id][position]
        if data is None:
            self.cache_list[cache_id][position] = self.add_data(cache_id, key)
        elif data[0] != key:
            self.cache_list[cache_id][position] = self.add_data(cache_id, key)
        return self.cache_list[cache_id][position]
        
    def add_data(self, cache_id, key):
        print(f"Getting from database for key {key}. Not stored in cache")
        query_database = QueryDatabase(key // 1000)
        value = query_database.get_data(key)
        return (key, value)




def main():
    cache = Cache(5, 10000)
    cache.build_cache()
    x = cache.get_data(3, 3500)
    print(x)
    x = cache.get_data(3, 3500)
    print(x)


if __name__ == "__main__":
    main()
