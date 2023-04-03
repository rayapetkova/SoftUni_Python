n = int(input())
dictionary = {}

for i in range(n):
    line = input().split()
    hero_name, hp, mp = line[0], int(line[1]), int(line[2])
    dictionary[hero_name] = {'hp': hp, 'mp': mp}

while True:
    line = input()
    if line == "End":
        break
    command = line.split(" - ")
    hero = command[1]
    if "CastSpell" in command:
        mp_needed, spell_name = int(command[2]), command[3]
        if dictionary[hero]['mp'] >= mp_needed:
            dictionary[hero]['mp'] -= mp_needed
            print(f"{hero} has successfully cast {spell_name} and now has {dictionary[hero]['mp']} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")
    elif "TakeDamage" in command:
        damage, attacker = int(command[2]), command[3]
        dictionary[hero]['hp'] -= damage
        if dictionary[hero]['hp'] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {dictionary[hero]['hp']} HP left!")
        else:
            print(f"{hero} has been killed by {attacker}!")
            del dictionary[hero]
    elif "Recharge" in command:
        amount = int(command[2])
        if dictionary[hero]['mp'] + amount > 200:
            print(f"{hero} recharged for {200 - dictionary[hero]['mp']} MP!")
            dictionary[hero]['mp'] = 200
        else:
            dictionary[hero]['mp'] += amount
            print(f"{hero} recharged for {amount} MP!")
    elif "Heal" in command:
        amount = int(command[2])
        current_hp = dictionary[hero]['hp']
        dictionary[hero]['hp'] = min(current_hp + amount, 100)
        if dictionary[hero]['hp'] == 100:
            print(f"{hero} healed for {100 - current_hp} HP!")
        else:
            print(f"{hero} healed for {amount} HP!")

for key, value in dictionary.items():
    print(f"{key}\n  HP: {value['hp']}\n  MP: {value['mp']}")