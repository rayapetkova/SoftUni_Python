SELECT driver_id,
       vehicle_type,
       CONCAT(campers.first_name, 
              ' ', 
              campers.last_name)
FROM vehicles
INNER JOIN campers 
ON campers.id = vehicles.driver_id