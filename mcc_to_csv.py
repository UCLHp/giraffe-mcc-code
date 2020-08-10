"""
Created on Tue Mar  3 15:39:19 2020
@author: abernett

Script to convert the water tank's mcc files into csv format
so they can be read into Giraffe software as reference
"""

MCC_FILENAME = "Example_PDD_150MeV.mcc"


# Read the mcc file that needs to be converted
lines = open(MCC_FILENAME).readlines()


SSD=None
#SSD="99999"
xstring = "X:"
ystring = "Y:"


# Extract SSD and all x,y data as separate strings
# (x,y data is between END_DATA and BEGIN_DATA tags)
readingdata = False
for line in lines:
    
    if "SSD=" in line:
        SSD = line.split("=")[1].strip()
   
    if "END_DATA" in line:
        readingdata = False
        
    if readingdata:     
        splitline = line.split()
        xstring = xstring + line.split()[0].strip() + ";"
        ystring = ystring + line.split()[1].strip() + ";"  
    
    if "BEGIN_DATA" in line:
        readingdata = True

#Remove final semicolon from x,y strings
xstring = xstring[:len(xstring)-1]
ystring = ystring[:len(ystring)-1]

#create a new csv file in the format required by Giraffe software
fout = open("output.csv", "w")
fout.write("Water phantom\n")
fout.write("SSD:{}\n".format(SSD) )
fout.write("Water offset (build-up):0\n")
fout.write("Radiation type:Proton\n")
fout.write("\n")
fout.write(xstring+"\n")
fout.write("\n")
fout.write(ystring+"\n")
fout.close()

