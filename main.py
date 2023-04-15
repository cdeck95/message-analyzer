import pandas as pd
import emoji
import io

# Function to count emojis in a text
def count_emojis(text):
    return sum(char in emoji.EMOJI_DATA for char in text)


# Read the CSV file
messages = pd.read_csv('./example_imessages.csv', parse_dates=['Message Date','Delivered Date','Read Date','Edited Date'])

# Display the first 5 rows of the DataFrame
print(messages.head())

# Perform any analysis, such as counting messages per sender
sender_counts = messages['Sender Name'].value_counts()
print(sender_counts)

# Iterate over each message and print the contents
for index, message in messages.iterrows():
    # Apply the count_emojis function to the "Text" column and create a new column "Emoji_Count"
    messages['Emoji_Count'] = messages['Text'].apply(count_emojis)
    # messageTxt = emoji.emojize(message['Text'], language="en")
    messageTxt = message['Text']
    type = message['Type']
    senderName = message['Sender Name']
    chatSession = message['Chat Session']
    if type=='Outgoing':
        to=chatSession
        sender='Me'
    else:
        to='Me'
        sender=chatSession
    print(f"Timestamp: {message['Message Date']}")
    print(f"Sender: {message['Sender Name']}")
    print(f"Receiver: {to}")
    print(f"Text: {messageTxt}")
    print(f"Emoji count: {count_emojis(messageTxt)}")
    print(f"Attachments: {message['Attachment']}")
    print()  # Print an empty line for readability

