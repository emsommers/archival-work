# Wipe HD or flash drive (Windows)

``` format e: /fs:FAT32 /p:2 ```

``` format e: /fs:NTFS /p:2 ```

e: is the drive name

[Source](https://www.lifewire.com/use-the-format-command-to-write-zeros-to-a-hard-drive-2626162)

# Delete hidden files
## Windows

``` del * /A:H ```

To delete hidden files from subfolders, add the /S flag

``` del * /A:H /S ```

To delete resource forks

``` del /s /q /f /a ._.* ```

``` del /s /q /f /a .* ```

To delete temporary or recovered files

``` del /s /q /a ~$* ```

``` del /p /s /a *.tmp ```

## Linux
``` find . -type f -name ".*" -delete ```

To delete thumbs.db

``` find . -iname thumbs.db -delete ```

# Tree list
## Windows
``` tree /f ```

## Linux
``` ls -a -h -R -x -l ```

D = date last modified

f = full path

h = size

o = output

# Brunnhilde

``` brunnhilde.py -n [source] [destination] [basename] ```

``` brunnhilde.py -n /storage/UTARMS/submission/b2021-0002_Lang/ /storage/UTARMS/metadata/ b2021-0002_Lang ```


