from server import emolytics
import importlib

def load_dataset():
    load_function = emolytics.config.get('LOAD_FUNCTION')
    mod_name, func_name = load_function.rsplit('.',1)
    mod = importlib.import_module(mod_name)
    func = getattr(mod, func_name)
    return func()
