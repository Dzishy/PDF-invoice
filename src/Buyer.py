import json
    

class Buyer():
    def __init__(self, DATA):
        
        buyerData = DATA.get("buyer", {})
        self.name = buyerData.get("name", "")
        self.address = buyerData.get("address", "")
        self.vatCode = buyerData.get("vatCode", "")
        
    def dispBuyer (self):
        '''A method returning a dictionary with buyer's details'''
        
        buyer = {}
        buyer['Buyer'] = self.name
        buyer['Address'] = self.address
        buyer['VAT Code'] = self.vatCode
        return buyer