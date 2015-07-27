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

def extractDocument(filename, outpath):
	zfile=zipfile.ZipFile(filename)
	files=zfile.namelist()

	for i in files:
		data=zfile.read(i)
		dirs=i.split("/")
		if len(dirs) > 1:
			dirs.pop()
			curpath=outpath
			for j in dirs:
				curpath=curpath+"/"+j
				os.mkdir(curpath)
		output=open(outpath+"/"+i,'wb')
		output.write(data)
		output.close()

def main(arg):
	inputPath = ''
	outputPath = ''

	inputPath = arg[0]
	outputPath = arg[1]

	if(inputPath != '' and outputPath != ''):
		extractDocument(inputPath, outputPath)

if __name__ == "__main__":
   main(sys.argv[1:])
