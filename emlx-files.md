# Working with emlx files to import them into ePadd

**Background:** accession included 4 folders that appeared to have been exported from the donor's email account: 

    Folder-name.mbox 
        Messages
            1152.emlx
            1157.emlx
            ...

    Sent-mail.mbox
        Messages
            1165.emlx
            1165.emlx
            ...

## Troubleshooting steps:

1. Tried importing emlx files into ePadd and converting using Emailchemmy dongle. This kept failing with an indexing error.

2. Converted emlx to MBOX using this script [https://github.com/imdatceleste/elmx2mbox](https://github.com/imdatceleste/elmx2mbox). The script was first found on the [LOC format description page for Apple Mail Email Format](https://www.loc.gov/preservation/digital/formats//fdd/fdd000615.shtml).

Before starting, copy email files to a folder under **emlx2mbox** folder into a folder named **Mail**. 

Run the script within a Conda environment:

### Steps in Terminal

```shell
conda create -n emlx2mbox
conda activate emlx2mbox
conda install -c conda-forge ruby
conda install -c conda-forge compilers

cd emlx2mbox
chmod u+x emlx2mbox.rb
./emlx2mbox.rb Mail

# Mail is the name of the folder with emlx files

conda deactivate
```

A *Converted* folder will be created with the mbox files inside.

**NOTE:** I had to edit line 96 of the original script to replace 'exists' with 'exist'

**NOTE 2:** 12 of the emlx files resulted in an 'Invalid date' error when converting to MBOX. I edited each file to fix the error in question: in the Date row, removed the timezone in parentheses (e.g. (EST)). Then re-ran the script.

3. Run ePadd and import the MBOX files. Success!