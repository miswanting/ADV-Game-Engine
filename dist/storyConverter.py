#coding=utf-8

'''
The format of this code is advocated!
'''

import lib_tpos

class storyConverter(object):

	"""
	This is an achieve of class-TPManager.
	It`s design to convert story files into a TP file.
	This program may be only used once. But it`s a effective way to exam the ability of class-TPManager.
	GL!
	"""

	tp = lib_tpos.TPManager()

	# Public function
	def compress(path, file):

		self.tp.init(file)
		self.tp.setPath(path)
		self.tp.pullContent()
	def decompress(file, path):
		pass

	# Private function

if __name__ == '__main__':
	# instantiation
	I = storyConverter()
	# compress TP file.
	I.compress('story\\老头の穿越之旅：血阳城\\', 'story\\老头の穿越之旅：血阳城.tp')
	# I.decompress('story\\老头の穿越之旅：血阳城.tp', 'story\\老头の穿越之旅：血阳城\\')
