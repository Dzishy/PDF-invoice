from fpdf import FPDF
from fpdf.fonts import FontFace
from Seller import Seller
from Buyer import Buyer
from Dates import Dates
        

class PDF(FPDF):
    
    def header(self):
        seller = Seller()
        # Adding logo
        self.image("PDF-invoice/logo-01.png",170,20,29)
        self.set_font("helvetica", "B", 22)
        # Printing title:
        self.set_y(20)
        self.cell(10, 6, "INVOICE", 0, new_x="LMARGIN", new_y="NEXT", align="L")
        self.ln(5)
        # Adding the invoice number
        self.set_font("helvetica", "", 13)
        self.cell(10, None, f'{seller.invNum()}', 0, new_x="LMARGIN", new_y="NEXT", align="L")
        self.ln(20)
        
    def footer(self):           
        self.set_y(-15)
        self.set_font("helvetica", "", 10)
        self.cell(0, 10, f"Page {self.page_no()}/{self.pages_count}", align='C')
    
    # Method to render a table from data
    def renderSidesTable(self, data, columns, width):
        with self.table(width=width, col_widths=columns, text_align=('l', 'c', 'l'), align='L', borders_layout='NONE', line_height=4, gutter_height=2) as table:
            for key, value in data.items():
                row = table.row()
                row.cell(key)
                row.cell(':')
                row.cell(value)
    
    def sidesInfo(self):
        seller = Seller()
        buyer = Buyer()
        self.set_font("helvetica", "", 10)

        # Save the current Y position
        y = self.get_y()

        # Render seller info table
        columns = (20, 5, 70)
        self.renderSidesTable(seller.dispSeller(), columns, 95)

        # Dynamically set X position for the buyer table
        self.set_xy(self.get_x() + 95, y)

        # Render buyer info table
        self.renderSidesTable(buyer.dispBuyer(), columns, 95)
        maxY = max(self.get_y(), y + (len(seller.dispSeller()) * 6))
        self.set_y(maxY + 5)
        
        self.cell(190, None,'', 1, align='C')
        self.ln (6)
        
        dates = Dates()
        self.set_x(10)
        y = self.get_y()
        self.renderSidesTable(dates.displayDates(),columns, 95)
        self.set_xy(self.get_x() + 95, y)
        self.renderSidesTable(seller.paymentDetails(),columns, 95)
        self.ln(10)
    
    def mainTable (self):
        self.set_font("helvetica", "", 10)
        seller = Seller()
        blue = (180, 230, 250)
        self.set_draw_color(blue)
        with self.table(width=190, col_widths=(10, 100, 26, 25, 29), align='L', line_height=5, padding=2, headings_style=FontFace(fill_color=blue)) as table:
            for rows in seller.itemsSold():
                row = table.row()
                for item in rows:
                    row.cell(item)
    
    def summary (self):
        self.set_font("helvetica", "", 10)
        seller = Seller()
        summary = seller.summary()
        blue = (180, 230, 250)
        self.set_draw_color(blue)
        with self.table(width=54, col_widths=(25, 29), align='R', line_height=5, padding=2, first_row_as_headings=False) as table:
            for i, rows in enumerate(summary):
                row = table.row()
                if i == len (summary)-1:
                    self.set_font("helvetica", "B", 10)
                    self.set_fill_color(180, 230, 250)
                for item in rows:
                    row.cell(item)
    
    def signatures (self):
        self.set_font('helvetica','', 8)
        h = 30
        self.set_fill_color(0, 0, 0)
        with self.table(width=190, col_widths=90, text_align=('c', 'c'), align='C', gutter_width=10, line_height=h) as table:
            row = table.row()
            row.cell("", padding=1)
            row.cell("", padding=1)
    
        with self.table(width=190, col_widths=90, text_align=('c', 'c'), align='C', borders_layout='NONE', gutter_width=10, first_row_as_headings=False) as table:
            row2 = table.row()
            row2.cell('Signature of the person authorised to receive the invoice')
            row2.cell('Signature of the person authorised to issue the invoice')
