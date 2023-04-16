import pandas as pd
import emoji
import io
import sqlite3
import datetime

def execute_query(query):
    # Connect to the database file
    conn = sqlite3.connect('messages.sqlite')
    cursor = conn.cursor()

    # Execute the query
    cursor.execute(query)
    results = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Return the results
    return results

def execute_contacts_query(query):
    # Connect to the database file
    conn = sqlite3.connect('contacts.sqlite')
    cursor = conn.cursor()

    # Execute the query
    cursor.execute(query)
    results = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Return the results
    return results

query = """
    SELECT
        chat.chat_identifier,
        count(chat.chat_identifier) AS message_count
    FROM
        chat
        JOIN chat_message_join ON chat. "ROWID" = chat_message_join.chat_id
        JOIN message ON chat_message_join.message_id = message. "ROWID"
    GROUP BY
        chat.chat_identifier
    ORDER BY
        message_count DESC
    LIMIT 25;
"""

results = execute_query(query)

# Handle the results
for row in results:
    phone_number = row[0]
    message_count = row[1]
    print(f"Phone number: {phone_number}, Messages exchanged: {message_count}")

groupMessageQuery = """
    SELECT
        chat.display_name,
        count(chat.display_name) AS group_message_count
    FROM
        chat
        JOIN chat_message_join ON chat. "ROWID" = chat_message_join.chat_id
        JOIN message ON chat_message_join.message_id = message. "ROWID"
    GROUP BY
        chat.display_name
    ORDER BY
        group_message_count DESC
    LIMIT 25;
"""

groupMessageCount = execute_query(groupMessageQuery)

# Handle the results
for row in groupMessageCount:
    group_chat_name = row[0]
    message_count = row[1]
    #group_chat_name_with_emojis = emoji.emojize(group_chat_name, language="en")
    print(f"Group Chat: {group_chat_name} || Messages exchanged: {message_count}")

drunkQuery = """
    SELECT
        chat.chat_identifier,
        count(chat.chat_identifier) AS message_count
    FROM
        chat
        JOIN chat_message_join ON chat. "ROWID" = chat_message_join.chat_id
        JOIN message ON chat_message_join.message_id = message. "ROWID"
    WHERE
    -- Check if the message date falls within the specified time range
    (strftime('%w', datetime((date - 978307200000000000) / 1000000000, 'unixepoch')) = '5' AND strftime('%H', datetime((date - 978307200000000000) / 1000000000, 'unixepoch')) >= '23') OR -- Friday 11pm or later
    (strftime('%w', datetime((date - 978307200000000000) / 1000000000, 'unixepoch')) = '6') OR -- Saturday
    (strftime('%w', datetime((date - 978307200000000000) / 1000000000, 'unixepoch')) = '0' AND strftime('%H', datetime((date - 978307200000000000) / 1000000000, 'unixepoch')) < '03') -- Sunday before 3am
    GROUP BY
        chat.chat_identifier
    ORDER BY
        message_count DESC
    LIMIT 25;
    """

drunkResults = execute_query(drunkQuery)

# Handle the results
for row in drunkResults:
    phone_number = row[0]
    message_count = row[1]
    print(f"Phone number: {phone_number}, Messages exchanged: {message_count}")

monthQuery = """
    SELECT 
        strftime('%m', datetime((date - 978307200000000000) / 1000000000, 'unixepoch')) AS month,
        COUNT(*) AS message_count
    FROM 
        message
    GROUP BY 
        strftime('%m', datetime((date - 978307200000000000) / 1000000000, 'unixepoch'))
    ORDER BY 
        month DESC
    """

monthResults = execute_query(monthQuery)
highestMessageCount = 0
mostActiveMonth = "00"
lowestMessageCount = 0
leastActiveMonth = "00"

# Handle the results
for row in monthResults:
    month = row[0]
    message_count = row[1]
    print(f"Month: {month}, Messages exchanged: {message_count}")

    if(message_count > highestMessageCount):
                highestMessageCount = message_count
                mostActiveMonth = month
    if(lowestMessageCount == 0):
        lowestMessageCount = message_count
        leastActiveMonth = month
    elif(message_count < lowestMessageCount):
        lowestMessageCount = message_count
        leastActiveMonth = month

print(f"Most Active Month: {mostActiveMonth}, Messages exchanged: {highestMessageCount}")
print(f"Least Active Month: {leastActiveMonth}, Messages exchanged: {lowestMessageCount}")


contactNamesQuery = """
Select
	ABPerson.First,
	ABPerson.Last,
	ABMultiValue.value
from
	ABPerson,
	ABMultiValue
where
	ABPerson.ROWID = ABMultiValue.record_id
order by
	ABPerson.First,
	ABPerson.Last
LIMIT 100;

    """

contactNameResults = execute_contacts_query(contactNamesQuery)

# Handle the results
for row in contactNameResults:
    print(row)

