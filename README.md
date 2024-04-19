
# A demo scraper for atlasobscura

This demo version can scrape data of trips from this website and store the information in PostgreSQL database. You can choose which continent to search trips for and how many pages you want to scrape. In the final result, the information of courses, stories, experiences and ... will be scraped too. 


## Authors

- [@Macan Mehri](https://www.github.com/macanMehri)


## Deployment

To deploy this project run

```bash
   pip install -r requirements.txt
```

Rename sample_settings.py file to local_settings.py. Put your databse informations in it.

```bash
   DATABASE = {
     'name': 'database name',
     'user': 'database user',
     'password': 'database password',
     'host': 'server host maybe localhost',
     'port': 5432
   }
```
## Run Locally

Clone the project

```bash
  git clone https://github.com/macanMehri/AtlasScraperDemo.git
```

Go to the project directory

```bash
  cd atlasobscura_project
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the program

```bash
  python main.py
```


## Features

- Avoid duplicated data
- Ease of use
- Able to search diffrent titles
- Number of pages that will be scraped can change

