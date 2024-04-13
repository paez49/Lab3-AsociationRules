from utils.utils import measure_time

from mlxtend.frequent_patterns import apriori, fpgrowth, association_rules
from mlxtend.preprocessing import TransactionEncoder

from typing import List
from model.model import Bill
import pandas as pd


@measure_time
def apriori_execution(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
    frequent_itemsets = apriori(df, min_support=threshold, use_colnames=True)
    rules = association_rules(
        frequent_itemsets, metric="confidence", min_threshold=threshold
    )
    print(rules.head().to_markdown())


@measure_time
def fp_growth_execution(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
    frequent_itemsets = fpgrowth(df, min_support=threshold, use_colnames=True)
    rules = association_rules(
        frequent_itemsets, metric="confidence", min_threshold=threshold
    )
    print(rules.head().to_markdown())


def execute_association_rules(bill_list: List[Bill]) -> None:
    transaction_list = []
    for bill in bill_list:
        transaction_list.append([trans.name for trans in bill.line_items])
    encoder = TransactionEncoder()
    encoded_data = encoder.fit(transaction_list).transform(transaction_list)
    df = pd.DataFrame(encoded_data, columns=encoder.columns_)

    thresholds = [0.2, 0.25, 0.3, 0.35]
    print("# Association Rules ")
    for threshold in thresholds:
        print(f"## Threshold: {threshold}")
        apriori_execution(df, threshold)
        fp_growth_execution(df, threshold)
