
import requests
from bs4 import BeautifulSoup
import glob 



def main():
  dkw = dokuwiki()
  dkw.path_dump = "./dump/"
  dkw.path_wiki = "./wiki/"
  #dkw.dumpAllPages(pages)
  dkw.convertAllPages()


class dokuwiki():
  def __init__(self):
    self.pages = None
    self.path_dump = None
    self.path_wiki = None

  def url_src(self, page):
    url = "https://razorenhanced.net/dokuwiki/doku.php?do=edit&id={}"
    return url.format(page)

  def url_dump(self, page):
    return self.path_dump+page+".txt"


  def extractCode(self, content):
    parser = BeautifulSoup(content, "html.parser")
    codeblocks = parser.find_all("code")
    for codeblock in codeblocks:
      

  def convertPage(self, content):
    return content


  def convertAllPages(self):
    files = glob.glob(self.path_dump+"*")
    for file in files:
      pathlen = len(self.path_dump)
      name = file[pathlen:]
      name = name.replace('.txt','')
      name = name.replace('\\','')
      print(name)

      content = None
      with open(file,'r') as f: content = f.read()
      
      converted = self.convertPage(content)
      with open(self.path_wiki+"/"+name+".md", 'w') as f: f.write(converted)


  

  def dumpAllPages(self, pages):
    self.pages = pages
    for page in self.pages:
      fullurl = self.url_src(page)
      src = self.dumpPage(fullurl)
      if src is None: continue
      print(src)
      filename = self.url_dump(page)
      with open(filename,'w') as file: file.write(src)
      


  def dumpPage(self, fullurl):
      req = requests.get(fullurl)
      if req.status_code >= 400: return None
      parser = BeautifulSoup(req.content, "html.parser")
      textareas = parser.find_all("textarea")
      if len(textareas) != 1: return None
      textarea = textareas[0]
      return textarea.text





# links manually dumped from sitemap => https://razorenhanced.net/dokuwiki/doku.php?id=alchemy&do=index
pages = [
"alchemy",
"animalpetscripts",
"autoloot_agent",
"autoloot_func",
"bandage_crafter",
"bandage_func",
"bandage_heal_agnet",
"bardscripts",
"blacksmithing",
"bola_crafter",
"bushido",
"carpentry",
"cast_function",
"casting_trainers",
"chivalry",
"combatscripts",
"command_list", 
"cooking",
"crafting",
"crafting_trainers",
"craftscripts",
"credzba",
"download",
"dps_func",
"dress_func",
"dress_undress_agent",
"enchanted_apple_crafter",
"enhanced_filters_tab",
"enhanced_hotkey_tab",
"enhanced_target_tab",
"enhanced_toolbar_tab",
"fletching",
"frank_castle",
"friend_list_agent",
"friends_func",
"full_mysticism_spellbook_crafter",
"full_necromancy_spellbook_crafter",
"full_spellbook_crafter",
"general_tab",
"gump_funcs",
"imbuing",
"inscription",
"install_configure",
"item_func",
"item_struct",
"journal_func",
"launcher",
"mage_and_eval_trainer",
"misc",
"misc_func",
"mobile_func",
"mobile_struct",
"mourn",
"mysticism",
"necromancy",
"organizer_agent",
"organizer_func",
"other",
"patches_for_osi_client",
"pathfinding_func",
"player_data_and_function",
"player_provided",
"poisoning",
"resourcegatheringscripts",
"restock_func",
"runebook_and_runic_atlas_copier",
"runic_atlas_crafter",
"scavenger_agent",
"scavenger_func",
"screen_shots_tab",
"sharedvalue_example",
"simple_input_example",
"skills_tab",
"sound_func",
"spellweaving",
"start",
"statics_func",
"tailoring",
"target_func",
"test",
"timer_func",
"tinkering",
"toolscripts",
"trainingscripts",
"treasurescripts",
"unblock",
"usewithcuo",
"utility",
"vendor_buy_agent",
"vendor_buy_func",
"vendor_sell_agent",
"vendor_sell_func",
"video_guide"]



if __name__ == '__main__':
  main()