
# Carver Edison Project Ryan Brandt 

## How to run 

1.Download the repository

2.From the root folder run the command: 

	docker-compose up 

The following chain of events will happen: 

1. Posgres starts and inicializes a database 
2. The manhattan excel data is downloaded and inserted into the database 
3. A flask api service is started on port 6001


## How to query

Send a post requests to the endpoint: http://localhost:6001/api/get-properties-sold

Example post json: 

	{ "low": "0", "high": "1000000000" }


## Average Sale Price By Year

![Alt text](avg.PNG?raw=true "Title")
