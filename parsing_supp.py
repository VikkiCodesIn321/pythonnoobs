import os
import string
import glob
from pathlib import Path
import re

#Start functions::
def parse_usw():
    '''Main function for USW'''
    fileTot = list(Path(fileDir).glob('**/*.inform'))
    for file in fileTot:
        hostname_output = []
        dis_port_count = 0
        with open(file, "r") as f:
            for line in f.readlines():
                if '"model_display" :' in line:
                    replacedLine = line.replace('"model_display" :', "").replace('"', "").replace(":", "").replace(",", "").strip()
                    print("Model: " + replacedLine)
                if '"_mac" :' in line:
                    replacedLine = line.replace('"_mac" :', "").replace('"', "").replace(":", "").replace(",", "").replace("-", ":").strip()
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
                if 'discarding' in line:
                    #replacedLine = line.replace("discarding", "").replace('"', "").replace(":", "").replace(",", "").replace("_", "").strip()
                    dis_port_count += 1
                    #print("# of Discarding Ports: " + str(replacedLine))
                if '"hostname" :' in line:
                    replacedLine = line.replace('"hostname" :', "").replace('"', "").replace(":", "").replace(",", "").strip()
                    hostname_output.append("Device Hostname: " + replacedLine)
            print(hostname_output[0])
            print("Num. of Discarding Ports: " + str(dis_port_count))
        f.close()
        print("+-----------------------------------------+")

def parse_uap():
    '''Main function for UAP'''
    fileTot = list(Path(fileDir).glob('**/*.inform'))
    for file in fileTot:
        hostname_output = []
        with open(file, "r") as f:
            for line in f.readlines():
                if '"model_display" :' in line:
                    replacedLine = line.replace('"model_display" :', "").replace('"', "").replace(":", "").replace(",", "").strip()
                    print("Model: " + replacedLine)
                    break
                if '"_mac" :' in line:
                    replacedLine = line.replace('"_mac" :', "").replace('"', "").replace(":", "").replace(",", "").replace("-", ":").strip()
                    print("MAC Address: " + replacedLine)
                if 'devextip' in line:
                    replacedLine = line.replace("devextip", "").replace('"', "").replace(":", "").replace(",", "").replace("_", "").strip()
                    print("Access Point IP: " + str(replacedLine))
                if '"hostname" :' in line:
                    replacedLine = line.replace('"hostname" :', "").replace('"', "").replace(":", "").replace(",", "").strip()
                    hostname_output.append("Device Hostname: " + replacedLine)
            print(hostname_output[0])
        f.close()
        print("+-----------------------------------------+")

while True:
    fileDir = str(input("Which directory should this be scanning? ")).strip()
    if "uap" in fileDir.lower():
        print("+-----------------------------------------+")
        parse_uap()
        next_step = str(input("Press enter to continue or type exit to leave. "))
        if "exit" in next_step:
            print("Thank you for using this utility!")
            break
        else:
            pass
    elif "usw" in fileDir.lower():
        print("+-----------------------------------------+")
        parse_usw()
        next_step = str(input("Press enter to continue or type exit to leave. "))
        if "exit" in next_step:
            print("Thank you for using this utility!")
            break
        else:
            pass
    else:
        print("Please choose a USW or UAP directory at this time.")
#print("Which device type would you like to parse?")
#print("UAP | USW | USG")
#deviceParse = str(input("Your selection: ")).upper().strip()
#print("+-----------------------------------------+")
#if deviceParse == "USW":
#    parse_usw()
#if deviceParse == "UAP":
#    parse_uap()
