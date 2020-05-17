import cx_Freeze

__version__ = "0.02"


executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
	name=f"FAN(Pre-Alpha Version {__version__}",
	options={"build_exe": {"packages": ["pygame"], 
							"include_files": ["Assets"]}},
	executables=executables
	)