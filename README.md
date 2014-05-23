C-Project-Generator
===================

A plug-in for Sublime-Text 3 which allows the creation and management of C projects.

##Create a Make file :

###Condition:
The project must have this file hierarchy:

#####Project\_Folder/ #####
1ere version
*  __Source/__ 
 *  _Folder which contain sources files_
 * _Ex.: file1.c_
 * _file2.c_
*  __Header/__
*  __Objects/__



2eme version


         - Source/
         - - - Folder which contain sources files
         - - - Ex.: file1.c
         - - - file2.c
         - Header/
         - Objects/



Open  Command Palette (in windows: `CTRL+Shift+P`) and  execute `Generate Make`.
This command will create the file `makefile.in` at the root of the project here: `Project Folder/`.

##Create a New C Project :
Open  Command Palette (in windows: `CTRL+Shift+P`) and  execute `Create C Project`. C Projects created by this command are optimised to work with the command: `Generate Make` of this plug-in.

An input box will appear on the bottom of Sublime, just give a name to your project and choose the folder of his creation.

####File hierarchy of the new project :####

#####Name\_of\_the\_Project/ #####
1ere version
*  __Source/__ 
 *  'Name of the Project.c'
*  __Header/__
*  __Objects/__



2eme version


         - Source/
         - - - 'Name of the Project.c'
         - Header/
         - Objects/

