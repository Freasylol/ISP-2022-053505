import sys
import os
from serializer import json_serializer as json
from tests import spanickroon
import math

def test_func_dumps_and_loads():
    ser = json.JSONSerializer()
    s = ser.dumps(spanickroon.f)
    fun = ser.loads(s)
    assert isinstance(fun(0), float)


def test_func_dump_and_load():
    ser = json.JSONSerializer()
    file = open("test.json", "w")

    ser.dump(spanickroon.f, file.name)
    fun = ser.load(file.name)

    file.close()
    os.remove(os.path.abspath(file.name))

    assert math.sin(42 * 123 * 0) == fun(0)

ser = json.JSONSerializer()

def test_obj_dump_and_load():
    ser = json.JSONSerializer()

    obj = ser.loads(ser.dumps(spanickroon.spanickroon_object))
    assert str(type(obj)) == str(type(spanickroon.spanickroon_object))