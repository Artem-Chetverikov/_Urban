import inspect
from pprint import pprint


def introspection_info(obj):
    dict_discr = dict()
    dict_discr['type'] = str(type(obj)).split("'")[1]
    methods = []
    attributes = []
    attr_and_metods = dir(obj)
    for item in attr_and_metods:
        if callable(getattr(obj, item)):
            methods.append(item)
        else:
            attributes.append(item)

    dict_discr['attributes'] = attributes
    dict_discr['methods'] = methods
    dict_discr['module'] = inspect.getmodule(obj)

    return dict_discr


class ForCheck:
    def __init__(self):
        self.attr_check = 11

    def func_check(self):
        print('check')


exeple_ = ForCheck()

number_info = introspection_info(exeple_)
pprint(number_info)

number_info_1 = introspection_info(42)
pprint(number_info_1)
