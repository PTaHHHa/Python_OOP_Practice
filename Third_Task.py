"""В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее уникальный номер объекта, и свойство,
в котором хранится принадлежность команде.. У героев есть метод увеличения собственного уровня,
добавления солдат и подсчёта их численности.

В основной ветке программы создается по одному герою для каждой команды. В цикле генерируются солдаты.
Их принадлежность команде определяется случайно. Солдаты разных команд добавляются в разные списки.

Измеряется длина списков солдат противоборствующих команд и выводится на экран. У героя, принадлежащего команде
с более длинным списком, поднимается уровень.
"""
import random


class Unit:
    def __init__(self, ID, team=None):
        if team is None:
            team = []
            self.team = team
        self.ID = ID


class Hero(Unit):
    def __init__(self, ID, name, team=None):
        super().__init__(ID, team)
        self.name = name
        self.lvl = 1

    def get_lvl(self):
        return self.lvl

    def lvl_up(self):
        self.lvl += 1

    def add_soldiers(self, soldiers):
        return self.team.append(soldiers)

    def count(self):
        return len(self.team)


hero1 = Hero(1, "Gabe Newell")
hero2 = Hero(2, "Tim Sweeney")
soldiers_number = random.randint(1, 51)
for i in range(soldiers_number):
    team_id = random.randint(0, 1)
    if team_id == 0:
        hero1.add_soldiers(i)
    else:
        hero2.add_soldiers(i)
if hero1.count() > hero2.count():
    hero1.lvl_up()
    print(f"{hero1.name} won, because his army consists of {hero1.count()} people. His level is {hero1.get_lvl()}")
else:
    hero2.lvl_up()
    print(f"{hero2.name} won, because his army consists of {hero2.count()} people. His level is {hero2.get_lvl()}")



