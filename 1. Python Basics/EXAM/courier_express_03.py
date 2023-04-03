shipment_weight_in_kg = float(input())
type_service = input()
distance_in_km = int(input())
total = 0

if type_service == "standard":
    if shipment_weight_in_kg < 1:
        price = 3
        total = (distance_in_km * price) / 100
    elif 1 <= shipment_weight_in_kg < 10:
        price = 5
        total = (distance_in_km * price) / 100
    elif 10 <= shipment_weight_in_kg < 40:
        price = 10
        total = (distance_in_km * price) / 100
    elif 40 <= shipment_weight_in_kg < 90:
        price = 15
        total = (distance_in_km * price) / 100
    elif 90 <= shipment_weight_in_kg < 150:
        price = 20
        total = (distance_in_km * price) / 100

elif type_service == "express":
    if shipment_weight_in_kg < 1:
        price = 3
        transport_price = (distance_in_km * price) / 100
        price_in_lv = price / 100
        markup_kg = (80 / 100) * price_in_lv
        markup_km = shipment_weight_in_kg * markup_kg
        all_markup = distance_in_km * markup_km
        total = transport_price + all_markup
    elif 1 <= shipment_weight_in_kg < 10:
        price = 5
        transport_price = (distance_in_km * price) / 100
        price_in_lv = price / 100
        markup_kg = (40 / 100) * price_in_lv
        markup_km = shipment_weight_in_kg * markup_kg
        all_markup = distance_in_km * markup_km
        total = transport_price + all_markup
    elif 10 <= shipment_weight_in_kg < 40:
        price = 10
        transport_price = (distance_in_km * price) / 100
        price_in_lv = price / 100
        markup_kg = (5 / 100) * price_in_lv
        markup_km = shipment_weight_in_kg * markup_kg
        all_markup = distance_in_km * markup_km
        total = transport_price + all_markup
    elif 40 <= shipment_weight_in_kg < 90:
        price = 15
        transport_price = (distance_in_km * price) / 100
        price_in_lv = price / 100
        markup_kg = (2 / 100) * price_in_lv
        markup_km = shipment_weight_in_kg * markup_kg
        all_markup = distance_in_km * markup_km
        total = transport_price + all_markup
    elif 90 <= shipment_weight_in_kg < 150:
        price = 20
        transport_price = (distance_in_km * price) / 100
        price_in_lv = price / 100
        markup_kg = (1 / 100) * price_in_lv
        markup_km = shipment_weight_in_kg * markup_kg
        all_markup = distance_in_km * markup_km
        total = transport_price + all_markup

print(f"The delivery of your shipment with weight of {shipment_weight_in_kg:.3f} kg. would cost {total:.2f} lv.")