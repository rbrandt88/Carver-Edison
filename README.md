
# Carver Edison Project Ryan Brandt 

## Pre 

The tasks on my cluster in Amazon ECS are perpetually stuck in a pending state. The should have converted to running. I was not able to figure out why in the amount of time. I apologize for this. 

Even though I wasn't able to host the container on AWS in the time, I would like to thank you for considering me. I will persue learning more about AWS in my free time. 


Python code: 3 hours

Learning Docker: 4 hours

Learning and issues with the container deployment on AWS: 5 hours + 

## How to run 

1. Download the repository

2. From the root folder run the command: 

		docker-compose up 

The following chain of events will happen: 

1. docker-compose.yml will be executed
2. Postgres will start and inicialize a database 
3. The api service will wait for the database to become active
4. After the all clear, the manhattan excel data will be downloaded and inserted into the database 
5. A flask api service will start on port 6001

## How to query

Send a post request to the endpoint: http://localhost:6001/api/get-properties-sold

Example post request json: 

	{ "low": "0", "high": "1000000000" }


## Other Information

utils.py contains fill_database(). The manhattan excel data will be downloaded and inserted into the database 

utils.py contains the plot function show_avg_sale_by_year(). It queries the database and plots the information in the bar a bar graph. 

## Average Sale Price By Year

![Alt text](avg.PNG?raw=true "Title")
