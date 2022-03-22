#
Items.UseItem(Player.Backpack)
Misc.Pause(5000)  # wait a bit to get stuff loaded
#
Misc.SetSharedValue("StaticTrees", True)
#Misc.SetSharedValue("LootBag", 0x40A8962C)
#if Player.Name == "Credzba":
#    Misc.SetSharedValue("BagOfHolding", 0x400EC1EB) 
#if Player.Name == "Dwarven Slaves":    
#    Misc.SetSharedValue("BagOfHolding", 0x402A5351)
#for i in Player.Backpack.Contains:
#    if Items.GetPropStringByIndex(i,0).lower() == "large bag of holding":
#        Misc.SetSharedValue("BagOfHolding", i.Serial)
#Misc.SetSharedValue("Pets", [])
#Misc.SetSharedValue("ClaimCommand", "[cleanup")
#Misc.RemoveSharedValue("BandSelf")
#Misc.SetSharedValue("BandSelf", "[everlastingbandself")
#Misc.SetSharedValue("IngotBag", 0x400508D9)
#for i in Player.Backpack.Contains:
#    if Items.GetPropStringByIndex(i,0).lower() == "trash bag":
#        Misc.SetSharedValue("TokenBag", i.Serial)
        