from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db:5432/myapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

@app.route('/api/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([{'id': item.id, 'name': item.name} for item in items])

def add_random_items():
    random_items = [
        "Crimson Jacket", "Teal Backpack", "Beige Hat", "Lime Towel", "Navy Gloves", "Maroon Chair", 
        "Cyan Water Bottle", "Ivory Phone Case", "Turquoise Blanket", "Amber Glasses", "Olive Shoes", 
        "Magenta Folder", "Lavender Candle", "Coral Necklace", "Charcoal Notebook", "Mint Headphones", 
        "Peach Cushion", "Indigo Scarf", "Rust Belt", "Fuchsia Earrings"
    ]
    
    existing_items = set(item.name for item in Item.query.all())
    
    for item_name in random_items:
        if item_name not in existing_items:
            new_item = Item(name=item_name)
            db.session.add(new_item)
    
    db.session.commit()
    print("Items added to the database.")

@app.before_first_request
def initialize_app():
    db.create_all()
    add_random_items()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    