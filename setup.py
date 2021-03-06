import cx_Freeze


# create an exe from file "FAN.py"
executables = [cx_Freeze.Executable("FAN.py")]


# setup cx_Freeze
cx_Freeze.setup(
	name="FAN",
	options={"build_exe": {"packages":["pygame", "numpy"], 
							"include_files":["Assets", "metaData.json"]}},
	executables = executables
	)