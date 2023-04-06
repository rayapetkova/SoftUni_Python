deposit_sum = float(input())
months = int(input())
annual_rate = float(input())

sum = deposit_sum + months * ((deposit_sum * annual_rate / 100) / 12)

print(sum)