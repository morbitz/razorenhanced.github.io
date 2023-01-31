# AutoComplete/Intellisense for RazorEnhanced in Visual Studio Code

[[<<<]](../index.md)


## 1. Installing Visual Studio Code ( VSCode )
- Download the software from: https://code.visualstudio.com/
- Install doc available from: https://code.visualstudio.com/docs/setup/windows
- Choose defaults
- Install & Launch VSCode

## 2. Install the Python Package for VSCode
- Download the add-on from: https://marketplace.visualstudio.com/items?itemName=ms-python.python
- Click Install on page, complete install in VSCode.
- This includes Python Language, Pylance and Jupyter.

## 3. Add IronPython Typings
- Download the IronPython Stubs from: https://github.com/gtalarico/ironpython-stubs
- Unziped the files into an empty folder.  For example: "C:/VSCode/ironpython-stubs-master"

## 4. Configure Settings.JSON in VSCode
- In VSCode
    - Press F1 to open Command Palette
    - Type "open user settings (json)"
    - Select "Open User Settings (JSON)" from list
    - Paste the following code in to the settings.json file.
    '''json
    {
        "python.analysis.extraPaths": [
            "C:/VSCode/ironpython-stubs-master/release/stubs",
            "C:/RazorEnhanced/Config"
        ]
    }
    - Edit paths to match your environment.
    - Save the settings.json file.

## 5. Create a new empty "AutoComplete.py" file in ".../RazorEnhanced/Lib/"
- This allows RE to find an empty AutoComplete.py file and not trigger an error.
- While still allowing VSCode to find the AutoComplete.py file in the RE Config folder.

## 6. Open RazorEnhanced script folder in VSCode
- File > Open Folder...
- Browse to your RazorEnhanced script folder
- Click "Select Folder"

## 7. Create a new .py file and add the following code
```py
from AutoComplete import *
Misc.SendMessage("Test: AutoComplete is working!", 68)
```

## 8. Verify that Intellisense is working
- Comment/Un-comment the import line in the test code above.
    - You should see the colors change on the Misc.SendMessage line as the Intellisense is removed and applied.
- Test with some other RE API's like Player or Items

## 10. Save the file in your RazorEnhanced Script folder.

## 11. In the Scripting Tab of RazorEnhanced, Add the file you just saved.

## 12. Test the script in RazorEnhanced to make sure it runs without errors.

## 13. In each of your scripts you want to edit in VSCode, add the import line:
```py
from AutoComplete import *
```


**Author: HeelYes#0441**

**Updated: 01/30/23 by Morbitz**
