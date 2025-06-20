🍕 Pizza Restaurant API
A Flask RESTful API for managing pizza restaurants, built with SQLAlchemy and Flask-Migrate. Implements an MVC-style architecture with support for restaurant-pizza relationships.

🚀 Quick Start
1. Install Dependencies

pipenv install flask flask-sqlalchemy flask-migrate
pipenv shell

2. Set Up the Database

export FLASK_APP=server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

3. Seed the Database and Run the Server

python server/seed.py
python server/app.py

Server will run at: http://127.0.0.1:5000

📦 API Endpoints
📍 Restaurants
GET /restaurants
→ Returns a list of all restaurants

GET /restaurants/<id>
→ Returns a specific restaurant and its pizzas
→ Returns 404 if not found

DELETE /restaurants/<id>
→ Deletes a restaurant and its relationships
→ Returns 204 on success, 404 if not found

🍕 Pizzas
GET /pizzas
→ Returns a list of all pizzas

🔗 Restaurant-Pizza Relationships
POST /restaurant_pizzas
→ Creates a new relationship between a restaurant and a pizza

Request Body Example:

{
  "price": 15,
  "pizza_id": 1,
  "restaurant_id": 2
}

Note:

price must be an integer between 1 and 30 (inclusive)

🗂️ Project Structure
server/
├── app.py                  # Application entry point
├── config.py               # Database configuration
├── models/                 # SQLAlchemy models
│   ├── restaurant.py
│   ├── pizza.py
│   └── restaurant_pizza.py
├── controllers/            # API route handlers (blueprints)
└── seed.py                 # Sample data seeder

🧠 Models
Restaurant
Fields: id, name, address

Pizza
Fields: id, name, ingredients

RestaurantPizza
Fields: id, price (1-30), restaurant_id, pizza_id

Deleting a restaurant automatically removes its associated restaurant-pizza relationships (cascade delete).

🧪 Testing
You can use Postman to test the API endpoints:

Import the provided file:
challenge-1-pizzas.postman_collection.json