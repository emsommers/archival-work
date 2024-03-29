https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy

# Example - file
robocopy [source] [destination] [file to copy] /copy:DAT /dcopy:DAT /tee /v /ts /log:[destination]\[robocopy][date].log

```
robocopy C:\Desktop\ E:\ archives.zip /copy:DAT /dcopy:T /tee /v /ts /log:E:\robocopy20210910.log
```

# Example - folders
robocopy [source folder to copy\] [destination] /e /copy:DAT /dcopy:DAT /tee /v /ts /log:[destination]\[robocopy][date].log

```
robocopy "H:\Desktop\Archives\" "E:\" /e /copy:DAT /dcopy:DAT /tee /v /ts /log:E:\robocopy20210804.log
```

* F7 + arrow to go back to last command
* If destination folder becomes hidden, append ``` /A-:SH ```
* If you need to exclude a folder, add to end ``` /XD [path] ```

```
robocopy E:\ K:\accessions_born-digital\utarms-submission\Clarkson_S\ /e /dcopy:DAT /copy:DATO /tee /v /ts /log:K:\accessions_born-digital\utarms-submission\robocopy20210910.log /XD "e:\System Volume Information" /A-:SH
```


# Flags
**/e**		Copies subdirectories, including empty directories.

**/copy: DAT**	Specifies which file properties to copy (DAT = data, attributes, time stamps)

**/dcopy: DAT**	Specifies what to copy in directories (DAT = data, attributes, time stamps)

**/tee**		Writes the status output to the console window, as well as to the log file.

**/v**		Produces verbose output, and shows all skipped files.

**/ts**		Includes source file time stamps in the output.

**/log**		Writes the status output to the log file
