import os
import string
import glob
from pathlib import Path
import re

fileDir = str(input("Which directory should this be scanning? ")).strip()

#Start functions::
def parse_usw():
    '''Main function for USW'''
    fileTot = list(Path(fileDir).glob('**/*.inform'))
    for file in fileTot:
        output = []
        with open(file, "r") as f:
            for line in f.readlines():
                if '"model_display" :' in line:
                    replacedLine = line.replace('"model_display" :', "").replace('"', "").replace(":", "").replace(",", "").strip()
                    print("Model: " + replacedLine)
                if '"_mac" :' in line:
                    replacedLine = line.replace('"_mac" :', "").replace('"', "").replace(":", "").replace(",", "").strip()
                    print("MAC Address: " + replacedLine)
                if '"stp_priority" :' in line:
                    replacedLine = line.replace('"stp_priority" :', "").replace('"', "").replace(":", "").replace(",", "").strip()
                    print("Spanning Tree Priority: " + replacedLine)
                if 'root_switch' in line:
                    replacedLine = line.replace("root_switch", "").replace('"', "").replace(",", "").strip().upper()
                    print("Root Bridge" + replacedLine)
                if 'devextip' in line:
                    replacedLine = line.replace("devextip", "").replace('"', "").replace(":", "").replace(",", "").replace("_", "").strip()
                    print("Switch IP: " + str(replacedLine))
                if '"hostname" :' in line:
                    replacedLine = line.replace('"hostname" :', "").replace('"', "").replace(":", "").replace(",", "").strip()
                    output.append("Device Hostname: " + replacedLine)
            print(output[0])
        f.close()
        print("+-----------------------------------------+")

def parse_uap():
    '''Main function for UAP'''
    fileTot = list(Path(fileDir).glob('**/*.inform'))
    for file in fileTot:
        output = []
        with open(file, "r") as f:
            for line in f.readlines():
                if '"hostname" :' in line:
                    replacedLine = line.replace('"hostname" :', "").replace('"', "").replace(":", "").replace(",", "").strip()
                    output.append("Device Hostname: " + replacedLine)
            print(output[0])
        f.close()
        print("+-----------------------------------------+")


print("Which device type would you like to parse?")
print("UAP | USW | USG")
deviceParse = str(input("Your selection: ")).upper().strip()
print("+-----------------------------------------+")
if deviceParse == "USW":
    parse_usw()
if deviceParse == "UAP":
    parse_uap()
