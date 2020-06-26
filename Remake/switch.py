g_X = None

def switch(x):
	global g_X
	g_X = x
	return

def case(x):
	global g_X
	return g_X == x