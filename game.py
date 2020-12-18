"""
Chapitre 11.1

Classes pour représenter un personnage.
"""


import random

import utils


class Weapon:
	"""
	Une arme dans le jeu.

	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""

	UNARMED_POWER = 20

	def __init__(self, nom, power, min_level):
		self.__name= name # le nom est privee
		self.power= power
		self.min_level= min_level

	@property #en ayant le property on peut acceder a la lecture du name, mais est inaccessible pour changement 
	def name(self):
    	return self.__name

class Character:
	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""

	def __init__(self, name, max_hp, attack, defense, level):
		self.__name=name
		self.max_hp=max_hp
		self.attack=attack
		self.defense=defense
		self.level=level
		self.hp=hp
		self.weapon=None

	@property #en ayant le property on peut acceder a la lecture du name, mais est inaccessible pour changement 
	def name(self):
    	return self.__name 

	def compute_damage(self, other):
		level_factor= (2*self.level)/5+2
		weapon_factor= self.weapon.power
		atk_def_factor= self.attack/other.defense
		critical= random.random() <=1/16
		modifier= (2 if critical else 1)*random.uniform(0.85, 1.0)
		damage= ((level_factor*weapon_factor*atk_def_factor)/50+2)*modifier
		return damage, critical

def deal_damage(attacker, defender):
	# TODO: Calculer dégâts
	damage=  attacker.compute_damage(defender)
	defender.hp-=dmage
	print(f"{attacker.name} used {attacker.weapon.name}")
	if critical:
		print("  Critical hit!")
	print(f"  {defender.name} took {damage} dmg")

def run_battle(c1, c2):
    attacker= c1
	attacker= c2
	turn=1
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	print(f"{attacker.name} starts a battle with {defender.name}!")
	while True:
		# TODO: Appliquer l'attaque
		deal_damage(attacker, defender)
		# TODO: Si le défendeur est mort
		if defender.hp<=0:
			print(f"{defender.name } is sleeping with the fishes.")
			break
		# Échanger attaquant/défendeur
		attacker, defender, defender, attacker
		turn+=1
	# TODO: Retourner nombre de tours effectués
	return turn


c1 = Character("Äpik", 200, 150, 70, 70)
c2 = Character("Gämmor", 250, 100, 120, 60)

c1.weapon = Weapon("BFG", 100, 69)
c2.weapon = Weapon("Deku Stick", 120, 1)

deal_damage(c1, c2)