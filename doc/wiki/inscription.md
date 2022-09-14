
<code>

#Inscription Trainer by Frank Castle

#

#What you need:

# 1 - 30.0+ Tinkering Skill. If you do not have it buy it up. 

# 1 - 30.0+ Inscription Skill. If you do not have it buy it up.

# 2 - a player made Tinker Tools

# 3 - a chest with plenty of iron ingots, reagents, and scrolls

# 

# Written and tested on OSI. 



from System.Collections.Generic import List



global stoCont



stoCont = Target.PromptTarget('Target your resource chest')

Misc.Pause(100)

Items.UseItem(stoCont)

Misc.Pause(1100)



Player.UseSkill('Hiding')

Misc.Pause(11000)



mandrakeroot = 0x0F86

bloodmoss = 0x0F7B

sulphurousash = 0x0F8C

nightshade = 0x0F88

blackpearl = 0x0F7A

spidersilk = 0x0F86

ginseng = 0x0F85

garlic = 0x0F84





def makeLast(skill, item, reg1, reg2, reg3, reg4, mana):

    Inscription = Player.GetSkillValue('Inscribe')

    pen = Items.FindByID(0x0FBF,-1,Player.Backpack.Serial)

    Items.UseItem(pen)

    while Inscription < skill and Inscription != Player.GetSkillCap('Inscribe'):

        while Player.Mana < mana:

            Misc.Pause(1100)

            Player.UseSkill('Meditation')

            Misc.Pause(12000)

            Items.UseItem(pen)

        Inscription = Player.GetSkillValue('Inscribe')

        checkRegs(reg1, reg2, reg3, reg4)

        Gumps.WaitForGump(460, 1500)

        Gumps.SendAction(460, 1999)

        Misc.Pause(500)

        

        if Journal.Search('You have worn out') == True:

            Journal.Clear()

            checkTools()

            pen = Items.FindByID(0x0FBF,-1,Player.Backpack.Serial)

            Items.UseItem(pen)

           

        if Items.BackpackCount(item,-1) > 20:

            scroll = Items.FindByID(item,-1,Player.Backpack.Serial)

            Misc.Pause(100)

            Items.Move(scroll,stoCont,0)

            Misc.Pause(300)     

        





def checkRegs(reg1, reg2, reg3, reg4):

    if Items.BackpackCount(reg1,0x0000) < 5:

        global stoCont

        Misc.Pause(1100)

        Reg = Items.FindByID(reg1,-1,stoCont)

        Misc.Pause(100)

        Items.Move(Reg,Player.Backpack.Serial,100)

        Misc.Pause(1100)

        

    if Items.BackpackCount(reg2,0x0000) < 5:

        global stoCont

        Misc.Pause(1100)

        Reg = Items.FindByID(reg2,-1,stoCont)

        Misc.Pause(100)

        Items.Move(Reg,Player.Backpack.Serial,100)

        Misc.Pause(1100)



    if Items.BackpackCount(reg3,0x0000) < 5:

        global stoCont

        Misc.Pause(1100)

        Reg = Items.FindByID(reg3,-1,stoCont)

        Misc.Pause(100)

        Items.Move(Reg,Player.Backpack.Serial,100)

        Misc.Pause(1100)



    if Items.BackpackCount(reg4,0x0000) < 5:

        global stoCont

        Misc.Pause(1100)

        Reg = Items.FindByID(reg4,-1,stoCont)

        Misc.Pause(100)

        Items.Move(Reg,Player.Backpack.Serial,100)

        Misc.Pause(1100)



    if Items.BackpackCount(0x0EF3,0x0000) < 5:

        global stoCont

        Misc.Pause(1100)

        Reg = Items.FindByID(0x0EF3,0x0000,stoCont)

        Misc.Pause(100)

        Items.Move(Reg,Player.Backpack.Serial,100)

        Misc.Pause(1100)        

        

def checkIngots():

    if Items.BackpackCount(0x1BF2,0x0000) < 15:

        global stoCont

        Misc.Pause(1100)

        ingot = Items.FindByID(0x1BF2,0x0000,stoCont)

        Misc.Pause(100)

        Items.Move(ingot,Player.Backpack.Serial,40)

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

        

    countTwo = Items.BackpackCount(0x0FBF,-1)

    while countTwo < 3:

        tinkerTool = Items.FindByID(0x1EB9,-1,Player.Backpack.Serial)

        Misc.Pause(100)

        Items.UseItem(tinkerTool)

        Gumps.WaitForGump(460, 10000)

        Gumps.SendAction(460, 30)

        Misc.Pause(1500)

        countTwo = Items.BackpackCount(0x0FBF,-1)

        Misc.SendMessage('I have {} pens in my bag'.format(countOne),48)

        

