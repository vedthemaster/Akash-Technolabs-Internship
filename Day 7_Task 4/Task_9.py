# Task 9  Create a class called scheme with scheme_id,
# scheme_name,outgoing_rate, and message_charge. Derive customer
# class form scheme and include cust_id, name and mobile_no
# data.Define necessary functions to read and display data

class scheme:

    def __init__(self,scheme_id,scheme_name,outgoing_rate,message_charge):
        self.id = scheme_id
        self.name = scheme_name
        self.rate = outgoing_rate
        self.charge = message_charge

    def get_rate(self):
        return self.rate

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_charge(self):
        return self.charge

    def display_scheme(self):
        return f'{self.id},{self.name},{self.charge},{self.charge}'
 
jio = scheme("1","Fiber","0.25","1")
airtel = scheme("1","opairtel","0.24","1.4")

print(jio.get_charge(),jio.get_name())
print(jio.display_scheme())

class customer(scheme):

    def __init__(self,cust_id,cust_name,cust_no):
        self.cid = cust_id
        self.cname = cust_name
        self.cno = cust_no

    def get_cid(self):
        return self.cid

    def get_cname(self):
        return self.cname

    def get_cno(self):
        return self.cno

    def display(self):
        return f'{self.cid},{self.cname},{self.cno}'

customer1 = customer("101","Magan","7541457458")
customer2 = customer("102","Chagan","9907978457")
customer3 = customer("103","Raman","9857487854")

print(customer1.display())



