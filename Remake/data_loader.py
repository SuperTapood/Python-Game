import json

version = "0.8"
state = "ALPHA"
author = "Team Index"
date = "26/6/2020"
night_num = 0
night_6_beat = 0
night_7_beat = 0

def create_json():
	dic = {}
	dic['night_num'] = night_num
	dic['sixth'] = night_6_beat
	dic['seventh'] = night_7_beat
	file = open("data.json", "w")
	json.dump(dic, file)
	return

def init():
	global version, state, date, night_num, night_6_beat, night_7_beat
	try:
		file = open("data.json")
		dic = json.load(file)
		assert type(dic) == dict
		night_num = dic['night_num']
		night_6_beat = dic['sixth']
		night_7_beat = dic['seventh']
	except:
		create_json()
		init()
	return

def save():
	create_json()
	return
