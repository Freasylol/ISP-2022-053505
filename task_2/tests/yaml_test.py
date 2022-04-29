import os
from serializer import yaml_serializer as yaml
from tests import spanickroon

import math

def test_dumps_and_loads():
    ser = yaml.YAMLSerializer()
    s = ser.dumps(spanickroon.f)
    fun = ser.loads(s)
    assert math.sin(42 * 123 * 0) == fun(0)


def test_dump_and_load():
    ser = yaml.YAMLSerializer()
    file = open("test.yaml", "w")

    ser.dump(spanickroon.f, file.name)
    fun = ser.load(file.name)

    file.close()
    os.remove(os.path.abspath(file.name))

    assert math.sin(42 * 123 * 0) == fun(0)
