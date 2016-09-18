from random import randint

import pandas as pd


def read_rating_history_dump():
    rating_df = pd.read_csv('GoogleChartsFlask/data/rating_history.csv')
    data = list()
    for index, row in rating_df.iterrows():
        data.append((row[0], row[1], row[2]))
    return data


def read_daily_rating_dump():
    rating_df = pd.read_csv('GoogleChartsFlask/data/daily_rating.csv')
    data = []
    for index, row in rating_df.iterrows():
        data.append((row[0], row[1], row[2], row[3], row[4], randint(3, 5) + randint(1, 10) / 10,
                     randint(3, 5) + randint(1, 10) / 10, randint(3, 5) + randint(1, 10) / 10))
    return data[:10]


def read_daily_rating_dump_all():
    rating_df = pd.read_csv('GoogleChartsFlask/data/daily_rating.csv')
    data = []
    for index, row in rating_df.iterrows():
        data.append((row[0], row[1], row[2], row[3], row[4], randint(3, 5) + randint(1, 10) / 10))
    return data[:10]


def read_rating_hive_dump():
    rating_df = pd.read_csv('hive_query_result', sep='\001', names='a b c d e'.split())
    data = []
    for index, row in rating_df.iterrows():
        data.append((row[0], row[1], row[2], row[3], row[4], randint(3, 5) + randint(1, 10) / 10))
