import json
from src.PDFBuilder import PdfBuilder

def main():
    
    with open('./input/input-data.json','r', encoding='utf-8') as jsonData:
        DATA = json.load(jsonData)
    
    invoice = PdfBuilder('P','mm','A4', DATA)
    
    invoice.add_page()

    invoice.set_font("DejaVu", "", 10)
    
    # Adding information about seller and buyer
    invoice.sidesInfo()
    
    # Adding information about items sold
    invoice.mainTable()
    invoice.ln(2.5)
    
    # Adding price summary 
    invoice.summary()
    invoice.ln(10)
    
    # Places for signatures
    invoice.signatures()
    
    # Generate invoice in pdf format
    ar = DATA['seller']['invoiceNumber'].replace(" ", "").split('/')
    invoice.output(f"./output/{ar[0]}-{ar[1]}.pdf")
 
main()