# HomeAutomation
Automating different parts of the house.
This is using [home-assistant](https://home-assistant.io/) as the base control.  Home assistant uses github as their base repository for there code [here](https://github.com/home-assistant/home-assistant) 

## Tasks that need to be run based on the day
Monday - Friday
 - [ ] Morning: Automated light turning on linked to Google calendar
   - [ ] Currently only based on time
 - [x] Turn on Bedroom light after waking up.  Tied to Sleep as android
 - [ ] Turn on Main kitchen light after waking up
   - [ ] Need to add kitchen master and slave switches

## Tasks run every day
Open/Close blinds
 - [ ] Open blinds in the morning after the sun is up
 - [ ] Close the blinds at night
   - [ ] Turn on a hallway light
     - [ ] Currently living room light turns on.  Need switch for hallway light
     - [ ] When home, turn off hallway light. Turn on Kitchen & Dining room lights

Turn on coach lights at night
 - [x] Once sun sets, turn on coach lights until 2AM

Front door (using smart lock & door bell)
 - [ ] Take picture of person ringing door bell and send email
 - [ ] If door is opened, take video of them entering/exiting and send email
   - [ ] Concerned about security with z-wave locks.  May implement with simple switch
 
Porch (Storage box for delivery)
 - [ ] When lid is opened, take video of porch
   - [ ] Need to add box and everything else

Turn off lights at night
 - [x] Turn off all interior lights when going to sleep
   - [x] Link this in with Sleep as android

## Tasks run occasionally 
Washer dryer
 - [ ] When washer or dryer is finished, send email/other alert
   - [x] Turn on washer/dryer room light
     - [x] Have automatic light
   - [ ] Need to get current meter



## Parts list

 - [ ] Synology NAS
   - [ ] May substitute for freenas box
 - [ ] Z-Wave Blinds (12 windows)
   - [ ] Back living group (4 windows: Dining room, Living room)
   - [ ] Front living group (2 windows: Front room)
   - [ ] Master bed group (3 windows)
   - [ ] Front Guest group (2 windows)
   - [ ] Rear Guest group (1 window)
 - [ ] Light switches
   - [ ] Coach Light group (2 main switches)
     - [ ] Pole light (1 main switch)
     - [x] Coach and porch lights (1 main switch)
   - [ ] Living space group (3 main switches + 1 aux switch)
     - [ ] Kitchen light group (1 main switch + 1 aux switch)
     - [ ] Dining room light group (1 main switch)
     - [x] Living room light group (1 main switch)
   - [ ] Bedroom group (3 main switches)
     - [x] Bedroom light group (1 main switch)
     - [ ] Should add switch for fan (1 main switch)
     - [ ] Master bath light group (1 main switch)
   - [ ] Auxilary group (2 main switches (+ 1 aux switch?))
     - [ ] Hallway light (1 main switch (+ 1 aux switch?))
 - [ ] Energy meter for washer & dryer

## Linked Apps
 - [x] Sleep as android
   - [x] Alarm start
   - [x] Alarm end
 - [x] Tasker
   - [x] Sending triggers to main hub
   - [x] Uses mqtt to send messages
 - [x] Home-assistant.io
