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
    message_count DESC;