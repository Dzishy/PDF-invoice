

class Buyer():
    def __init__(self):
        self.name = 'BEST SOLUTIONS SP. Z O.O.'
        self.address = 'Long Street 1, 00-000 Funcity'
        self.nip = '0000000000'
        
    def dispBuyer (self):
        '''A method returning a dictionary with buyer's details'''
        
        buyer = {}
        buyer['Buyer'] = self.name
        buyer['Address'] = self.address
        buyer['NIP'] = self.nip
        return buyer