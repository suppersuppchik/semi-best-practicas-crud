import pymongo
import schemas
import bson


def get_smartphones(db):
    return db.find()


def add_smartphone(db, smartphone: schemas.CreateSmartphone):
    smartphone_as_dict = smartphone.model_dump()
    db.insert_one(smartphone_as_dict)
    return schemas.CreateSmartphone(**smartphone_as_dict)


def update_smartphone(db, smartphone_id: str, smartphone: schemas.UpdateSmartphone):
    data = dict()
    if smartphone.title:
        data['title'] = smartphone.title
    if smartphone.price:
        data['price'] = smartphone.price
    db.update_one({'_id': bson.ObjectId(smartphone_id)}, {'$set': data})
    return schemas.UpdateSmartphone(**data)


def delete_smartphone(db, smartphone_id: str):
    db.delete_one({"_id": bson.ObjectId(smartphone_id)})
    return schemas.DeleteSmartphone(_id=bson.ObjectId(smartphone_id))
