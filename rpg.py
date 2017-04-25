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
	print "welcome brave %s, you have encountered %s." % (the_hero.name, monster)


	while monster.health > 0 and the_hero.is_alive():
		print "You have %d health and %d power." % (the_hero.health, the_hero.power)
		print "The goblin has %d health and %d power." % (monster.health, monster.power)
		print "What do you want to do?"
		print "1. fight goblin"
		print "2. do nothing"
		print "3. flee"
		print "> ",
		user_input = raw_input()
		if user_input == "1":
				monster.health -= the_hero.power
					## you could also rwite goblin_health - goblin_health - heropower
				print "You have done %d damage to the monster" % the_hero.power
				if monster.health <= 0:
					print "You have defeated the %s!" monster.name
					the_hero.xp += monster.xp_value
					the_hero.check

		elif user_input == "2":
			pass
				## if you need this to exist but you dont want the code to do anything

		if user_input == "3":
			print "Goodbye, coward"
			break
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
