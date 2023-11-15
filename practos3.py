# -*- coding: cp1251 -*-
import random
import json
import csv
import os

# Глобальные переменные
weapons = ['меч', 'лук', 'посох']
enemies = {'гоблин': 20, 'орк': 30, 'дракон': 100}
inventory = set()

def print_inventory():
    print("Ваш инвентарь:")
    for item in inventory:
        print(item)

def fight(enemy):
    print(f"Вы встретили {enemy}!")
    player_hp = 100
    enemy_hp = enemies[enemy]
    print(f"Ваше здоровье: {player_hp}")
    print(f"Здоровье {enemy}: {enemy_hp}")
    weapon = random.choice(weapons)
    print(f"Вам достался {weapon}")
    while player_hp > 0 and enemy_hp > 0:
        action = input("Выберите действие (атаковать / убежать): ")
        if action == "атаковать":
            damage = random.randint(10, 20)
            enemy_hp -= damage
            print(f"Вы нанесли {damage} единиц урона")
            if enemy_hp > 0:
                damage = random.randint(5, 15)
                player_hp -= damage
                print(f"{enemy} нанес вам {damage} единиц урона")
        elif action == "убежать":
            if random.random() < 0.5:
                print("Вы успешно убежали!")
                return
            else:
                print("Попытка убежать провалилась!")
                damage = random.randint(5, 15)
                player_hp -= damage
                print(f"{enemy} нанес вам {damage} единиц урона")
        else:
            print("Неверное действие!")
    if player_hp <= 0:
        print("Вы проиграли!")
    else:
        print("Вы победили!")
        inventory.add(weapon)
        print(f"Вы получили {weapon}")

def save_game():
    save_data = {
        'inventory': list(inventory)
    }
    with open('save.json', 'w') as file:
        json.dump(save_data, file)

def delete_save():
    if os.path.exists('save.json'):
        os.remove('save.json')
        print("Сохранение удалено")
    else:
        print("Сохранение не найдено")

def update_csv():
    all_data = []
    if os.path.exists('game_data.csv'):
        with open('game_data.csv', 'r') as file:
            reader = csv.reader(file)
            all_data = list(reader)
            all_data = [data for data in all_data if data]  # Remove empty rows
    with open('game_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for item in inventory:
            all_data.append(['user', item])
        writer.writerows(all_data)

def start_game():
    print("Добро пожаловать в игру!")
    print("Вы - герой, который очутился в темном лесу.")
    print("Ваша задача - добраться до дракона и победить его.")
    print("Удачи!")
    print()

    save_exists = os.path.exists('save.json')
    if save_exists:
        load_save = input("Найдено сохранение. Загрузить сохранение? (да / нет): ")
        if load_save == 'да':
            with open('save.json', 'r') as file:
                save_data = json.load(file)
            inventory.update(save_data['inventory'])

    while True:
        action = input("Выберите действие (пойти дальше / посмотреть инвентарь / выход): ")
        if action == "пойти дальше":
            enemy = random.choice(list(enemies.keys()))
            fight(enemy)
        elif action == "посмотреть инвентарь":
            print_inventory()
        elif action == "выход":
            print("Спасибо за игру!")
            break
        else:
            print("Неверное действие!")

# Запуск игры
start_game()
