from PDF import PDF

def main():
    invoice = PDF('P','mm','A4')
    invoice.add_page()
    # Adding information about seller and buyer
    invoice.sidesInfo()
    # Adding information about items sold
    invoice.mainTable()
    invoice.ln(5)
    # Adding price summary 
    invoice.summary()
    invoice.ln(10)
    # Places for signatures
    invoice.signatures()
    # Generate invoice in pdf format
    invoice.output("PDF-invoice/invoice.pdf")
main()