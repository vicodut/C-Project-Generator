import sublime, sublime_plugin
import sys
from os import listdir, mkdir, environ
from os.path import isfile, isdir, join
import os
from shutil import copyfile
import shutil
import sys
import json
from pprint import pprint

name = "Cash"
path = "./"
headersP = "Header/"
sourcesP = "Source/"
objectsP = "Objects/"
headersPath = path + headersP
sourcesPath = path + sourcesP
objectsPath = path + objectsP
makefile = path + "makefile"

system = sys.platform

data_json = sublime.packages_path() + "/Makefile Generator/Data/Data.sublime-setting"
with open(data_json) as data_file:
	data = json.load(data_file)
fic = data["startfolder"][0]["folder"]

print("Fichier de départ : "+ fic)
if fic == "User":
	if system == "win32":
		folder = "C:" + environ["HOMEPATH"]
	elif system == "linux":
		folder = environ["HOME"]
else:
 	if system == "win32":
 		folder = "C:" + fic
 	elif system == "linux":
 		folder = fic

def echo(string):
	global makefile
	# sys.stdout.write(string)
	print(string, end='')
	makefile.write(string)

def isNotIgnored(string):
	# echo("\n=====================test ignore: " + string)
	rep = 1
	string = string + "\n"
	fichier = path + ".makeignore"
	# print("$$$$$$$$$$$$$$$$$$$$$$$$$$" + fichier)
	if isfile(fichier):
		# print("123")
		miFile = open(path + '.makeignore', 'r+')
		# print(miFile)
		for line in miFile:
			#echo("<" + line + ">")
			#echo("{" + string + "}")
			if line == string:
				rep = 0
		miFile.close()
		#print (rep)
	# if not rep:
	# 	echo(" ignored ")
	return rep

class GenerateMakefileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		global makefile
		global name
		global path
		global headersP
		global sourcesP
		global objectsP
		global headersPath
		global sourcesPath
		global objectsPath
		global makefile
		path = ((self.view.file_name()).rsplit(os.sep, 2)[0]).replace(os.sep, '/') + "/"
		name = (path).split("/")[-2]
		headersP = "Header/"
		sourcesP = "Source/"
		objectsP = "Objects/"
		headersPath = path + headersP
		sourcesPath = path + sourcesP
		objectsPath = path + objectsP
		makefile = path + "makefile"

		makefile = open(path + "makefile", 'w')

		sources = [ (f.rsplit('.'))[0] for f in listdir(sourcesPath) if isfile(join(sourcesPath,f)) ]

		echo("" + name + ':')
		for source in sources:
			# pass
			if isNotIgnored(source + ".c"):
				echo(" " + objectsP + source + ".o")
		echo("\n\tgcc $^ -o $@\n")

		# echo("============================")

		for source in sources:
			if isNotIgnored(source + ".c"):
				headers = []
				sourceFile = open(sourcesPath + source + ".c", 'r+')
				
				echo("\n" + objectsP + source + ".o: " + sourcesP + source + ".c")
				
				# for line in sourceFile:
				line = sourceFile.readline()
				while not (line.startswith("#inc") or line.startswith("# inc")):
					line = sourceFile.readline()

				while (line.startswith("#inc") or line.startswith("# inc") or line == "\n"):
					if not (line == "\n" or "<" in line):
						header = line.split("\"")[1]
						header = (header.rsplit("/", 1)[-1]).rsplit("\\", 1)[-1]
						header = header.rsplit(".", 1)[0]
						headers += [header]
					line = sourceFile.readline()
				
				for header in headers:
					if isNotIgnored(header + ".h"):
						echo(" " + headersP + header + ".h")
				echo("\n\tgcc -c " + sourcesP + source + ".c -o " + objectsP + source + ".o\n")
		makefile.close()

global NameProject
class CreateProjectCommand(sublime_plugin.WindowCommand):
	def run(self):
		print("NewProject")


		self.window.show_input_panel('Name of New Project :', '',
            self.on_done, self.on_change, self.on_cancel)
	def on_done(self, input):
		global NameProject
		NameProject = input
		self.window.run_command('new_project')
	def on_change(self, input):
		pass

	def on_cancel(self):
	    pass

class CreateFilesProjectCommand(sublime_plugin.WindowCommand):
	def run(self):
	   	print(ProjetFolder)
	   	path = ProjetFolder + NameProject  #!!!! PATH
	   	#print(path)
	   	try:
	   		mkdir(path)
	   		print("Le Projet \"" + NameProject + "\" Créé")
	   		sublime.status_message("Le Projet \"" + NameProject + "\" Créé")
	   		mkdir(path + "/Source")
		   	mkdir(path + "/Header")
		   	mkdir(path + "/Objects")
		   	PathFichier = path + "/Source/"
		   	PathPackageDefault = sublime.packages_path() + "/Makefile Generator/Data/Default.c"
		   	copyfile(PathPackageDefault, PathFichier + NameProject + ".c")
	   	except (OSError):
	   		sublime.status_message("Erreur création projet")
	   		print ("Erreur création projet")
	   		sublime.error_message("Erreur création projet : Le dossier \"" + NameProject + "\" est déjà existant")
	   	Main = PathFichier + NameProject + '.c'
	   	print (Main)
	   	self.window.open_file(Main)


global ProjetFolder 
class NewProjectCommand(sublime_plugin.WindowCommand):
	def run(self):  
		global folder
		# try:
		# 	folder = environ["HOME"]
		# except Exception:
		# 	try:
		# 		folder = environ["HOMEPATH"]
		# 	except Exception:
		# 		print("Variables d'environnement")
		
		if not folder.endswith("/"):
			folder += "/"
		self.menu(-1)

	def showPanel(self, itemsList):
		sublime.set_timeout(lambda: self.window.show_quick_panel(itemsList, self.menu), 10)

	def menu(self, arg):
		global folder
		global foldersList
		global selectedItem
		self.generateList(folder)
		if arg == 0:
			self.create(foldersList[arg])
		elif arg == 1:
			pass
		else:
			if not (arg == -1):
				if foldersList[arg] == "..":
					folder = folder.rsplit("/", 2)[0] + "/"
				else: 
					folder += foldersList[arg] + "/"
				self.generateList(folder)
	
			self.showPanel(foldersList)

		
	def result(self, arg):
		global foldersList
		global selectedItem
		print(foldersList[arg])
		selectedItem = arg
		self.menu(selectedItem)

	def create(self, arg):
		global ProjetFolder
		ProjetFolder = arg
		print("Final" + arg)
		self.window.run_command('create_files_project')



	def generateList(self, folder):
		global foldersList
		foldersList = [folder] + ["Cancel"] + [".."] + [ (f.rsplit('/'))[0] for f in listdir(folder) if isdir(join(folder ,f)) ]


class CopierCommand(sublime_plugin.WindowCommand):
	def run(self):
		print("Hello")
		PathPackageDefault = "C:/Users/Victor/Documents/data.json"
		system = sys.platform
		print(system)
		
		fichier = {}
		fichier["folder"] = PathPackageDefault
		print(json.dumps(fichier, indent=4))
		with open(PathPackageDefault, 'w', encoding='utf-8') as f:
			json.dump(fichier, f, indent=4)

		#self.view.run_command('by')


class FichiersCommand(sublime_plugin.WindowCommand):
	def run(self):
		data_json = "C:/Users/Victor/Documents/data.json"
		with open(data_json) as data_file:
			data = json.load(data_file)
		fic = data["folder"]
		print(fic)
			