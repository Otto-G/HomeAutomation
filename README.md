# HomeAutomation
Automating different parts of the house.
This is using [home-assistant](https://home-assistant.io/) as the base control.  Home assistant uses github as their base repository for there code [here](https://github.com/home-assistant/home-assistant) 

## Tasks that need to be run based on the day
Monday - Friday
 - [ ] Morning: Automated light turning on linked to Google calendar
   - [x] Currently only based on time
 - [x] Turn on Bedroom light after waking up.  
   - Tied to Sleep as android
 - [ ] Turn on Main kitchen light after waking up
   - [ ] Need to add kitchen master and slave switches
 - [x] Start podcast in morning after waking up
   - Uses [Tasker](https://tasker.dinglisch.net/) and [Beyondpod](https://www.beyondpod.mobi/android/index.htm)
   
Saturday - Sunday
 - [ ] Turn on lights after waking up if needed
 - [ ] Start podcast in the morning after waking up

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
   - [ ] Coach Light group (1 main switches)
     - [x] Coach and porch lights (1 [main switch](https://www.amazon.com/gp/product/B00PYMGOHM?th=1&pldnSite=1))
   - [ ] Living space group (3 main switches + 1 aux switch)
     - [ ] Kitchen light group (1 main switch + 1 aux switch)
     - [ ] Dining room light group (1 main switch)
     - [x] Living room light group (1 [main switch](https://www.amazon.com/gp/product/B00PYMGOHM?th=1&pldnSite=1))
   - [ ] Bedroom group (3 main switches)
     - [x] Bedroom light group (1 [main switch](https://www.amazon.com/gp/product/B00PYMGOHM?th=1&pldnSite=1))
     - [ ] Switch for fan (1 main switch)
     - [ ] Master bath light group (1 main switch)
   - [ ] Auxilary group (2 main switches (+ 1 aux switch?))
     - [ ] Hallway light (1 main switch + 1 aux switch)
     - [ ] Utility room (washer & dryer) (1 [automatic switch](https://www.amazon.com/TOPGREENER-TSOS5-W-Single-Pole-Fluorescent-Incandescent/dp/B015G8VLNA/ref=sr_1_4?s=hi&ie=UTF8&qid=1487179597&sr=1-4&keywords=automatic+light+switch))
 - [ ] Energy meter for washer & dryer

## Linked Apps
 - [Sleep as android](http://sleep.urbandroid.org/)
   - Alarm start
   - Alarm end
 - [Tasker](https://tasker.dinglisch.net/)
   - Sending triggers to main hub
   - Uses mqtt to send messages
 - [Home-assistant](https://home-assistant.io/)
   - Main hub
 - [Owntracks](http://owntracks.org/)
   - Used for location tracking
 - [Pebble watch](https://www.pebble.com/)
   - Used for starting sleep as android and motion during sleeping
 - [Beyondpod](https://www.beyondpod.mobi/android/index.htm)
   - Used to download podcasts and play them offline
   - Updates automatically early in the morning
