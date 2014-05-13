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
projectName = ""
projetFolder = "" 

system = sys.platform

data_json = sublime.packages_path() + "/Makefile Generator/Data/Data.sublime-setting"

with open(data_json) as data_file:
	data = json.load(data_file)

fic = data["startfolder"][0]["folder"]

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

def printAndWrite(string):
	global makefile
	print(string, end='')
	makefile.write(string)

def isNotIgnored(string):
	rep = 1
	string = string + "\n"
	fichier = path + ".makeignore"

	if isfile(fichier):

		miFile = open(path + '.makeignore', 'r+')

		for line in miFile:
			if line == string:
				rep = 0
		miFile.close()

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

		headersPath = path + headersP
		sourcesPath = path + sourcesP
		objectsPath = path + objectsP

		makefile = path + "makefile"
		makefile = open(path + "makefile", 'w')

		sources = [ (f.rsplit('.'))[0] for f in listdir(sourcesPath) if isfile(join(sourcesPath,f)) ]
		printAndWrite("" + name + ':')

		for source in sources:
			if isNotIgnored(source + ".c"):
				printAndWrite(" " + objectsP + source + ".o")

		printAndWrite("\n\tgcc $^ -o $@\n")

		for source in sources:
			if isNotIgnored(source + ".c"):
				headers = []

				sourceFile = open(sourcesPath + source + ".c", 'r+')
				printAndWrite("\n" + objectsP + source + ".o: " + sourcesP + source + ".c")
				
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
						printAndWrite(" " + headersP + header + ".h")
				printAndWrite("\n\tgcc -c " + sourcesP + source + ".c -o " + objectsP + source + ".o\n")

		makefile.close()


class CreateProjectCommand(sublime_plugin.WindowCommand):
	def run(self):
		print("NewProject")

		self.window.show_input_panel('Name of New Project :', '',
            self.on_done, self.on_change, self.on_cancel)

	def on_done(self, input):
		global projectName
		projectName = input
		self.window.run_command('new_project')

	def on_change(self, input):
		pass

	def on_cancel(self):
	    pass

class ProjectCommand(sublime_plugin.WindowCommand):
	def run(self):
	   	print(projetFolder)
	   	path = projetFolder + projectName  #!!!! PATH

	   	try:
	   		mkdir(path)
	   		print("Le Projet \"" + projectName + "\" a été créé")

	   		sublime.status_message("Le Projet \"" + projectName + "\" Créé")

	   		mkdir(path + "/Source")
		   	mkdir(path + "/Header")
		   	mkdir(path + "/Objects")
		   	pathFile = path + "/Source/"

		   	pathPackageData = sublime.packages_path() + "/Make Generator/Data/Default.c"
		   	copy(pathPackageData, pathFile + projectName + ".c")

	   	except (OSError):
	   		sublime.status_message("Erreur création projet")
	   		print ("Erreur création projet")
	   		sublime.error_message("Erreur création projet : Le dossier \"" + projectName + "\" est déjà existant")

	   	Main = pathFile + projectName + '.c'
	   	print (Main)

	   	self.window.open_file(Main)



class NewProjectCommand(sublime_plugin.WindowCommand):
	def run(self):  
		global folder
		
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
		global projetFolder

		projetFolder = arg
		print("Final" + arg)

		self.window.run_command('create_files_project')



	def generateList(self, folder):
		global foldersList

		foldersList = ["Choose : [ \"" + folder + "\" ]"] + ["[ Cancel ]"] + ["[ .. ]"] + [ (f.rsplit('/'))[0] for f in listdir(folder) if isdir(join(folder ,f)) ]



# ################################# #
# 	  FONCTIONS POUR LES TESTS		#
#    ---------//////----------- 	#
# 	     FUNCTION FOR TESTS			#
# ################################# #



class CopierCommand(sublime_plugin.WindowCommand):
	def run(self):
		print("Hello")
		pathPackageData = "C:/Users/Victor/Documents/data.json"
		system = sys.platform
		print(system)
		
		fichier = {}
		fichier["folder"] = pathPackageData
		print(json.dumps(fichier, indent=4))
		with open(pathPackageData, 'w', encoding='utf-8') as f:
			json.dump(fichier, f, indent=4)

		#self.view.run_command('by')


class FichiersCommand(sublime_plugin.WindowCommand):
	def run(self):
		data_json = "C:/Users/Victor/Documents/data.json"
		with open(data_json) as data_file:
			data = json.load(data_file)
		fic = data["folder"]
		print(fic)
			

# ############# #
# 	  TODO		#
# ############# #
