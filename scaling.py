from globals import screen

def screen_percent(x_or_y, percentage, length=None, origin='center'):
	if x_or_y == 'x':
		if length is None:
			return int((screen.get_width() / 100) * percentage)
		else:
			if origin == 'center':
				return int(((screen.get_width() / 100) * percentage) - (length / 2))
			elif origin == 'left':
				return int((screen.get_width() / 100) * percentage)
			elif origin == 'right':
				return int(((screen.get_width() / 100) * percentage) - (length))
	if x_or_y == 'y':
		if length is None:
			return int((screen.get_height() / 100) * percentage)
		else:
			if origin == 'center':
				return int(((screen.get_height() / 100) * percentage) - (length / 2))
			elif origin == 'left':
				return int((screen.get_height() / 100) * percentage)
			elif origin == 'right':
				return int(((screen.get_height() / 100) * percentage) - (length))


# WORK IN PROGRESS; May or may not implement

# player_class_parchments = container((0, 0, 100, 100), 4, (10, 10), 'space-around')
# player_class_parchments = container((0, 0, 100, 100), 4, [(10, 10)], 'space-around')
# player_class_parchments = container((0, 0, 100, 100), 4, [(10, 10), (15, 10), (7, 8)], 'space-around')
# player_class_parchments = container((0, 0, 100, 100), 4, [(10, 10), (15, 10), (7, 8)], 'space-between', '25')
# player_class_parchments = container((0, 0, 100, 100), 4, [(10, 10), (15, 10), (7, 8)], 'left', ['25', '25', '0', '0'])
# def container(rect, num_of_items, item_rects, item_align='space-between', container_padding=None, item_margin=None):


# 	for item in num_of_items:
# 		if item_align == 'space-between':
# 			pass
# 		elif item_align == 'space-around':
# 			pass
# 		elif item_align == 'center':
# 			pass
# 		elif item_align == 'left':
# 			pass
# 		elif item_align == 'right':
# 			pass
# 		else:
# 			print('Invalid item_align')
# 			break
