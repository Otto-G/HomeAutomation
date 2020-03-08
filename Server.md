# Home Server

**Operating System:** Debian 10 "Buster"

#### Major Programs:

* [Cockpit](https://github.com/cockpit-project/cockpit)
    * Web based server admin page
* [Cockpit-zfs-manager](https://github.com/optimans/cockpit-zfs-manager)
    * Plug-in for Cockpit that allows managing of ZFS pools
* [Traefik](https://github.com/containous/traefik)
    * Reverse proxy
* [Docker](https://www.docker.com/)
    * Container system to hold different systems.  Part of the main way that the system is organized.  
    

#### Installed programs:

    sudo aptitude install docker lm-sensors hddtemp
    sudo aptitude install -t buster-backports cockpit dkms spl-dkms zfs-dkms zfsutils-linux
    
## Docker Containers

* [Home Assistant](https://www.home-assistant.io/docs/installation/docker/)
    * Config is saved [here](https://github.com/Otto-G/HomeAutomation/blob/master/configuration.yaml)
* Transmission
    * Torrent downloading, still need to determine where to get/roll my own image
* [Plex](https://github.com/plexinc/pms-docker)
    * Media server
* [Syncthing](https://syncthing.net/)
    * Home rolled docker image