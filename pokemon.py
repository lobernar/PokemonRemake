import pygame

class Pokemon:
    def __init__(self):
        self.hp = 100
        self.max_hp = 100
        self.type = []
        self.name = 'Pikachu'
        self.nickname = ''
        self.level = 5
        self.exp = 0
        self.attack = 1
        self.defence = 1
        self.sp_attack = 1
        self.sp_defence = 1
        self.speed = 1
        self.moves = ['Tackle']