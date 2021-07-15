# RE Autocomplete for Visual Studio Code Setup
This info comes from entries in Discord, and links to sites mentioned in Discord
1. INSTALL VISUAL STUDIO CODE.   You can download the software here.   
    https://code.visualstudio.com/  Or any other location you find.
        1.1 Took defaults on Select Additional Task
        1.2 Install.  Installed into …\VSCode\
        1.3 Launch VSC

2. INSTALL THE PYTHON PACKAGE FOR VS CODE you can download it here
    https://marketplace.visualstudio.com/items?itemName=ms-python.python
    a. This includes Python Language, Pylance and Jupyter

3. DOWNLOAD THE IRONPYTHON STUBS FROM @Gui_Talarico github.  
    1. Unziped the files into …\VSCode\ironpython-stubs-master

4. Restart VSC (Alt-F4 to close)

5. CONFIGURE JSON SETTINGS IN VSC
    a. In VSC  file > Preferences > Settings (or Ctrl+comma if you’re on windows 10)
    b. Under the Settings tab, enter “python.autoComplete.extraPaths” into the Search Settings box (no quotes).
        i.    Click on the “Edit in settings.json” link/button.
        ii.    Add the following into the line provided:  "…\\VSCode\\ironpython-stubs-master"
        iii.    Use the full path for your environment, include the quotes and double slashes.
        iv.    Hit CTRL-S to save the changes
        v.    Close the “settings.json” editor.
    c.    Click on the “Clear Setting Search Input” icon that is on the far right of the Search Box.
    d.    Under the Settings tab, enter “python.analysis.extraPaths” into the Search Settings box (no quotes).
        1. In the String Item area, add the following: ...\RazorEnh\Config 
        2. Use the full path for your environment, no quotes, no double \
        3. Click the OK button.
    e. Hit CTRL+S to save the changes, then ALT+F4 to exit VSC, then restart VSC.

6. Open a new file and add the following code (Test File to verify from)
```py
AutoComplete import *
Misc.SendMessage("Test MSC. AutoComplete working!", 33)
```

7. Verify that Intellisense is working for the ER specific objects, like Misc.  Note if you comment, and then uncomment         the Import line of code, you should see the colors change on the Misc. line of code as the Intellisense is applied and         removed.

8. Save the file into your ER Script folder.

9. In the Scripting Tab of ER, Add the file you created in the ER Script folder

10 .In the …\RazorEnh\Lib directory, create a file named AutoComplete.py, and paste: 
    # Empty shell to allow from AutoComplete import * to work.
    a.    Save the file.
    b.    This allows ER to find an empty AutoComplete.py file and not kick out an error, while still allowing VSC to             find the AutoComplete.py file in the ER Config folder.

11. Test the execution of the test file that was created in VSC, and make sure it runs successfully in ER.

12. In each of your scripts you want to edit in VSC, add the import:
```py
from AutoComplete import *
```

13. I was able to add the …\RazorEnh\Scripts folder to the VSC Explorer by using File>Open Folder.
