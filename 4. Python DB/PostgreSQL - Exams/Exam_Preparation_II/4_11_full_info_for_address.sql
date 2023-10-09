CREATE TABLE search_results (
    id SERIAL PRIMARY KEY,
    address_name VARCHAR(50),
    full_name VARCHAR(100),
    level_of_bill VARCHAR(20),
    make VARCHAR(30),
    condition CHAR(1),
    category_name VARCHAR(50)
);



CREATE OR REPLACE PROCEDURE sp_courses_by_address(
	address_name IN VARCHAR(100)
)
AS
$$
   BEGIN
   		 TRUNCATE TABLE search_results;

   	     INSERT INTO search_results(address_name, full_name, level_of_bill, make, condition, category_name)
		 SELECT
		 	    a.name,
				clients.full_name,
				CASE
					 WHEN courses.bill <= 20 THEN 'Low'
					 WHEN courses.bill <= 30 THEN 'Medium'
					 ELSE 'High'
				END,
				cars.make,
				cars.condition,
				categories.name
		  FROM addresses AS "a"
		  JOIN courses ON a.id = courses.from_address_id
		  JOIN clients ON courses.client_id = clients.id
		  JOIN cars ON courses.car_id = cars.id
		  JOIN categories ON cars.category_id = categories.id
		  WHERE a.name = address_name
		  ORDER BY cars.make ASC, clients.full_name ASC;
   END;
$$
LANGUAGE plpgsql;