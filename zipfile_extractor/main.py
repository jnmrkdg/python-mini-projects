from zipfile import ZipFile

#Extract All Files in Zip File
with ZipFile('my_files.zip', 'r') as zip_object:
    zip_object.extractall()

#Extract Individual Files From Zip File
#with ZipFile('my_files.zip', 'r') as zip_object:
#    print(zip_object.namelist()) 
#    zip_object.extract('code_snippet.png')

#with ZipFile('my_files.zip', 'r') as zip_object:
#    file_names = zip_object.namelist()
#
#    for file_name in file_names:
#        if file_name.endswith('.csv'):
#            zip_object.extract(file_name)