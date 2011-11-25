import os
import codecs, sys
import re
import unicodedata

mydir = '/Users/myUser/myTextDir'
printfile = open('/Users/myUser/myOutputDir/OCR_Locator_Output.txt', 'w')
printfile_bad = open('/Users/myUser/myOutputDir/OCR_Locator_NOTEXT.txt', 'w')
limit = 50000000

print >> printfile, 'DOCUMENT\tFILE_SIZE\tCHAR_COUNT\tWORD_COUNT\tALPHA_NUM_COUNT\tLINE_COUNT\tWARNING_FLAG\tTEXT'
print >> printfile_bad, 'DOCUMENT\tFILE_SIZE\tCHAR_COUNT\tWORD_COUNT\tALPHA_NUM_COUNT\tLINE_COUNT\tWARNING_FLAG\tTEXT'
print 'DOCUMENT\tFILE_SIZE\tCHAR_COUNT\tWORD_COUNT\tALPHA_NUM_COUNT\tLINE_COUNT\tWARNING_FLAG\tTEXT'

def myloop(loop, dirr, filess):
     for child in filess:
         if os.path.isfile(dirr+'/'+child):
            file = open(dirr+'\\'+child, 'r')
            file_size = os.path.getsize(dirr+'\\'+child)
            printvar_stripped = file.readlines()
            number_of_lines = printvar_stripped.count('\n') + 1
            file.close()
            stripped = []
            countvar = 1
            printthis = []
            if int(file_size) < int(limit) :
                for lines in printvar_stripped:
                    stripped_line = " ".join(lines.split())
                    stripped.append(stripped_line)
                    printthis = " ".join(stripped)
            else :
                continue
            number_of_characters = len(printthis)
            if (int(number_of_characters == 0)):
                wordcount = 0
                alphanumeric_chars = 0
            else:
                wordcount = len(re.findall("\w+",printthis))
                alphanumeric_chars = len(re.findall("\w",printthis))
            if ((int(alphanumeric_chars) < 30)) or (int(number_of_lines > int(alphanumeric_chars))):
                warning_flag = '1'
            else :
                warning_flag = '0'
            print (child) + '\t'  +  str(file_size) + '\t' + '\t' + str(number_of_characters) + '\t' + str(wordcount) + '\t' + str(alphanumeric_chars) + '\t' + str(number_of_lines)   + '\t'+ str(warning_flag) + 't' + str(printthis[0:20000])
            print >> printfile, ((child) +  '\t'  +  str(file_size) + '\t' + str(number_of_characters) + '\t' + str(wordcount) + '\t' + str(alphanumeric_chars) + '\t' + str(number_of_lines)  + '\t' + str(warning_flag) + '\t' + str(printthis[0:20000]))
            if warning_flag == '1':
                print >> printfile_bad, ((child) +  '\t' +  str(file_size) + '\t'  +  str(number_of_characters) + '\t' + str(wordcount) + '\t' + str(alphanumeric_chars) + '\t' + str(number_of_lines)  + '\t' + str(warning_flag) + '\t' + str(printthis[0:20000]))

os.path.walk(mydir, myloop, 3)
printfile.close()
printfile_bad.close()
