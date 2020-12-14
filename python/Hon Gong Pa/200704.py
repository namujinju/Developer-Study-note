class Monster:

    count = 0
    monsters = []

    @classmethod
    def print(self):
        for monster in Monster.monsters:
            print(str(monster))

    def __init__(self, name, hp, mp, atk):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.atk = atk

        Monster.count += 1
        Monster.monsters.append(self)
    
    def battlenum(self):
        return self.hp + self.mp * 0.5 + self.atk * 1.5

    def __str__(self):
        return "{}의 전투력은 {}입니다".format(self.name, self.battlenum())


    #크기 비교
    def __lt__(self, value):
        return self.battlenum() < value.battlenum()
    def __le__(self, value):
        return self.battlenum() <= value.battlenum()
    def __gt__(self, value):
        return self.battlenum() > value.battlenum()
    def __ge__(self, value):
        return self.battlenum() >= value.battlenum()
    def __eq__(self, value):
        return self.battlenum() == value.battlenum()
    def __ne__(self, value):
        return self.battlenum() != value.battlenum()

monsters = [
    Monster("slime", 100, 0, 16),
    Monster("bat", 150, 0, 20),
    Monster("ghost", 300, 100, 15)
]

Monster.print()

print(Monster("slime", 100, 0, 16) > Monster("bat", 100, 0, 16))




