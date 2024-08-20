def sellerInfo (self):
        seller = Seller()
        buyer = Buyer()
        self.set_font("helvetica", "", 12)
        y = self.get_y()
        with self.table(width=90, col_widths=(20, 4, 70), text_align=('l', 'c', 'l'),align='L',borders_layout='NONE', line_height=6) as table:
            for key, value in seller.dispSeller().items():
                row = table.row()
                row.cell(key)
                row.cell(':')
                row.cell(value)
        
        self.set_xy(105, y)
        
        with self.table(width=95, col_widths=(20, 4, 75), text_align=('l', 'c', 'l'),align='L',borders_layout='NONE', line_height=6) as table:
            for key, value in buyer.dispBuyer().items():
                row = table.row()
                row.cell(key)
                row.cell(':')
                row.cell(value)