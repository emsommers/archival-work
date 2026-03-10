# ExifTool

Using [ExifTool](https://exiftool.org/)

## Export all the embedded metadata in folders of photos to a csv file

**exiftool -csv -r (recursive) > /output location/file.csv /directoryToScan**

```
exiftool -csv -r > /storage/UTARMS/01_submission/A2026_UofTCommunications/metadata.csv /storage/UTARMS/01_submission/A2026_UofTCommunications/extracted/
```

**Note:** works with PDFs too!!

## List all the time based tags

```
exiftool -time:all -G1 -a -s file.jpg

exiftool -time:all -G1 -a -s 15aug07_13.JPG
```

## Change 2099 year date in EXIF to 2007 (subtract 92 years)
```
exiftool '-DateTimeOriginal-=92:0:0 0' 'Directory'

exiftool '-DateTimeOriginal-=92:0:0 0' '/storage/UTARMS/02_ingest/A2022-0003_HartHouse/A2022-0003_CD033/Farm Aug 07/Farm Aug 07'
```

```
dry-run exiftool '-DateTimeOriginal-=92:0:0 0' '/storage/UTARMS/02_ingest/A2022-0003_HartHouse/A2022-0003_CD033/Farm Aug 07/Farm Aug 07'
```

## Change file modified date on the system with the date from EXIF metadata (DateTimeOriginal)

```
exiftool '-FileModifyDate<DateTimeOriginal' -r 'Directory'
```



