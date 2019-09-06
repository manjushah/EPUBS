from  ebooklib import epub
import os
import sys
import uuid
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

source_file = sys.argv[1]
df = pd.read_excel('epub_files.xlsx', sheetname='Sheet1')
print("Column headings:")

for i in df.index:
    
    print(df['FileName'][i]) 
    print(df['Title'][i])
    
    title = df['Title'][i]
    identifier = str(uuid.uuid1())
    # set metadata
    book = epub.read_epub(source_file +'.epub')
    book.set_identifier(identifier)
    
    # write to the file
    epub.write_epub('new_epubs/' + df['FileName'][i] + '.epub', book, {})
    cmd = "python epubtag.py -T " + "'"+title +"'"+ " " + "new_epubs/" + df['FileName'][i]+".epub"
    print(cmd)
    os.system(cmd)
