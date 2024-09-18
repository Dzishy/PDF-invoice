# A Python invoice generator.
[Sample invoice](https://github.com/Dzishy/PDF-invoice/blob/main/output/invoice.pdf)

The program generates invoices in widely used PDF format and utilizes a .json file as a data sourse. It supports special characters like Euro symbol or diacritical marks.

This invoice generating program was written in Python 3.12.4 using FPDF2 library.

## Instructions:
1. Clone the repository
2. Install fpdf2 library
3. Open the "assets" folder and replace sample logo and signature images with your logo and signature.
4. Go to the "input" folder, open the [input-data.json](https://github.com/Dzishy/PDF-invoice/blob/main/input/input-data.json) file and change the data for your invoice:
    - change the seller information, such as name, address, payment details, tax rate, invoice number and currency for your invoice, also change the path to your logo and signature
    - ```"seller": {
          "name": "MISTER TWISTER",
          "address": "Calmstreet 1/1, 00-000 Dreamcity",
          "vatCode": "0000000000",
          "phone": "+12345678900",
          "paymentMethod": "Bank Transfer",
          "bank": "Best Bank Ever",
          "swift": "BBEDRPW",
          "account": "XL10 0000 0000 0000 0000 0000 0000",
          "taxRate": 0,
          "logo": "./assets/logo-01.png",
          "signature": "./assets/signature.png",
          "invoiceNumber": "nr 1/16.08.2024",
          "currency": "€"
    - provide product information, such as number on a list, name of service, quantity, unit price and the total amount
    - ```"products":{
          "product1": {
              "no": "1",
              "nameOfService": "Usługi komputerowe",
              "quantity": 160,
              "unitPrice": 25,
              "amount": 4000
          },
          "product2": {
              "no": "2",
              "nameOfService": "Usługi dodatkowe",
              "quantity": 10,
              "unitPrice": 30,
              "amount": 300
          }
    - change the buyer information: buyer name, address, vat code
    - ```"buyer": {
          "name": "BEST SOLUTIONS SP. Z O.O.",
          "address": "Long Street 1, 00-000 Funcity",
          "vatCode": "0000000000"
      },
    - update dates: date of issue, date of sale and due date
    - ```    "dates": {
          "issue": "2024-08-21",
          "sale": "2012-12-12",
          "due": "2013-01-01"
      }
5. Run the [main.py](https://github.com/Dzishy/PDF-invoice/blob/main/main.py) file and find your invoice in the output folder.


### Author: 
Dziyana Shydlouskaya
### Licence: 
MIT
