from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data with Kenyan butcher names
vendors = {
    "1": {
        "name": "Kwa Maina's Butchery",
        "specialty": "Premium Beef",
        "location": "Burma Market, Stall 12",
        "rating": "4.5 ★"
    },
    "2": {
        "name": "Mama Nia's Fresh Meat",
        "specialty": "Goat & Mutton",
        "location": "Burma Market, Stall 25",
        "rating": "4.2 ★"
    },
    "3": {
        "name": "Bwana Asman's Halal Meat",
        "specialty": "Halal Certified",
        "location": "Burma Market, Stall 8",
        "rating": "4.7 ★"
    }
}

meat_types = [
    "Beef - Fillet", "Beef - Chuck", "Beef - Stewing",
    "Goat Meat", "Mutton", "Chicken Whole", "Chicken Pieces"
]

@app.route('/')
def home():
    return render_template('index.html', vendors=vendors)

@app.route('/order/<vendor_id>', methods=['GET', 'POST'])
def order(vendor_id):
    vendor = vendors.get(vendor_id)
    if not vendor:
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        # Process the order (in a real app, save to database)
        name = request.form.get('name')
        phone = request.form.get('phone')
        meat_type = request.form.get('meat_type')
        quantity = request.form.get('quantity')
        
        print(f"New Order: {quantity}kg of {meat_type} from {vendor['name']} for {name} ({phone})")
        
        return render_template('order.html', 
                            vendor=vendor, 
                            meat_types=meat_types,
                            success=True)
    
    return render_template('order.html', 
                         vendor=vendor, 
                         meat_types=meat_types,
                         success=False)

if __name__ == '__main__':
    app.run(debug=True)