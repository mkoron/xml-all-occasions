"""
Handles the parsing of a xml file and creates a full website based on the xml tags.
"""
from xml.sax.handler import ContentHandler
import dispatcher
import os

class WebsiteConstructor(dispatcher.Dispatcher, ContentHandler):
    passthrough = False

    def __init__(self, directory):
        self.directory = [directory]
        self.ensureDirectory()

    def ensureDirectory(self):
        path = os.path.join(*self.directory)
        if not os.path.isdir(path): os.makedirs(path)

    def characters(self, chars):
        if self.passthrough: self.out.write(chars)

    def defaultStart(self, name, attrs):
        if self.passthrough:
            self.out.write('<' + name)
            for key, val in attrs.items():
                self.out.write(' {}="{}"'.format(key, val))
            self.out.write('>')

    def defaultEnd(self, name):
        if self.passthrough:
            self.out.write('</{}>'.format(name))

    def startDirectory(self, attrs):
        self.directory.append(attrs['name'])
        self.ensureDirectory()

    def endDirectory(self):
        self.directory.pop()

    def startPage(self, attrs):
        filename = os.path.join(*self.directory + [attrs['name'] + '.html'])
        try:
            self.out = open(filename, 'w')
        except IOError:
            print("There has been an error in writing the output files")
        self.writeHeader(attrs['title'])
        self.passthrough = True

    def endPage(self):
        self.passthrough = False
        self.writeFooter()
        self.out.close()

    def writeHeader(self, title):
        self.out.write('<html>\n <head>\n <title>')
        self.out.write(title)
        self.out.write('</title></head>\n <body>')

    def writeFooter(self):
        self.out.write('</body>\n </html>\n')
