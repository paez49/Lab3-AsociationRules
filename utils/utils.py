import pandas as pd
from typing import List
import math

def to_csv(text: str) -> str:
    """Convert raw text of .dbf to a .csv file.

    Args:
        text (str): Raw text with transactions and special characters.
    """
    double_space = "  "
    df = pd.DataFrame(
        columns=["Bill Id", "Product Name", "Count", "Tax", "Unit Price", "Subtotal"]
    )
    while double_space in text:
        text = text.replace(double_space, " ")
        
    with open("borrar.txt", "w") as file:
        file.write(text)
    # Obtianing the bill of each line
    bill_list = text.split("\n")[12:]

    for i, bill in enumerate(bill_list):
        transactions = bill.split("")[0:]
        # Obtain the transactions of the bill
        for trans in transactions:
            # Get data from transaction
            trans_info = trans.split()
            if not trans_info:
                continue
            if trans_info[2] == "UNID" or trans_info[2] == "UNIDAD":
                count = int(float(trans_info[3]))
                tax = 0.0
            else:
                count = int(float(trans_info[2]))
                tax = float(trans_info[6])
            unit_price = float(trans_info[4])
            subtotal = float(count * unit_price)
            possible_name = trans_info[
                10:16
            ]  # Usually in the data, the name began in index of 10
            name = get_name(possible_name)

            df = pd.concat(
                [
                    df,
                    pd.DataFrame(
                        {
                            "Bill Id": [i],
                            "Product Name": [name],
                            "Count": [count],
                            "Tax": [tax],
                            "Unit Price": [unit_price],
                            "Subtotal": [subtotal],
                        }
                    ),
                ],
                ignore_index=True,
            )

    df.to_csv("transactions.csv", index=False)


def get_name(possible_name: List[str]) -> str | None:
    """Obtain real name of the product from the list of possible names.

    Args:
        possible_name (List[str]): List with possible names of the product.

    Returns:
        str: Name of the product.
    """
    name = []
    for char in possible_name:
        if char == "B":
            break
        name.append(char)
    if name: 
        if name[0] == "0":
            return "null"
        if name[0].isnumeric():
            name = name[1:] 
    else:
        return "null"
    
    return " ".join(name)
