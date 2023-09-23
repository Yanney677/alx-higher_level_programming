#!/usr/bin/python3
"""Define a module for the class Base """
from json import dumps, loads

class Base:
    """A representation of the Class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of the Base Class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Jsonify a list of dictionaries."""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Unjsonify a list of dictionaries."""
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save objects to a JSON file"""
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        """Create an instance from a dictionary"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Load objects from a JSON file"""
        from os import path
        filename = "{}.json".format(cls.__name__)
        if not path.isfile(filename):
            return []
        with open(filename, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save objects to a CSV file"""
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y] for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y] for o in list_objs]
        filename = "{}.csv".format(cls.__name__)
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """Load objects from a CSV file"""
        from models.rectangle import Rectangle
        from models.square import Square
        ret = []
        filename = "{}.csv".format(cls.__name__)
        with open(filename, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    d = {"id": row[0], "width": row[1], "height": row[2],
                            "x": row[3], "y": row[4]}
                else:
                    d = {"id": row[0], "size": row[1], "x": row[2],
                            "y": row[3]}
                ret.append(cls.create(**d))
        return ret

    @staticmethod
    def draw(list_rectangle, list_square):
        """Draw objects using the Turtle graphics library"""
        import turtle
        import time
        from random import randrange
        for i in list_rectangle + list_square:
            t = turtle.Turtle()
            t.color((randrange(255), randrange(255), randrange(255)))
            t.pensize(1)
            t.penup()
            t.setpos((i.x + t.pos()[0], i.y - t.pos()[1]))
            t.pendown()
            t.pensize(10)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.end_fill()

        time.sleep(5)

