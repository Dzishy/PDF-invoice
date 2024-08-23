import json

class Dates ():
    def __init__(self, DATA):
        
        dateData = DATA.get("dates",{})
        self.issue = dateData.get("issue", "")
        self.sale = dateData.get("sale", "")
        self.due = dateData.get("due", "")

    def displayDates(self):
        '''A method to create a dictionary with dates details'''
        dates = {}
        dates['Date of issue'] = self.issue
        dates['Date of sale'] = self.sale
        dates['Due date'] = self.due
        return dates