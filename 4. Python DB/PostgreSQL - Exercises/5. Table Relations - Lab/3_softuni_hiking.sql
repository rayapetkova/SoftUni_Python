SELECT start_point,
       end_point,
		   leader_id,
CONCAT(campers.first_name, ' ', campers.last_name)
FROM routes
JOIN campers ON campers.id = routes.leader_id;