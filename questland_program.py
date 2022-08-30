import csv

#Class for handling the items in the game
class Item(object):
    def __init__(self, List):

        self.dictql = {"Name": List[0], "Category": List[1], "Potential": List[2], "Health": List[3], 
                     "Atack": List[4], "Defense": List[5], "Magic": List[6], "Collection": List[7], 
                     "C1": List[8], "C2": List[9], "C3": List[10]}

             
# 7 items of each category (helmet, armor, ...)
# 5 items of each type (magic/attack/def/hp) in collections

myItems = []

#Get the csv file with data and save items to myItems:

with open('questland.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        newItem = Item(row)
        myItems.append(newItem.dictql)
        line_count += 1

    print(f'Processed {line_count} items.')





        
        
        
        
        