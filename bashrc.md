## If you accidentally delete the .bashrc file from Home folder :sweat_smile:

[[Source link]](https://askubuntu.com/questions/198730/how-to-restore-bashrc-file)

You'll know this happened if your Terminal window suddenly looks like this (note the change in text colour):
![Terminal window after bashrc has been deleted](/screenshots/screenshot_noBashSettings.png)

1. Copy the skeleton ```.bashrc``` file over to Home folder:

```
cp /etc/skel/.bashrc ~/
```

2. Load the new one:

```
source ~/.bashrc
```

### Then restore any bash settings you may have, eg.:

#### CONDA:
* Add path variable:
```
$ echo 'export PATH=/home/sommerse/miniconda3/bin:$PATH' >> ~/.bashrc
$ source ~/.bashrc
```
* Initialize bash
```
conda init bash
```
#### Restore settings for scripts folder:
```
nano ~/.bashrc
```
Then add to file:
```
# My scripts path
export PATH="/home/sommerse/Desktop/Scripts/archival-work:$PATH"
```

```
source ~/.bashrc
```