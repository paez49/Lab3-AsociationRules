from utils.data import Parser

def main() -> None:
    parser = Parser()
    
    #parser.parse_data() #Uncomment if you want to read de .dbf again.
    bill_list, df = parser.to_model()
    #parser.show_general_info(df, bill_list)

if __name__ == "__main__":
    main()
