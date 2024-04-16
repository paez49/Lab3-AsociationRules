from utils.data import Parser
from utils.asociation_rules import execute_association_rules
def main() -> None:
    parser = Parser()
    
    parser.parse_data() #Uncomment if you want to read de .dbf again.
    bill_list, df = parser.to_model()
    parser.show_general_info(df, bill_list)
    execute_association_rules(bill_list)

if __name__ == "__main__":
    main()
