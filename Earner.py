
class Earner:
    """docstring for Earner."""

    def __init__(self, params ={
    'rate': 0, 'weekly': 0, 'annual': 0, 'monthly': 0
    }):
        if 'rate' in params:
            if params['rate'] is not '':
                self.rate = float(params['rate'])
            else:
                self.rate = 0

        if 'weekly' in params:
            if params['weekly'] is not '':
                self.weekly = float(params['weekly'])
            else:
                self.weekly = 0

        if 'annual' in params:
            if params['annual'] is not '':
                self.annual = float(params['annual'])
            else:
                self.annual = 0
        else:
            self.annual = 0

        if 'monthly' in params:
            if params['monthly'] is not '':
                self.monthly = float(params['monthly'])
            else:
                self.monthly = 0
        else:
            self.monthly = 0

    #requires rate and weekly
    def calcAnnual(self):
        self.annual = self.rate * self.weekly * 4 * 12

    #requires rate and weekly OR Annual
    def calcMonthly(self):
        self.monthly = self.rate * self.weekly
        if self.annual is not 0:
            self.monthly = self.annual / 12

    #requires annual and rate
    def calcWeekly(self):
        if self.annual > 0:
            self.weekly = self.annual / 12 / 4 / self.rate
        elif self.monthly > 0:
            self.weekly = self.monthly / 4 / self.rate

    #requires monthly or annual and weekly
    def calcRate(self):
        if self.annual > 0 and self.weekly > 0:
            self.rate = self.annual / 12 / 4 / self.weekly
        elif self.monthly > 0 and self.weekly > 0:
            self.rate = self.monthly / 4 / self.weekly


    def controller(self):

        self.calcRate()

        self.calcWeekly()

        self.calcAnnual()

        self.calcMonthly()
