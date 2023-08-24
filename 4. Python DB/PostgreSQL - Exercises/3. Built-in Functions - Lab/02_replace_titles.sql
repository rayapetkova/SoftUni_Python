UPDATE books
SET title = REPLACE(title, 'The', '***')
WHERE title LIKE 'The%';

SELECT title
FROM books
WHERE title LIKE '***%'
ORDER BY id;