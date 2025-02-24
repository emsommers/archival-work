#!/usr/bin/python3

import os
import csv
import sys
import subprocess

# locations of stuff
sourcedir = '/storage/UTARMS/02_in-progress'
destination = '/storage/UTARMS/03_processed'

sip_name= input ("Enter accession-number_name, e.g. B2019-0005_Kidd: ")

#################################
########## FOLDER NAMES #########
#################################

# e.g. 03_in-process/sip_name
sip_dir = os.path.join(destination, sip_name)

# e.g. 03_in-process/sip_name/objects
object_dir = os.path.join(sip_dir, "objects")

# variable to append word string 'files_' to sip_name for eventual folder creation
sip_files = "files_" + sip_name

# e.g. 03_in-process/sip_name/objects/files_sip_name
accession_dir = os.path.join(object_dir, sip_files)

# e.g 03_in-process/sip_name/metadata
metadata_dir = os.path.join(sip_dir, "metadata")

# e.g 03_in-process/sip_name/metadata/submissionDocumentation
subdoc_dir = os.path.join(metadata_dir, "submissionDocumentation")

# create folders
for newfolder in object_dir, metadata_dir, accession_dir, subdoc_dir:
    os.makedirs(newfolder)

# create csv file
CSV_HEADERS = ["filename", "dc.title", "dc.creator", "dc.date", "dcterms.extent", "dc.description", "dcterms.accessRights", "dc.source", "dcterms.isPartOf", "dcterms.type", "dc.identifier",]
CSV_DATA = ["objects", "", "", "", "xx digital files ()", "", "", "", "AIC#", "Archival Information Package", ""]

# where the csv will be created and it's name
csv_path = os.path.join(metadata_dir, "metadata.csv")
with open(csv_path, 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(CSV_HEADERS)
    writer.writerow(CSV_DATA)

# copy (rsync) files from /02 to /03 folder, assuming folder name in /02 = sip_name 
rsyncsourcepath = os.path.join(sourcedir, sip_name)
rsyncsourcedir = rsyncsourcepath + "/"
subprocess.run(['rsync', '-rltv', '--progress', '--stats', rsyncsourcedir, accession_dir])

sys.exit ("Creating SIP directories, metadata spreadsheet, copying files, and exiting.")