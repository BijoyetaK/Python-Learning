import os
datafolder = 'Data'
filename = 'Article.txt'

#Prompt to enter the text to search
input_txt_search = input("Enter the text you wish to search : ")
input_txt_search = input_txt_search.lower()

# Set path for file
#txtfilepath = os.path.join("Data", "Article.txt")
txtfilepath = "{0}/{1}/{2}".format(os.getcwd(), datafolder, filename)
found = False
#Open the textfile

with open(txtfilepath, encoding = 'utf-8') as textfile:
       lines = textfile.readlines()
       for line in lines:
           #if line.find(input_txt_search) != -1:
           if input_txt_search in line.lower():
               found = True
               print("The string exists in the file " , input_txt_search)
               print("The string is in Line Number ", lines.index(line)) 
               print("Line :" ,line)           
if not found:
    print("Text not found")

                

# with open(txtfilepath, 'r', encoding = 'utf-8') as fp:
#      for ln_no, line in enumerate(fp):
#           if input_txt_search in line:
#                print("The string exists in the file " , input_txt_search)
#                print("The string is in Line Number ", ln_no) 
#                print("Line :" ,line)
#                break            
#           else:
#                print("Text not found")

      
       
    #print(contents)
    #for line in textfile:
    #   print(line.strip())


       