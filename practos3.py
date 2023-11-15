# -*- coding: cp1251 -*-
import random
import json
import csv
import os

# ���������� ����������
weapons = ['���', '���', '�����']
enemies = {'������': 20, '���': 30, '������': 100}
inventory = set()

def print_inventory():
    print("��� ���������:")
    for item in inventory:
        print(item)

def fight(enemy):
    print(f"�� ��������� {enemy}!")
    player_hp = 100
    enemy_hp = enemies[enemy]
    print(f"���� ��������: {player_hp}")
    print(f"�������� {enemy}: {enemy_hp}")
    weapon = random.choice(weapons)
    print(f"��� �������� {weapon}")
    while player_hp > 0 and enemy_hp > 0:
        action = input("�������� �������� (��������� / �������): ")
        if action == "���������":
            damage = random.randint(10, 20)
            enemy_hp -= damage
            print(f"�� ������� {damage} ������ �����")
            if enemy_hp > 0:
                damage = random.randint(5, 15)
                player_hp -= damage
                print(f"{enemy} ����� ��� {damage} ������ �����")
        elif action == "�������":
            if random.random() < 0.5:
                print("�� ������� �������!")
                return
            else:
                print("������� ������� �����������!")
                damage = random.randint(5, 15)
                player_hp -= damage
                print(f"{enemy} ����� ��� {damage} ������ �����")
        else:
            print("�������� ��������!")
    if player_hp <= 0:
        print("�� ���������!")
    else:
        print("�� ��������!")
        inventory.add(weapon)
        print(f"�� �������� {weapon}")

def save_game():
    save_data = {
        'inventory': list(inventory)
    }
    with open('save.json', 'w') as file:
        json.dump(save_data, file)

def delete_save():
    if os.path.exists('save.json'):
        os.remove('save.json')
        print("���������� �������")
    else:
        print("���������� �� �������")

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
    print("����� ���������� � ����!")
    print("�� - �����, ������� �������� � ������ ����.")
    print("���� ������ - ��������� �� ������� � �������� ���.")
    print("�����!")
    print()

    save_exists = os.path.exists('save.json')
    if save_exists:
        load_save = input("������� ����������. ��������� ����������? (�� / ���): ")
        if load_save == '��':
            with open('save.json', 'r') as file:
                save_data = json.load(file)
            inventory.update(save_data['inventory'])

    while True:
        action = input("�������� �������� (����� ������ / ���������� ��������� / �����): ")
        if action == "����� ������":
            enemy = random.choice(list(enemies.keys()))
            fight(enemy)
        elif action == "���������� ���������":
            print_inventory()
        elif action == "�����":
            print("������� �� ����!")
            break
        else:
            print("�������� ��������!")

# ������ ����
start_game()
