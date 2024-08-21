


class Seller():
    def __init__(self):
        self.name = 'MISTER TWISTER'
        self.address = 'Calmstreet 1/1, 00-000 Dreamcity'
        self.nip = '0000000000'
        self.phone = '+12345678900'
        self.paymentMethod = 'Bank Transfer'
        self.bank = 'Best Bank Ever'
        self.swift = 'BBEDRPW'
        self.account = 'XL10 0000 0000 0000 0000 0000 0000'
        self.signature = './signature.png' # Enter a path to the image with the signature
        self.invoiceNumber = 'nr 1/16.08.2024' # Enter the current invoice number  
        
    def dispSeller (self):
        '''A method to create a dictionary with seller details'''
        
        seller = {}
        seller['Seller'] = self.name
        seller['Address'] = self.address
        seller['NIP'] = self.nip
        seller['Phone'] = self.phone
        return seller
    
    def paymentDetails (self):
        '''A method to create a dictionary with payment details'''
        
        payment = {}
        payment['Payment method'] = self.paymentMethod
        payment['Bank'] = self.bank
        payment['SWIFT'] = self.swift
        payment['Account NO'] = self.account
        return payment
    
    def itemsSold (self):
        '''Create a list of provided services or sold items and return this list'''
        
        quantity = 160 
        price = 25
        amount = quantity * price
                
        items = [('No', 'Name of service', 'Quantity', 'Unit price', 'Amount')]
        # add a tuple with sold item or provided service details to the 'items' list
        items.append(('1', 'Computer services', f'{quantity}', f'{price}', f'EUR {amount:,.2f}'))
        
        return items
    
    def summary(self):
        '''Calculate total summary of the invoice and return a list with summary details'''
        
        subtotal = 0
        items = self.itemsSold()
        for i in range (1,len(items)):
            amount = items[i][4].replace('EUR','').strip().replace(',','')
            subtotal += float(amount)
        taxRate = 0
        taxAmount = subtotal * taxRate
        total = subtotal + taxAmount
        
        summary = [('Subtotal:', f'EUR {subtotal:,.2f}'),
                   (f'Tax ({taxRate*100}%):', f'EUR {taxAmount:,.2f}'),
                   ('TOTAL:', f'EUR {total:,.2f}'),
        ]
        return summary
    