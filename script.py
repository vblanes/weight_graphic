import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from datetime import date, datetime
import argparse


def plot_graph(init_date: datetime, end_date: datetime, filepath: str ='pesos.csv') -> None:
    df = pd.read_csv(filepath, sep=',')
    df['date_ordinal'] = pd.to_datetime(df['date']).apply(lambda date: date.toordinal())
    df['date'] = pd.to_datetime(df['date'])
    # filter the df by dates
    if init_date is not None:
        df = df[df['date']>=init_date]
    if end_date is not None:
        df = df[df['date']<=end_date]

    sns.set_theme(color_codes=True)
    ax = sns.regplot(
        data=df,
        x='date_ordinal',
        y='weight',
    )
    # Tighten up the axes for prettiness
    ax.set_xlim(df['date_ordinal'].min() - 1, df['date_ordinal'].max() + 1)
    ax.set_ylim(0, df['weight'].max() + 1)
    ax.set_xlabel('date')
    new_labels = [date.fromordinal(int(item)) for item in ax.get_xticks()]
    ax.set_xticklabels(new_labels)

    plt.ylim(90, 110)
    plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Create a graph to track your weight!")
    parser.add_argument('--init', '-i', type=lambda s: datetime.strptime(s, '%d/%m/%Y'), nargs='?')
    parser.add_argument('--end', '-e', type=lambda s: datetime.strptime(s, '%d/%m/%Y'), nargs='?')

    args = parser.parse_args()
    plot_graph(init_date=args.init, end_date=args.end)
        