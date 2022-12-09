"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, hasFixed, hasContract):
        self.name = name
        self.hasFixed = hasFixed
        self.hasContract = hasContract


    def get_pay(self):
        return

    def __str__(self):
        return self.name


class SalaryEmployee(Employee):
    def __init__(self, monthly_wage):
        self.pay = monthly_wage
    
    def get_pay(self):
        if self.hasFixed = True:
        pass

class HourlyEmployee(Employee):
    def __init__(self, hourly_wage, hours_worked):
        self.pay = hourly_wage * hours_worked


    
class ContractCommisson:
    def __init__(self, number_of_contracts, contract_price):
        # self.number_of_contracts = number_of_contracts
        # self.contract_price = contract_price
        self.contract_com= number_of_contracts * contract_price

class FixedBonusCommisson:
    def __init__(self, bonus):
        self.fixed_bonus = bonus
    
   






# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
