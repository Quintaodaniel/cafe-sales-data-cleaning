# Data Cleaning Project: Cafe Sales 

This project demonstrates a complete, step-by-step data cleaning process applied to a raw cafe sales dataset. The primary goal is to transform the "dirty" data into a clean, well-structured, and reliable dataset ready for analysis.

## Objective

The main objective is to prepare the `dirty_cafe_sales.csv` file for exploratory data analysis (EDA) by addressing common data quality issues.

## Cleaning Process

The entire process is documented within the Jupyter Notebook. The key steps include:

1.  **Initial Diagnosis:** First look at the data to identify issues like missing values, incorrect data types, and inconsistencies.
2.  **Adjusting Data Types:** Converting columns to their correct types (e.g., `object` to `float` and `datetime`).
3.  **Standardizing Errors:** Replacing varied representations of missing or erroneous data (like `UNKNOWN`, `ERROR`, ` `) with a standard `NaN`.
4.  **Handling Null Values:** Applying different strategies for nulls based on the column's importance (removing rows for essential columns, imputing for contextual ones).
5.  **Data Validation:** Re-calculating derived columns (like `Total Spent`) to ensure data integrity.
6.  **Duplicate Check:** Verifying and removing any duplicate entries.
7.  **Saving the Clean Data:** Exporting the final, clean DataFrame to a new CSV file.

## Tech Stack

* **Python**
* **Pandas**
* **NumPy**
* **Jupyter Notebook**

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Quintaodaniel/cafe-sales-data-cleaning.git](https://github.com/Quintaodaniel/cafe-sales-data-cleaning.git)
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd cafe-sales-data-cleaning
    ```
3.  **Install the required libraries:**
    ```bash
    pip install pandas numpy jupyter
    ```
4.  **Open the Jupyter Notebook:**
    ```bash
    jupyter notebook
    ```
    Then, open and run the `.ipynb` file to see the complete cleaning process.

## Outcome

The final output is the `cleaned_cafe_sales.csv` file located in the `data/processed` directory. This dataset is consistent, properly formatted, and ready for analysis and visualization.