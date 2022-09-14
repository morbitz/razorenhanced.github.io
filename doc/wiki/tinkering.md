
<code>

#Tinkering Trainer by Frank Castle

#

#What you need:

# 1 - 30.0+ Tinkering Skill. If you dont have it buy it up. 

# 2 - a player made Tinker Tools

# 3 - a chest with plenty of iron ingots

# 4 - a trash barrel locked down and secured within reach

#

# Written and tested on OSI.

#

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!IMPORTANT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# MAKE SURE YOU HAVE NO RINGS, BRACELETS, SCISSORS, TONGS, OR SPYGLASSES YOU WISH TO KEEP IN YOUR BACKPACK

from System.Collections.Generic import List



global stoCont



stoCont = Target.PromptTarget('Target your resource chest')

Misc.Pause(100)

Items.UseItem(stoCont)

Misc.Pause(1100)



Player.UseSkill('Hiding')

Misc.Pause(11000)



GFilter = Items.Filter()

GFilter.RangeMax = 5

GFilter.OnGround = True

GFilter.Enabled = True

GFilter.Movable = True

garbagecan = List[int]((0x0E77, 0x0E77))  

GFilter.Graphics = garbagecan



def checkIngots():

    if Items.BackpackCount(0x1BF2,0x0000) < 12:

        global stoCont

        Misc.Pause(1100)

        ingot = Items.FindByID(0x1BF2,0x0000,stoCont)

        Misc.Pause(100)

        Items.Move(ingot,Player.Backpack.Serial,200)

        Misc.Pause(1100)



def checkTools():

    countOne = Items.BackpackCount(0x1EB9,-1)

    while countOne < 3:

        tinkerTool = Items.FindByID(0x1EB9,-1,Player.Backpack.Serial)

        Misc.Pause(100)

        Items.UseItem(tinkerTool)

        Gumps.WaitForGump(460, 10000)

        Gumps.SendAction(460, 11)

        Misc.Pause(1500)

        countOne = Items.BackpackCount(0x1EB9,-1)

        Misc.SendMessage('I have {} tinker tools in my bag'.format(countOne),48)

    

def saveItem(item):

    global stoCont

    if Player.Weight > Player.MaxWeight - 30:

        if Items.BackpackCount(item,-1) > 0:

            move = Items.FindByID(item,-1,Player.Backpack.Serial)

            Items.Move(move,stoCont,0)

        

def TrashItem(item):

    garbagecans = Items.ApplyFilter(GFilter)

    Misc.Pause(500)

    garbagecan = Items.Select(garbagecans, 'Nearest')

    Misc.Pause(500)

    if Items.BackpackCount(item,-1) > 0:

        move = Items.FindByID(item,-1,Player.Backpack.Serial)

        Items.Move(move,garbagecan,0) 

        Misc.Pause(1100)   

   

    

while True:

    Tinkering = Player.GetSkillValue('Tinkering')

    if Tinkering < 45:

        checkIngots()

        checkTools()

        tinkerTool = Items.FindByID(0x1EB9,-1,Player.Backpack.Serial)

        Misc.Pause(100)

        Items.UseItem(tinkerTool)

        Gumps.WaitForGump(460, 1500)

        Gumps.SendAction(460, 8)   #MAKE SCISSORS

        TrashItem(0x0F9E)

        Misc.Pause(100)



        

    elif Tinkering >= 45 and Tinkering < 60:

        checkIngots()

        checkTools()

        tinkerTool = Items.FindByID(0x1EB9,-1,Player.Backpack.Serial)

        Misc.Pause(100)

        Items.UseItem(tinkerTool)

        Gumps.WaitForGump(460, 1500)

        Gumps.SendAction(460, 20)  #MAKE TONGS

        TrashItem(0x0FBC) 

        

    elif Tinkering >= 60 and Tinkering < 75:

        checkIngots()

        checkTools()

        tinkerTool = Items.FindByID(0x1EB9,-1,Player.Backpack.Serial)

        Misc.Pause(100)

        Items.UseItem(tinkerTool)

        Gumps.WaitForGump(460, 1500)

        Gumps.SendAction(460, 25)  #MAKE LOCKPICKS

        saveItem(0x14FB)

       

    elif Tinkering >= 75 and Tinkering < 85:

        checkIngots()

        checkTools()

        tinkerTool = Items.FindByID(0x1EB9,-1,Player.Backpack.Serial)

        Misc.Pause(100)

        Items.UseItem(tinkerTool)

        Gumps.WaitForGump(460, 1500)

        Gumps.SendAction(460, 2) #MAKE BRACELETS

        TrashItem(0x1086)



    elif Tinkering >= 85 and Tinkering < 90:

        checkIngots()

        checkTools()

        tinkerTool = Items.FindByID(0x1EB9,-1,Player.Backpack.Serial)

        Misc.Pause(100)

        Items.UseItem(tinkerTool)

        Gumps.WaitForGump(460, 1500)

        Gumps.SendAction(460, 56) #MAKE SPYGLASS

        TrashItem(0x14F5)

        

    elif Tinkering >= 90 and Tinkering != Player.GetSkillCap('Magery'):

        checkIngots()

        checkTools()

        tinkerTool = Items.FindByID(0x1EB9,-1,Player.Backpack.Serial)

        Misc.Pause(100)

        Items.UseItem(tinkerTool)

        Gumps.WaitForGump(460, 10000)

        Gumps.SendAction(460, 1) #MAKE RINGS

        TrashItem(0x108A)

   

    elif Tinkering == Player.GetSkillCap('Tinkering'):

        Misc.ScriptStopAll()

    Misc.Pause(1100)





</code>