# class Transport:
#     def __init__(self, name, speed):
#         self.name=name
#         self.speed=speed
#
#
#     def info(self):
#         print(f"Bu mashina nomi {self.name}, tezligi {self.speed}")
#
#
# class Car(Transport):
#     def info(self):
#         print(f"Bu mashina nomi {self.name}, tezligi {self.speed}")
#
#
# class Bicycle(Transport):
#     def info(self):
#         print(f"Bu velosiped nomi {self.name}, tezligi {self.speed}")
#
#
#
# c=Car("Nexia 2", 280)
# c.info()
#
# b=Bicycle("Gonka", 30)
# b.info()
#
# t=Transport("AUDI", 300)
# t.info()
#










class Product:
    def __init__(self, name, price, quantity):
        self.name=name
        self.price=price
        self.quantity=quantity



    def info(self):
        print(f"Bu maxsulot nomi {self.name}, narxi {self.price}, miqdori {self.quantity}")

    def sell(self, amount):
        if self.quantity>=amount:
            self.quantity -= amount
            print(f"{amount} ta {self.name} sotildi. Qolgan miqdor: {self.quantity}")

        else:
            print("Maxsulot yetarli emas!")

    def restock(self, amount):
        self.quantity += amount
        print(f"{amount} ta {self.name} omborga qo'shildi. Yangi miqdor: {self.quantity}")





a=Product("Apple", 1000, 10)
a.info()




class Electronics(Product):
    def __init__(self, name, price, quantity, warranty):
        super().__init__(name, price, quantity)
        self.warranty=warranty

    def info(self):
        print(f"Nomi {self.name}, Narxi {self.price}, Miqdori {self.quantity}, Garantiyasi {self.warranty}")



class Food(Product):
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity)
        self.expiration_date=expiration_date

    def info(self):
        print(f"Nomi {self.name}, Narxi {self.price}, Miqdori {self.quantity}, Yaroqlilik muddati {self.expiration_date}")


    def sell(self, amount):
        if self.expiration_date<=0:
            print("Xatolik: Mahsulotning yaroqlilik muddati o'tgan!")
            return


        return super().sell(amount)


class Basket:
    def __init__(self):
        self.data = []

    def add(self, product, price):
        self.data.append({'product': product, 'price': price})
        print(f"{product} ({price}) savatga qo'shildi")

    def remove(self, product):
        for item in self.data:
            if item['product'] == product:
                self.data.remove(item)
                print(f"{product} savatdan olib tashlandi")
                return
        print(f"{product} savatda topilmadi")

    def show(self):
        if not self.data:
            print("Savat bo'sh")
        else:
            print("Savat tarkibi")
            for item in self.data:
                print(f"- {item['product']}: {item['price']}")

    def calculating(self):
        total = sum(item['price'] for item in self.data)
        print(f"Umumiy narx: {total}")


basket = Basket()
basket.add("olma", 2)
basket.add("nok", 1)
basket.show()
basket.calculating()
basket.remove("Shaftoli")
basket.show()




e=Electronics("Muzlatgich", 100, "10ta", "1yil")
print(e.info())



f = Food("Sut", 500, 20, 0)  # Yaroqlilik muddati o'tgan
print(f.info())
f.sell(5)






