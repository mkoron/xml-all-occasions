"""
The program takes a xml file as input and gives a complete website
with the appertaining web pages in the folder public_html as output.

Example:

    You can use the program as following:

        python main input_file.xml

"""
from xml.sax import parse
import sys
import dispatcher
import constructor

if __name__ == '__main__':
    parse(sys.argv[1], constructor.WebsiteConstructor('public_html'))