#!/usr/bin/python
# -*- coding: UTF-8 -*-
# A simple way to take snapshot for VM. You can even authorise this to one of your colleagues.
# You can create a EXE file for it using:
#   pyinstaller -F -i YourIcon.ico TakeSnapshot.py

print("\nInitiating Login Sequence ....")

import atexit
import requests
from pyVim import connect
from pyVmomi import vim
import time
time.sleep(0.5)

#####################
#https://gist.github.com/michaelrice/a6794a017e349fc65d01
#dirty work around to make python 2.7.9 work for pyvmomi
#I dont know why but it fix my problems too.
#######################
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context
#####################

def TakeSnapshot(VmName,UUID,instance_search,SnapName,SnapMemory,Description):
    global service_instance

    TheVM = service_instance.content.searchIndex.FindByUuid(None, UUID, True, instance_search)
    if TheVM is None:
        print("\n\n\n",VmName + ": Error, Unable to locate VirtualMachine.")
        raise SystemExit("Unable to locate VirtualMachine.")

    desc = None
    if Description:
        desc = Description

    task = TheVM.CreateSnapshot_Task(name=SnapName,
                                  description=desc,
                                  memory=SnapMemory,
                                  quiesce=False)

    print("\nSnapshot Completed for " + VmName)

    del TheVM
    '''
    #The following code will list a tree view of snapshots.
    #for some unlocated reasons, this tree view doesn't show the snap we take
    #so I just keep the code here.
    TheVM = service_instance.content.searchIndex.FindByUuid(None, UUID, True, instance_search)
    snap_info = TheVM.snapshot

    tree = snap_info.rootSnapshotList
    while tree[0].childSnapshotList is not None:
        print("Snap: {0} => {1}".format(tree[0].name, tree[0].description))
        if len(tree[0].childSnapshotList) < 1:
            break
        tree = tree[0].childSnapshotList
    '''

# Disable the checking of certification.
requests.packages.urllib3.disable_warnings()
# Initiate the connection to VMware vSphere.
service_instance = connect.SmartConnect(
        host="127.0.0.1", # The WMware Vcenter IP
        user="Snapshot@vsphere.local", # You should create an account with limited privilege for this.
        pwd="YourPassWord",
        port=443)

print("\nlogging In ....")
time.sleep(0.5)
atexit.register(connect.Disconnect, service_instance)

print("\nRequesting Vcenter Control ....\n\n")
time.sleep(0.7)
# Get the session ID from the connection.
# If we do not have an ID, we quit.
session_id = ""
session_id = service_instance.content.sessionManager.currentSession.key
if session_id == "":
    print("Error, Unable to Login.")
    raise SystemExit("Unable to Login.")

#Let's play some ASCII art here, just for fun :)
Mark1='*'
Mark2=' '
Lines1=9
Lines2=4
for i in range(Lines1):
    i1=int(Lines1+Lines2-i)
    i2=i*2
    print(Mark1*i1 + Mark2*i2 + Mark1*i1)
print("****  Access Granted  ****")
for i in range(Lines1):
    i1=i+Lines2+1
    i2=int((Lines1-1-i)*2)
    print(Mark1*i1+Mark2*i2+Mark1*i1)

time.sleep(1.4)
print("\n==========================")
print("==== Welcome, Snapper ====")
print("==========================")
print("\nYour Session ID is: %s" % session_id)
print("\n\n")
time.sleep(0.5)

# Generate a name with taken date for the snapshot.
TheTime=time.localtime()
SnapName=time.strftime("%Y%m%d", TheTime) #format the time string into（'20181116'）
Description=time.strftime("%Y-%m-%d %H:%M:%S", TheTime) #format into（'2018-11-16 21:25:13'）
Description+='\n不带内存的快照\n=== Taken by Your Name ==='
SnapMemory=False # A snapshot with or without memory
instance_search = False

TakeSnapshot('ServerA','The-instance-ID-of-ServerA',instance_search,SnapName,SnapMemory,Description)
TakeSnapshot('ServerB','The-instance-ID-of-ServerB',instance_search,SnapName,SnapMemory,Description)
TakeSnapshot('ServerC','The-instance-ID-of-ServerC',instance_search,SnapName,SnapMemory,Description)

print("================================")
print("==== All Missions Completed ====")
print("================================")

input('\n\n按回车键退出...')
