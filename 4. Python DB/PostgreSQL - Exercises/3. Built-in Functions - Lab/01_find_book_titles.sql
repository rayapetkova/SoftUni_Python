SELECT title
FROM books
WHERE title LIKE 'The%'
ORDER BY id;





-- second solution:
--
-- SELECT title
-- FROM books
-- WHERE LEFT(title, 3) = 'The'
-- ORDER BY id;