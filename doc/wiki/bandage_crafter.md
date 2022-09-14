
<code>

#Bandage Crafter by Frank Castle

#

#What you need:

#1 Scissors

#2 a storage container with a lot of bolts of cloth

# enough room in your backpack to hold 200 stones



stoCont = Target.PromptTarget('Target your storage container')

while True:

    clothbolt = Items.FindByID(0x0F95,-1,stoCont)

    Items.Move(clothbolt,Player.Backpack.Serial,40)

    Misc.Pause(1100)

    Scissors = Items.FindByID(0x0F9E,-1,Player.Backpack.Serial)

    Bclothbolt = Items.FindByID(0x0F95,-1,Player.Backpack.Serial)

    Items.UseItem(Scissors)

    Target.WaitForTarget(10000,False)

    Target.TargetExecute(Bclothbolt)

    Misc.Pause(1100)

    CutCloth = Items.FindByID(0x1766,-1,Player.Backpack.Serial)

    Items.UseItem(Scissors)

    Target.WaitForTarget(10000,False)

    Target.TargetExecute(CutCloth)

    Misc.Pause(1100)

    bBandies = Items.FindByID(0x0E21,-1,Player.Backpack.Serial)

    Items.Move(bBandies,stoCont,0)

    Misc.Pause(1100)

    

</code>    