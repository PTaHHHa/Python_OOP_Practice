""" Есть класс "Воин". От него создаются два экземпляра-юнита. Каждому устанавливается здоровье в 100 очков. В
случайном порядке они бьют друг друга. Тот, кто бьет, здоровья не теряет. У того, кого бьют, оно уменьшается на 20
очков от одного удара. После каждого удара надо выводить сообщение, какой юнит атаковал, и сколько у противника
осталось здоровья. Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том,
кто одержал победу. """
import random


class Warrior:
    def __init__(self, name):
        self.name = name
        self.__hp = 100

    def getHP(self):
        return self.__hp

    def fight(self):
        self.__hp -= 20


bruh1 = Warrior("Gabe Newell")
bruh2 = Warrior("Tim Sweeney")

while bruh1.getHP() > 0 and bruh2.getHP() > 0:
    turn = random.randint(0, 1)
    if turn == 0:
        bruh2.fight()
        print(f"{bruh1.name} attacked {bruh2.name}. {bruh2.name} has {bruh2.getHP()}HP left")
    else:
        bruh1.fight()
        print(f"{bruh2.name} attacked {bruh1.name}. {bruh1.name} has {bruh1.getHP()}HP left")
    if bruh1.getHP() == 0:
        print(f"{bruh1.name} defeated")
    elif bruh2.getHP() == 0:
        print(f"{bruh2.name} defeated")
