
======Scripting - Organizer control function======

Here can find some information about Enhanced Scripting function to control organizer engine by script!



=====Check Status=====



{|style="font-size:85%; border:solid 2px; width: 50%;"

|style="font-size:150%;  padding: 2px" colspan="2" | **Check OrganizerStatus**

|- style="background-color:#f0f0f0;"

|**Syntax**

|style="width: 90%" | Organizer.Status( )

|-

|colspan="2" |**Description:**

|-

|colspan="2" |Get a bool value of Organizer engine status, if running or not

|- style="background-color:#f0f0f0;"

|**Returns**

|bool

|-

|**In Object:**

|Organizer

|- style="background-color:#f0f0f0;"

|**Parameters:**

|none



|}



=====Start=====



{|style="font-size:85%; border:solid 2px; width: 50%;"

|style="font-size:150%;  padding: 2px" colspan="2" | **Start Organizer**

|- style="background-color:#f0f0f0;"

|**Syntax**

|style="width: 90%" | Organizer.FStart( )

|-

|colspan="2" |**Description:**

|-

|colspan="2" |Start Organizer engine.

|- style="background-color:#f0f0f0;"

|**Returns**

|void

|-

|**In Object:**

|Organizer

|- style="background-color:#f0f0f0;"

|**Parameters:**

|none



|}





=====Stop=====



{|style="font-size:85%; border:solid 2px; width: 50%;"

|style="font-size:150%;  padding: 2px" colspan="2" | **Stop Organizer**

|- style="background-color:#f0f0f0;"

|**Syntax**

|style="width: 90%" | Organizer.FStop( )

|-

|colspan="2" |**Description:**

|-

|colspan="2" |Stop scavenger engine.

|- style="background-color:#f0f0f0;"

|**Returns**

|void

|-

|**In Object:**

|Organizer

|- style="background-color:#f0f0f0;"

|**Parameters:**

|none



|}





=====Change List=====





{|style="font-size:85%; border:solid 2px; width: 50%;"

|style="font-size:150%;  padding: 2px" colspan="2" | **Change Organizer item list**

|- style="background-color:#f0f0f0;"

|**Syntax**

|style="width: 90%" | Organizer.ChangeList(string)

|-

|colspan="2" |**Description:**

|-

|colspan="2" |Change list of oganizer item, List must be exist in organizer GUI configuration

|- style="background-color:#f0f0f0;"

|**Returns**

|void

|-

|**In Object:**

|Organizer

|- style="background-color:#f0f0f0;"

|**Parameters:**

|ListName



|}



=====Script Execution of Organizer List=====





{|style="font-size:85%; border:solid 2px; width: 50%;"

|style="font-size:150%;  padding: 2px" colspan="2" | **Run Organizer from python**

|- style="background-color:#f0f0f0;"

|**Syntax**

|style="width: 90%" | Organizer.RunOnce(string ListName, int SourceContainer, int DestinationContainer, int DragDelay)

|-

|colspan="2" |**Description:**

|-

|colspan="2" |Run the specified Organizer list, using the source, dest, and drag delay specified. Note: source, dest, and drag delay can be -1 and they will use whatever is specified on the gui

|- style="background-color:#f0f0f0;"

|**Returns**

|void

|-

|**In Object:**

|Organizer

|- style="background-color:#f0f0f0;"

|**Parameters:**

|string ListName, int SourceContainer, int DestinationContainer, int DragDelay

|- style="background-color:#f0f0f0;"

|**Example**

|<code>

Organizer.RunOnce("test", 0x42292AD3, 0x4005A1AD, 1000)

</code>

|}