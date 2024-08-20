import datetime as date


class Dates ():
    def __init__(self):
        self.issue = str(date.date.today())
        self.sale = "2012-12-12"
        self.due = "2013-01-01"

    def displayDates(self):
        dates = {}
        dates['Issue'] = self.issue
        dates['Sale'] = self.sale
        dates['Due'] = self.due
        return dates