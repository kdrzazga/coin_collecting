from datetime import datetime


class Event:
    def __init__(self, name, months: tuple, days: tuple):
        self.months = (months,)
        self.days = days
        self.name = name

    def __str__(self):
        return self.name

    def active(self):
        return datetime.now().month in self.months and datetime.now().day in self.days
