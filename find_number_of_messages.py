from read_data import read_data

def find_number_of_messages(data: dict)->int:
    """
    Get the total number of messages.

    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        int: Total number of messages.
    
    """
    count = 0
    messages = data['messages']
    for msg in messages:
        if msg['type'] == 'message':
            count += 1
    return count
print(find_number_of_messages(read_data('data/result.json')))