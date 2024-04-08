from utils import const,utils
def parse():
    file_path = "files/fc15032024.DBF"
    with open(file_path, 'r',encoding='ISO-8859-1') as file:
        text = file.read()
    for char in const.SPECIAL_CHARS.values():
        text = text.replace(char,"")
        
    text = text.replace("\x00"," ")
  
    
    text = utils.to_csv(text)
    
    

def main() -> None:
    parse()
     
if __name__ == "__main__":
    main()