# ZipFreeCadHandling

Basic handling of the project file generated by freeCad.

The zipreading decomprese the file and transform it into the multiple files, being the most interesting the document.xml
  it requires two parameters:
    python zipreading.py <input adress> <output adress>
      input adress being the adress of the project file from freecad ending in fcstd
      output adress being the adress where you want the files to be generated

The zipwriting comprese the files generated by the previous file into a project for freeCad.
  it requires two paramenters:
    python zipwriting.py <input adress> <output adress>
      input adress being the adress of the document.xml
      output adress being the adress where you want the freecad project (fcstd) to be generated
