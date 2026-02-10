import os


class LiverpoolTxtPipeline:
    def open_spider(self, spider):
        os.makedirs("output", exist_ok=True)
        self.file = open("output/laptops.txt", "w", encoding="utf-8")
        self.counter = 1

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        self.file.write(f"{self.counter}\n")
        self.file.write(f"Marca: {item['brand']}\n")
        self.file.write(f"Descripción: {item['description']}\n")
        self.file.write(f"Precio: {item['price']}\n")
        self.file.write("-" * 60 + "\n")

        self.counter += 1
        return item