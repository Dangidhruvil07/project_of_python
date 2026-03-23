from flask import Flask, render_template, request, redirect , url_for , flash
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/ecommerce" 
mongo = PyMongo(app)
 
db = mongo.db
users = db.users
#  LOGIN

from flask import session

app.secret_key = "secret123"   # add this at top

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = mongo.db.users.find_one({
            "email": email,
            "password": password
        })

        if user:
            session["user"] = email   #  store email
            return redirect("/products")
        else:
            return render_template("login.html", error="Invalid email or password ")

    return render_template("login.html")



#  REGISTER

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        confirm = request.form["confirm_password"]
        if password != confirm:
            return render_template("register.html", error="Passwords do not match ")

        # check existing user
        existing_user = mongo.db.users.find_one({"email": email})
        if existing_user:
            return render_template("register.html", error="User already exists ")

        mongo.db.users.insert_one({
            "name": name,
            "email": email,
            "password": password
        })

        return redirect("/")   # go to login

    return render_template("register.html")



#  PRODUCTS
@app.route("/products")
def products():
    if "user" not in session:
        return redirect("/")

    all_products = list(mongo.db.products.find())

    return render_template("products.html", products=all_products)
# category
@app.route("/category/<cat>")
def category(cat):

    if "user" not in session:
        return redirect("/")

    filtered_products = list(mongo.db.products.find({"category": cat}))

    return render_template("products.html", products=filtered_products)
#  CART
@app.route("/cart")
def cart():

    if "user" not in session:
        return redirect("/")

    items = list(mongo.db.cart.find({"email": session["user"]}))

    total = sum(item["price"] * item.get("quantity", 1) for item in items)

    return render_template("cart.html", cart_items=items, total=total)

#check the addtocart
@app.route("/add_to_cart/<id>")
def add_to_cart(id):

    from bson.objectid import ObjectId
    from flask import session, redirect, request, flash

    if "user" not in session:
        return redirect("/")

    try:
        product = mongo.db.products.find_one({"_id": ObjectId(id)})
    except:
        return "Invalid Product ID ❌"

    if not product:
        return "Product Not Found ❌"

    item = mongo.db.cart.find_one({
        "name": product["name"],
        "email": session["user"]
    })

    if item:
        mongo.db.cart.update_one(
            {"_id": item["_id"]},
            {"$inc": {"quantity": 1}}
        )
    else:
        mongo.db.cart.insert_one({
            "name": product["name"],
            "price": int(product["price"]),
            "image": product["image"],
            "quantity": 1,
            "email": session["user"]
        })

    flash("Added to cart ✅")

    return redirect(request.referrer)  # 🔥 MAGIC LINE

from flask import session
@app.route("/checkout")
def checkout():

    if "user" not in session:
        return redirect("/")

    cart_items = list(mongo.db.cart.find({"email": session["user"]}))

    if cart_items:
        total = sum(item["price"] * item.get("quantity", 1) for item in cart_items)

        mongo.db.orders.insert_one({
            "email": session["user"],
            "items": cart_items,
            "total": total
        })

        mongo.db.cart.delete_many({"email": session["user"]})

        return render_template("checkout.html", total=total)

    return "Cart is Empty"


from bson.objectid import ObjectId

@app.route("/remove/<id>")
def remove(id):
    mongo.db.cart.delete_one({"_id": ObjectId(id)})
    return redirect("/cart")

# my orders

@app.route("/myorders")
def myorders():
    from flask import session

    if "user" not in session:
        return redirect("/login")

    orders = mongo.db.orders.find({
        "email": session["user"]
    }).sort("_id",-1)

    return render_template("myorders.html", orders=orders)

@app.route("/logout")
def logout():
    session.pop("user", None)   #  remove user
    return redirect("/")        # go to login page


# RUN APP

if __name__ == "__main__":
    app.run(debug=True, port=7000)