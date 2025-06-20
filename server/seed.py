from server import create_app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()

def seed_data():
    with app.app_context():
        
        db.session.query(RestaurantPizza).delete()
        db.session.query(Restaurant).delete()
        db.session.query(Pizza).delete()
        db.session.commit()

        restaurants = [
            Restaurant(name="Napoli Nights", address="21 Tuscany Blvd"),
            Restaurant(name="The Cheesy Crust", address="77 Mozzarella Ln"),
            Restaurant(name="Brick Oven Bliss", address="305 Firewood Dr")
        ]
        db.session.add_all(restaurants)
        db.session.commit()

        pizzas = [
            Pizza(name="BBQ Chicken", ingredients="BBQ sauce, mozzarella, grilled chicken, red onions"),
            Pizza(name="Four Cheese", ingredients="Mozzarella, parmesan, cheddar, gorgonzola"),
            Pizza(name="Tropical Delight", ingredients="Tomato sauce, mozzarella, ham, pineapple, bell peppers")
        ]
        db.session.add_all(pizzas)
        db.session.commit()

        restaurant_pizzas = [
            RestaurantPizza(price=10, pizza_id=1, restaurant_id=1),
            RestaurantPizza(price=12, pizza_id=2, restaurant_id=1),
            RestaurantPizza(price=9, pizza_id=3, restaurant_id=2),
            RestaurantPizza(price=11, pizza_id=1, restaurant_id=3),
            RestaurantPizza(price=13, pizza_id=2, restaurant_id=3)
        ]
        db.session.add_all(restaurant_pizzas)
        db.session.commit()

        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_data()
