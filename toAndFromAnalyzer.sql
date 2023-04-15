SELECT
    count(*) AS message_count,
    sum(length(message.text)) AS character_count,
    sum(length(message.text)) / 3000 AS estimated_page_count, -- not sure where I got this number, but it seems reasonable
    message.is_from_me,
FROM
    chat
    JOIN chat_message_join ON chat. "ROWID" = chat_message_join.chat_id
    JOIN message ON chat_message_join.message_id = message. "ROWID"
WHERE
    chat.chat_identifier = 'fill in identifier'
GROUP BY
    message.is_from_me;