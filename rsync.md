rsync -rltv --progress --stats --log-file=[*log file name and location*] [*stuff to transfer path*] [*path to transfer to*]


Example: 

```
rsync -rltv --progress --stats /home/sommerse/Desktop/UTARMS-K/accessions_born-digital/utarms-ingest/B2019-0005/ /storage/UTARMS/03_in-process/B2019-0005_Kidd
```

**-r** recursive

**-l** preserve symlinks

**-t** preserve modification times

**-v** verbose

**--progress** show progress during transfer

**--stats** give some file-transfer stats

Can also exclude folders or specific types of files (e.g. hidden one):

```--exclude='myFolderName'```

```--exclude=".*"```

```--exclude="*.jpg"```

```
rsync -rltv --progress --stats --exclude='System Volume Information' --exclude=".*"  /media/sdc1/ /storage/UTARMS/01_submission/B2017-0008_Bliss
```