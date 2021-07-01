"""
Script: AutoDoc.py
Version: 0.1
Author: Dalamar Kanan
Project: Razor Enhanced - AutoDoc
    
Contact: 
    https://discord.gg/2NmXqQ5QAk (@RE Dev)
    Dalamar#2877
    cesare.montresor@gmail.com 
    
Abstract:
    This script produce RazorEnhanced API documentation (only HTML atm) by reading the *Scripting API Data* contained in Config/AutoComplete.json
    The AutoComplete.json file it produced by the counterpart of this script inside RarzorEnhaced engine:
    https://github.com/RazorEnhanced/RazorEnhanced/blob/release/0.8/Razor/RazorEnhanced/AutoDoc.cs 
    

Classes:
    HTML:
        - Containes *all the HTML* code and functions as a theme template. HTML is used by AutoDocHTML and can be used directly.
        - This class can be copied/replaced/customized to alter the structure of the page and make custom Themes.
        - However, before changing this class is adivced to first attempt customization via css (much easier).
        - The standard generated page includes by default also a main.css and a main.js.
        - HTML class don't use *complex object* in input, just *simple string*.

    AutoDoc:
        - Loads the Config/AutoComplete.json and provide convenience methods to query and filter the data.
        - AutoDoc is used by AutoDocHTML and can be used directly.
        - AutoDoc produce *complex object* as result of the json structure.

    AutoDocHTML: 
        - AutoDocHTML uses both AutoDoc and HTML classes.
        - Pull the data as *complex objects* from AutoDoc and combine them into *simple strings* give it to the HTML class to decorate.
        - Return elaborate HTML Chunks, with data.
        - AutoDocHTML shoudn't contain any *actual HTML*

Main:
    - Reperents the entry point of this script, the first function that Run when you Run the script. ( see the end of this file for details )
    - The code in the main() function should be minimal, ideally only 2 lines:
        adio=AutoDocHTML(doc_path)
        adio.MakeDocumentation()
        


Updates:
    29-Jun-2021: Dalamar
        At the time of writing, the main() function is messy because is used to test everything else.
"""

import json
import os


def main():
    output_path = "/api/"
    # setup AutoDocHTML to a test path
    doc_path = Misc.CurrentScriptDirectory()+output_path
    adhtml=AutoDocHTML(doc_path)
    
    # generates the main menu from the list of classes
    menu = adhtml.MainMenuHTML()
    index_html = HTML.BasePage(menu,"RazorEnhanced API Documentation")
    adhtml.WriteToFile("{}index.html".format(output_path), index_html)
    
    # generates doc page for the Player class ( usefull for testing ) 
    # player_html = adhtml.ClassHTML("Player")
    # player_html = HTML.BasePage(player_html,"Player - RazorEnhanced API")
    # adhtml.WriteToFile("Player.html", player_html)
    
    ## generates doc pages for All the classes.
    for cls in adhtml.ad.GetClasses():
        className = cls["itemClass"]
        filename = "{}{}.html".format(output_path,className)
        player_html = adhtml.ClassHTML(className)
        player_html = HTML.BasePage(player_html,"{} - RazorEnhanced API".format(className))
        adhtml.WriteToFile(filename, player_html)
    
    
    
class HTML():
    @staticmethod
    def ClassContainer(name, description, properties, contructors, methods, cssId=None, cssClass=None ):
        name_html = HTML.Div(name,cssClass="class-name")
        description_html = HTML.Div(description,cssClass="class-description")
        properties_html = "" if len(properties) == 0 else HTML.Div(properties,cssClass="class-properties")
        contructors_html = "" if len(contructors) == 0 else HTML.Div(contructors,cssClass="class-contructors")
        methods_html = "" if len(methods) == 0 else HTML.Div(methods,cssClass="class-methods")
        
        class_content = "\n".join([
            name_html,
            description_html,
            properties_html,
            contructors_html,
            methods_html
        ])
        
        class_html = HTML.Div(class_content, cssId=cssId, cssClass=cssClass)
        return class_html
    
    def PropertiesContainer():
        # TODO
        return ""
        
    def ConstructorContainer():
        # TODO
        return ""
        
# content
    @staticmethod
    def MethodContainer(className, methodName, description, signature, parameters, returns, cssId=None, cssClass=None ):
        className_html = HTML.Div(className,cssClass="method-class-name")
        methodName_html = HTML.Div(methodName,cssClass="method-name")
        signature_html = HTML.Div(signature,cssClass="method-signature")
        description_html = "" if len(description) == 0 else HTML.Div(description,cssClass="method-description")
        parameters_html = "" if len(parameters) == 0 else HTML.Div(parameters,cssClass="method-parameters")
        returns_html = "" if len(returns) == 0 else HTML.Div(returns,cssClass="method-returns")
        
        method_content = "\n".join([
            className_html,
            methodName_html,
            signature_html,
            description_html,
            parameters_html,
            returns_html
        ])
        
        class_html = HTML.Div(method_content, cssId=cssId, cssClass=cssClass)
        return class_html
    
