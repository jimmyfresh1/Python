class Shoe:
    def __init__(self, brand, shoe_type,price):
        self.brand=brand
        self.type=shoe_type
        self.price=price
        self.in_stock=True 

    def on_sale(self, percent):
        self.price= self.price * (1-percent)

skater_shoe=Shoe("Vans", "Low-tops", 59.99)
print(skater_shoe.brand)
print(skater_shoe.price)
skater_shoe.on_sale(.3)
print(skater_shoe.price)