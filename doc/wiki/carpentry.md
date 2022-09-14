
<code>

#Carpentry Trainer by Frank Castle

#

#What you need:

# 1 - 30.0+ Tinkering Skill. If you do not have it buy it up. 

# 1 - 30.0+ Carpentry Skill. If you do not have it buy it up.

# 2 - a player made Tinker Tools

# 3 - a chest with plenty of iron ingots and wood

# 

# Written and tested on OSI. 



from System.Collections.Generic import List



global stoCont







    



stoCont = Target.PromptTarget('Target your resource chest')

Misc.Pause(100)

Items.UseItem(stoCont)

Misc.Pause(1100)



GFilter = Items.Filter()

GFilter.RangeMax = 5

GFilter.OnGround = True

GFilter.Enabled = True

GFilter.Movable = True

garbagecan = List[int]((0x0E77, 0x0E77))  

GFilter.Graphics = garbagecan



Player.UseSkill('Hiding')

Misc.Pause(11000)





def makeLast(skill, item):

    Carpentry = Player.GetSkillValue('Carpentry')

    plane = Items.FindByID(0x1030,-1,Player.Backpack.Serial)

    Items.UseItem(plane)

    while Carpentry < skill and Carpentry != Player.GetSkillCap('Carpentry'):

        Carpentry = Player.GetSkillValue('Carpentry')

        checkBoards()

        Gumps.WaitForGump(460, 1500)

        Gumps.SendAction(460, 1999)

        Misc.Pause(500)

        Misc.SendMessage('Crafting Last',48)

        

        if Journal.Search('You have worn out') == True:

            Journal.Clear()

            checkTools()

            plane = Items.FindByID(0x1030,-1,Player.Backpack.Serial)

            Items.UseItem(plane)

           

        if Items.BackpackCount(item,-1) > 0:

            craft = Items.FindByID(item,-1,Player.Backpack.Serial)

            hatchet = Items.FindByID(0x0F43,-1,Player.Backpack.Serial)

            Items.UseItem(hatchet)

            Target.WaitForTarget(1500,False)

            Target.TargetExecute(craft)

            Misc.Pause(1100)

            Misc.SendMessage('Chopping',48)

    

        





def checkBoards():

    if Items.BackpackCount(0x1BD7,0x0000) < 25:

        global stoCont

        Misc.SendMessage('Getting Boards',48)

        Misc.Pause(1100)

        board = Items.FindByID(0x1BD7,0x0000,stoCont)

        Misc.Pause(100)

        Items.Move(board,Player.Backpack.Serial,200)

        Misc.Pause(1100)

        

def checkIngots():

    if Items.BackpackCount(0x1BF2,0x0000) < 15:

        global stoCont

        Misc.SendMessage('Getting Ingots',48)

        Misc.Pause(1100)

        ingot = Items.FindByID(0x1BF2,0x0000,stoCont)

        Misc.Pause(100)

        Items.Move(ingot,Player.Backpack.Serial,40)

        Misc.Pause(1100)

        

def checkTools():

    checkIngots()

    checkBoards()

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

        

    countTwo = Items.BackpackCount(0x1030,-1)

    while countTwo < 3:

        tinkerTool = Items.FindByID(0x1EB9,-1,Player.Backpack.Serial)

        Misc.Pause(100)

        Items.UseItem(tinkerTool)

        Gumps.WaitForGump(460, 10000)

        Gumps.SendAction(460, 73)

        Misc.Pause(1500)

        countTwo = Items.BackpackCount(0x1030,-1)

        Misc.SendMessage('I have {} joining planes in my bag'.format(countTwo),48)

        

def hatchetCheck(): 

    hatchetCount = Items.BackpackCount(0x0F43,-1)

    if hatchetCount < 1:

        checkTools()

        tinkerTool = Items.FindByID(0x1EB9,-1,Player.Backpack.Serial)

        Misc.Pause(100)

        Items.UseItem(tinkerTool)

        Gumps.WaitForGump(460, 10000)

        Gumps.SendAction(460, 12)

        Misc.Pause(500)

        Misc.SendMessage('I now have a hatchet',48)



        

