# This is a procedural approach to a text based rpg game
# The hero is fighitng a goblin
# He has the option to:

# 1. fight

def main():
	hero_health = 10
	hero_power = 5
	goblin_health = 6
	goblin_power = 2

	while the_goblin.health > 0 and the_hero.health > 0:
		print "You have %d health and %d power." % (the_hero.health, the_hero.power)
		print "The goblin has %d health and %d power." % (the_goblin.health, the_goblin.power)
		print "What do you want to do?"
		print "1. fight goblin"
		print "2. do nothing"
		print "3. flee"
		print "> ",
		user_input = raw_input()

		if user_input == "1":
			goblin_health -= hero_power
				## you could also rwite goblin_health - goblin_health - heropower
			print "You have done %d damage to the goblin" % hero_power
			if goblin_health <= 0:
				print "You have defeated the goblin!"

		elif user_input == "2":
			pass
			## if you need this to exist but you dont want the code to do anything

		if user_input == "3":
			print "Goodbye, coward"
			break
		else:
			print "Invalid input %s" % user_input

		if goblin_health > 0:
			hero_health -= goblin_power
			print "The goblin hits you for %d damge" % goblin_power
			if hero_health <= 0:
					print " You have been killed by the goblin."

		if hero_health > 0 and hero_health < 5
			print " You have gone into a rage. Your power has increased!"
			hero_power += 5

main()