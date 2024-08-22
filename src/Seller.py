import json


class Seller():
    
    with open('./input/input-data.json','r') as jsonData:
        DATA = json.load(jsonData)
    
    currency = DATA.get("seller").get("currency")
    
    def __init__(self):
                
        sellerData = self.DATA.get("seller", {})  # Use .get() to avoid KeyError if "buyer" doesn't exist
        self.name = sellerData.get("name", "")
        self.address = sellerData.get("address", "")
        self.vatCode = sellerData.get("vatCode", "")
        self.phone = sellerData.get("phone", "")
        self.paymentMethod = sellerData.get("paymentMethod", "")
        self.bank = sellerData.get("bank", "")
        self.swift = sellerData.get("swift", "")
        self.account = sellerData.get("account", "")
        self.logo = sellerData.get("logo", "") # Enter a path to the image with the logo
        self.signature = sellerData.get("signature", "") # Enter a path to the image with the signature
        self.invoiceNumber = sellerData.get("invoiceNumber", "") # Enter the current invoice number  
        
    def dispSeller (self):
        '''A method to create a dictionary with seller details'''
        
        seller = {}
        seller['Seller'] = self.name
        seller['Address'] = self.address
        seller['VAT Code'] = self.vatCode
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
        
        items = [('No', 'Name of service', 'Quantity', f'Unit price ({self.currency})', f'Amount ({self.currency})')]
        productsData = self.DATA.get("products", {})
        
        for value in productsData.values():
            no = value.get("no", "")
            nameOfService = value.get("nameOfService", "")
            quantity = value.get("quantity", "")
            unitPrice = value.get("unitPrice", "")
            amount = value.get("amount", "")
            # add a tuple with sold item or provided service details to the 'items' list
            items.append((no, nameOfService, f'{quantity}', f'{unitPrice:,.2f}', f'{amount:,.2f}'))
        
        return items
    
    def summary(self):
        '''Calculate total summary of the invoice and return a list with summary details'''
        
        subtotal = 0
        items = self.itemsSold()
        for i in range (1,len(items)):
            amount = items[i][4].replace(",", "")
            subtotal += float(amount)
        taxRate = self.DATA.get("seller", {}).get('taxRate', "")
        taxAmount = subtotal * taxRate
        total = subtotal + taxAmount
        
        summary = [('Subtotal:', f'{self.currency} {subtotal:,.2f}'),
                   (f'Tax ({taxRate*100}%):', f'{self.currency} {taxAmount:,.2f}'),
                   ('TOTAL:', f'{self.currency} {total:,.2f}'),
        ]
        return summary
    