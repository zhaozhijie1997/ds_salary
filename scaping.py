import scraper as sp
import pandas as pd
df = sp.get_jobs("data scientist", 10, False,2)
df.to_csv('Details.csv',index=False)