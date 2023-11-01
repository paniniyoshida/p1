# -*- coding: cp1251 -*-
import random

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

def start_game():
    print("����� ���������� � ����!")
    print("�� - �����, ������� �������� � ������ ����.")
    print("���� ������ - ��������� �� ������� � �������� ���.")
    print("�����!")
    print()
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
