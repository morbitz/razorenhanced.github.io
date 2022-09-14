
<code>

#Poisoning Trainer by Frank Castle

#

#What you need:

# 1 - 30.0+ Poisoning Skill. If you do not have it buy it up. 

# 2 - a dagger. Dont be a bitch.  Go buy a dagger.

# 3 - a chest with stacks of lesser poison potions, poison potions, greater poison potions, and deadly poison potions

#     This is written to use stacks of poisons.  Kegs are a thing of the past.  Get with the times. 

# Written and tested on OSI.





from System.Collections.Generic import List

global weapon

stoCont = Target.PromptTarget('Target your resource chest')

def chooseWeapon():

    global weapon

    weapon = Target.PromptTarget('Target your DAGGER to be poisoned')

    daggerIDS = [0x0F51,0x0F52]

    pWeapon = Items.FindBySerial(weapon)

    if not pWeapon.ItemID in daggerIDS:

        Misc.SendMessage('I SAID DAGGER! WHAT PART OF THAT DO YOU NOT UNDERSTAND???',65)

        chooseWeapon()

chooseWeapon()    

source = Items.FindBySerial(stoCont)

Items.UseItem(stoCont) 

Misc.Pause(1100)

for P in Items.FindBySerial(source.Serial).Contains:

    if P.ItemID == 0x0F0A:

        Items.WaitForProps(P,10000)

        Misc.Pause(500)

        props = Items.GetPropStringList(P)

        Misc.Pause(500)

        prop = props[0].split(' ')[1]

        Misc.Pause(500)

        if prop == 'Lesser':

            lesserPoison = Items.FindBySerial(P.Serial)

        if prop == 'Poison':

            normalPoison = Items.FindBySerial(P.Serial)

        if prop == 'Greater':

            greaterPoison = Items.FindBySerial(P.Serial)

        if prop == 'Deadly':

            deadlyPoison = Items.FindBySerial(P.Serial)

    

skill = Player.GetSkillValue('Poisoning') 



def train():

    if skill < 40:

        if lesserPoison:

            Player.UseSkill("Poisoning")

            Target.WaitForTarget(1500, False)

            Target.TargetExecute(lesserPoison)

            Target.WaitForTarget(10000, False)

            Target.TargetExecute(weapon)

        else:

            Misc.SendMessage('I am out of Lesser Poison potions.  Halting Script.', 33)

            pots = False

            

    elif skill > 39.9 and skill < 70:

        if normalPoison:

            Player.UseSkill("Poisoning")

            Target.WaitForTarget(1500, False)

            Target.TargetExecute(normalPoison)

            Target.WaitForTarget(10000, False)

            Target.TargetExecute(weapon)

        else:

            Misc.SendMessage('I am out of Poison potions.  Halting Script.', 33)

            pots = False

            

    elif skill > 69.9 and skill < 92:

        if greaterPoison:

            Player.UseSkill("Poisoning")

            Target.WaitForTarget(1500, False)

            Target.TargetExecute(greaterPoison)

            Target.WaitForTarget(10000, False)

            Target.TargetExecute(weapon)

        else:

            Misc.SendMessage('I am out of Greater Poison potions.  Halting Script.', 33)

            pots = False



    elif skill > 91.9 and skill < 100:

        if deadlyPoison:

            Player.UseSkill("Poisoning")

            Target.WaitForTarget(1500, False)

            Target.TargetExecute(deadlyPoison)

            Target.WaitForTarget(10000, False)

            Target.TargetExecute(weapon)

        else:

            Misc.SendMessage('I am out of Deadly Poison potions.  Halting Script.', 33) 

            pots = False

            

pots = True

while skill < 100 and pots == True:

    global skill

    train()

    Misc.Pause(10500)

    

            

</code>