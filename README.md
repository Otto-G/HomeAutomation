# HomeAutomation
Automating different parts of the house.
This is using [home-assistant](https://home-assistant.io/) as the base control.  Home assistant uses github as their
 base repository for their code [here](https://github.com/home-assistant/home-assistant)
 
 The system that Home-Assistant is running on is currently going through a change from Freenas to Debian with ZFS on
  Linux.  

## Tasks that need to be run based on the day
Monday - Friday
 - [x] Turn on Bedroom light and living room light as needed after waking up.  
   - Tied to Sleep as android tracking stop (run in Tasker)
 - [ ] Turn on Main kitchen light after waking up
   - [ ] Need to add kitchen master and slave switches
 - [x] Start podcast in morning after waking up
   - Uses [Tasker](https://tasker.dinglisch.net/) and [AntennaPod](https://antennapod.org/)
   
Saturday - Sunday
 - [x] Turn on lights after waking up if needed
   - Tied to sleep as android tracking stop (run in Tasker)
 - [x] Start podcast in the morning after waking up
   - Tied to sleep as android tracking stop (run in Tasker)

## Tasks run every day
Open/Close blinds
 - [ ] Open blinds in the morning after the sun is up
 - [ ] Close the blinds at night
 - [x] Turn on a hallway light
  
Turn on coach lights at night
 - [x] Once sun sets, turn on coach lights until 2AM

Front door (using smart lock & door bell)
 - [ ] Take picture of person ringing door bell and send email
 - [ ] If door is opened, take video of them entering/exiting and send email
   - [ ] Concerned about security with z-wave locks.  May implement with simple switch

Turn off lights at night
 - [x] Turn off all interior lights when going to sleep
   - [x] Link this in with Sleep as android

## Tasks run occasionally 
Washer dryer
 - [ ] When washer or dryer is finished, send email/other alert
   - [x] Turn on washer/dryer room light
     - [x] Have automatic light sensor
   - [ ] Need to get current meter



## Parts list

 - [x] Freenas box --> Pending change to Debian w/ ZFS on Linux
   - [InWin IW-MS04 ITX Case](https://www.amazon.com/gp/product/B0167NCADS/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)
   - [AsRock J3710](https://www.amazon.com/gp/product/B01E97ZTPA/ref=oh_aui_search_asin_title?ie=UTF8&psc=1)
   - [8GB Crucial Ram x 2](https://www.amazon.com/gp/product/B006YG8X9Y/ref=ppx_od_dt_b_asin_title_s00?ie=UTF8&psc=1)
   - [HGST Ultrastar 7k4000 3TB x 2](https://www.amazon.com/gp/product/B01LYVD7ME/ref=ppx_od_dt_b_asin_title_s00?ie=UTF8&psc=1)
   - [Aeotec z-wave adapter](https://www.amazon.com/gp/product/B00X0AWA6E/ref=oh_aui_search_asin_title?ie=UTF8&psc=1)
   - [Intel PRO/1000 Pt Network adapter](https://www.amazon.com/gp/product/B000BMZHX2/ref=oh_aui_search_asin_title?ie=UTF8&psc=1)
     - !! Note, x4 PCI slot where motherboard only has x1.  I modified motherboard to fit card, don't really recommend.  Still better than Realtek.  
   - [Sandisk 240GB SSD for boot](https://www.amazon.com/gp/product/B01F9G43WU)
 - [ ] Z-Wave Blinds (12 windows)
   - [ ] Back living group (4 windows: Dining room, Living room)
   - [ ] Front living group (2 windows: Front room)
   - [ ] Master bed group (3 windows)
   - [ ] Front Guest group (2 windows)
   - [ ] Rear Guest group (1 window)
 - [ ] Light switches
   - [x] Coach Light group (1 main switches)
     - [x] Coach and porch lights (1 [main switch](https://www.amazon.com/gp/product/B00PYMGOHM?th=1&pldnSite=1))
   - [ ] Living space group (3 main switches + 1 aux switch)
     - [ ] Kitchen light group (1 main switch + 1 aux switch)
     - [ ] Dining room light group (1 main switch)
     - [x] Living room light group (1 [main switch](https://www.amazon.com/gp/product/B00PYMGOHM?th=1&pldnSite=1))
   - [ ] Bedroom group (3 main switches)
     - [x] Bedroom light group (1 [main switch](https://www.amazon.com/gp/product/B00PYMGOHM?th=1&pldnSite=1))
     - [ ] Switch for fan (1 main switch)
     - [ ] Master bath light group (1 main switch)
   - [x] Auxiliary group (2 main switches (+ 1 aux switch?))
     - [x] Hallway light (1 main switch + 1 aux switch [aux switch not needed])
     - [x] Utility room (washer & dryer) (1 [automatic switch](https://www.amazon.com/TOPGREENER-TSOS5-W-Single-Pole-Fluorescent-Incandescent/dp/B015G8VLNA/ref=sr_1_4?s=hi&ie=UTF8&qid=1487179597&sr=1-4&keywords=automatic+light+switch))
 - [ ] Door sensor
   - [x] [Garage Door (Entryway)](https://smile.amazon.com/gp/product/B01N5HB4U5/ref=oh_aui_detailpage_o02_s00?ie=UTF8&psc=1)
   - [ ] Front Door
   - [ ] Back Door
   - [ ] Outside Garage Door
 - [ ] Energy meter for washer & dryer
 - [x] Thermostat (Nest E)

## Linked Apps
 - [Sleep as android](http://sleep.urbandroid.org/)
   - Alarm start
   - Alarm end
 - [Tasker](https://tasker.dinglisch.net/)
   - Sending triggers to main hub
   - Uses HTTP Post to send messages (directly triggering automations)
 - [Autovoice](https://joaoapps.com/autovoice/)
   - Tasker plugin to communicate with google home/assistant
   - Used to trigger Sleep as Android
 - [Home-assistant](https://home-assistant.io/)
   - Main hub
 - [Owntracks](http://owntracks.org/)
   - Used for location tracking
 - [AntennaPod](https://antennapod.org/)
   - Used to download podcasts and play them offline
   - Updates automatically early in the morning
