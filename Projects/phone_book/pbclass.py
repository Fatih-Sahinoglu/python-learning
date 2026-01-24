import os

class PhoneBook:
    file_name="Projects/phone_book/phonebook.txt"
    def __init__(self):
        if not os.path.exists(self.file_name):
            with open(self.file_name,"w",encoding="utf-8") as f:
                pass
    
    def add(self,fname,lname,num):
        with open(self.file_name,"a",encoding="utf-8") as f:
            f.write(f"{fname} {lname} {num}\n")
            f.flush()
            print(f"'{fname} {lname}' added")

    def show(self):
        with open(self.file_name,"r",encoding="utf-8") as f:
            print("Phone Book:")
            print(f.read())
        
    def delete(self,name):
        with open(self.file_name,"r",encoding="utf-8") as f:
            line=f.readlines()
            found=False
        with open(self.file_name,"w",encoding="utf-8") as f:
            for l in line:
                fname,lname,num=l.strip().split(" ")
                if fname!=name:
                    f.write(l)
                else:
                    found=True
                
            if found:
                print(f"'{name}' deleted")
            else:
                print(f"in Phone book '{name}' not exist")   


            