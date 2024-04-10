from utils import const, utils
from model.model import Bill, Transaction


from typing import List, Tuple
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


def to_model() -> Tuple[List[Bill], pd.DataFrame]:
    """Create the Transaction and Bill objects from the .csv file.

    Returns:
        Tuple[List[Bill], pd.DataFrame]: Bills objects and the df with the transactions.
    """
    df = pd.read_csv("output_files/transactions.csv", dtype={"Product Name": str})

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
            if not isinstance(row["Product Name"], float) and math.isnan(
                row["Product Name"]
            ):
                transaction_list.append(trans)

    bill_dict = [b.to_dict() for b in bill_list]
    json_data = json.dumps(bill_dict, indent=4)
    with open("output_files/bills.json", "w") as outfile:
        outfile.write(json_data)

    return bill_list, df


def main() -> None:
    #parser() #Uncomment if you want to read de .dbf again.
    bill_list, df = to_model()
    utils.general_info(df, bill_list)


if __name__ == "__main__":
    main()