def selectCraft():        

    Inscription = Player.GetSkillValue('Inscribe')

    if Inscription < 30:

        while Player.Mana < 11:

            Player.UseSkill('Meditation')

            Misc.Pause(8100)

        checkRegs(mandrakeroot, bloodmoss, mandrakeroot, mandrakeroot)

        checkTools()

        pen = Items.FindByID(0x0FBF,-1,Player.Backpack.Serial)

        Misc.Pause(100)

        Items.UseItem(pen)

        Gumps.WaitForGump(460, 10000)

        Gumps.SendAction(460, 22)   #MAKE TELEPORT

        makeLast(30, 0x1F42, mandrakeroot, bloodmoss, mandrakeroot, mandrakeroot,11)

        Misc.Pause(100)





    if Inscription < 55 and Inscription >= 30 :

        lastScroll = Items.FindByID(0x1F42, -1, Player.Backpack.Serial)

        if lastScroll:

            Items.Move(lastScroll,stoCont,0)

            Misc.Pause(1100)

        while Player.Mana < 11:

            Player.UseSkill('Meditation')

            Misc.Pause(8100)

        checkRegs(mandrakeroot, bloodmoss, blackpearl, mandrakeroot)

        checkTools()

        pen = Items.FindByID(0x0FBF,-1,Player.Backpack.Serial)

        Misc.Pause(100)

        Items.UseItem(pen)

        Gumps.WaitForGump(460, 10000)

        Gumps.SendAction(460, 32)   #MAKE RECALL

        makeLast(55, 0x1F4C, mandrakeroot, bloodmoss, blackpearl, mandrakeroot, 11)

        Misc.Pause(100)        

        

    if Inscription >= 55 and Inscription < 65 :

        lastScroll = Items.FindByID(0x1F4C, -1, Player.Backpack.Serial)

        if lastScroll:

            Items.Move(lastScroll,stoCont,0)

            Misc.Pause(1100)

        while Player.Mana < 16:

            Player.UseSkill('Meditation')

            Misc.Pause(8100)

        checkRegs(mandrakeroot, nightshade, blackpearl, mandrakeroot)

        checkTools()

        pen = Items.FindByID(0x0FBF,-1,Player.Backpack.Serial)

        Misc.Pause(100)

        Items.UseItem(pen)

        Gumps.WaitForGump(460, 10000)

        Gumps.SendAction(460, 33)   #MAKE BLADE SPIRITS

        makeLast(65, 0x1F4D, mandrakeroot, nightshade, blackpearl, mandrakeroot, 16)

        Misc.Pause(100)

        

    if Inscription >= 65 and Inscription < 85 :

        lastScroll = Items.FindByID(0x1F4D, -1, Player.Backpack.Serial)

        if lastScroll:

            Items.Move(lastScroll,stoCont,0)

            Misc.Pause(1100)

        while Player.Mana < 20:

            Player.UseSkill('Meditation')

            Misc.Pause(8100)

        checkRegs(blackpearl, nightshade, blackpearl, blackpearl)

        checkTools()

        pen = Items.FindByID(0x0FBF,-1,Player.Backpack.Serial)

        Misc.Pause(100)

        Items.UseItem(pen)

        Gumps.WaitForGump(460, 10000)

        Gumps.SendAction(460, 42)   #MAKE ENERGY BOLT

        makeLast(85, 0x1F56,blackpearl, nightshade, blackpearl, blackpearl, 20)

        Misc.Pause(100)

        

    if Inscription >= 85 and Inscription < 94 :

        lastScroll = Items.FindByID(0x1F56, -1, Player.Backpack.Serial)

        if lastScroll:

            Items.Move(lastScroll,stoCont,0)

            Misc.Pause(1100)

        while Player.Mana < 40:

            Player.UseSkill('Meditation')

            Misc.Pause(8100)

        checkRegs(blackpearl, mandrakeroot, sulphurousash, sulphurousash)

        checkTools()

        pen = Items.FindByID(0x0FBF,-1,Player.Backpack.Serial)

        Misc.Pause(100)

        Items.UseItem(pen)

        Gumps.WaitForGump(460, 10000)

        Gumps.SendAction(460, 52)   #MAKE GATE TRAVEL

        makeLast(94, 0x1F60, blackpearl, mandrakeroot, sulphurousash, sulphurousash, 40)

        Misc.Pause(100)       

        

    if Inscription >= 94 and Inscription < 100 :

        lastScroll = Items.FindByID(0x1F60, -1, Player.Backpack.Serial)

        if lastScroll:

            Items.Move(lastScroll,stoCont,0)

            Misc.Pause(1100)

        while Player.Mana < 50:

            Player.UseSkill('Meditation')

            Misc.Pause(8100)

        checkRegs(bloodmoss, garlic, ginseng, ginseng)

        checkTools()

        pen = Items.FindByID(0x0FBF,-1,Player.Backpack.Serial)

        Misc.Pause(100)

        Items.UseItem(pen)

        Gumps.WaitForGump(460, 10000)

        Gumps.SendAction(460, 59)   #MAKE RESURRECTION

        makeLast(100 ,0x1F67, bloodmoss, garlic, ginseng, ginseng, 50)

        Misc.Pause(100) 



        

    if Inscription == Player.GetSkillCap('Inscribe'):

        lastScroll = Items.FindByID(0x1F67, -1, Player.Backpack.Serial)

        if lastScroll:

            Items.Move(lastScroll,stoCont,0)

            Misc.Pause(1100)

        Misc.ScriptStopAll()

        

    Misc.Pause(1100)



while True:

    selectCraft()

</code>