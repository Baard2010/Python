# -*- coding: utf-8 -*-
"""
Reads the Seaclear directory file CHARTCAL.DIR and creates a .txt file for
each chart. the .txt files are used by imgkap.exe together with the chart files
(.png) to create openCPN chart files (.kap)
Also a .bat file is created to run imgkap.exe multiple times (for each chart)  
"""
fout = open('test.txt', 'w')
fbat = open('convert.bat', 'w')
fin = open('CHARTCAL.DIR', 'r')

print "making .txt (preprocessing file) for imgkap.exe, and .bat file "
numFiles = 0

for line in fin:
    if line.startswith('['):
        filename = line[1:len(line)-6]
        print ('Processing ' + filename + '.png')
        if not fout.closed:
            fout.close()
        fbat.write('imgkap ' + filename + '.png ' + filename + '.txt ' + filename + '.kap\n')        
        fout = open(filename + '.txt', 'w')
        numFiles += 1

    if line.startswith('SC'):
        scale = line[3:len(line)-1]
    if line.startswith('WI'):
        WI = line[3:len(line)-1] # pixels
    if line.startswith('HE'):
        HE = line[3:len(line)-1] # pixels
    if line.startswith('B1='):
        snum = line[3:len(line)-1]
        snum = snum.split(',')
        fnum1 = float(snum[0])
        fnum1 = round(fnum1, 8)
        fnum2 = float(snum[1])
        fnum2 = round(fnum2, 8)
        B1y = fnum1
        B1x = fnum2
    if line.startswith('B2='):
        snum = line[3:len(line)-1]
        snum = snum.split(',')
        fnum1 = float(snum[0])
        fnum1 = round(fnum1, 8)
        fnum2 = float(snum[1])
        fnum2 = round(fnum2, 8)
        B2y = fnum1
        B2x = fnum2
    if line.startswith('B3='):
        snum = line[3:len(line)-1]
        snum = snum.split(',')
        fnum1 = float(snum[0])
        fnum1 = round(fnum1, 8)
        fnum2 = float(snum[1])
        fnum2 = round(fnum2, 8)
        B3y = fnum1
        B3x = fnum2
    if line.startswith('B4='):
        snum = line[3:len(line)-1]
        snum = snum.split(',')
        fnum1 = float(snum[0])
        fnum1 = round(fnum1, 8)
        fnum2 = float(snum[1])
        fnum2 = round(fnum2, 8)
        B4y = fnum1
        B4x = fnum2

    if line.startswith('PC=0'): #end of block -> start writing
        fout.write('VER/2.0\n')
        fout.write('BSB/NA=' + filename + '\n')
        fout.write('  NU=1,RA=' + WI + ',' + HE + ',DU=72\n')
        fout.write('KNP/SC=' + scale + ',GD=WGS84,PR=MERCATOR\n')
        lat = (B2y + B4y) / 2
        lat = round(lat, 1)
        fout.write('  PP=' + str(lat) + ',PI=UNKNOWN,SP=UNKNOWN,SK=0.0,TA=90.0\n')
        fout.write('  UN=METERS,SD=MLWS,DX=000,DY=000\n')
        fout.write('CED/SE=info,RE=1,ED=2\n')
        fout.write('OST/1\n')
        s1 = str(B2y) + ',' + str(B2x) + '\n'
        s2 = str(B1y) + ',' + str(B1x) + '\n'
        s3 = str(B4y) + ',' + str(B4x) + '\n'
        s4 = str(B3y) + ',' + str(B3x) + '\n'
        fout.write('REF/1,0,' + HE + ',' + s1)
        fout.write('REF/2,0,0,' + s2)
        fout.write('REF/3,' + WI + ',0,' + s3)
        fout.write('REF/4,' + WI + ',' + HE + ',' + s4)
        fout.write('PLY/1,' + s1)
        fout.write('PLY/2,' + s2)
        fout.write('PLY/3,' + s3)
        fout.write('PLY/4,' + s4)
        fout.write('DTM/0.00,0.00\n')
        fout.write('CPH/0.0\n')
        
fout.close()
fin.close() 
fbat.close()

print('Processed ' + str(numFiles) + ' files')
   
