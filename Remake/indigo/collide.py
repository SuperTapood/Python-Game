from .exceptions import CollideResponseError, CollideTypeError
from inspect import signature


# base collision rules
def collision(sprite1, sprite2):
	if sprite1.x < sprite2.x + sprite2.w:
		if sprite1.x + sprite1.w > sprite2.x:
			if sprite1.y < sprite2.y + sprite2.h:
				if sprite1.y + sprite1.h > sprite2.y:
					return True
	return False

def check_valid_resp(resp):
	if len(signature(resp).parameters) != 2:
		print(len(signature(resp).parameters))
		raise CollideResponseError(resp.__name__)
	return

def check_valid_group(group):
	if hasattr(group, "object_type"):
		if group.object_type == "Group":
			return
	raise CollideTypeError(type(group).__name__)



def sprite_sprite_collision(sprite1, sprite2, resp):
	check_valid_resp(resp)
	if collision(sprite1, sprite2):
		resp(sprite1, sprite2)
	return

def sprite_group_collision(sprite1, group, resp):
	check_valid_resp(resp)
	check_valid_group(group)
	for obj in group:
		if collision(sprite1, obj):
			resp(sprite1, obj)
	return

def group_group_collision(group1, group2, resp):
	check_valid_resp(resp)
	check_valid_group(group1)
	check_valid_group(group2)
	for obj in group1:
		for pbj in group2:
			if collision(obj, pbj):
				resp(obj, pbj)
	return