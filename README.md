C-Project-Generator
===================

A plug-in for Sublime-Text 3 which allows the creation and management of project C.

##Create a Make file :

###Condition:
The project must have this file hierarchie:

#####Project Folder/ :#####
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



Open  Command Palette : `CTRL+Shift+P` execute `Generate Make`.
This command will create the file `makefile.in` at the root of the project here: `Project Folder/`.
