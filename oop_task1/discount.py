from shop import Shop

class Discount(Shop):
    def __init__(self, shop_name, store_type):
        super().__init__(shop_name, store_type)
        self.discount_products = []

    def get_discount_products(self):
        print("Товари зі знижкою:")
        for product in self.discount_products:
            print(f"- {product}")

if __name__ == "__main__":
    store = Shop("Мій Магазин", "Одяг")
    print(store.shop_name)
    print(store.store_type)
    store.describe_shop()
    store.open_shop()

    store1 = Shop("Магазин 1", "Книги")
    store2 = Shop("Магазин 2", "Електроніка")
    store3 = Shop("Магазин 3", "Продукти")

    store1.describe_shop()
    store2.describe_shop()
    store3.describe_shop()

    print(store.number_of_units)
    store.number_of_units = 10
    print(store.number_of_units)

    store.set_number_of_units(20)
    print(store.number_of_units)
    store.increment_number_of_units(5)
    print(store.number_of_units)

    store_discount = Discount("Знижковий Магазин", "Взуття")
    store_discount.discount_products = ["Кросівки", "Босоніжки", "Туфлі"]
    store_discount.get_discount_products()
