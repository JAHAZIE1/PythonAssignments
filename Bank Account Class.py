'''

See below the examples of use and test cases:


john01 = Person("John", "Doe")
john01.set_address("Birkbeck, Malet st., WC1E 7HX")
john01s_account = IndividualBankAccount("12-34-56", "12345678", john01)
#Test1 checks john01s_account.get_account_data()=="John Doe 12-34-56 12345678"
john01s_account.set_sort_code("11-11-11")
#Test2 check john01s_account.get_sort_code()=="11-11-11"


mary01 = Person("Mary", "Ann")
mary01.set_address("UCL, Gower st., WC1E 6BT")
mary01s_account = IndividualBankAccount("65-43-21", "87654321", mary01)
#Test3 checks mary01s_account.get_account_data()=="Mary Ann 65-43-21 87654321"
mary01s_account.set_account_number("99999999")
#Test4 checks mary01s_account.get_account_number()=="99999999"


acc02 = SharedBankAccount("11-22-33", "11223344", [john01, mary01])
#Test5 checks acc02.get_account_data()=="John Doe, Mary Ann, 11-22-33 11223344"


'''


class Person:
    '''to handle person's details'''
    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln
        self.address = None
    def set_address(self, adr):
        self.address = adr

    def print_name(self):
        return self.first_name + " " + self.last_name

class BankAccount:
    def __init__(self, sort_code, account_number):
        self.sort_code = str(sort_code)
        self.a_no = str(account_number)

    def set_sort_code(self, sort_code):
        self.sort_code = sort_code
    def get_sort_code(self):
        return self.sort_code
    def set_account_number(self, account_number):
        self.a_no = account_number
    def get_account_number(self):
        return self.a_no
    def get_account_data(self):
        return self.sort_code + self.a_no

class IndividualBankAccount(BankAccount):
    def __init__(self, sort_code, account_number, owner):
        super().__init__(sort_code, account_number)
        self.name = Person.print_name(owner)


    def get_account_data(self):
        _name = self.name
        S_C = self.sort_code
        A_N = self.a_no
        return _name + " " + S_C + " " + A_N

class SharedBankAccount(BankAccount):
    def __init__(self, sort_code, account_number, owners):
        super().__init__(sort_code, account_number)
        self.name1 = Person.print_name(owners[0])
        self.name2 = Person.print_name(owners[1])


    def get_account_data(self):
        _name1 = self.name1
        _name2 = self.name2
        S_C = self.sort_code
        A_N = self.a_no
        return _name1 + "," + " " + _name2 + "," + " " + S_C + " " + A_N
