from flask_sqlalchemy import SQLAlchemy
import json
from flask import Flask
from settings import app, db

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    email = db.Column(db.String(100))
    role = db.Column(db.String(100))
    phone = db.Column(db.String(20))

    def get_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "email": self.email,
            "role": self.role,
            "phone": self.phone
        }


class Order(db.Model):
    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(300))
    start_date = db.Column(db.String)
    end_date = db.Column(db.String)
    address = db.Column(db.String(200))
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def get_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "address": self.address,
            "customer_id": self.customer_id,
            "executor_id": self.executor_id
        }

class Offer(db.Model):
    __tablename__ = "offer"
    id = db.Column(db.Integer,  primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def get_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "executor_id": self.executor_id
        }

def read_json(file_name):
    with open(file_name, "r", encoding='UTF-8') as read_file:
        return json.load(read_file)


def init_database():
    db.drop_all()
    db.create_all()

    users = read_json("data/users.json")
    orders = read_json("data/orders.json")
    offers = read_json("data/offers.json")

    for user in users:
        user_new = User(
            id=user.get("id"),
            first_name=user.get("first_name"),
            last_name=user.get("last_name"),
            age=user.get("age"),
            email=user.get("email"),
            role=user.get("role"),
            phone=user.get("phone")
        )

        db.session.add(user_new)
        db.session.commit()




    for order in orders:
        order_new = Order(
            id = order.get("id"),
            name = order.get("name"),
            description =order.get("description"),
            start_date = order.get("start_date"),
            end_date = order.get("end_date"),
            address = order.get("address"),
            customer_id = order.get("customer_id"),
            executor_id = order.get("executor_id")
        )

        db.session.add(order_new)
        db.session.commit()




    for offer in offers:
        offer_new = Offer(
            id=offer.get("id"),
            order_id=offer.get("order_id"),
            executor_id = offer.get("executor_id")
        )

        db.session.add(offer_new)
        db.session.commit()



