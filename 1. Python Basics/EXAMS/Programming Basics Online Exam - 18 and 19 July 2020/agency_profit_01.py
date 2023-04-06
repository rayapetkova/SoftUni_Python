name = input()
adult_tickets_num = int(input())
kids_tickets_num = int(input())
net_price_for_one_adult_ticket = float(input())
service_fee = float(input())

net_price_for_one_kid_ticket = net_price_for_one_adult_ticket - ((70 / 100) * net_price_for_one_adult_ticket)
price_for_adult_ticket_with_service_fee = net_price_for_one_adult_ticket + service_fee
price_for_kid_ticket_with_service_fee = net_price_for_one_kid_ticket + service_fee
price = (adult_tickets_num * price_for_adult_ticket_with_service_fee) + (kids_tickets_num * price_for_kid_ticket_with_service_fee)
total_price = (20 / 100) * price
print(f"The profit of your agency from {name} tickets is {total_price:.2f} lv.")