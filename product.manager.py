import time

class Product:
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = float(price)
        self.category = category

    def __str__(self):
        return f'{self.id}, {self.name}, {self.price}, {self.category}'

class ProductManager:
    def __init__(self):
        self.products = []

    def load_products(self, filepath):
        with open(filepath, 'r') as file:
            for line in file:
                id, name, price, category = line.strip().split(', ')
                self.products.append(Product(id, name, price, category))
        print("Products loaded successfully.")

    def add_product(self, id, name, price, category):
        self.products.append(Product(id, name, price, category))
        print(f"Product added: ID {id}, Name: {name}, Price: {price}, Category: {category}")

    def update_product(self, id, **kwargs):
        for product in self.products:
            if product.id == id:
                product.name = kwargs.get('name', product.name)
                product.price = float(kwargs.get('price', product.price))
                product.category = kwargs.get('category', product.category)
                print(f"Product updated: {product}")
                return True
        return False

    def delete_product(self, id):
        for i, product in enumerate(self.products):
            if product.id == id:
                del self.products[i]
                print(f"Product with ID {id} deleted.")
                return True
        print("Product not found.")
        return False

    def search_product(self, **kwargs):
        results = []
        for product in self.products:
            if all(getattr(product, key) == value for key, value in kwargs.items()):
                results.append(product)
        return results

    def quick_sort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.quick_sort(arr, low, pi - 1)
            self.quick_sort(arr, pi + 1, high)

    def partition(self, arr, low, high):
        i = low - 1
        pivot = arr[high].price
        for j in range(low, high):
            if arr[j].price <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def sort_products_by_price(self):
        start_time = time.time()
        if self.products:
            self.quick_sort(self.products, 0, len(self.products) - 1)
        end_time = time.time()
        print(f"Sorting Time: {end_time - start_time:.2f} seconds")

    def display_products(self):
        for product in self.products:
            print(product)

def main():
    manager = ProductManager()

  
    manager.load_products('product_data.txt')
    print("Loaded Products:")
    manager.display_products()


    manager.add_product('12345', 'Console VVNOX', '499.98', 'Video Game')

   
    manager.update_product('30483', name='Knife Set Deluxe', price='99.99')

   
    manager.delete_product('13471')


    search_results = manager.search_product(name='Knife Set Deluxe')
    print("\nSearch Results:")
    for product in search_results:
        print(product)


    manager.sort_products_by_price()
    print("\nSorted Products by Price:")
    manager.display_products()

if __name__ == "__main__":
    main()
