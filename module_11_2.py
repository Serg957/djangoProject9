
import inspect
def introspection_info(obj):
    obj_type = type(obj)
    obj_attributes = dir(obj)

    def methods():
        callable(methods)
        return (methods.__dir__())

    module = obj.__class__.__module__


    dictionary = {'type': obj_type, 'attributes': obj_attributes, 'methods': methods(), 'module': module}

    return dictionary


number_info = introspection_info(42)
print(number_info)