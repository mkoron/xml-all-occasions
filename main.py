"""
The program takes a xml file as input and gives a complete website
with the appertaining web pages in the folder public_html as output.

Example:

    You can use the program as following:

        python main input_file.xml

"""
import os.path
from xml.sax import parse
import sys
import constructor

if __name__ == '__main__':
    inputFile = sys.argv[1]
    if os.path.isfile(inputFile):
        parse(inputFile, constructor.WebsiteConstructor('public_html'))
    else:
        print("There has been an error reading the file.")