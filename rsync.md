rsync -rltv --progress --stats --log-file=[*log file name and location*] [*stuff to transfer path*] [*path to transfer to*]


Example: 

```
rsync -rltv --progress --stats rsync -rltv --progress --stats /home/sommerse/Desktop/UTARMS-K/accessions_born-digital/utarms-ingest/B2019-0005/ /storage/UTARMS/in-process/B2019-0005_Kidd
```

**-r** recursive

**-l** preserve symlinks

**-t** preserve modification times

**-v** verbose

**--progress** show progress during transfer

**--stats** give some file-transfer stats