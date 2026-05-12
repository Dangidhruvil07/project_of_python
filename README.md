# HexaMobiles 📱

A modern full-stack ecommerce web application built using **Flask** and **MongoDB**.

HexaMobiles allows users to browse products, explore categories, add items to cart, place orders, and manage their shopping experience with a clean modern UI.

---

# ✨ Features

## 🛍 Product Features

* View all products
* Browse by categories
* Product cards with images and pricing
* Responsive modern UI
* Hero section and animated product layout

## 👤 Authentication

* User Registration
* User Login
* Session-based authentication
* Logout functionality
* Flash notifications for login success/error
* Login required for cart and orders

## 🛒 Cart System

* Add to cart
* Quantity handling
* Remove cart items
* Cart total calculation

## 📦 Orders

* Checkout functionality
* Order placement
* My Orders page
* Order history storage in MongoDB

## 🎨 UI Features

* Responsive design
* Bootstrap integration
* Custom CSS styling
* Animated flash messages
* Login modal popup
* Mobile friendly navbar

---

# 🛠 Tech Stack

## Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript
* Jinja2 Templates

## Backend

* Python
* Flask
* Flask-PyMongo

## Database

* MongoDB

---

# 📂 Project Structure

```bash
HexaMobiles/
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── script.js
│   │
│   └── images/
│       ├── iphone.jpg
│       ├── s26.jpg
│       ├── laptop.jpg
│       └── ...
│
├── templates/
│   ├── base.html
│   ├── products.html
│   ├── login.html
│   ├── register.html
│   ├── cart.html
│   ├── checkout.html
│   └── myorders.html
│
├── app.py
├── insert_products.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/HexaMobiles.git
cd HexaMobiles
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install flask flask-pymongo pymongo
```

---

## 4️⃣ Start MongoDB

Make sure MongoDB is running locally.

```bash
mongod
```

---

## 5️⃣ Insert Sample Products

```bash
python insert_products.py
```

---

## 6️⃣ Run Flask App

```bash
python app.py
```

---

# 🌐 Open in Browser

```bash
http://127.0.0.1:7000
```

---

# 🔐 Authentication Flow

## Public Access

Users can:

* Browse products
* View categories
* Explore the homepage

## Login Required

Users must login to:

* Add products to cart
* Checkout
* View orders

---

# 🗃 MongoDB Collections

## users

```json
{
  "name": "John",
  "email": "john@gmail.com",
  "password": "123456"
}
```

## products

```json
{
  "name": "iPhone",
  "price": 80000,
  "image": "iphone.jpg",
  "category": "phone"
}
```

## cart

```json
{
  "name": "iPhone",
  "price": 80000,
  "quantity": 1,
  "email": "john@gmail.com"
}
```

## orders

```json
{
  "email": "john@gmail.com",
  "items": [],
  "total": 120000
}
```

---

# 🚀 Future Improvements

* Payment Gateway Integration
* Admin Dashboard
* Product Search
* Wishlist
* Product Reviews
* JWT Authentication
* Password Hashing
* Razorpay / Stripe Payments
* AI Product Recommendations
* Email Verification

---

# 🔒 Security Note

Currently passwords are stored as plain text for learning purposes.

For production:

* Use password hashing
* Use environment variables
* Add CSRF protection
* Secure sessions

---

# ⭐ Support

If you like this project:

* Star the repository
* Fork the project
* Share with others

---

# 📜 License

This project is open-source and available under the MIT License.
