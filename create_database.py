

class CreateDatabase():
    def __init__(self, input_file):
        self.input_file = input_file
        self.location = ""

    def create(self):
        print("Creating databases")
        count = 0
        db_file_name = None
        db_file = None
        with open(self.input_file, "r") as file:
            for line in file:
                print(line)
                if count % 1000 == 0:
                    if db_file: db_file.close()
                    value = count // 1000
                    db_file_name = f"database{value}.txt"
                    db_file = open(db_file_name, "a")
                    db_file.write(f"{count} {line}")
                else:
                    db_file.write(f"{count} {line}")
                count += 1
            db_file.close()
                    
                    
def main():
    create_database = CreateDatabase("raw_data.txt.txt")
    create_database.create()
     

if __name__ == "__main__":
    main()
