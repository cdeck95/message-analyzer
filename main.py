import pandas as pd
import emoji
import io
import sqlite3

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

query2 = """
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

results2 = execute_query(query2)

# Handle the results
for row in results2:
    group_chat_name = row[0]
    message_count = row[1]
    #group_chat_name_with_emojis = emoji.emojize(group_chat_name, language="en")
    print(f"Group Chat: {group_chat_name} || Messages exchanged: {message_count}")

drunkQuery = """
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

drunkResults = execute_query(drunkQuery)

# Handle the results
for row in drunkResults:
    group_chat_name = row[0]
    message_count = row[1]
    #group_chat_name_with_emojis = emoji.emojize(group_chat_name, language="en")
    print(f"Group Chat: {group_chat_name} || Messages exchanged: {message_count}")


