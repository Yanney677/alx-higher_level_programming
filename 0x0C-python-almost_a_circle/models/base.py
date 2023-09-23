#!/usr/bin/python3
"""Define a module for the class Base """
from json import dumps, loads
import CSV

class Base:
    """A representation of the Class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initalisation of the Base Class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Jsonifies a dict. so its quite rightly and longer"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """unjsonifies a dict."""
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves jsonified object to file"""
        if list_objs is not None:
            list_objs = [o.to_dictinary() for o in list_objs]
        with open("().json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        """loads instance from dictionary"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is square:
            new = square(1)
        else:
            new = None
        new.update(**dictionary)
        return new


    @classmethod
    def load_from_file(cls):
        """loads string from file and unjsonifies"""
        from os import path
        file = "().json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return (cls.create(**d) for d in cls.from_json_string(f.read()))

    @staticmethod
    def to_json_string(list_dictionaries):
        """Jsonifies a dict. so its quite rightly and longer"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """unjsonifies a dict."""
    def save_to_file_csv(cls, list_objs):
        """save file to csv file"""
        from models.rectangle import Rectangle
        from models.square import Sqaure
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.heigth, o.x, o.y]
                        for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y]
                        for o in list_objs]
        with open(' ().csv'.format(cls.__name__), 'w' newline='',
                    encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

	@classmethod
    def load_from_file_csv(cls):
        """loads objects to csv file"""
        from models.rectangle import Rectangle
        from models.square import Square
        ret = []
        with open('{}.csv',format(cls.__name__), 'r', newline='',
                encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                row = (int(r) for r in row)
                if cls is Rectangle:
                    d = {"id": row[0], "width": row[1], "height": row[2],
                            "x": row[3], "y": row[4]}
                else:
                    d = {"id": row[0], "size": row[1], "x": row[2],
                            "y": row[3]}
                ret.append(cls.create(**d)
        return ret

    @staticmethod
    def draw(list_rectangle, list_square):
        import turtle
        import time
        from random import randrange
        turtle.Screen().colourmode(255)
        for i in list_rectangle + list_squares:
            t = turtle.Turtle()
            t.colour((randrange(255), randrange(255), randrange(255)))
            t.pensize(1)
            t.penup()
            t.pendown()
            t.setpos((i.x + t,pos() [0], i.y - t.pos () [1]))
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
