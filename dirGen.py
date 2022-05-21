#make a function for this code(not necesarrily, can be used in loop as well(input from user))

#direcId:folderName
#parent_child: 0 or 1 (1 if child)
#parentId:id of parent(fetch direcId:folderName from dictionary)
#testTrain:0 or 1 create the test/train folder(if 1 create the tt folders(fetch dirList from the dataset))
#folderName:name of the folder
#logic:- if child, append the parentDir + folderName in dictionary :D (id makes it functional)
import os

dic={}

def fn(direcId,parent_child,parentId,testTrain,folderName):
    if direcId not in dic:
        dic.update({direcId:folderName})
        if parent_child:
            dic.update({direcId:dic[parentId]+'/'+folderName})
    addr=''
    if parent_child:
        addr=dic[direcId]
        arr=addr.split('/')
    else:
        addr=folderName
        if os.path.exists(addr)!=1:
            os.mkdir(addr)

    if parent_child:
        addr=''
        for folders in arr:
            addr=addr+folders
            if os.path.exists(addr)!=1:
                os.mkdir(addr)
            addr=addr+'/'

    if testTrain:
        os.mkdir(addr+'/testing')
        os.mkdir(addr+'/training')
#example:-
fn(1,0,0,0,'experiment3')
fn(2,1,1,1,'frequency')
fn(3,1,1,0,'frequencyWithIndex')
fn(4,1,1,0,'classProbability')
fn(5,1,1,1,'preprocessd')
fn(6,1,4,0,'counterforth')
fn(7,1,3,1,'counter')
fn(8,1,3,1,'excel')
fn(9,1,1,1,'frequencyRatio')
fn(10,1,1,0,'result')
fn(11,1,1,0,'selectedFeatures')
fn(12,1,1,1,'')                     # this will only make tt dir
                                    # if code dosnt work for tt for EXISTING DIR try [ fn(anyId,1,idOfDir,1,'') ]  change the parameters to dir generating error 



