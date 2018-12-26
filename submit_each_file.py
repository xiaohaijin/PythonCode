#!/usr/bin/env python3


import os
import stat


def getFileList(fileDir):
    fileList = os.listdir(fileDir)
    newFileList = []
    for eachFile in fileList:
        if eachFile[:31] not in newFileList:
            newFileList.append(eachFile)
    return newFileList


def createSubmitFile(eventRootName):
    fileName = str(eventRootName).split("_")[4]
    submitComtent = """Universe     = vanilla
Notification = Error
Initialdir   = /star/u/jhai/selfSC_GL/test/submit/submit6.8_9
Executable   = $(Initialdir)/run47.csh
Arguments    = $(Process)
Log          = $(Initialdir)/log/job47_$(Process).log
Output       = $(Initialdir)/log/job47_$(Process).out
Error        = $(Initialdir)/log/job47_$(Process).err
GetEnv       = True
+Job_Type    = "cas"
Queue 1"""

    submitComtentResult = submitComtent.split("\n")
    fileObject = open(fileName + ".con", "w")
    for eachLine in submitComtentResult:
        if eachLine.lower().startswith("executable"):
            eachLine = "Executable   = $(Initialdir)/" + fileName + ".csh"
        fileObject.write(eachLine+'\n')
    fileObject.close()


def createRunShell(eventRootName):
    fileName = str(eventRootName).split("_")[4]
    shellContent = """#!/bin/csh
stardev
root4star -b -q -l 'doEvents_SCGL_Calib.C(5000,"./output/*19072018_raw_5000008*")'
"""

    shellContentResult = shellContent.split("\n")
    fileObject = open(fileName + ".csh", "w")
    for eachLine in shellContentResult:
        eachLine.strip('\n')
        if eachLine.lower().startswith("root4star"):
            eachLine = """root4star -b -q -l 'doEvents_SCGL_Calib.C(5000,"/star/u/jhai/scratch/test/""" + eventRootName + "*" + """")'"""
        fileObject.write(eachLine+"\n")
    fileObject.close()
    os.chmod(fileName + ".csh", stat.S_IRWXU)


def main():
    fileDir = "/star/u/jhai/scratch/test"
    eventFileList = getFileList(fileDir)
    for eachEventFile in eventFileList:
        eachEventFile = eachEventFile[:31]
        createRunShell(eachEventFile)
        createSubmitFile(eachEventFile)


if __name__ == "__main__":
    main()
