# data-engineering-greatExpectations
 A demo for Data Engineer for using Great Expectations

---

## Language
* For programming language, this repo use `Python`
* For structured query language, this repo use `PostgreSQL`
* For manage data container, this repo use `Docker`
---

## Data Platform
* Docker
* Airflow
* GreatExpectations
* PostgreSQL
---

## Application
* Visual Studio Code (VSCode)
* DBeaver
* Docker Desktop
---

## Credentials
* Airflow (http://localhost:8080)
	* User: `airflow`
	* Password: `airflow`

* PostgreSQL (localhost:5432)
	* Host: `localhost`
	* Port: `5432`
	* Database: `postgres` 
	* Schema: `postgres`
	* User: `postgres`
	* Password: `KantorAHP123!`
---

## Docker Setup
1. Install Docker Desktop
2. Create a folder called `voting-data-engineering` on your local computer
3. Open VSCode and choose the folder  `voting-data-engineering`
---


## Airflow Setup
1. Install Airflow
---

## GreatExpectations Setup
1. Install GreatExpectations
---

## PostgreSQL Setup
1. Install `PostgreSQL`
2. Install `DBeaver` from this [link](https://dbeaver.io/)
3. Make a PostgreSQL connection on `DBeaver` called `postgres` and the credentials refers from [`Credentials`](https://github.com/skhosyih/data-engineering-greatExpectations/blob/main/README.md#credentials)
4. Make a table called `payment` and load a table from a [payments](https://github.com/skhosyih/data-engineering-greatExpectations/blob/main/voting-data-engineering/data/mart/payments.csv) csv file 
---

## Additional Resources
This repo has several reference sources for working on it:
* [Demo data pipeline with dbt, Airflow, Great Expectations](https://github.com/spbail/dag-stack)
* [Building A Robust Data Pipeline With Great Expectations, dbt and Airflow](https://medium.com/@Sasakky/building-a-robust-data-pipeline-with-great-expectations-dbt-and-airflow-d12b8bba030)
* [Simple data pipeline](https://github.com/goFrendiAsgard/platform-data)
