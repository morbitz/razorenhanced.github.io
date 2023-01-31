# RazerEnhanced AutoComplete for Visual Studio Code

[[<<<]](../index.md)

## 1. Installing Visual Studio Code ( VSCode )
- Download the software from: https://code.visualstudio.com/
- Choose defaults
- Install
- Launch VSCode

## 2. Install the Python Package for VSCode
- Download the add-on from: https://marketplace.visualstudio.com/items?itemName=ms-python.python
- This includes Python Language, Pylance and Jupyter

## 3. Add IronPython Typings
- Download the IronPython Stubs from: https://github.com/gtalarico/ironpython-stubs
- Unziped the files into  ".../VSCode/ironpython-stubs-master"

## 4. Restart VSCode

## 5. Configure JSON Settings in VSCode
- In VSCode
  - File > Preferences > Settings

- Under the Settings tab, enter “python.autoComplete.extraPaths” into the Search Settings box (no quotes).
  - Click on the “Edit in settings.json” link/button.
  - Add the following into the line provided:  ".../VSCode/ironpython-stubs-master/release/stubs"
    - Use the full path for your environment, include the quotes and forward slashes or double backs slashes.
  - Hit CTRL+S to save the changes.

- Close the “settings.json” editor.
- Click on the “Clear Setting Search Input” icon that is on the far right of the Search Box.

- Under the Settings tab, enter “python.analysis.extraPaths” into the Search Settings box (no quotes).
  - In the String Item area, add the following: ".../RazorEnhanced/Config"
    - Use the full path for your environment, include the quotes and forward slashes or double backs slashes.
  - Hit CTRL+S to save the changes.

## 6. Restart VSCode

## 7. Open RazorEnhanced script folder in VSCode
- File > Open Folder...
- Browse to your RazorEnhanced script folder
- Click "Select Folder"

## 8. Create a new .py file and add the following code
```py
if True == False: from AutoComplete import *
Misc.SendMessage("Test Misc. AutoComplete working!", 33)
```

## 9. Verify that Intellisense is working
- Comment/Uncomment the import line in the test code above.
    - You should see the colors change on the Misc.SendMessage line as the Intellisense is applied and removed.
- Test with some other RE API's like Player or Items

## 10. Save the file in your RazorEnhanced Script folder.

## 11. In the Scripting Tab of RazorEnhanced, Add the file you just saved.

## 12. Test the script in RazorEnhanced to make sure it runs without errors.

## 13. In each of your scripts you want to edit in VSCode, add the import:
```py
if True == False: from AutoComplete import *
```


**Author: HeelYes#0441**
**Updated: Morbitz 01/30/23**
