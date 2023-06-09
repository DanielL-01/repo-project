import logging
from datetime import datetime 

def record_log(original_function):
    logging.basicConfig(filename="{}.log".format(original_function.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info("Ran with args: {} and kwargs {}".format(datetime.now(),args,kwargs))
        return original_function(*args, **kwargs)

    return wrapper

@record_log
def display_info(name, age, school="IGS Palembang"):
    print("display_info ran with arguments ({} {} {})".format(name, age, school))

@record_log
def display_Something(*args, **kwargs):
    print(f"DONE! {args}, {kwargs}")

display_info("Kevin", 10)
display_Something("1px", "solid", "Black", margin="10px")