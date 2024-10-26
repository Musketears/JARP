import pathlib

def get_files(directory:pathlib.Path) -> list:
	list_of_files = (p for p in directory.iterdir() if p.stem not in ("__init__", "__pycache__"))
	print(directory)
	return_list = list()

	for file in list_of_files:
		if file.is_dir():
			return_list.extend(get_files(file))
		else:
			return_list.append(file)

	return return_list

def _load_cogs():
	cogs_dir = pathlib.Path(__file__).parent.joinpath("src")
	paths = get_files(cogs_dir)

	for path in paths:
		# trim = str(path).replace(str(cogs_dir), "")
		# trim = trim.replace(".py", "")
		# main_path = "cogs" + trim.replace("\\", ".")
		print(path)
		main_path = (
			str(path).replace("/", ".").replace(".app.src.", "").replace(".py", "")
		)  # comment this and uncomment above 4 lines to run on windows
		print(main_path)
		# print(main_path)
		# bot.load_extension(main_path)

_load_cogs()
