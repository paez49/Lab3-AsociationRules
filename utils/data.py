from model.model import Bill
from utils.const import SPECIAL_CHARS
from utils.utils import measure_time
from model.model import Bill, Transaction


from typing import List, Tuple
import pandas as pd
import math
from collections import defaultdict
import json
import random


class Parser:
    def parse_data(self):
        """Read .dbf file and delete special characters, and convert it to a .csv file."""
        file_path_1 = "files/fc15032024.DBF"
        file_path_2 = "files/fc05042024.DBF"

        with open(file_path_1, "r", encoding="ISO-8859-1") as file:
            text_1 = file.read()
        with open(file_path_2, "r", encoding="ISO-8859-1") as file:
            text_2 = file.read()
        texts = [text_1, text_2]
        i = 0
        last_bill_index = 0
        for i, text in enumerate(texts):
            for char in SPECIAL_CHARS.values():
                text = text.replace(char, "")

            last_bill_index = self.to_csv(text, i, last_bill_index)

    def to_csv(self, text: str, index_file: int, last_bill_index: int) -> int:
        """
        Convert the text of the .dbf to a .csv file with the transactions.
        Args:
            text (str): Raw text of the .dbf file.
            index_file (int): Index file to save the transactions.
            last_bill_index (int): Last bill index in the previous file.

        Returns:
            int: Last bill index written in the file.
        """
        double_space = "  "
        df = pd.DataFrame(
            columns=[
                "Bill Id",
                "Product Name",
                "Count",
                "Tax",
                "Unit Price",
                "Subtotal",
            ]
        )
        while double_space in text:
            text = text.replace(double_space, " ")

        # Obtianing the bill of each line
        bill_list = text.split("\n")[12:]
        i = last_bill_index
        for bill in bill_list:
            transactions = bill.split("")[0:]
            # Obtain the transactions of the bill
            for trans in transactions:
                # Get data from transaction
                trans_info = trans.split()
                if not trans_info:
                    continue
                if (
                    trans_info[2] == "UNID" or trans_info[2] == "UNIDAD"
                ):  # Some transactions have the word "UNID" instead of "UNIDAD"
                    count = int(float(trans_info[3]))
                    tax = 0.0
                else:
                    count = int(float(trans_info[2]))
                    tax = float(trans_info[6])
                unit_price = float(trans_info[4])
                subtotal = float(count * unit_price)
                possible_name = trans_info[
                    10:20
                ]  # Usually in the data, the name began in index of 10
                name = self.get_product_name(possible_name)
                if name != "null" and not self.are_only_numbers(name):
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
            i += 1

        df.to_csv(f"output_files/transactions_{index_file}.csv", index=False)
        return i

    def get_product_name(self, possible_name: List[str]) -> str:
        """Obtain real name of the product from the list of possible names.

        Args:
            possible_name (List[str]): List with possible names of the product.

        Returns:
            str: Name of the product. If the name is not valid, return "null".
        """
        name = []
        if possible_name and possible_name[0].isnumeric():
            possible_name = possible_name[1:]
        for i, char in enumerate(possible_name):
            if char == "B" or char == ",":
                break

            if self.are_only_numbers(char):
                if i + 1 < len(possible_name) and possible_name[i + 1].isalpha():
                    name.append(char)
            else:
                name.append(char)
        if not name:
            return "null"

        return " ".join(name)

    def are_only_numbers(self, text: str) -> bool:
        """Check if the text is only numbers.

        Args:
            text (str): Text to check.

        Returns:
            bool: True if the text is only numbers, False otherwise.
        """
        text_no_spaces = text.replace(" ", "")
        text_no_points = text_no_spaces.replace(".", "")
        return all(char.isnumeric() for char in text_no_points)

    def show_general_info(self, df: pd.DataFrame, bill_list: List[Bill]) -> None:
        """Show general information of the transactions.

        Args:
            df (pd.DataFrame): Dataframe with the transactions.
            bill_list (List[Bill]): List with the Bill objects.
        """
        print("# General Information")
        print(f"The total registered transactions on friday was: {df.shape[0]:,}")

        total_count_items = sum(bill.count_items for bill in bill_list)
        max_count_items = max(bill.count_items for bill in bill_list)
        total_bills = len(bill_list)
        mean_products = total_count_items / total_bills
        total_sells = sum(bill.total for bill in bill_list)
        total_taxes = sum(bill.total_taxes for bill in bill_list)

        print(f"The total items bought on friday was: {total_count_items:,}")
        print(f"The total amount of bills on friday was: {total_bills:,}")
        print(f"The mean of products per bill on friday was: {mean_products:.2f}")
        print(
            f"The max amount of products in a bill on friday was: {max_count_items:,}"
        )
        print(f"The total sells on friday was: {total_sells:,.2f}")
        print(f"The total taxes on friday was: {total_taxes:,.2f}")

        product_count = defaultdict(int)
        print("")
        for invoice in bill_list:
            for item in invoice.line_items:
                product = item.name
                product_count[product] += 1

        most_sell_it = []
        print("## The top 10 most bought products on friday were: ")
        for i, (product, count) in enumerate(
            sorted(product_count.items(), key=lambda x: x[1], reverse=True)[:10]
        ):
            print(f"{i+1}. {product}: {count}")
            most_sell_it.append(product)

        less_sell_it = []
        print("")
        print("## The top 10 least bought products on friday were: ")
        for index, (product, count) in enumerate(
            sorted(product_count.items(), key=lambda x: x[1])[:10], start=1
        ):
            print(f"{index}. {product}: {count}")
            less_sell_it.append(product)

        print(
            "## One of the less bought products was'MAIZ TOSTADO 160GR' and was selled with:"
        )
        selled_with_corn = []
        for bill in bill_list:
            for item in bill.line_items:
                if item.name in "MAIZ TOSTADO 160GR":
                    selled_with_corn = [t.name for t in bill.line_items][0:10]
                    break
        for prod in selled_with_corn:
            print(f"- {prod}")
        self.obtain_combos(bill_list, less_sell_it, most_sell_it)
        # print(df.describe())

    def obtain_combos(
        self, bill_list: List[Bill], less_sell_it: List[str], most_sell_it: List[str]
    ) -> None:
        """Obtain the possible combos of the less bought products with the most bought products.

        Args:
            bill_list (List[Bill]): List with the Bill objects.
            less_sell_it (List[str]): List with the less bought products.
            most_sell_it (List[str]): List with the most bought products.
        """
        dict_combos = {}
        for bill in bill_list:
            for item in bill.line_items:
                if item.name in less_sell_it:
                    posible_combos = set(
                        [t.name for t in bill.line_items if t.name in most_sell_it]
                    )
                    dict_combos[item.name] = list(posible_combos)
        with open("output_files/combos.json", "w") as file:
            json.dump(dict_combos, file, indent=4)

    def to_model(self) -> Tuple[List[Bill], pd.DataFrame]:
        """Create the Transaction and Bill objects from the .csv file.

        Returns:
            Tuple[List[Bill], pd.DataFrame]: Bills objects and the df with the transactions.
        """
        df_1 = pd.read_csv(
            "output_files/transactions_0.csv", dtype={"Product Name": str}
        )
        df_2 = pd.read_csv(
            "output_files/transactions_1.csv", dtype={"Product Name": str}
        )

        df = pd.concat([df_1, df_2], ignore_index=True)
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
                transaction_list.append(trans)

        bill_dict = [b.to_dict() for b in bill_list]
        json_data = json.dumps(bill_dict, indent=4)
        with open("output_files/bills.json", "w") as outfile:
            outfile.write(json_data)

        return bill_list, df
