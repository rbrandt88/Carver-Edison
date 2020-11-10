
import pandas as pd
import numpy as np 
import urllib.request
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import psycopg2
plt.style.use('ggplot') 

engine = create_engine('postgresql://postgres:postgres@db:5432/sales', echo=False)

def fill_database():
	print('FILL DATABASE')
	#download excel sheet
	urllib.request.urlretrieve('https://www1.nyc.gov/assets/finance/downloads/pdf/rolling_sales/rollingsales_manhattan.xls', 'manhattan.xls')
	
	#parse
	df = pd.read_excel('manhattan.xls')
	col_names =  df.iloc[3]
	df = df.iloc[4:]
	df.columns = col_names
	df.reset_index(drop=True,inplace=True)
	print(df.head(5))

	#insert into sql table
	df.to_sql('manhattan', con=engine, if_exists='replace', index=True)
	engine.execute("ALTER TABLE manhattan ADD PRIMARY KEY (index)")



def show_avg_sale_by_year():

	avgs = engine.execute('''SELECT date_part('year', "SALE DATE") as year, avg("SALE PRICE") FROM manhattan group by date_part('year',"SALE DATE");''').fetchall()
	
	dates, prices = zip(*avgs)

	dates = [round(d) for d in dates]
	prices = [round(p) for p in prices]
	#print(dates,prices)

	fig, ax = plt.subplots(figsize =(16, 9))

	y_pos = [i for i, _ in enumerate(dates)]

	ax.barh(y_pos, prices, color='green')
	ax.set_yticks(y_pos) 
	ax.set_yticklabels(dates)

	for i in ax.patches: 
		plt.text(i.get_width()+0.2, i.get_y()+0.5,  
             str(round((i.get_width()), 2)), 
             fontsize = 12, fontweight ='bold', 
             color ='grey') 

	ax.set_title('Average Price of Houses in Manhattan by Year')
	ax.set_xlabel("Average Price")
	ax.set_ylabel("Year")

	plt.show()


#show_avg_sale_by_year()
#fill_database()



