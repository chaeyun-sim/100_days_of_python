# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json


def turn_right():
		turn_left()
		turn_left()
		turn_left()

def jump():
		if wall_in_front():
				turn_right()
				if wall_in_front():
						turn_left()
						if wall_in_front():
								turn_leftt()
						else:
								move()
				else:
						move()
		else:
				move()

while not at_goal():
		if wall_in_front():
				jump()
		else:
				move()