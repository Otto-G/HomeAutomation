# HomeAutomation
Automating different parts of the house

## Tasks that need to be run based on the day
Monday - Friday
 * Morning: Automated light turning on linked to Google calendar
 * Turn on Bedroom light after waking up
 * Turn on Main kitchen light after waking up

## Tasks run every day
Open/Close blinds
 * Open blinds in the morning after the sun is up
 * Close the blinds at night
   * Turn on a hallway light
     * When home, turn off hallway light. Turn on Kitchen & Dining room lights

Turn on coach lights at night
 * Once sun sets, turn on coach lights until 1AM

Front door (using smart lock & door bell)
 * Take picture of person ringing door bell and send email
 * If door is opened, take video of them entering/exiting and send email
 
Porch (Storage box for delivery)
 * When lid is opened, take video of porch

## Tasks run occasionally 
Washer dryer
 * When washer or dryer is finished, send email/other alert
   * Turn on washer/dryer room light



## Parts list

 * Z-Wave Blinds (12 windows)
   * Back living group (4 windows: Dining room, Living room)
   * Front living group (2 windows: Front room)
   * Master bed group (3 windows)
   * Front Guest group (2 windows)
   * Rear Guest group (1 window)
 * Light switches
   * Coach Light group (3 main switches)
     * Porch light (1 main switch) 
     * Pole light (1 main switch)
     * Coach lights (1 main switch)
   * Living space group (3 main switches + 1 aux switch)
     * Kitchen light group (1 main switch + 1 aux switch)
     * Dining room light group (1 main switch)
     * Living room light group (1 main switch)
   * Bedroom group (2 main switches)
     * Bedroom light group (1 main switch)
     * Master bath light group (1 main switch)
   * Auxilary group (2 main switches (+ 1 aux switch?))
     * Hallway light (1 main switch (+ 1 aux switch?))
     * Washer/Dryer light (1 main switch)
 * Energy meter for washer & dryer
