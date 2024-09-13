import random
from enum import Enum
from random import randint, choice


class SuperAbility(Enum):
    HEAL = 1
    BOOST = 2
    CRITICAL_DAMAGE = 3
    BLOCK_DAMAGE_AND_REVERT = 4
    REVIVE = 5
    STEAL_HEALTH_AND_TRANSFER = 6
    ABSORB_DAMAGE = 7
    STUNNING_HEAT = 8



class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.name} health: {self.health} damage: {self.damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None
        self.original_damage = damage
        self.skip_next_round = False

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        hero = choice(heroes)
        self.__defence = hero.ability

    def attack(self, heroes):
        if self.skip_next_round:
            print(f'{self.name} is stunned and skips the round.')
            self.skip_next_round = False
            return

        for hero in heroes:
            if hero.health > 0:
                if (hero.ability == SuperAbility.BLOCK_DAMAGE_AND_REVERT and
                        self.defence != SuperAbility.BLOCK_DAMAGE_AND_REVERT):
                    hero.blocked_damage = choice([5, 10])
                    hero.health -= (self.damage - hero.blocked_damage)

                else:
                    hero.health -= self.damage

    def reset_damage(self):
        self.damages = self.original_damage

    def __str__(self):
        return 'BOSS ' + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def attack(self, boss):
        boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)
        self.base_damage = damage # I wanted Magician to boost only the base damage of the Warriers, without boosting their superpower

    def apply_super_power(self, boss, heroes):
        coefficient = randint(2, 5)
        boss.health -= (self.base_damage * coefficient)
        print(f'Warrior {self.name} hits critically: {(self.base_damage * coefficient)} power')

# to be able to change base.damage for Warriors, in case of when Magician boosts base_damage
    @property
    def damage (self):
        return self.base_damage

    @damage.setter
    def damage (self, value):
        self.base_damage = value

# 2. Magic должен увеличивать атаку каждого героя после каждого раунда на n-ное количество
# Magician only boosts base_damage of Warriors, not boosting super.abilities damage power

class Magic(Hero):
    def __init__(self, name, health, damage, boost):
        super().__init__(name, health, damage, SuperAbility.BOOST)
        self.__boost = boost

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0:
                if isinstance(hero, Witcher):
                    print(f"Magician {self.name} does not boost Witcher {hero.name}'s damage")
                elif isinstance(hero, Warrior):
                    hero.base_damage  += self.__boost
                    print(f"Magician {self.name} boosted Warrior {hero.name}'s damage by {self.__boost}. New damage: {hero.base_damage} ")
                elif isinstance(hero, Hacker):
                    print(f"Magician {self.name} does not boost Hacher {hero.name}'s damage")

                else:
                    hero.damage += self.__boost
                    print(f" Magician {self.name} boosts: {hero.name}'s damage by {self.__boost}. New damage: {hero.damage} ")



class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.health += self.__heal_points


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.BLOCK_DAMAGE_AND_REVERT)
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def apply_super_power(self, boss, heroes):
        boss.health -= self.__blocked_damage
        print(f'Berserk {self.name} reverted {self.__blocked_damage}')

#1. Witcher, не наносит урон боссу, но получает урон от босса. Имеет 1 шанс оживить первого погибшего героя, отдав ему свою жизнь, при этом погибает сам/а.
class Witcher(Hero):
    def __init__(self, name, health, damage, revive):
        super().__init__(name, health, damage, SuperAbility.REVIVE)
        self.__revive = revive
        self.__has_revived = False # to track whether Witcher has revived a hero

    def apply_super_power(self, boss, heroes):
        if not self.__has_revived:
            for hero in heroes:
                if hero.health <= 0 and hero != self:
                    hero.health = self.__revive
                    self.health = 0 # in this case Witcher dies after reviving a hero
                    self.__has_revived = True
                    print(f'Witcher {self.name} sacrifices her life to revive life of {hero.name} with her {self.__revive} healing points ')
                    break

    def attack(self, boss):
        pass


