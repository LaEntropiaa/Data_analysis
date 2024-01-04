import numpy as np
import pandas as pd
import datetime

reddit_data = pd.read_csv(r"data_sets\reddit_data.csv")
del reddit_data["ups"]
del reddit_data["author_flair_css_class"]
del reddit_data["distinguished"]
reddit_data["edited"] = np.where(reddit_data["edited"] > 0, True, False)
reddit_data["controversiality"] = np.where(reddit_data["controversiality"] > 0, True, False)
reddit_data["body"] = pd.Series(reddit_data["body"], dtype=pd.StringDtype())
reddit_data["created_utc"] = reddit_data["created_utc"].apply(lambda x:datetime.datetime.utcfromtimestamp(x) )

print(reddit_data["created_utc"].head(20))