# pages
    @staticmethod
    def BasePage(body, title=""):
        css_html = HTML.CSS("./main.css")
        js_html = HTML.JS("./main.js")
        header_html = css_html +"\n"+ js_html
        body_html = HTML.Div(body,cssId="redoc-page-container")
        
        return HTML.EmptyPage(body_html, title, header_html)
        
        
    @staticmethod
    def EmptyPage(body,title="",header=""):
        title_html = "" if len(title)==0 else "\n<title>{}</title>\n".format(title)
        header_html = "" if (len(header)==0 and len(title_html)==0) else "\n<header>{}\n{}\n</header>\n".format(title_html,header)
        body_html = "" if len(body)==0 else "\n<body>\n{}\n</body>\n".format(body)
        return '<!Doctype html>{}{}</html>'.format(header_html, body_html)
    
# subemenets
    
 
    @staticmethod
    def ParamForSignature(name, paramType, cssId=None,  cssClass=None ):
        if cssClass is None: cssClass = 'redoc-method-params-sign'
        cssId = '' if cssId is None else ' id="{}"'.format(cssId)
        cssClass = ' class="{}"'.format(cssClass)
        name_html =  HTML.VariableName(name)
        type_html = '' if paramType is None or paramType == "" else HTML.VariableType(paramType)
        return '<div{}{}>{}{}</div>'.format(cssId, cssClass, name_html, type_html )
    
    @staticmethod
    def ParamForDescription(name, type, description, cssId=None,  cssClass=None ):
        if cssClass is None: cssClass = 'redoc-method-params'
        cssId = '' if cssId is None else ' id="{}"'.format(cssId)
        cssClass = ' class="{}"'.format(cssClass)
        name_html =  HTML.VariableName(name)
        type_html =  HTML.VariableType(type)
        desc_html =  '' if description is None or description == "" else HTML.Div(description, cssClass='redoc-method-params-desc')
        return '<div{}{}>{}{}{}</div>'.format(cssId, cssClass, name_html, type_html, desc_html) 
    
    @staticmethod
    def VariableType(content, cssId=None,  cssClass=None):
        if cssClass is None: cssClass = 'redoc-variable-type'
        cssId = '' if cssId is None else ' id="{}"'.format(cssId)
        cssClass = ' class="{}"'.format(cssClass)
        return '<div{}{}>{}</div>'.format(cssId, cssClass, content)
        
    @staticmethod
    def VariableName(content, cssId=None,  cssClass=None):
        if cssClass is None: cssClass = 'redoc-variable-name'
        cssId = '' if cssId is None else ' id="{}"'.format(cssId)
        cssClass = ' class="{}"'.format(cssClass)
        return '<div{}{}>{}</div>'.format(cssId, cssClass, content)
        
    @staticmethod
    def MethodReturn(type, description, cssId=None,  cssClass=None):
        if cssClass is None: cssClass = 'redoc-method-return'
        cssId = '' if cssId is None else ' id="{}"'.format(cssId)
        cssClass = ' class="{}"'.format(cssClass)
        type_html =  HTML.VariableType(type)
        desc_html =  '' if description is None or description == "" else HTML.Div(description, cssClass='redoc-method-return-desc')
        return '<div{}{}>{}{}</div>'.format(cssId, cssClass, type_html, desc_html)
    
        
# base html elements
    @staticmethod
    def CSS(url,inline=False):
        css_html = '<style>{}</style>' if inline else '<link rel="stylesheet" type="text/css" href="{}">'
        css_html = css_html.format(url)
        return css_html
        
        
    @staticmethod
    def JS(url,inline=False):
        js_html = '<script>\n{}\n</script>' if inline else '<script src="{}"></script>'
        js_html = js_html.format(url)
        return js_html
    
        
    @staticmethod
    def Div(content, cssId=None,  cssClass=None ):
        cssId = '' if cssId is None else ' id="{}"'.format(cssId)
        cssClass = '' if cssClass is None else ' class="{}"'.format(cssClass)
        return '<div{}{}>{}</div>'.format(cssId, cssClass, content)
        
    @staticmethod
    def Link(content, url=None, cssId=None,  cssClass=None ):
        url = '' if url is None else ' href="{}"'.format(url)
        cssId = '' if cssId is None else ' id="{}"'.format(cssId)
        cssClass = '' if cssClass is None else ' class="{}"'.format(cssClass)
        return '<a{}{}{}>{}</a>'.format(cssId, cssClass, url, content)
        
        
    
