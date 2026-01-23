import time
#flush() for dont wait at buffer write direct
with open("File_Handling/lesson38/write.txt","w",encoding="utf-8") as f:

    for i in range(10): #for visualize
        f.write(f"{i+1}. log\n")
        f.flush()
        time.sleep(1)

