import cx_Freeze


executables = [cx_Freeze.Executable("FAN.py")]

cx_Freeze.setup(
	name="FAN",
	options={"build_exe": {"packages": ["pygame"], 
							"include_files": ["Assets"]}},
	executables=executables
	)