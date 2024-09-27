import inspect

def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = dir(obj)

    def methods():
        return methods.__dir__()

    module = obj.__class__.__module__

    dictionary = {'type': obj_type, 'attributes': attributes, 'methods': methods(), 'module': module}
    return dictionary


info = introspection_info(48)
print(info)
string_info = introspection_info('Строка')
print(string_info)
dict_info = introspection_info({'Ряд': 9})
print(dict_info)