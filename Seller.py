


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
        
    def dispSeller (self):
        seller = {}
        seller['Seller'] = self.name
        seller['Address'] = self.address
        seller['NIP'] = self.nip
        seller['Phone'] = self.phone
        return seller
    
    def paymentDetails (self):
        payment = {}
        payment['Payment method'] = self.paymentMethod
        payment['Bank'] = self.bank
        payment['SWIFT'] = self.swift
        payment['Account NO'] = self.account
        return payment
    
    def invNum (self):
        self.invoiceNumber = 'nr 1/16.08.2024'
        invNum = self.invoiceNumber
        return invNum
    
    def itemsSold (self):
        totalHours = 160
        price = 25
        amount = totalHours * price
                
        items = (('No', 'Name of service', 'Quantity (hrs)', 'Unit price', 'Amount'),
                 ('1', 'Computer services', f'{totalHours}', f'{price}', f'EUR {amount:,.2f}'),
                 ('1', 'Computer services', f'{totalHours}', f'{price}', f'EUR {amount:,.2f}'),
                 ('1', 'Computer services', f'{totalHours}', f'{price}', f'EUR {amount:,.2f}'),
                 ('1', 'Computer services', f'{totalHours}', f'{price}', f'EUR {amount:,.2f}'),
                 ('1', 'Computer services', f'{totalHours}', f'{price}', f'EUR {amount:,.2f}'),
                 ('1', 'Computer services', f'{totalHours}', f'{price}', f'EUR {amount:,.2f}'),
                 ('1', 'Computer services', f'{totalHours}', f'{price}', f'EUR {amount:,.2f}'),
                 ('1', 'Computer services', f'{totalHours}', f'{price}', f'EUR {amount:,.2f}'),
                 ('1', 'Computer services', f'{totalHours}', f'{price}', f'EUR {amount:,.2f}'),
                 ('1', 'Computer services', f'{totalHours}', f'{price}', f'EUR {amount:,.2f}'),
                 ('1', 'Computer services', f'{totalHours}', f'{price}', f'EUR {amount:,.2f}'),
                 ('1', 'Computer services', f'{totalHours}', f'{price}', f'EUR {amount:,.2f}'),
                 ('1', 'Computer services', f'{totalHours}', f'{price}', f'EUR {amount:,.2f}'),
                 ('1', 'Computer services', f'{totalHours}', f'{price}', f'EUR {amount:,.2f}'),
                 ('1', 'Computer services', f'{totalHours}', f'{price}', f'EUR {amount:,.2f}'),
                 ('1', 'Computer services', f'{totalHours}', f'{price}', f'EUR {amount:,.2f}'),
                 ('1', 'Computer services', f'{totalHours}', f'{price}', f'EUR {amount:,.2f}'),
                 ('1', 'Computer services', f'{totalHours}', f'{price}', f'EUR {amount:,.2f}'),   
        )
        return items
    
    def summary(self):
        subtotal = 0
        items = self.itemsSold()
        for i in range (1,len(items)):
            amount = items[i][4].replace('EUR','').strip().replace(',','')
            subtotal += float(amount)
        taxRate = 0.23
        taxAmount = subtotal * taxRate
        total = subtotal + taxAmount
        
        summary = (('Subtotal:', f'EUR {subtotal:,.2f}'),
                   (f'Tax ({taxRate*100}%):', f'EUR {taxAmount:,.2f}'),
                   ('TOTAL:', f'EUR {total:,.2f}'),
                   )
        return summary
