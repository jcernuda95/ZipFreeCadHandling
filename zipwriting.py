import os,sys,string
import xml.sax
import xml.sax.handler
import xml.sax.xmlreader
import zipfile

# SAX handler to parse the Document.xml
class DocumentHandler(xml.sax.handler.ContentHandler):
	def __init__(self, dirname):
		self.files = []
		self.dirname = dirname

	def startElement(self, name, attributes):
		item=attributes.get("file")
		if item != None:
			self.files.append(os.path.join(self.dirname,str(item)))

	def characters(self, data):
		return

	def endElement(self, name):
		return

def createDocument(filename, outpath):
	files=getFilesList(filename)
	dirname=os.path.dirname(filename)
	guixml=os.path.join(dirname,"GuiDocument.xml")
	if os.path.exists(guixml):
		files.extend(getFilesList(guixml))
	compress=zipfile.ZipFile(outpath,'w',zipfile.ZIP_DEFLATED)
	for i in files:
		dirs=os.path.split(i)
		#print i, dirs[-1]
		compress.write(i,dirs[-1],zipfile.ZIP_DEFLATED)
	compress.close()

def getFilesList(filename):
	dirname=os.path.dirname(filename)
	handler=DocumentHandler(dirname)
	parser=xml.sax.make_parser()
	parser.setContentHandler(handler)
	parser.parse(filename)

	files=[]
	files.append(filename)
	files.extend(iter(handler.files))
	return files


def main(arg):
	inputPath = ''
	outputPath = ''

	inputPath = arg[0]
	outputPath = arg[1]

	if(inputPath != '' and outputPath != ''):
		createDocument(inputPath, outputPath)

if __name__ == "__main__":
   main(sys.argv[1:])