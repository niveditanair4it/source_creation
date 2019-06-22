import inspect

from database.db_config import AdminView

attributes = inspect.getmembers(AdminView, lambda a: not (inspect.isroutine(a)))
abc = [a for a in attributes if not (a[0].startswith('__') and a[0].endswith('__'))]
print(attributes)
print(abc)
