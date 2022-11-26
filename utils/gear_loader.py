# A class to initialize the attack gear of maximum potential for each slot
# The items we work with are a list of dictionaries and 
# We pass them as an argument in the object instantiation and save them in the gear attribute 
# We take the maximum potential ATTACK item from each slot in the gear and add it to the gear

class GearLoader:
    def __init__(self, items):
        self.items = items
        self.gear = {'HELM': None, 'CHEST': None, 'GLOVES': None, 'BOOTS': None, 'RING': None, 'NECKLACE': None, 'TALISMAN': None}
        self.initialize_gear()

    def initialize_gear(self):
        for item in self.items:
            if item['Type'] == 'ATTACK' and (self.gear[item['Slot']] == None or item['Potential'] > self.gear[item['Slot']]['Potential']):
                self.gear[item['Slot']] = item