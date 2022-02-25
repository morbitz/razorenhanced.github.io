# RE Autocomplete for Visual Studio Code Setup

**Author: HeelYes#0441**

This info comes from entries in Discord, and links to sites mentioned in Discord
## 1. INSTALL VISUAL STUDIO CODE (VSC).   
- Download the software here: https://code.visualstudio.com/ 
- Took defaults on Select Additional Task
- Install. (ex: Install path C:/program files/VSCode/ )
- Launch VSC
  
## 2. INSTALL THE PYTHON PACKAGE FOR VS CODE 
- Download the add-one: https://marketplace.visualstudio.com/items?itemName=ms-python.python
- This includes Python Language, Pylance and Jupyter

## 3. ADD ITONPYTHON TYPEINGS
- Download the IronPython stubs from @Gui_Talarico github: https://github.com/gtalarico/ironpython-stubs 
- Unziped the files into /VSCode/ironpython-stubs-master

## 4. Restart VSC (Alt-F4 to close)

## 5. CONFIGURE JSON SETTINGS IN VSC      
- In VSC  file > Preferences > Settings (or Ctrl+comma if you’re on windows 10).    
- Under the Settings tab, enter “python.autoComplete.extraPaths” into the Search Settings box (no quotes).    
  - Click on the “Edit in settings.json” link/button.    
  - Add the following into the line provided:  "…\\VSCode\\ironpython-stubs-master".    
  - Use the full path for your environment, include the quotes and double slashes.    
  - Hit CTRL-S to save the changes.    
  - Close the “settings.json” editor.    
- Click on the “Clear Setting Search Input” icon that is on the far right of the Search Box.    
- Under the Settings tab, enter “python.analysis.extraPaths” into the Search Settings box (no quotes).    
  - In the String Item area, add the following: ...\RazorEnh\Config     
  - Use the full path for your environment, no quotes, no double \    
  - Click the OK button.    
- Hit CTRL+S to save the changes, then ALT+F4 to exit VSC, then restart VSC.    

## 6. Open a new file and add the following code     
Test File to verify from      
```py
AutoComplete import *
Misc.SendMessage("Test MSC. AutoComplete working!", 33)
```

## 7. Verify that Intellisense is working
- Check for some of the RE API, like Player or like Misc.SendMessage.     
- Try to comment/uncomment the line of code of the "import", you should see the colors change on the Misc.SendMessage line, as the Intellisense is applied and removed.    

## 8. Save the file into your ER Script folder.    

## 9. In the Scripting Tab of ER, Add the file you created in the ER Script folder    

## 10. In the …\RazorEnhanced\Lib directory
- create a empty file named AutoComplete.py
- Save the file.    
- This allows RE to find an empty AutoComplete.py file and not trigger an error, while still allowing VSC to find the AutoComplete.py file in the RE Config folder.    

## 11. Test the execution of the test file that was created in VSC, and make sure it runs successfully in ER.    
    
## 12. In each of your scripts you want to edit in VSC, add the import:    
```py
from AutoComplete import *    
```    

## 13. I was able to add the …\RazorEnhanced\Scripts folder to the VSC Explorer by using File>Open Folder.

