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

import zipfile
with zipfile.ZipFile("test.zip","r")as zipfile:
    file_list=zipfile.namelist()
    print("content of the zipfile",file_list)