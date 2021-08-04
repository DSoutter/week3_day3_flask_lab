from models.order import *
from models.customer import *


customer1 = Customer("Jeremy")
customer2 = Customer("Dimitar")
customer3 = Customer("Maggie")


order1 = Order(customer1.name, "04/08/2021", 3, "disposable")
order2 = Order(customer2.name, "02/08/2021", 5, "buff")
order3 = Order(customer3.name, "01/08/2021", 4, "reusable")

orders = [order1, order2, order3]