class AutoDocHTML:
    def __init__(self, output_path=None):
        self.doc_path = Misc.CurrentScriptDirectory() + "/Docs/" if output_path is None else output_path
        self.ad = AutoDoc()
    
    def MainMenuHTML(self, menuId='redoc-main-menu', itemClass='redoc-main-menu-entry'):
        classList = self.ad.GetClasses()
        links = []
        for cls in classList:
            name = cls["itemClass"]
            url = "./{}.html".format(name)
            html = HTML.Link(name, url, cssClass=itemClass )
            links.append( html )
        #
        links_html = "\n".join(links)
        main_menu = HTML.Div(links_html, cssId=menuId)
        return main_menu
        
    def ClassHTML(self, className, classId='redoc-class-', itemClass='redoc-class'):
        classList = self.ad.GetClasses(className)
        if len(classList)==0: return "Class not found: {}".format(className);
        doc_class = classList[0]
        
        description = doc_class["itemDescription"]
        properties_html = self.ProperiesHTML(className)
        constructors_html = self.ConstructorsHTML(className)
        methods_html = self.MethodsHTML(className)
        
        class_html = HTML.ClassContainer(className, description, properties_html, constructors_html, methods_html, cssId=classId, cssClass=itemClass)
        return class_html
        
    def ProperiesHTML(self, className):
        # TODO
        return "TODO: "+className+" Properties"
        
    def ConstructorsHTML(self, className):
        # TODO
        return "TODO: "+className+" Constructors" 
        
    def MethodsHTML(self, className):
        methodList = self.ad.GetMethods(className)
        methods_html_list = []
        for method in methodList:
            methods_html_list.append( self.MethodDetailHTML(className, method["itemName"]) )
        #    
        methods_html = "\n".join(methods_html_list)
        
        return methods_html
        
        
    def MethodDetailHTML(self, className, methodName):
        methodList = self.ad.GetMethods(className, methodName)
        methods_html_list = []
        for method in methodList:
            description = method["itemDescription"]
            paramList = method["paramList"]
            methodReturn = HTML.MethodReturn(method["returnType"], method["returnDesc"] )
            paramSignature = [HTML.ParamForSignature(p['itemName'], p['itemType']) for p in paramList]
            paramDescription = [HTML.ParamForDescription(p['itemName'], p['itemType'], p['itemDescription']) for p in paramList]
            cssClass = 'redoc-method-container' 
            
            signature_html = "({})".format( ", ".join(paramSignature) )
            paramsDesc = "\n".join(paramDescription)
            
            
            method_html = HTML.MethodContainer(className, methodName, description, signature_html, paramsDesc, methodReturn, cssClass=cssClass )
            methods_html_list.append(method_html)
            
        #    
        methods_html = "\n".join(methods_html_list)
        
        return methods_html
        
    def WriteToFile(self, path, content):
        fullpath = self.doc_path + path
        dirpath  = os.path.dirname(fullpath)
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)
        Misc.SendMessage(fullpath)
        file = open(fullpath,'w+')
        file.write(content)
        file.close()
        
     
        
    
    

class AutoDoc:
    # Load data from AutoComplete.json and provides several convenience methods to query the content.
    
    def __init__(self):
        self.api_data = None
        self.api_path = Misc.ConfigDirectory() + "/AutoComplete.json"
        
    def GetSettings(self):
        api = self.GetPythonAPI()
        docs = api["settings"]
        return docs
        
    def GetClasses(self, filterClass=None):
        api = self.GetPythonAPI()
        docs = api["classes"]
        docs = list( sorted(docs, key=lambda doc: doc["itemClass"]) )
        if filterClass is not None:
            docs = list(filter(lambda doc: doc["itemClass"] == filterClass,docs))
        return docs
    
    def GetProperties(self, filterClass=None):
        api = self.GetPythonAPI()
        docs = api["properties"]
        if filterClass is not None:
            docs = list(filter(lambda doc: doc["itemClass"] == filterClass,docs))
        #
        docs = list( sorted(docs, key=lambda doc: (doc["itemClass"], doc["itemName"]) ) )
        return docs
        
    def GetConstructors(self, filterClass=None):
        api = self.GetPythonAPI()
        docs = api["constructors"]
        if filterClass is not None:
            docs = list(filter(lambda doc: doc["itemClass"] == filterClass, docs))
        #
        docs = list( sorted(docs, key=lambda doc: (doc["itemClass"], doc["itemName"]) ) )
        return docs
        
    def GetMethods(self, filterClass=None, filterName=None):
        api = self.GetPythonAPI()
        docs = api["methods"]
        
        if filterClass is not None:
            docs = list(filter(lambda doc: doc["itemClass"] == filterClass,docs))
        #
        if filterName is not None:
            docs =  list(filter(lambda doc: doc["itemName"] == filterName,docs))
        #
        docs = list( sorted(docs, key=lambda doc: (doc["itemClass"], doc["itemName"], -len(doc["paramList"]) ) ) )
        return docs
    
    
    def GetPythonAPI(self):
        if self.api_data is not None: return self.api_data
        
        Misc.SendMessage("Loading from Path:\n{}".format(self.api_path))
        
        api_file = open(self.api_path,'r+')
        api_json = api_file.read()
        api_file.close()
        Misc.SendMessage("File Size: {}".format(len(api_json)) )
        self.api_data = json.loads(api_json)
        
        return self.api_data
        


"""
By placing the call to the main function at the bottom of the file, there is the freedom to rearrage the code freely in the file.

NOTE: *if __name__ == '__main__':* make sure that the main() is called only when the script is run directly.
      In this way is possible to safely use this file also via "include autodoc" without worrying that the main() would be executed.
"""
if __name__ == '__main__':
    main() 
