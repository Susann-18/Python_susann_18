# import zipfile
# with zipfile.ZipFile("zipdata.zip","r")as zipfile:
#     file_list=zipfile.namelist()
#     print("content of the zipfile",file_list)


# import zipfile
# with zipfile.ZipFile("zipdata.zip","w")as zipfile:
#     zipfile.write("file1.txt")
#     zipfile.write("file2.txt")

# import zipfile
# with zipfile.ZipFile("test.zip","w")as zipf:
#     zipf.write("test1.txt")
#     zipf.write("test2.csv")

# import zipfile
# with zipfile.ZipFile("test.zip","r")as zipfile:
#     file_list=zipfile.namelist()
#     print("content of the zipfile",file_list)

# import zipfile
# with zipfile.ZipFile("datatest.zip","w")as zipfile:
#     zipfile.write("zipffile.txt")
#     zipfile.write("zipffilee.txt")

# import zipfile
# with zipfile.ZipFile("datatest.zip","r")as zipfile:
#     file_list=zipfile.namelist()
#     print("content of the zipfile",file_list)

import zipfile

file_to_extract = 'zipffile.txt'
extraction_path = "C:/Users/Cyber Security/Music"

with zipfile.ZipFile('datatest.zip', 'r') as zipf:
    if file_to_extract in zipf.namelist():
        zipf.extract(file_to_extract, extraction_path)
        print(f"'{file_to_extract}' has been extracted to '{extraction_path}'.")
    else:
        print(f"'{file_to_extract}' does not exist in the ZIP archive.")
