#! /usr/bin/env python3

from datetime import datetime
import calendar
from functools import wraps
import argparse
import pandas as pd
import os
import praw
import sqlite3
import time
import sys

TIMESTAMP_A = 1504657288
TIMESTAMP_B = 1507249288

# DEBUG


def timing(method):
    @wraps(method)
    def timed(*args, **kwargs):
        time_s = time.time()

        # TODO Write comment
        result = method(*args, **kwargs)

        time_e = time.time()

        print("Elapsed time: {0}".format(time_s - time_e))

        return result

    # TODO Write comment
    return timed


def format_data(submissions, subreddit=None):
    for data in submissions:
        yield data.id, subreddit, data.title, data.ups, data.url

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # For Python versions prior to 3.0

config = ConfigParser()

# Ignore the possibility of this failing
config.read("../config.ini")

reddit = praw.Reddit(
    # [client_data]
    client_id=config["client_data"]["client_id"],
    client_secret=config["client_data"]["client_secret"],
    user_agent=config["client_data"]["user_agent"],

    # [credentials]
    username=config["credentials"]["username"],
    password=config["credentials"]["password"]
)

if __name__ == "__main__":
    is_present = os.path.exists(config["DEFAULT"]["file"])
    subreddits = config["input"]["subreddits"].split('\n')
    parser = argparse.ArgumentParser(description='Grab posts by time')
    parser.add_argument('--store', default='csv',
                        help="Choose db or csv (db = database)")
    parser.add_argument('--subreddit', default='python',
                        help="Choose subreddit to search")
    parser.add_argument('--output', default='test.csv',
                        help="Name of output file")
    parser.add_argument('--time1', default=1507608000,
                        help="Timestamp A format month/day/year")
    parser.add_argument('--time2', default=1508212800,
                        help="Timestamp B format month/day/year")
    parser.add_argument('--print', default=False,
                        help="Print first 5 posts")
    args = parser.parse_args()

    if not isinstance(args.time1, int) or not isinstance(args.time2, int):
        month1, day1, year1 = args.time1.split('/')
        month2, day2, year2 = args.time2.split('/')
        dt1 = datetime(int(year1), int(month1), int(day1))
        dt2 = datetime(int(year2), int(month2), int(day2))
        t1 = calendar.timegm(dt1.timetuple())
        t2 = calendar.timegm(dt2.timetuple())
    else:
        t1, t2 = args.time1, args.time2

    if args.store == 'csv':
        subreddit = reddit.subreddit(args.subreddit)
        submissions = subreddit.submissions(t1, t2)
        if args.print:
            b = [x for index, x in enumerate(submissions) if index < 6]
            print(b)
            sys.exit()
        data = [[data.id, args.subreddit,
                 data.title, data.ups, data.url, data.created_utc] for data in submissions]
        df = pd.DataFrame(data,
                          columns=['id', 'subreddit', 'title', 'ups', 'url', 'created_utc'])
        df.to_csv(args.output, index=False)
    else:
        with sqlite3.connect(config["DEFAULT"]["file"]) as connect:
            cursor = connect.cursor()
            if is_present is not True:
                cursor.execute('''
                    CREATE TABLE `submissions` (
                        `id` PRIMARY KEY,
                        `subreddit`,
                        `title`,
                        `ups`,
                        `url`
                    )
                ''')
                # TODO Write comment
                for subreddit in [reddit.subreddit(name) for name in subreddits if name]:
                    submissions = subreddit.submissions(TIMESTAMP_A, TIMESTAMP_B)
                    # Prepare the collected data and submit it
                    cursor.executemany('''
                            INSERT OR IGNORE INTO `submissions`
                            VALUES (?, ?, ?, ?, ?)
                    ''', format_data(submissions, subreddit.display_name))
