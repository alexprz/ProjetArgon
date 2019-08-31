# ProjetArgon
**Why is this project on GitHub ?**

This project has been made as part of our lessons in ENPC school.
It is not made to be reused as it does not bring anything particular
to the community (it is not a package).
Why is it on GitHub then ?
There may be 2 reasons for this project to be hosted on GitHub:
- To collaborate with my project partner (if any).
- To be able to show some projects and code to recruiters.

With this in mind, here are the files to look at.

**Where to look at ?**

```data_cleaning/```  
This folder contains files which clean the raw data. 

```algo/demand_forecasting/random_forest/```  
This folder contains files which prepare the data for the training (```transform_features.py```), train the Random Forest model (```random_forest.py```) and estimate the demand with the trained model (```compute_demand.py```).

## Installation
Install dependencies by running :

```
pip install -r requirements.txt
```

Create the folders `data/` and `data/data_raw/`:
```
mkdir data
mkdir data/data_raw
```

Move the files Articles.csv, Sales.csv, Stock.csv, Market_Data.csv, Location.csv in the folder `data/data_raw/`,
```
mv /path/to/the/file ./data/data_raw/
```

### Cleaning of the dataset

Clean the dataset by running :
```
cd data_cleaning
python main.py
```

#### Operations made on the raw dataset
In the file `Articles.csv`, we removed the column(s):
```
Budget Class
```

In the file `Location.csv`, we removed the comumn(s):
```
isWFJactive
```

In the file `Stock.csv`, we replaced `Zone (BR Vision)` by `Zone`

In the file `Stocks.csv`, we replaced `ITEM_CODE` by `Item_Code`.

In all the files, we removes spaces and parentheses from the column names.

### Making joins
Once data are cleaned, make all joins by running :
```
python make_joins.py
```
