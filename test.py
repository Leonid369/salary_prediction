import gs_scrapper as gs
import pandas as pd
import pickle


path = '/Users/saraswathishanmugamoorthy/Documents/chromedriver'

'''
df = gs.get_jobs("data scientist", 15, False,path,15 )
print(df)


pickle_out = open("df.pickle", "wb")
pickle.dump(df,pickle_out)
pickle_out.close()
'''

pickle_in = open("df.pickle", "rb")
df1 = pickle.load(pickle_in)
df1.to_csv('glassdoor_jobs_scrap.csv', index=False)
