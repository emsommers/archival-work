A few Powershell commands when working in Windows

**1. To generate a csv file with checksums**

```Get-ChildItem "H:\My Documents\Zoom\*.*" -Recurse -force | Select-Object FullName,CreationTime,LastWriteTime,Length,@{n='SHA256';ex={(Get-FileHash $_.fullname).hash}} | export-csv "H:\My Documents\nameofmyfile.csv"```

Then in Excel to round up the :

* =ROUND((SUM(D3:D15) / 1000000),1) & " MB"
* =ROUND((SUM(D3:D15) / 1e+9),1) & " GB"

[Source](https://stackoverflow.com/questions/46947946/output-file-properties-like-filename-etc-in-powershell-into-a-csv)

**2. Quickly list all filenames in a folder to a txt or csv file**

```Get-ChildItem | Select-Object -ExpandProperty Name > names.txt```