def selectCraft():

    hatchetCheck()

    Misc.Pause(2000)

    Carpentry = Player.GetSkillValue('Carpentry')

    if Carpentry < 48:

        checkBoards()

        checkTools()

        Misc.SendMessage('Making Medium Crates',48)

        plane = Items.FindByID(0x1030,-1,Player.Backpack.Serial)

        Items.UseItem(plane)

        Gumps.WaitForGump(460, 10000)

        Gumps.SendAction(460, 99)   

        makeLast(48, 0x0E3E)

        Misc.Pause(100)





    if Carpentry >= 48 and Carpentry < 53 :

        lastCraft = Items.FindByID(0x0E3E, -1, Player.Backpack.Serial)

        if lastCraft:

            hatchet = Items.FindByID(0x0F43,-1,Player.Backpack.Serial)

            Items.UseItem(hatchet)

            Target.WaitForTarget(1500,False)

            Target.TargetExecute(lastCraft)

            Misc.Pause(500)

        checkBoards()

        checkTools()

        Misc.SendMessage('Making Large Crates',48)

        plane = Items.FindByID(0x1030,-1,Player.Backpack.Serial)

        Items.UseItem(plane)

        Gumps.WaitForGump(460, 10000)

        Gumps.SendAction(460, 100)   

        makeLast(53, 0x0E3C)

        Misc.Pause(100)        

        

    if Carpentry >= 53 and Carpentry < 60 :

        lastCraft = Items.FindByID(0x0E3C, -1, Player.Backpack.Serial)

        if lastCraft:

            hatchet = Items.FindByID(0x0F43,-1,Player.Backpack.Serial)

            Items.UseItem(hatchet)

            Target.WaitForTarget(1500,False)

            Target.TargetExecute(lastCraft)

            Misc.Pause(500)

        checkBoards()

        checkTools()

        Misc.SendMessage('Making Wooden Shields',48)

        plane = Items.FindByID(0x1030,-1,Player.Backpack.Serial)

        Items.UseItem(plane)

        Gumps.WaitForGump(460, 10000)

        Gumps.SendAction(460, 120)   

        makeLast(60, 0x1B7A)

        Misc.Pause(100)

        

    if Carpentry >= 60 and Carpentry < 74 :

        lastCraft = Items.FindByID(0x1B7A, -1, Player.Backpack.Serial)

        if lastCraft:

            hatchet = Items.FindByID(0x0F43,-1,Player.Backpack.Serial)

            Items.UseItem(hatchet)

            Target.WaitForTarget(1500,False)

            Target.TargetExecute(lastCraft)

            Misc.Pause(500)

        checkBoards()

        checkTools()

        Misc.SendMessage('Making Fukiyas',48)

        plane = Items.FindByID(0x1030,-1,Player.Backpack.Serial)

        Items.UseItem(plane)

        Gumps.WaitForGump(460, 10000)

        Gumps.SendAction(460, 122)   

        makeLast(74, 0x27AA)

        Misc.Pause(100)

        

    if Carpentry >= 74 and Carpentry < 79 :

        lastCraft = Items.FindByID(0x27AA, -1, Player.Backpack.Serial)

        if lastCraft:

            hatchet = Items.FindByID(0x0F43,-1,Player.Backpack.Serial)

            Items.UseItem(hatchet)

            Target.WaitForTarget(1500,False)

            Target.TargetExecute(lastCraft)

            Misc.Pause(500)

        checkBoards()

        checkTools()

        Misc.SendMessage('Making Quarter Staffs',48)

        plane = Items.FindByID(0x1030,-1,Player.Backpack.Serial)

        Items.UseItem(plane)

        Gumps.WaitForGump(460, 10000)

        Gumps.SendAction(460, 118)   

        makeLast(79, 0x0E89)

        Misc.Pause(100)       

        

    if Carpentry >= 79 and Carpentry < 82 :

        lastCraft = Items.FindByID(0x0E89, -1, Player.Backpack.Serial)

        if lastCraft:

            hatchet = Items.FindByID(0x0F43,-1,Player.Backpack.Serial)

            Items.UseItem(hatchet)

            Target.WaitForTarget(1500,False)

            Target.TargetExecute(lastCraft)

            Misc.Pause(500)

        checkBoards()

        checkTools()

        Misc.SendMessage('Making Gnarled Staffs',48)

        plane = Items.FindByID(0x1030,-1,Player.Backpack.Serial)

        Items.UseItem(plane)

        Gumps.WaitForGump(460, 10000)

        Gumps.SendAction(460, 119)   

        makeLast(82 ,0x13F8)

        Misc.Pause(100) 

        

    if Carpentry >= 82 and Carpentry < 96 :

        lastCraft = Items.FindByID(0x13F8, -1, Player.Backpack.Serial)

        if lastCraft:

            hatchet = Items.FindByID(0x0F43,-1,Player.Backpack.Serial)

            Items.UseItem(hatchet)

            Target.WaitForTarget(1500,False)

            Target.TargetExecute(lastCraft)

            Misc.Pause(500)

        checkBoards()

        checkTools()

        Misc.SendMessage('Making Black Staffs',48)

        plane = Items.FindByID(0x1030,-1,Player.Backpack.Serial)

        Items.UseItem(plane)

        Gumps.WaitForGump(460, 10000)

        Gumps.SendAction(460, 906)   

        makeLast(96 ,0x0DF0)

        Misc.Pause(100) 

 

    if Carpentry >= 96 and Carpentry < 100 :

        lastCraft = Items.FindByID(0x0DF0, -1, Player.Backpack.Serial)

        if lastCraft:

            hatchet = Items.FindByID(0x0F43,-1,Player.Backpack.Serial)

            Items.UseItem(hatchet)

            Target.WaitForTarget(1500,False)

            Target.TargetExecute(lastCraft)

            Misc.Pause(500)

        checkBoards()

        checkTools()

        Misc.SendMessage('Making Wild Staffs',48)

        plane = Items.FindByID(0x1030,-1,Player.Backpack.Serial)

        Items.UseItem(plane)

        Gumps.WaitForGump(460, 10000)

        Gumps.SendAction(460, 135)   

        makeLast(100 ,0x2D25)

        Misc.Pause(100)        



        

    if Carpentry == Player.GetSkillCap('Carpentry'):

        lastCraft = Items.FindByID(0x2D25, -1, Player.Backpack.Serial)

        if lastCraft:

            hatchet = Items.FindByID(0x0F43,-1,Player.Backpack.Serial)

            Items.UseItem(hatchet)

            Target.WaitForTarget(1500,False)

            Target.TargetExecute(lastCraft)

            Misc.Pause(500)

        Misc.SendMessage('You have reached Grandmaster',48)    

        Misc.ScriptStopAll()

        

    Misc.Pause(1100)



while True:

    selectCraft()

</code>