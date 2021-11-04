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

`brunnhilde.py` -n [source] [destination] [basename]

``` brunnhilde.py -n /storage/UTARMS/submission/b2021-0002_Lang/ /storage/UTARMS/metadata/ b2021-0002_Lang ```


