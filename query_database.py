class QueryDatabase():
    def __init__(self, db_id):
        self.db_name = 'database' + str(db_id) + '.txt'
        

    def get_data(self, index):
        with open(self.db_name, 'r') as file:
            for line in file:
                data = line.split(" ")
                if data[0] == str(index): return data[1]
        return ""



def main():
    # only for testing
    query_database = QueryDatabase(0)
    x = query_database.get_data(0)
    print(x)
    
if __name__ == "__main__":
    main()
