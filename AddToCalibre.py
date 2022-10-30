from openpyxl import *
import os
import glob


#physics
pathPhy = 'G:\Meine Ablage\ebooks\physics'
tagPhy = 'Physics'
cellPhy= 'B4'
#german
pathGer = 'G:\Meine Ablage\ebooks\german'
tagGer = 'german'
cellGer = 'B5'
#RF
pathRF = 'G:\Meine Ablage\ebooks\RF'
tagRF = 'RF'
cellRF = 'B6'
#semiconductors
pathSC = 'G:\Meine Ablage\ebooks\semiconductors'
tagSC = 'semiconductors'
cellSC = 'B7'

#Analog
pathAna = 'G:\Meine Ablage\ebooks\Analog'
tagAna = 'Analog'
cellAna = 'B8'


def AddToCalibre(path, tag , cell) :
    files = glob.glob('{}\*.pdf'.format(path)) 
    last = max(files ,key= os.path.getctime,default=0,)
    myW = load_workbook(r'G:\Meine Ablage\ebooks\HowManyFiles.xlsx')
    myS = myW.active
    val = myS['{}'.format(cell)] 
    if len(files) > int(val.value) :
        print("we found one in {}".format(tag))
        os.system('calibredb add -T "{tag}" "{file}" '.format(tag=tag , file=last))
    else :
        print("we didnt find in {}".format(tag))
    myS['{}'.format(cell)] = len(files)
    myW.save(r'G:\Meine Ablage\ebooks\HowManyFiles.xlsx')
    
AddToCalibre(  pathPhy, tagPhy , cellPhy )
AddToCalibre(pathGer  , tagGer , cellGer )
AddToCalibre( pathRF , tagRF ,  cellRF)
AddToCalibre(pathSC,tagSC,cellSC)
AddToCalibre( pathAna , tagAna , cellAna )
