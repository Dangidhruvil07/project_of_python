from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["ecommerce"]


db.products.insert_many(
    [
        {"name": "iPhone", "price": 80000, "image": "iphone.jpg", "category": "phone"},
        {
            "name": "Samsung S26",
            "price": 70000,
            "image": "s26.jpg",
            "category": "phone",
        },
        {
            "name": "OnePlus",
            "price": 65000,
            "image": "oneplus.jpg",
            "category": "phone",
        },
        {
            "name": "Google",
            "price": 75000,
            "image": "gogle.jpg",
            "category": "phone",
        },
        {"name": "realme", "price": 75000, "image": "realme.jpg", "category": "phone"},
        {
            "name": "HP Laptop",
            "price": 50000,
            "image": "laptop.jpg",
            "category": "laptop",
        },
        {
            "name": "Dell Inspiron",
            "price": 60000,
            "image": "laptop1.jpg",
            "category": "laptop",
        },
        {
            "name": "Boat Headphones",
            "price": 3000,
            "image": "headphone.jpg",
            "category": "audio",
        },
        {
            "name": "Sony Headphones",
            "price": 8000,
            "image": "headphone1.jpg",
            "category": "audio",
        },
        {
            "name": "Apple Watch",
            "price": 25000,
            "image": "smartwatch.jpg",
            "category": "accessories",
        },
        {
            "name": "Noise Smartwatch",
            "price": 5000,
            "image": "smartwatch1.jpg",
            "category": "accessories",
        },
    ]
)

print("Products Inserted ✅")
# print(list(db.products.find()))
# db.products.delete_many({})
