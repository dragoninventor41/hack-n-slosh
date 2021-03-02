class SceneManager:
	def __init__(self, default_scene):
		self.scene = default_scene

	def change_scene(self, new_scene):
		self.scene = new_scene
