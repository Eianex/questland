import time

from utils.item_loader import ItemLoader
from utils.gear_loader import GearLoader

# Find best combination of items in the configuration: 7 items in gear + 20 in collection.
# Items have three Links: Link1, Link2, Link3. The names of the items they link to.
# Item only needs 2 links present in configuration for being connected and give extra power.

# Load the items from a file using the ItemLoader class.
itemReceiver = ItemLoader('data/ItemDataReduced.csv')
# Save each item as a dictionary in a big list of items (list of dictionaries).
items = itemReceiver.items
# Initialize the gear, set up the maximum potential attack gear for each slot using the GearLoader class.
gearReceiver = GearLoader(items)
# Save the gear in a dictionary. The keys are the slots and the values are the items (dictionaries too).
gear = gearReceiver.gear
# Delete the already equipped gear from the items list
for item in gear.values(): items.remove(item)

types = ['ATTACK', 'DEFENCE', 'HEALTH', 'MAGIC']                                # 4 types of items.
slots = ['HELM', 'CHEST', 'GLOVES', 'BOOTS', 'RING', 'NECKLACE', 'TALISMAN']    # 7 slot gear categories.

# Initialize the collection empty for now, five items per type. Key names follow: 'ATTACK1', 'DEFENCE1', etc.
collection = {
    'ATTACK1': {},     'ATTACK2': {},     'ATTACK3': {},     'ATTACK4': {},     'ATTACK5': {},
    'DEFENSE1': {},    'DEFENSE2': {},    'DEFENSE3': {},    'DEFENSE4': {},    'DEFENSE5': {},
    'HEALTH1': {},     'HEALTH2': {},     'HEALTH3': {},     'HEALTH4': {},     'HEALTH5': {},
    'MAGIC1': {},      'MAGIC2': {},      'MAGIC3': {},      'MAGIC4': {},      'MAGIC5': {}
              }

# Function to print equipped items
def print_hero(gear, collection):
    print('Gear:')
    for slot in gear.keys():
        print(slot, gear[slot]['Name'])
    print('')
    print('Collection:')
    for item in collection.values():
        for type1 in types:
            if item != {} and item['Type'] == type1:
                print(type1, item['Name'])
    
# Function to merge both dictionaries (gear and collection) into one dictionary
def merge_dicts(gear, collection):
    merged_dict = {}
    for slot in slots:
        merged_dict[slot] = gear[slot]
    for key, value in collection.items():
        merged_dict[key] = value
    return merged_dict

# Function gets item (dictionary) from items provided its name
def get_item_by_name(name, items):
    for item in items:
        if item['Name'] == name:
            return item

# Function that returns a list of names of items in the gear and collection
def get_gear_names(gear, collection):
    gear_names = []
    for item in gear.values():
        if item != {}:
            gear_names.append(item['Name'])
    for item in collection.values():
        if item != {}:
            gear_names.append(item['Name'])
    return gear_names

# Function count appearances of items inside a list and return (item:count) pairs as a dictionary
def item_appearance(items):
    links = {}
    for item in items:
        if item in links:
            links[item] += 1
        else:
            links[item] = 1
    return links

# Function to get links from (gear + collection) and return their count as a dictionary. Ignore equipped items.
def get_links_count(gear, collection):
    links = []
    all_items = merge_dicts(gear, collection)
    item_names = get_gear_names(gear, collection)

    for item in all_items.values():
        if item != {}:
            for link in ['Link1', 'Link2', 'Link3']:
                if item[link] not in get_gear_names(gear, collection):
                    links.append(item[link])
    
    links_count = item_appearance(links)
    return links_count

# Function gets highest count of links from (gear + collection) and returns the items with that count
def get_items_with_highest_link_count(gear, collection, items):
    links_count = get_links_count(gear, collection)
    highest_count = max(links_count.values())
    highest_count_items = []
    
    link_items_names = links_count.keys()
    link_items = []
    for name in link_items_names:
        link_items.append(get_item_by_name(name, items))
    
    for item in link_items:
        if links_count[item['Name']] == highest_count:
            highest_count_items.append(item)
    if highest_count == 1:
        tmp_list = []
        tmp_list.append(highest_count_items[0])
        return tmp_list
    if highest_count <= 0:
        return [{}]
        print('No items with links found.')
    return highest_count_items

# Function that adds an item to the collection using its type and removes it from the items list 
def add_item_to_collection(item, collection, items):
    for key in collection.keys():
        if key.startswith(item['Type']) and collection[key] != {}:
            print('Collection is full for this type: ', item['Type'], item['Name'])
        if key.startswith(item['Type']) and collection[key] == {}:
            collection[key] = item
            items.remove(item)
            break
        
# Function that adds items with highest link count to the collection
def add_items_with_highest_link_count(gear, collection, items):
    highest_count_items = get_items_with_highest_link_count(gear, collection, items)
    
    # Add items with highest link count to the collection
    for item in highest_count_items:
        add_item_to_collection(item, collection, items)

# While get_links_count returns a dictionary with at least one item with count > 1
# add items with highest link count to the collection

print('Initial gear:')
print_hero(gear, collection)
print('')

for i in range(1,6):
    add_items_with_highest_link_count(gear, collection, items)
    print('Added items with highest link count iteration', i)
    print_hero(gear, collection)
    print('')

    time.sleep(0.1)