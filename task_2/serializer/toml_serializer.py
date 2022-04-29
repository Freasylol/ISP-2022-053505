import toml
from serializer import packer
from serializer.serializer import Serializer


class TOMLSerializer(Serializer):

    def dumps(self, obj):
        return toml.dumps(packer.pack(obj))

    def loads(self, string):
        return packer.unpack(toml.loads(string))
