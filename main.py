from py_imessage import imessage

phone_number = '1234567890'
apple_id = 'your_apple_id'
password = 'your_password'

with imessage.apple_message_handler(phone_number, apple_id, password) as handler:
    messages = handler.get_messages()
