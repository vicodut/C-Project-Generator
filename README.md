C-Project-Generator
===================

A plug-in for Sublime-Text 3 which allows the creation and management of C projects.

##Create a Make file :

###Condition:
The project must have this file hierarchy:


#####Project\_Folder/ #####
*  __Source/__ 
 *  _Folder which contain sources files_
 * _Ex.: file1.c_
 * _file2.c_
*  __Header/__
*  __Objects/__



Open  Command Palette (in windows: `CTRL+Shift+P`) and  execute `Generate Make`.
This command will create the file `makefile.in` at the root of the project here: `Project Folder/`.

##Create a New C Project :
Open  Command Palette (in windows: `CTRL+Shift+P`) and  execute `Create C Project`. C Projects created by this command are optimised to work with the command: `Generate Make` of this plug-in.

An input box will appear on the bottom of Sublime, just give a name to your project and choose the folder of his creation.

####File hierarchy of the new project :####


#####Name\_of\_the\_Project/ #####
*  __Source/__ 
 *  'Name of the Project.c'
*  __Header/__
*  __Objects/__


#### Start folder for choose project location :####
By default the reachearche start folder is the USER path (`C:/Users/Name` for windows, `/home/Name` for linux). If you have a specific location where you want to save your project without the need each time to return by the navigation panel, you can  change the value of this folder in `.../Sublime Text/Packages/C Projects Generator/Data/Data.sublime-setting` the default file is :
  {
	"startfolder": 
		[{
			"folder": "User"
		}]
	}
	
User is default value which will return the user path of the system in the plug-in. So to change the path you must put your path to the folder you need.

Example:
If i want to start at : `C:/Users/MyName/Documents/Projects` i must put:


  {
	"startfolder": 
		[{
			"folder": "C:/Users/MyName/Documents/Projects"
		}]
	}
	

