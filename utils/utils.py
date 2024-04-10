from model.model import Bill

import pandas as pd
from typing import List
from collections import defaultdict
import json

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

    df.to_csv("output_files/transactions.csv", index=False)


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


def general_info(df: pd.DataFrame, bill_list: List[Bill]) -> None:
    print(f"The total registered transactions on friday was: {df.shape[0]:,}")

    total_count_items = sum(bill.count_items for bill in bill_list)
    max_count_items = max(bill.count_items for bill in bill_list)
    total_bills = len(bill_list)
    mean_products = total_count_items / total_bills
    total_sells = sum(bill.total for bill in bill_list)
    total_taxes = sum(bill.total_taxes for bill in bill_list)

    print(f'The total items bought on friday was: {total_count_items:,}')
    print(f"The total amount of bills on friday was: {total_bills:,}")
    print(f"The mean of products per bill on friday was: {mean_products:.2f}")
    print(f"The max amount of products in a bill on friday was: {max_count_items:,}")
    print(f"The total sells on friday was: {total_sells:,.2f}")
    print(f"The total taxes on friday was: {total_taxes:,.2f}")

    product_count = defaultdict(int)
    print("")
    for invoice in bill_list:
        for item in invoice.line_items:
            product = item.name
            product_count[product] += 1

    most_sell_it = []
    print("The top 10 most bought products on friday were: ")
    for i, (product, count) in enumerate(
        sorted(product_count.items(), key=lambda x: x[1], reverse=True)[:10]
    ):
        print(f"{i+1}. {product}: {count}")
        most_sell_it.append(product)

    less_sell_it = []
    print("")
    print("The top 10 least bought products on friday were: ")
    for index, (product, count) in enumerate(sorted(product_count.items(), key=lambda x: x[1])[:10], start=1):
        print(f"{index}. {product}: {count}")
        less_sell_it.append(product)

    print(
        "One of the less bought products was'MAIZ TOSTADO 160GR' and was selled with:"
    )
    for bill in bill_list:
        for item in bill.line_items:
            if item.name in "MAIZ TOSTADO 160GR":
                print([t.name for t in bill.line_items][0:10])
                break

    obtain_combos(bill_list, less_sell_it,most_sell_it)
    print(df.describe())


def obtain_combos(bill_list: List[Bill], less_sell_it: List[str], most_sell_it: List[str]) -> None:
    dict_combos = {}
    for bill in bill_list:
        for item in bill.line_items:
            if item.name in less_sell_it:
                posible_combos = set([t.name for t in bill.line_items if t.name in most_sell_it])
                dict_combos[item.name] = list(posible_combos)
    with open('output_files/combos.json', 'w') as file:
        json.dump(dict_combos, file,indent=4)
