import csv

# A class to load the gear items from a file and save them in a list of dictionaries
class ItemLoader:
    def __init__(self, file_name):
        self.file_name = file_name
        self.headers = []
        self.items = []
        self.load_items()
    
    def load_items(self):
        with open(self.file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            item_count = 0
            for row in csv_reader:
                if item_count == 0:
                    self.headers = row
                else:                
                    self.items.append(self.create_item(row))
                item_count += 1
            print(f'Processed {item_count} items.')
            
    def create_item(self, row):
        item = {}
        for i in range(len(row)):
            item[self.headers[i]] = row[i]
        return item