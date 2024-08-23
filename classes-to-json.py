import datetime as date
import json

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
        self.taxRate = 0
        self.logo = "./assets/logo-01.png" # Enter a path to the image with the logo
        self.signature = './assets/signature.png' # Enter a path to the image with the signature
        self.invoiceNumber = 'nr 1/16.08.2024' # Enter the current invoice number   
        self.currency = 'EUR'   
    
    def to_dict(self):
        return self.__dict__
    
class Product():
    def __init__(self):
        self.no = '1'
        self.nameOfService = 'Computer services'
        self.quantity = 160
        self.unitPrice = 25
        self.amount = self.quantity*self.unitPrice
        
    def to_dict(self):
        return self.__dict__

class Buyer():
    def __init__(self):
        self.name = 'BEST SOLUTIONS SP. Z O.O.'
        self.address = 'Long Street 1, 00-000 Funcity'
        self.nip = '0000000000'
        
    def to_dict(self):
        return self.__dict__
        
class Dates ():
    def __init__(self):
        self.issue = str(date.date.today())
        self.sale = "2012-12-12"
        self.due = "2013-01-01"
        
    def to_dict(self):
        return self.__dict__
    
class Invoice:
    def __init__(self, seller, product, buyer, dates):
        self.seller = seller
        self.product = product
        self.buyer = buyer
        self.dates = dates

    def to_dict(self):
        # Convert the nested objects to dictionaries as well
        return {
            "seller": self.seller.to_dict(),
            "product": self.product.to_dict(),
            "buyer": self.buyer.to_dict(),
            "dates": self.dates.to_dict(),
        }
        
def save_to_json(obj, filename):
    with open(filename, 'w') as json_file:
        json.dump(obj.to_dict(), json_file, indent=4)

# Example usage
seller = Seller()
product = Product()
buyer = Buyer()
dates = Dates()
invoice = Invoice(seller=seller, product=product, buyer=buyer, dates=dates)

save_to_json(invoice, 'invoice.json')