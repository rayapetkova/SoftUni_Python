SELECT name, start_date
FROM projects
WHERE name in ('Mountain', 'Road', 'Touring')
LIMIT 20;