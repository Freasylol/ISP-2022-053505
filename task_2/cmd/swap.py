from serializer.serializer_factory import *
from cmd.args_parser import ArgsParser

dump_in, load_from = ArgsParser.getargs()


def get_creator(filename: str) -> SerializerCreator | None:
    filetype = filename.lower().split('.')[-1]
    creators = {
        'json': JSONSerializerCreator,
        'yaml': YAMLSerializerCreator,
        'toml': TOMLSerializerCreator
    }
    return creators.get(filetype, None)


def dump(obj, filename: str) -> any:
    creator = get_creator(filename)
    if creator is None:
        return None
    ser = creator().create_serializer()
    ser.dump(obj, filename)
    obj = ser.load(filename)

    print('Object dumped')
    return obj


def load(filename: str) -> any:
    creator = get_creator(filename)
    if creator is None:
        return None
    ser = creator().create_serializer()
    item = ser.load(filename)

    print('Object loaded')
    return item


def convert():
    global obj
    if load_from is not None:
        obj = load(''.join(load_from))

    if dump_in is not None:
        dump(obj, ''.join(dump_in))
