rsync -rltv --progress --stats --log-file=[*log file name and location*] [*stuff to transfer path*] [*path to transfer to*]


Example: 

```
rsync -rltv --progress --stats --log-file=/storage/UTARMS/metadata/b2021-0002_lang/rsync20210910.log /storage/UTARMS/submission/Lang /storage/UTARMS/ingest/b2021-0002_Lang
```

**-r** recursive

**-l** preserve symlinks

**-t** preserve modification times

**-v** verbose

**--progress** show progress during transfer

**--stats** give some file-transfer stats