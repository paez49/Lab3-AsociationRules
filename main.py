from utils import const, utils
from model.model import Bill, Transaction
import pandas as pd
import json
import math
def parser():

    file_path = "files/fc15032024.DBF"

    with open(file_path, "r", encoding="ISO-8859-1") as file:
        text = file.read()

    for char in const.SPECIAL_CHARS.values():
        text = text.replace(char, "")

    text = utils.to_csv(text)


def to_model():
    df = pd.read_csv("transactions.csv",dtype={"Product Name":str})
    
    bill_list = []
    transaction_list = []

    bill_id = int(df["Bill Id"][0])

    for _, row in df.iterrows():

        new_bill_id = row["Bill Id"]
        trans = Transaction(
            row["Product Name"],
            row["Count"],
            row["Unit Price"],
            row["Tax"],
            row["Subtotal"],
            )
        
        if bill_id == new_bill_id:
            if row["Product Name"]:
                transaction_list.append(trans)
        else:
            
            bill = Bill(bill_id, transaction_list)
            bill_list.append(bill)
            bill_id = new_bill_id
            transaction_list = []
            if not isinstance(row["Product Name"],float) and math.isnan(row["Product Name"]):
                transaction_list.append(trans)
        
    bill_json = [b.to_dict() for b in bill_list]
    json_data = json.dumps(bill_json, indent=4)
    with open("bills.json", "w") as outfile:
        outfile.write(json_data)
def main() -> None:
    #parser() #Uncomment if you want to read de .dbf again.
    to_model()


if __name__ == "__main__":
    main()
