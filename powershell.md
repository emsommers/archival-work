# PowerShell

A few PowerShell commands when working in Windows

## 1. To generate a csv file with checksums**

```Get-ChildItem "H:\My Documents\Zoom\*.*" -Recurse -force | Select-Object FullName,CreationTime,LastWriteTime,Length,@{n='SHA256';ex={(Get-FileHash $_.fullname).hash}} | export-csv "H:\My Documents\nameofmyfile.csv"```

Then in Excel, to round up the bytes (Length column):

* =ROUND((SUM(D3:D15) / 1000000),1) & " MB"
* =ROUND((SUM(D3:D15) / 1e+9),1) & " GB"

[Source](https://stackoverflow.com/questions/46947946/output-file-properties-like-filename-etc-in-powershell-into-a-csv)

## 2. Quickly list all filenames in a folder to a txt or csv file**

```Get-ChildItem | Select-Object -ExpandProperty Name > names.txt```

## 3. Create folders with padded numbers

Open PowerShell in current working directory then:

```1..20 | ForEach-Object { New-Item -ItemType Directory -Name ("A2017-0013_df{0:D3}" -f $_) }```

Will result in

A2017-0013_df001

A2017-0013_df002

…

A2017-0013_df020

## 4. Count the number of jpgs within all folders and subdirectories

```Get-ChildItem -Recurse -Include *.jpg -Path "K:\Digitized Photos\Marshall Negs\JPGS_UTAO" | Measure-Object```

*See also PowerShell script on K:\ - countJPG.ps1*

## 5. List folders and their file counts

```dir -recurse |  ?{ $_.PSIsContainer } | %{ Write-Host $_.FullName (dir $_.FullName | Measure-Object).Count }```