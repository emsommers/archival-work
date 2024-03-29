- [Wipe HD or flash drive](#wipe-hd-or-flash-drive)
  * [Windows](#windows)
  * [Linux](#linux)
- [Delete hidden files](#delete-hidden-files)
  * [Windows](#windows-1)
  * [Linux](#linux-2)
- [Tree list](#tree-list)
  * [Windows](#windows-2)
  * [Linux](#linux-2)
- [Brunnhilde](#brunnhilde)
- [How to make scripts executable from anywhere on the computer](#how-to-make-scripts-executable-from-anywhere-on-the-computer)
- [Permissions](#permissions)
- [Mount drive (when it is not showing up)](#mount-drive)
- [ffmpeg (audio & video conversion)](#ffmpeg)
- [cd-info](#cd-info)
---

# Wipe HD or flash drive 
## Windows

``` format e: /fs:FAT32 /p:2 ```

``` format e: /fs:NTFS /p:2 ```

e: is the drive name

[Source](https://www.lifewire.com/use-the-format-command-to-write-zeros-to-a-hard-drive-2626162)

## Linux

```sudo dd if=/dev/zero of=/dev/sdc1 status=progress```

use `df` command to list disks and find the correct path, e.g. /dev/sdc1

# Delete hidden files
## Windows

``` del * /a:h ```

To delete hidden files from subfolders, add the /S flag

``` del * /a:h /S ```

To delete resource forks

``` del /s /q /f /a ._.* ```

``` del /s /q /f /a .* ```

To delete temporary or recovered files

``` del /s /q /a ~$* ```

``` del /p /s /a *.tmp ```

[Source/Syntax](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/del)


## Linux
``` find . -type f -name ".*" -delete ```

To delete thumbs.db

``` find . -iname thumbs.db -delete ```

# Tree list
## Windows

tree [drive:\][path] /f /a > [output]

``` tree "K:\B2021-0001" /f /a > tree_b2021-0001.txt ```

## Linux
tree -a -s -D -N [/myPath/here] > [output.txt]

``` tree -a -s -D -N /storage/ingest/B2021-0002 > /storage/metadata/B2021-0002/tree.txt ```

To print tree inside cwd: **./**

```tree -a -s -D -N ./ > output.txt```

To print HTML version of tree:

```tree -a -s -D -N -H --nolinks /storage/ingest/B2021-0002 > /storage/metadata/B2021-0002/tree.html```

**For help:** tree --help

# Brunnhilde
https://github.com/tw4l/brunnhilde

`brunnhilde.py` --hash HASH -nz [source] [destination]

``` brunnhilde.py --hash sha256 -nz /storage/UTARMS/01_submission/B2021-0002_Lang/ /storage/UTARMS/05_metadata/B2021-0002_Lang ```

To upgrade:
``` sudo pip install brunnhilde --upgrade ```

# How to make scripts executable from anywhere on the computer

In home directory, open `.bashrc` file:

```nano .bashrc```

At the bottom of the file, add the following lines indicating the location of your scripts folder:

```
# My scripts path
export PATH="/home/sommerse/Desktop/Scripts/archival-work:$PATH"
```

Save the file and exit, then in Terminal:
``` source ~/.bashrc ```

Voila! You can now run scripts in the Terminal from any location

# Permissions
Changing r/w/e permissions when a new user account is created

```sudo chmod u=rwx,g=rwx,o=r /storage```

To make check the user's groups: ```groups username```
To check members of a group: ```members groupname```

Changing owner and permissions recursively:

```sudo chown -R username:group /path/to/my/files```

```sudo chown -R sommerse:floppy /storage/UTARMS/02_ingest/A2022-0003_HartHouse```
# Mount drive
Find the label of the drive, e.g. /dev/sdc2

```sudo fdisk -l```

Create mounting point (if it doesn't already exist)

```sudo mkdir /media/usb-drive```

Mount drive

```sudo mount /dev/sdc2 /media/usb-drive```

Unmount drive

```umount /media/usb-drive```

# ffmpeg
https://ffmpeg.org/

ffmpeg -i [source] [output]

```ffmpeg -i /storage/UTARMS/myfile.wmv /storage/UTARMS/myfile.mp4```

# cd-info
To learn more about a CD, especially if it is an audio cd

https://linux.die.net/man/1/cd-info

Insert cd into drive then in Terminal enter ```sudo cd-info```

![Terminal window showing cd-info output](/screenshots/screenshot_cd-info.png)