#3 Hacker, который будет через раунд забирать у Босса N-ое количество здоровья и переводить его одному из героев.
class Hacker(Hero):
    def __init__(self, name, health, damage, stolen_health):
        super().__init__(name, health, damage, SuperAbility.STEAL_HEALTH_AND_TRANSFER)
        self.__stolen_health = stolen_health

    @property
    def stolen_health(self):
        return self.__stolen_health

    @stolen_health.setter
    def stolen_health(self, value):
        self.__stolen_health = value

    def attack(self, boss):
        pass

    def apply_super_power(self, boss, heroes):
        if round_number % 2 == 0:
            if boss.health > 0:
                boss.health -= self.__stolen_health
                recepient = choice([hero for hero in heroes if hero.health > 0 and hero != self])
                recepient.health += self.__stolen_health
                print(f'Hacker {self.name} steals {self.__stolen_health} health points from {boss.name} and transferred them to {recepient.name}')


# ДОПОЛНИТЕЛЬНОЕ: Добавить в проект уникальную реализацию суперспособности  2-х героев: 4. Golem and 7. Thorina

class Hero_1(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.ABSORB_DAMAGE)
        self.__absorb_damage_fraction = 1 / 5

    def apply_super_power(self, boss, heroes):
        if self.health > 0:
    #had to add additional condiction for skipping of the round of the boss in case Thorina stunned him, so Golem would not absorb damage
            if not boss.skip_next_round:
                total_damage = boss.damage
                absorbed_damage = total_damage * self.__absorb_damage_fraction
                self.health -= absorbed_damage
                print(f' {self.name} absorbs {absorbed_damage} damage.')
            else:
                print(f'{self.name} cannot absorb damage because {boss.name} is skipping the round.')


class Hero_2(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.STUNNING_HEAT)
        self.__stun_chance = 0.25

    @property
    def stun_chance(self):
        return self.__stun_chance


    def apply_super_power(self, boss, heroes):
        if random.random() < self.stun_chance:
            boss.skip_next_round = True
            print(f'{self.name} stunned the {boss.name}! The {boss.name} will skip the next round. ')

    def attack(self, boss):
        boss.health -= self.damage







round_number = 0


def show_statistics(boss, heroes):
    print(f'ROUND {round_number} ------------------')
    print(boss)
    for hero in heroes:
        print(hero)


def is_game_over(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
        return True
    return False


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)

    for hero in heroes:
        if isinstance(hero, Hero_2) and hero.health > 0 and random.random() < hero.stun_chance:
            boss.skip_next_round = True
            print(f'{hero.name} stunned {boss.name}! {boss.name} will skip the next round.')

    if not boss.skip_next_round:
        boss.attack(heroes)

    for hero in heroes:
        if hero.health > 0 and boss.health > 0 and boss.defence != hero.ability:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)

    boss.reset_damage()

    show_statistics(boss, heroes)

def game_round(boss, heroes):
    for hero in heroes:
        if isinstance(heroes) and hero.health > 0:
            if hero.has_stunned:
                boss_skip_round = True
            else:
                boss_skip_round = False
            if boss_skip_round:
                print(f'{boss.name} is stunned and skips this round.')
                boss.damage = 0
            else:
                boss.damage = original_boss_damage
def start_game():
    boss = Boss('Tanos', 1000, 50)
    warrior_1 = Warrior('Thor', 290, 10)
    warrior_2 = Warrior('Hercules', 280, 15)
    magic = Magic('Strange', 270, 20, 2)
    doc = Medic('Aibolit', 250, 5, 15)
    assistant = Medic('Junior', 300, 5, 5)
    berserk = Berserk('Jonathan', 260, 10)
    witcher = Witcher('Artemida', 250, 0, 50)
    hacker = Hacker('Santo', 200, 0, 5)
    hero_1 = Hero_1('Golem', 1000, 1)
    hero_2 = Hero_2('Thorina', 200, 20)


    heroes_list = [warrior_1, warrior_2, magic, assistant, berserk, doc, witcher, hacker, hero_1, hero_2]

    show_statistics(boss, heroes_list)
    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)


start_game()
