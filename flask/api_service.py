
import flask
from sqlalchemy import create_engine
import psycopg2
from utils import fill_database

app = flask.Flask(__name__)

#add retry logic 
engine = create_engine('postgresql://postgres:postgres@db:5432/sales', echo=False)

#get the list of properties sold within user provided price range
#low price and high price bounds required
@app.route('/api/get-properties-sold', methods=['POST'])
def get_properties_sold_between():

	low = flask.request.json["low"]
	high = flask.request.json["high"]

	#check values
	try:
		low = int(low)
		high = int(high)

		print("HIGH ", high, " LOW ", low)

	except:
		return 'bad request!', 400

	addresses = engine.execute('''SELECT "ADDRESS", "index" FROM manhattan WHERE "SALE PRICE" BETWEEN {} AND {};'''.format(low,high)).fetchall()

	#print(addresses)
	if addresses == []:
		return flask.jsonify({'addresses': []})
	else: 
		addresses, indexs = zip(*addresses)
		return flask.jsonify({'addresses': list(addresses)})


if __name__ == "__main__":
	fill_database()
	app.run(host='0.0.0.0',debug=True,port=6000)

