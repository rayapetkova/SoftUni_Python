SELECT title, to_char(cost, '99.999') AS "modified_price"
FROM books
ORDER BY id;