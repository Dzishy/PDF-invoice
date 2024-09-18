from fpdf import FPDF
from fpdf.fonts import FontFace
from .Seller import Seller
from .Buyer import Buyer
from .Dates import Dates
        

class PdfBuilder(FPDF):
    
    BLUE = (180, 230, 250)

    def __init__ (self, orientation, units, format, DATA):
        super().__init__(orientation, units, format)
        
        self.SELLER = Seller(DATA)
        self.BUYER = Buyer(DATA)
        self.DATES = Dates(DATA)
        
        self.add_font('DejaVu', '', 'assets/DejaVuSans.ttf', uni=True)
        self.add_font('DejaVu', 'B', 'assets/DejaVuSans-Bold.ttf', uni=True)
    
    def header(self):
        '''A header with logo and invoice number'''
        
        # Adding logo
        self.image(self.SELLER.logo,170,20,29)
        self.set_font("DejaVu", "B", 22)
        # Printing title:
        self.set_y(20)
        self.cell(10, 6, "INVOICE", 0, new_x="LMARGIN", new_y="NEXT", align="L")
        self.ln(5)
        # Adding the invoice number
        self.set_font("DejaVu", "", 13)
        self.cell(10, None, f'{self.SELLER.invoiceNumber}', 0, new_x="LMARGIN", new_y="NEXT", align="L")
        self.ln(20)
        
    def footer(self):
        '''A footer with page number'''     
              
        self.set_y(-15)
        self.cell(0, 10, f"Page {self.page_no()}/{self.pages_count}", align='C')
    
    
    def renderTable(self, data):
        '''Method to render a table from data'''
        
        with self.table(width=95, col_widths=(20, 5, 70), text_align=('l', 'c', 'l'), align='L', borders_layout='NONE', line_height=4, gutter_height=2) as table:
            for key, value in data:
                row = table.row()
                row.cell(key,)
                row.cell(':')
                row.cell(value)
    
    def sidesInfo(self):
        '''Adding information about the seller, the buyer, payment details and dates'''
        
        # Save the current Y position
        y = self.get_y()
        
        # Render seller info table
        self.renderTable(self.SELLER.dispSeller().items())
        # Dynamically set X position for the buyer table
        self.set_xy(self.get_x() + 95, y)
        # Render buyer info table
        self.renderTable(self.BUYER.dispBuyer().items())
        
        # Calculate y for drawing a division line
        maxY = max(self.get_y(), y + (len(self.SELLER.dispSeller()) * 6))
        self.set_y(maxY + 5)
        self.set_draw_color(self.BLUE)
        self.set_line_width(1)        
        # Draw a blue division line 1mm wide
        self.cell(190, None,'', 1, align='C')       
        # Set the rest of the document lines back to 0,25mm
        self.set_line_width(0.25)        
        self.ln (6)
        
        # Draw tables with payment details and dates
        
        self.set_x(10)
        y = self.get_y()
        self.renderTable(self.DATES.displayDates().items())
        self.set_xy(self.get_x() + 95, y)
        self.renderTable(self.SELLER.paymentDetails().items())
        self.ln(10)
    
    def mainTable (self):
        '''A table with sold items or provided services'''
        
        with self.table(width=190, col_widths=(10, 100, 20, 30, 30), align='L', line_height=5, padding=2, headings_style=FontFace(fill_color=self.BLUE)) as table:
            for rows in self.SELLER.itemsSold():
                row = table.row()
                for item in rows:
                    row.cell(item)
    
    def summary (self):
        '''A total summary of the invoice'''
        
        summary = self.SELLER.summary()
        with self.table(width=60, col_widths=(30, 30), align='R', line_height=5, padding=2, first_row_as_headings=False) as table:
            for i, rows in enumerate(summary):
                row = table.row()
                if i == len (summary)-1:
                    self.set_font("DejaVu", "B", 10)
                    self.set_fill_color(self.BLUE) 
                for item in rows:
                    row.cell(item)
        # Set the fill color back to white, because previously it was set to blue            
        self.set_fill_color(255,255,255)
        
    def signatures (self):
        '''Creating space for signatures and adding an image with the seller's signature'''
        
        self.set_font('DejaVu','', 8)
        # Create the first cell for buyer's signature
        self.cell(90, 30, "", 1, new_x="RIGHT", new_y="TOP", align="C")
        self.set_x(110)
        # Create the second cell for seller's signature
        self.cell(90, 30, "", 1, new_x="CENTER", new_y="TOP", align="C")
        y = self.get_y() + 5
        # Insert an image with the signature
        self.image(self.SELLER.signature, y=y, w=90, h=20, keep_aspect_ratio=True)
        self.ln(28.5)
        self.set_x(15)
        self.cell(80, None, "Signature of the person authorised to receive the invoice", 0, new_x="RIGHT", new_y="TOP", align="C",fill=True)
        self.set_x(115)
        self.cell(80, None, "Signature of the person authorised to issue the invoice", 0, new_x="LMARGIN", new_y="NEXT", align="C",fill=True)

