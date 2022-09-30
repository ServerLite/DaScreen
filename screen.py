from os import system

class Window():
	def __init__(self, screen_width, screen_height):
		self.SCREEN_WIDTH = screen_width
		self.SCREEN_HEIGHT = screen_height
		self.screen = self.clear_screen()
		self.positions = dict()

	def clear_screen(self):
		return [[" " for i in range(self.SCREEN_WIDTH)] for i in range(self.SCREEN_HEIGHT)]
	
	def display(self):
	    for row in self.screen:
	        for column in row:
	            print(column, end=" ")
	        print("")

	def generate_border(self, id, init_width, init_height, width, height, style):
		self.positions[id] = list()
		for h in range(init_height, height+init_height):
			for w in range(init_width, width+init_width):
				if h == init_height or h == height+init_height-1 or w == init_width or w == width+init_width-1:
					self.positions[id].append((w, h))
					self.screen[h][w] = style

	def detect_collision(self, object_1, object_2):
		object_position_1 = self.positions[object_1]
		object_position_2 = self.positions[object_2]
		leading_1 = object_position_1 if len(object_position_1) > len(object_position_2) else object_position_2
		leading_2 = object_position_1 if len(object_position_1) < len(object_position_2) else object_position_2
		
		for object_1 in leading_1:
			for object_2 in leading_2:
				if object_1[0] == object_2[0] and object_1[1] == object_2[1]:
					return True
		return False


	def generate_square(self, id, init_width, init_height, width, height, style):
		self.positions[id] = list()
		for h in range(init_height, height+init_height):
			for w in range(init_width, width+init_width):
				self.positions[id].append((w, h))
				self.screen[h][w] = style
