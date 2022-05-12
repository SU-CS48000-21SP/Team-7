import os.path
from asyncio.windows_events import NULL

def sort_comments(game_name):


    save_path = r"C:\Users\atabe\GitRepos\cs48000-group7"
   
    app_name1 = "positive_comments"
    app_name2 = "negative_comments"

    completeName1 = os.path.join(save_path, app_name1+".txt") 
    completeName2 = os.path.join(save_path, app_name2+".txt") 
    completeName3 = os.path.join(save_path, game_name+".txt")
    
    f1 = open(completeName1, "a", encoding="utf-8")
    f2 = open(completeName2, "a", encoding="utf-8")
    f3 = open(completeName3, "r", encoding="utf-8")       
    lines = f3.readlines()
    
    for line in lines:
        
 
        print(line)
        inp = input("Enter 1 for positive, Enter 0 for negative, Enter 2 to end:")
        print(inp)
    
        if inp == "0" :
            f1.write(line)
        if inp == "1" :
            f2.write(line)
        if inp == "2" :
            break


    f3.close()
    f1.close()
    f2.close()
    


if __name__ == '__main__':
    
    sort_comments("Gumslinger")
    print("-------------DONE------------------------")