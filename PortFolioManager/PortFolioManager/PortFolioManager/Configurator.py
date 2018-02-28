import json

class Configurator:
    def __init__(self):
       self.data = json.load(open('config.json'))
 
    def BuildUIData(self):
        UIComponent = {}

        return self.data
 

