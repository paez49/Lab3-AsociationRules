from model.model import Bill

import pandas as pd
from typing import List, Dict, Any
from collections import defaultdict

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
        if char == "B" or char == ",":
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

def general_info(df:pd.DataFrame,bill_list:List[Bill]) -> None:
    print(f"The total registered transactions on friday was: {df.shape[0]}")
    
    total_count_items = sum(bill.count_items for bill in bill_list)
    max_count_items = max(bill.count_items for bill in bill_list)
    total_bills = len(bill_list)
    mean_products = total_count_items/total_bills
    
    print(f"The total items bought on friday was: {total_count_items}")
    print(f"The total amount of bills on friday was: {total_bills}")
    print(f"The mean of products per bill on friday was: {mean_products}")
    print(f"The max amount of products in a bill on friday was: {max_count_items}")
    
    product_count = defaultdict(int)

    for invoice in bill_list:
        for item in invoice.line_items:
            product = item.name
            product_count[product] += 1
    print("The top 5 most bought products on friday were: ")        
    for i, (product, count) in enumerate(sorted(product_count.items(), key=lambda x: x[1], reverse=True)[:10]):
        print(f"{i+1}. {product}: {count}")
    
    print("The least bought products on friday were: ")
    for index, (product, count) in enumerate(sorted(product_count.items(), key=lambda x: x[1])[:10], start=1):
        print(f"{index}. {product}: {count}")
    
    
    
    print(df.describe())