#!/usr/bin/python3

import os
import csv
import sys

# where I want the folders to go
destination = '/home/sommerse/Desktop/UTARMS/03_in-process'
#folder names
sip_name= input ("Enter accession-number_name, e.g. B2019-0005_Kidd: ")
sip_dir = os.path.join(destination, sip_name)
sip_files = "files_" + sip_name
object_dir = os.path.join(sip_dir, "objects")
accession_dir = os.path.join(object_dir, sip_files)
metadata_dir = os.path.join(sip_dir, "metadata")
subdoc_dir = os.path.join(metadata_dir, "submissionDocumentation")

for newfolder in object_dir, metadata_dir, accession_dir, subdoc_dir:
    os.makedirs(newfolder)

CSV_HEADERS = ["filename", "dc.title", "dc.creator", "dc.date", "dcterms.extent", "dc.description", "dcterms.accessRights", "dc.source", "dcterms.isPartOf", "dcterms.type", "dc.identifier",]
CSV_DATA = ["objects", "", "", "", "xx digital files ()", "", "", "", "AIC#", "Archival Information Package", ""]
csv_path = os.path.join(metadata_dir, "metadata.csv")
with open(csv_path, 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(CSV_HEADERS)
    writer.writerow(CSV_DATA)

sys.exit ("Creating SIP directories, metadata spreadsheet, and exiting. Goodbye!")
