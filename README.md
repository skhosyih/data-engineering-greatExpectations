# data-engineering-greatExpectations
 A data quality demo for Data Engineer using Great Expectations

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

* PostgreSQL (`localhost:5432`)
	* Host: `localhost`
	* Port: `5432`
	* Database: `postgres` 
	* Schema: `postgres`
	* User: `postgres`
	* Password: `KantorAHP123!`
---

## File Management Setup
1. Create a folder called **`voting-data-engineering`** on your local computer
2. Open VSCode and choose the folder  **`voting-data-engineering`**
3. Create a several folders in the folder **`voting-data-engineering`** named:
	*  `data`: Contains data folders that can be used to perform data quality 
	*  `etl`: Contains the data platform folder which is used to perform data quality along with the platform setup
4. Load `mart` folder that contains:
   * `customers` table
   * `orders` table
   * `payments` table
5. On this case, only use `payments` table
6. Create a several folders in the folder `etl` named:
   * `airflow`: For orchestrate data pipeline and data quality
   * `gx`: For check the data quality

## Docker Setup
1. Install Docker Desktop and Open `Docker Desktop Installer.exe`
2. When prompted, ensure the Use WSL 2 instead of Hyper-V option on the Configuration page is selected or not depending on your choice of backend
3. Follow the instructions on the installation wizard to authorize the installer and proceed with the install
4. When the installation is successful, select Close to complete the installation process
---

## Airflow Setup and Run
1. Open VSCode and choose the folder **`voting-data-engineering/etl/airflow`** by fetching `docker-compose.yaml` on the terminal. Insert this code in terminal:
```
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.6.3/docker-compose.yaml'
``` 
2. Make a `./dags`, `./logs`, `./plugins`, `./config` dir and set the user 
```
mkdir -p ./dags ./logs ./plugins ./config
echo -e "AIRFLOW_UID=$(id -u)" > .env
```
3. Initialize the database on folder **`voting-data-engineering/etl/airflow`** using this command:
```
docker compose up airflow-init
```
4. Run the airflow on folder **`voting-data-engineering/etl/airflow`** using this command:
```
docker compose up
```
---

## GreatExpectations Setup and Run
1. Install Great Expectations, Great Expectations, and also dbt for airflow for Airflow in this command:
```
pip install great-expectations
pip install airflow-provider-great-expectations
pip install airflow-dbt
```
2. Create `.env`, `Dockerfile`, `requirements.txt` files on folder **`voting-data-engineering/etl/airflow`** based on this [link](https://github.com/skhosyih/data-engineering-greatExpectations/tree/main/voting-data-engineering/etl/airflow) to set requirement for insert the GreatExpectations and also dbt
3. Set the `docker-compose.yaml` based on this [link](https://github.com/skhosyih/data-engineering-greatExpectations/blob/main/voting-data-engineering/etl/airflow/docker-compose.yaml)
4. GreatExpectations always run if you initialize the GreatExpectations package on Jupyter Notebook files, or based set on `schedule_interval` in Airflow  
---

## PostgreSQL Setup and Run
1. Install `PostgreSQL`
2. Install `DBeaver` from this [link](https://dbeaver.io/)
3. Make a PostgreSQL connection on `DBeaver` called `postgres` and the credentials refers from [`Credentials`](https://github.com/skhosyih/data-engineering-greatExpectations/blob/main/README.md#credentials)
4. Make a table called `payment` and load a table from a [payments](https://github.com/skhosyih/data-engineering-greatExpectations/blob/main/voting-data-engineering/data/mart/payments.csv) csv file 
5. `PostgreSQL` always run in the background
---

## Additional Resources
This repo has several reference sources for working on it:
* [Demo data pipeline with dbt, Airflow, Great Expectations](https://github.com/spbail/dag-stack)
* [Building A Robust Data Pipeline With Great Expectations, dbt and Airflow](https://medium.com/@Sasakky/building-a-robust-data-pipeline-with-great-expectations-dbt-and-airflow-d12b8bba030)
* [Simple data pipeline](https://github.com/goFrendiAsgard/platform-data)
