from xml.sax import parse
import dispatcher
import constructor

if __name__ == '__main__':
    parse('website.xml', constructor.WebsiteConstructor('public_html'))