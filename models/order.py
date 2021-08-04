class Order:
    def __init__(self, customer_name, order_date, quantity, mask_type):
        self.customer_name = customer_name
        self.order_date = order_date
        self.quantity = quantity
        self.mask_type = mask_type

    # def customer_name(self, customer):
    #     self.customer_name = customer.name
    #     return self.customer_name