from read_data import read_data
from find_all_users_id import find_all_users_id

def find_user_message_counts(data: dict) -> dict:
    """
    Bu funksiya har bir foydalanuvchining xabarlar sonini topadi.
    
    Parametrlar:
        data (dict): JSON faylidan olingan ma'lumotlar lug'ati.
    Qaytadi:
        dict: Foydalanuvchilar ID lariga muvofiq xabarlar soni.
    """
    message_counts = []
    messages = data['messages']
    
    for msg in messages:
        if msg['type'] == 'message':
            user_id = msg['from_id']  # Xabarning yuboruvchisi ID sini olish
            if user_id not in message_counts:
                message_counts[user_id] = 0  # Foydalanuvchi ID si uchun boshlang'ich qiymat
            message_counts[user_id] += 1  # Xabarlar sonini oshirish

    return message_counts

# JSON faylini o'qish
data = read_data('data/result.json')

# Har bir foydalanuvchining xabarlar sonini hisoblash
user_message_counts = find_user_message_counts(data)

# Natijani chiqarish
print(user_message_counts)