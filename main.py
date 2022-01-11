from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates', static_folder='static')

orders = {}
finished_orders = []


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        order_name = request.form['Name']
        order_location = request.form['Location']
        order_foods = request.form['Foods']
        orders.update({order_name: [order_location, order_foods]})
    return render_template("index.html")


@app.route("/coffee", methods=["GET"])
def coffee():
    return render_template("coffee.html")


@app.route("/partners", methods=["GET"])
def partners():
    return render_template("partners.html")


@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")


@app.route("/employee-portal/orders", methods=["GET"])
def employee_portal():
    return f"Orders: {orders}\n Finished Orders: {finished_orders}"


@app.route("/employee-portal/remove/<order_name>", methods=["GET"])
def remove(order_name):
    finished_orders.append(order_name)
    del orders[order_name]
    return f"removed order from {order_name}!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6969)
