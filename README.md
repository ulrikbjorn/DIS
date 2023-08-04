# DiS Project
##### Ulrik Bjørn Meelby, rgt545

## BlueChip Stock Trader
I have implemented a stock portfolio DBMS using Flask for the web layer and PostgreSQL for the database layer. The web-app allows an investor to manage (view and trade) a portfolio of stocks using simulated price data.
 
## How to compile
Besides PostgreSQL and Flask, the necessary Python packages can be found in requirements.txt. After the required dependencies have been installed the database can be created by executing 'createdb bluechip' in the terminal. Load the database schemes by executing 'psql bluechip < schema.sql' and 'psql bluechip < schema_ins.sql' The settings of the database can be modified in __init__.py.

## How to run & interact
To run the web-app execute 'python3 run.py' in the terminal, which will host the web-app from http://127.0.0.1:5000. 
The database consists of 4 users that for simplicity sake share the same password (memestock). The user-id's are (3000,3001,3002,3003). 
Each investor owns a portfolio of shares and is allowed to carry out trades. 

## Functionality & Limitations
Due to unforseen technical struggles, I failed to extend the functionality beyound logging-in, viewing the portfolio and placing orders. The web-app is able to interact with the datapase and update the portfolio, but there are no checks in place to avoid over-spending and buying non-existing shares. Furthermore, I have not implemented a consolidated view of the portfolio which is unelegant to say the least and the selling of shares is not fully supported.

I have relied on the provided banking template and modified it to suit my needs, but I underestimated the time needed to get familiar with the codebase. One of the main features I did get to implement was the Profit/Loss metric, which for each individual purchase of shares calculates the difference between the purchase price and the current price multiplied by the number of shares owned. I really put a lot of effort into the project, and I sincerely hope that it is sufficient. 

## E/R Diagram
I updated the E/R Diagram to reflect the actually implemented features rather than my initial ambitions.  




