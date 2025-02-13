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







import uuid
from random import choice


class Product:
    def __init__(self, name, price, quantity):
        self.id=uuid.uuid4()
        self.name=name
        self.price=price
        self.quantity=quantity



    def info(self):
        print(f"Bu maxsulot nomi {self.name}, narxi {self.price}, miqdori {self.quantity}, ID: {self.id}")

    def sell(self, amount):
        if self.quantity>=amount:
            self.quantity -= amount
            print(f"{amount} ta {self.name} sotildi. Qolgan miqdor: {self.quantity}")

        else:
            print("Maxsulot yetarli emas!")

    def restock(self, amount):
        self.quantity += amount
        print(f"{amount} ta {self.name} omborga qo'shildi. Yangi miqdor: {self.quantity}")









class Electronics(Product):
    def __init__(self, name, price, quantity, warranty):
        super().__init__(name, price, quantity)
        self.warranty=warranty

    def info(self):
        print(f"Nomi {self.name}, Narxi {self.price}, Miqdori {self.quantity}, Garantiyasi {self.warranty}, ID: {self.id}")



class Food(Product):
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity)
        self.expiration_date=expiration_date

    def info(self):
        print(f"Nomi {self.name}, Narxi {self.price}, Miqdori {self.quantity}, Yaroqlilik muddati {self.expiration_date}, ID: {self.id}")


    def sell(self, amount):
        if self.expiration_date<=0:
            print("Xatolik: Mahsulotning yaroqlilik muddati o'tgan!")
            return


        return super().sell(amount)


class Basket:
    def __init__(self):
        self.data = []

    def add(self, product):
        self.data.append({'product': product, 'price': product.price})
        print(f"{product.name} ({product.price}) savatga qo'shildi")

    def remove(self, product_name):
        for item in self.data:
            if item['product'].name == product_name:
                self.data.remove(item)
                print(f"{item['product'].name} savatdan olib tashlandi")
                return
        print(f"{product_name} savatda topilmadi")

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


def menu():
    basket=Basket()
    while True:
        print("\nMenu")
        print("1. Maxsulot qo'shish!")
        print("2. Maxsulot olib tashlash!")
        print("3. Savatni ko'rsatish!")
        print("4.Umumiy narxni hisoblash!")
        print("5. Chiqish")
        choice=input("Tanlang!")
        if choice=="1":
            name=input("Maxsulot nomi:")
            price=float(input("Maxsulot narxi:"))
            quantity=int(input("Maxsulot miqdori:"))
            product=Product(name, price, quantity)
            basket.add(product)

        elif choice=="2":
            product_name=input("Olib tashlanadigan maxsulot nomi:")
            basket.remove(product_name)

        elif choice=="3":
            basket.show()

        elif choice=="4":
            basket.calculating()

        elif choice=="5":
            print("Dasturdan chiqyabsiz...")

        else:
            print("Notog'ri tanlov, Iltimos qaytadan urinib ko'ring.")


menu()




