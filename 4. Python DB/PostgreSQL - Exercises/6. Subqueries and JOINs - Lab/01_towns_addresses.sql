SELECT addresses.town_id,
towns.name,
addresses.address_text
FROM addresses
JOIN towns ON towns.town_id = addresses.town_id
WHERE towns.name in ('San Francisco', 'Sofia', 'Carnation')
ORDER BY addresses.town_id, addresses.address_id;