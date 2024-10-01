import json
from read_data import read_data

def find_all_users_id(data: dict) -> list:
    """ 
    This function will find all the users in the json data and return the list of user IDs.
    
    Parameters:
        data (dict): Dictionary containing the data from the JSON file.
    
    Returns:
        list: List containing all the user IDs.
    """
    res = []
    for message in data['messages']:
        if 'id' in message:
            res.append(message['id'])
    return res

# JSON faylini o'qish va foydalanuvchi ID larini topish
print(find_all_users_id(read_data('data/result.json')))

