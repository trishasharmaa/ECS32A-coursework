import random

def main():
    attacker_hp = int(input("Enter the attacker's hp: "))
    attacker_strength = int(input("Enter the attacker's strength: "))
    attacker_accuracy = float(input("Enter the attacker's accuracy: "))
    attacker_crit_chance = float(input("Enter the attacker's crit chance: "))
    attacker_dodge_rate = float(input("Enter the attacker's dodge rate: "))
    defender_hp = int(input("Enter the defender's hp: "))
    defender_strength = int(input("Enter the defender's strength: "))
    defender_accuracy = float(input("Enter the defender's accuracy: "))
    defender_crit_chance = float(input("Enter the defender's crit chance: "))
    defender_dodge_rate = float(input("Enter the defender's dodge rate: "))
    defender_guarding = input("Is the defender guarding? Y for yes, n for no: ").lower()

    fight(seed, attacker_hp, attacker_strength, attacker_accuracy, attacker_crit_chance, attacker_dodge_rate,
          defender_hp, defender_strength, defender_accuracy, defender_crit_chance, defender_dodge_rate)

def fight(attacker_hp, attacker_strength, attacker_accuracy, attacker_crit_chance, attacker_dodge_rate,
          defender_hp, defender_strength, defender_accuracy, defender_crit_chance, defender_dodge_rate,
          defender_guarding):
    seed = int(input("Enter the seed to run the fight with: "))
    random.seed(seed)

    while attacker_hp > 0 and defender_hp > 0:
        attacker_hit = random.random()
        if attacker_hit >= attacker_accuracy / 100:  # Attacker misses
            print("attacker missed defender")
        else:
            attacker_crit = random.random()
            if attacker_crit < attacker_crit_chance / 100:  # Attacker lands a critical hit
                defender_hp -= attacker_strength + 1
                print(f"attacker crit defender for {attacker_strength + 1} points of damage")
            else:
                defender_dodge = random.random()
                if defender_dodge < defender_dodge_rate / 100:  # Defender dodges
                    print("defender dodged attacker's attack")
                else:
                    defender_hp -= random.randint(attacker_strength // 2, attacker_strength)
                    print(f"attacker hits defender for {random.randint(attacker_strength // 2, attacker_strength)} points of damage")



        print(f"After fighting the attacker has {attacker_hp} hp left and the defender has {defender_hp} hp left")
main()