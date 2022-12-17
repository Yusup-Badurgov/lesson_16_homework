import json
from flask import Flask, Blueprint, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

from sqlmodels import User, Offer, Order

from settings import app, db
api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route("/users", methods=["GET", "POST"])
def page_users():
    if request.method == "GET":
        user_data = [user.get_dict() for user in User.query.all()]
        return json.dumps(user_data), 200

    elif request.method == "POST":
        user_data = json.loads(request.data)

        user_new = User(
            id=user_data.get("id"),
            first_name=user_data.get("first_name"),
            last_name=user_data.get("last_name"),
            age=user_data.get("age"),
            email=user_data.get("email"),
            role=user_data.get("role"),
            phone=user_data.get("phone")
        )
        db.session.add(user_new)
        db.session.commit()
        db.session.close()

        return "Пользователь добавлен", 201


@api_blueprint.route("/users/<int:pk>", methods=["GET", "PUT", "DELETE"])
def users_modification(pk):
    if request.method == "GET":
        return json.dumps(User.query.get(pk).get_dict()), 200

    elif request.method == "PUT":
        user_data = json.loads(request.data)
        user_change = User.query.get(pk)

        user_change.first_name = user_data.get("first_name")
        user_change.last_name = user_data.get("last_name")
        user_change.age = user_data.get("age")
        user_change.email = user_data.get("email")
        user_change.role = user_data.get("role")
        user_change.phone = user_data.get("phone")

        db.session.add(user_change)
        db.session.commit()
        db.session.close()
        return "Пользователь обновлен", 204

    elif request.method == "DELETE":
        user_delete = User.query.get(pk)
        db.session.delete(user_delete)
        db.session.commit()
        db.session.close()
        return "Пользователь удален", 204



@api_blueprint.route("/orders", methods=["GET", "POST"])
def page_orders():
    if request.method == "GET":
        order_data = [order.get_dict() for order in Order.query.all()]
        return json.dumps(order_data), 200

    elif request.method == "POST":
        order = json.loads(request.data)

        order_new = Order(
            id=order.get("id"),
            name=order.get("name"),
            description=order.get("description"),
            start_date=order.get("start_date"),
            end_date=order.get("end_date"),
            address=order.get("address"),
            customer_id=order.get("customer_id"),
            executor_id=order.get("executor_id")
        )

        db.session.add(order_new)
        db.session.commit()
        return "Заказ добавлен", 201


@api_blueprint.route("/orders/<int:pk>", methods=["GET", "PUT", "DELETE"])
def order_modification(pk):
    if request.method == "GET":
        return json.dumps(Order.query.get(pk).get_dict()), 200

    elif request.method == "PUT":
        order_data = json.loads(request.data)
        order_change = Order.query.get(pk)

        order_change.name=order_data.get("name")
        order_change.description=order_data.get("description")
        order_change.start_date=order_data.get("start_date")
        order_change.end_date=order_data.get("end_date")
        order_change.address=order_data.get("address")
        order_change.customer_id=order_data.get("customer_id")
        order_change.executor_id=order_data.get("executor_id")

        db.session.add(order_change)
        db.session.commit()
        return "Заказ обновлен", 204

    elif request.method == "DELETE":
        order_delete = Order.query.get(pk)
        db.session.delete(order_delete)
        db.session.commit()
        return "Заказ удален", 204


@api_blueprint.route("/offers", methods=["GET", "POST"])
def page_offers():
    if request.method == "GET":
        offer_data = [offer.get_dict() for offer in Offer.query.all()]
        return json.dumps(offer_data), 200

    elif request.method == "POST":
        offer = json.loads(request.data)

        offer_new = Offer(
            id=offer.get("id"),
            order_id=offer.get("order_id"),
            executor_id=offer.get("executor_id")
        )

        db.session.add(offer_new)
        db.session.commit()
        return "Исполнитель добавлен", 201


@api_blueprint.route("/offers/<int:pk>", methods=["GET", "PUT", "DELETE"])
def offer_modification(pk):
    if request.method == "GET":
        return json.dumps(Offer.query.get(pk).get_dict()), 200

    elif request.method == "PUT":
        offer_data = json.loads(request.data)
        offer_change = Offer.query.get(pk)

        offer_change.order_id = offer_data.get("order_id")
        offer_change.executor_id = offer_data.get("executor_id")

        db.session.add(offer_change)
        db.session.commit()
        return "Исполнитель обновлен", 204

    elif request.method == "DELETE":
        offer_delete = Offer.query.get(pk)
        db.session.delete(offer_delete)
        db.session.commit()
        return "Исполнитель удален", 204
