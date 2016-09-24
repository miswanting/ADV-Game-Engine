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

	tpos = lib_tpos.TPOS()

	# Public function
	def convert(path, file):

		

	# Private function

if __name__ == '__main__':
	# instantiation
	I = storyConverter()
	# compress TP file.
	I.convert('story\\老头の穿越之旅：血阳城', 'story\\老头の穿越之旅：血阳城.tp')
	# I.decompress('story\\老头の穿越之旅：血阳城.tp', 'story\\老头の穿越之旅：血阳城\\')
