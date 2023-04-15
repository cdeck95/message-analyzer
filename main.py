import pandas as pd

# Read the CSV file
messages = pd.read_csv('./example_imessages.csv', parse_dates=['timestamp'])

# Display the first 5 rows of the DataFrame
print(messages.head())

# Perform any analysis, such as counting messages per sender
sender_counts = messages['sender'].value_counts()
print(sender_counts)

# You can also analyze the content of messages, dates, and other information

# Iterate over each message and print the contents
for index, message in messages.iterrows():
    print(f"Timestamp: {message['timestamp']}")
    print(f"Sender: {message['sender']}")
    print(f"Receiver: {message['receiver']}")
    print(f"Text: {message['text']}")
    print()  # Print an empty line for readability