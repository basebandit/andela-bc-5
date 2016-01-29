
def data_type(my_data_type):
    if isinstance(my_data_type, str):
        return len(my_data_type)
    elif my_data_type == None:
        return 'no value'
    elif isinstance(my_data_type, bool):
        return my_data_type
    elif isinstance(my_data_type, int):
        if my_data_type > 100:
            return 'more than 100'
        elif my_data_type < 100:
            return 'less than 100'
        elif my_data_type == 100:
            return 'equal to 100'
    elif isinstance(my_data_type, list):
        if len(my_data_type) >= 3:
            return my_data_type[2]
        else:
            return None

print(data_type(None))