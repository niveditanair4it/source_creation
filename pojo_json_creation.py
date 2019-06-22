import json
import re

from database.db_config import Base


# attributes = inspect.getmembers(AdminView, lambda a: not (inspect.isroutine(a)))


# dict_attr = AdminView.__dict__
# print(dict_attr)
def camelize_classname(tablename):
    """Produce a 'camelized' class name, e.g. """
    "'words_and_underscores' -> 'WordsAndUnderscores'"
    if tablename.rfind("v1_") > 0:
        tablename = tablename[tablename.rfind("v1_") + 3:]
    return str(tablename[0].upper() + \
               re.sub(r'_([a-z])', lambda m: m.group(1).upper(), tablename[1:]))


def get_table_meta(table_dict, table_col, table_name):
    primary = [x.name for x in table_col.columns if x.primary_key == True][0]
    foreign = [camelize_classname(x.column.table.name) for x in table_col.foreign_keys]
    data = {
        "pojo": table_name,
        "fields": ",".join([x.name for x in table_col.columns]),
        "genCol": primary,
        "manyToOne": ",".join(foreign),
    }
    return data


def get_pojo_json():
    json_data = json.dumps([get_table_meta(c.__dict__, c.__table__, c.__name__) for c in Base.classes])

    return json_data


print(get_pojo_json())

# for c in Base.classes:
#    print(c.__name__)
#    print(get_table_meta(c.__dict__, c.__table__, c.__name__))
#    json_data = [get_table_meta(c.__dict__, c.__table__, c.__name__)]

# print(get_table_meta(Project.__dict__, Project.__table__, "Project"))

# print(get_table_meta(AdminView.__dict__, AdminView.__table__, "AdminView"))

# print(attributes)
# abc = [a for a in attributes if not (a[0].startswith('__') and a[0].endswith('__'))]
# for x in attributes:
#     print({"name":x[0],"attribute_type":x[1]})

# print("abc",abc)
