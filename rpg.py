from hero import Hero

from goblin import Goblin

from Vampire import Vampire

the_goblin = Goblin()


#the_hero.cheer_hero()
hero_name = raw_input("What is the name, brave adventurer?")

the_hero = Hero(hero_name)

monsters = []
monsters.append(Goblin())
monsters.append(Vampire())



for monster in monsters:
	print "Welcome brave %s, you have encountered %s." % (the_hero.name, monster.name)


	while monster.health > 0 and the_hero.is_alive():
		print "You have %d health and %d power." % (the_hero.health, the_hero.power)
		print "The %s has %d health and %d power." % (monster.name, monster.health, monster.power)
		print "What do you want to do?"
		print "1. Fight %s" % monster.name
		print "2. do nothing"
		print "3. flee"
		print "4. Drink Beer of life"
		print "xxx ",
		user_input = raw_input()
		if (user_input == "1"):
				monster.take_damage(the_hero.power)
				
				print "You have done %d damage to the %s!" % (the_hero.power, monster.name)
				if monster.health <= 0:
					print "You have defeated the %s!" % (monster.name)
					the_hero.xp += monster.xp_value
					the_hero.check_level()

		elif user_input == "2":
			pass
				## if you need this to exist but you dont want the code to do anything

		elif user_input == "3":
			print "Goodbye, coward"
			break

		elif user_input == "4":
			the_hero.increase_health(20)

		else:
			print "Invalid input %s" % user_input

		if monster.health > 0:
			the_hero.health -= monster.power
			print "The goblin hits you for %d damge" % monster.power
			if the_hero.health <= 0:
				print " You have been killed by the goblin."

		if the_hero.health > 0 and the_hero.health < 5:
			print " You have gone into a rage. Your power has increased!"
			the_hero.power += 5
