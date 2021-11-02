https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy

# Example - file
robocopy [source] [destination] [file to copy] /copy:DATO /dcopy:DAT /tee /v /ts /log:[destination]\[robocopy][date].log
robocopy C:\Desktop\ E:\ archives.zip /copy:DAT /dcopy:T /tee /v /ts /log:E:\robocopy20210910.log

# Example - folders
robocopy [source folder to copy\] [destination] /e /copy:DATO /dcopy:DAT /tee /v /ts /log:[destination]\[robocopy][date].log
robocopy "H:\Desktop\Archives\" "E:\" /e /copy:DATO /dcopy:DAT /tee /v /ts /log:E:\robocopy20210804.log

# Flags
/e		Copies subdirectories, including empty directories.
/copy: DATO	Specifies which file properties to copy (DATO = data, attributes, time stamps, owner information)
/dcopy: DAT	Specifies what to copy in directories (DAT = data, attributes, time stamps)
/tee		Writes the status output to the console window, as well as to the log file.
/v		Produces verbose output, and shows all skipped files.
/ts		Includes source file time stamps in the output.
/log		Writes the status output to the log file
