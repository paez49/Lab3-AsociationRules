from utils.utils import measure_time

from mlxtend.frequent_patterns import apriori, fpgrowth, association_rules
from mlxtend.preprocessing import TransactionEncoder

import matplotlib.pyplot as plt
from typing import List
from model.model import Bill
import pandas as pd
import seaborn as sns
import re


@measure_time
def apriori_execution(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
    frequent_itemsets = apriori(df, min_support=threshold, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.8)
    print(rules.head().to_markdown())
    plot_apriori_rules(rules, threshold)


@measure_time
def fp_growth_execution(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
    frequent_itemsets = fpgrowth(df, min_support=threshold, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.8)
    print(rules.head().to_markdown())
    plot_fp_growth_rules(rules, threshold)


def plot_apriori_rules(rules: pd.DataFrame, threshold: float) -> None:
    print("### K = 1")
    apriori_single_consequent_rules = rules[
        rules["consequents"].apply(lambda x: len(x) == 1)
    ]
    print_rules(apriori_single_consequent_rules)

    # Graph
    df_to_graph = apriori_single_consequent_rules.head(30)
    df_to_graph["antecedents"] = df_to_graph["antecedents"].apply(join_frozenset)
    sns.set_style("whitegrid")
    plt.figure(figsize=(12, 6))
    sns.barplot(
        x="antecedents",
        y="confidence",
        data=df_to_graph,
        color="skyblue",
        label="Confianza",
    )
    plt.xticks(rotation=45, ha="right")
    plt.xlabel("Reglas de Asociación")
    plt.ylabel("Valor")
    plt.title("Confianza y Soporte de Reglas de Asociación")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"images/apriori_k1_{threshold}.png")
    print(f"![Apriori K = 1 Threshold {threshold} ](images/apriori_k1_{threshold}.png)")

    print("### K > 1")
    multi_consequent_rules = rules[rules["consequents"].apply(lambda x: len(x) > 1)]
    print_k_greater_than_one(multi_consequent_rules)

    df_to_graph = multi_consequent_rules.head(30)
    df_to_graph["antecedents"] = df_to_graph["antecedents"].apply(join_frozenset)
    sns.set_style("whitegrid")
    plt.figure(figsize=(12, 6))
    sns.barplot(
        x="antecedents",
        y="confidence",
        data=df_to_graph,
        color="skyblue",
        label="Confianza",
    )
    plt.xticks(rotation=45, ha="right")
    plt.xlabel("Reglas de Asociación")
    plt.ylabel("Valor")
    plt.title("Confianza y Soporte de Reglas de Asociación")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"images/apriori_k_g_1_{threshold}.png")
    print(
        f"![Apriori K > 1 Threshold {threshold} ](images/apriori_k_g_1_{threshold}.png)"
    )


def plot_fp_growth_rules(rules: pd.DataFrame, threshold: float) -> None:
    print("### K = 1")
    fp_growth_single_consequent_rules = rules[
        rules["consequents"].apply(lambda x: len(x) == 1)
    ]
    print_rules(fp_growth_single_consequent_rules)
    df_to_graph = fp_growth_single_consequent_rules.head(30)
    df_to_graph["antecedents"] = df_to_graph["antecedents"].apply(join_frozenset)

    sns.set_style("whitegrid")
    plt.figure(figsize=(12, 6))
    sns.barplot(
        x="antecedents",
        y="confidence",
        data=df_to_graph,
        color="skyblue",
        label="Confianza",
    )
    plt.xticks(rotation=45, ha="right")
    plt.xlabel("Reglas de Asociación")
    plt.ylabel("Valor")
    plt.title("Confianza y Soporte de Reglas de Asociación")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"images/fp_growth_k1_{threshold}.png")
    print(
        f"![Apriori K = 1 Threshold {threshold} ](images/fp_growth_k1_{threshold}.png)"
    )

    print("### K > 1")
    multi_consequent_rules = rules[rules["consequents"].apply(lambda x: len(x) > 1)]
    print_k_greater_than_one(multi_consequent_rules)

    df_to_graph = multi_consequent_rules.head(30)
    df_to_graph["antecedents"] = df_to_graph["antecedents"].apply(join_frozenset)
    sns.set_style("whitegrid")
    plt.figure(figsize=(12, 6))
    sns.barplot(
        x="antecedents",
        y="confidence",
        data=df_to_graph,
        color="skyblue",
        label="Confianza",
    )
    plt.xticks(rotation=45, ha="right")
    plt.xlabel("Reglas de Asociación")
    plt.ylabel("Valor")
    plt.title("Confianza y Soporte de Reglas de Asociación")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"images/fp_growth_k_g_1_{threshold}.png")
    print(
        f"![Apriori K > 1 Threshold {threshold} ](images/fp_growth_k_g_1_{threshold}.png)"
    )


def execute_association_rules(bill_list: List[Bill]) -> None:
    transaction_list = []
    for bill in bill_list:
        transaction_list.append([trans.name for trans in bill.line_items])
    encoder = TransactionEncoder()
    encoded_data = encoder.fit(transaction_list).transform(transaction_list)
    df = pd.DataFrame(encoded_data, columns=encoder.columns_)

    thresholds = [0.1, 0.2, 0.25, 0.3, 0.35]
    print("# Association Rules ")
    for threshold in thresholds:
        print(f"## Threshold: {threshold}")
        apriori_execution(df, threshold)
        fp_growth_execution(df, threshold)


def print_rules(rules):
    count = 0
    for _, row in rules.iterrows():
        if count < 3:
            print(f"* {list(row['antecedents'])[0]} -> {list(row['consequents'])[0]}")
            count += 1
        else:
            break


def print_k_greater_than_one(rules):
    count = 0
    for _, row in rules.iterrows():
        if count < 5:
            antecedent = ", ".join(list(row["antecedents"]))
            consequent = ", ".join(list(row["consequents"]))
            print(f"* {antecedent} -> {consequent}")
            count += 1
        else:
            break
    else:
        print("**No results for K greater than 1.**")


def join_frozenset(frozen_set):
    return ", ".join(frozen_set)
