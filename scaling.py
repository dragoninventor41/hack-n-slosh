from globals import *

def screenPercent(x_or_y, percentage, length=None, origin='center'):

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





	# elif x_or_y == 'y':
		# pass
	# else:
		# print(f'{x_or_y} is an invalid argument')

	# if width_or_height is None: # No need to do alternate alignment; defaults to left side
	# 	if x_or_y == 'x':
	# 		return int((screen.get_width() / 100) * percentage)
	# 	elif x_or_y == 'y':
	# 		return int((screen.get_height() / 100) * percentage)
	# 	else:
	# 		print('Invalid argument')
	# else:
	# 	if x_or_y == 'x':
	# 		return int(((screen.get_width() / 100) * percentage) - (width_or_height / 2))
	# 	elif x_or_y == 'y':
	# 		return int(((screen.get_height() / 100) * percentage) - (width_or_height / 2))
	# 	else:
	# 		print('Invalid argument')
