# Master's Thesis Online Appendix I: Code
This repository contains the code used in the Master's thesis:

> ***Fine-tuning FinBERT for Stock Return Prediction in Response to Corporate Ad-hoc Disclosures (2021)***

The objective of the thesis is to fine-tune the pre-trained language model FinBERT on a classification task to predict the direction of a company's stock price (positive, negative, neutral) in response to regulatory-induced corporate ad-hoc disclosures.

### Copyright note
The code for fine-tuning FinBERT is adapted from [Araci (2020)](https://github.com/ProsusAI/finBERT). The code for implementing the LSTM benchmark model is adapted from [Radu Fotolescu (2020)](https://gitlab.com/radufotolescu/useful/-/blob/17fe1803f414537a99dd2d210e5581b9bc97bc4f/kaggle/nlp-disaster-tweets/5_baseline_models.ipynb).

## Models
This thesis proposes four models for fine-tuning. They each differ in the type of textual input (headlines or full articles) and whether there are two or three classes to predict. The model names are as follows:

- Headline_3_24_return_adj
- Headline_2_24_return_adj
- News_3_24_return_adj
- News_2_24_return_adj

Each model is trained using FinBERT and the LSTM benchmark model. In total, there are 8 model results reported in the thesis.

## Files
This files contained in this repository were used for different steps in the research framework.

### Data gathering
- `Scrape_URLs.py` creates a list of URLs for all ad-hoc announcements on pages 1 to 7500
- `Detect_language_URLs.py` detects the language of each URL and only keeps articles written in English
- `Scrape_ADHOC.py` opens each URL, scrapes the specified content and saves it in a dataframe

### Data preprocessing
- `Text_preprocessing.py` writes ad-hoc announcements to a local database, performs an SQL query using RegEx to remove disclaimers and preface texts, and saves the cleaned text
- `Labeling.py` joins the `adhoc_clean.csv` and `factset_data.csv` dataframes and replaces the numerical return values with categories indicating whether the stock price increased, decreased, or stayed stable

### Model training
- `FinBERT_finetuning.ipynb` Google Colab notebook for fine-tuning the four proposed models 
- `LSTM_benchmark.ipynb` Google Colab notebook for training a LSTM neural network as benchmark on the same dataset

## Datasets
The two datasets used for this task are located in the folder `data`. 

- `adhoc_clean.csv` contains ad-hoc headlines and full news that have already been cleaned from prefaces and disclaimers
- `factset_data.csv` contains the return data fetched using FactSet Excel Add-In for each combination of datetime and identifier

For creating the final dataset, both dataframes were joined, numerical returns coded into categories (e.g., positive, negative, neutral for the three-class task) and finally filtered depending on the model to be trained. For example, for the model ***News_3_24_return_adj*** the three-class replacement function was applied and all columns except *News* and *Label* were discarded. The same procedure was repeated for all other models and the respective datasets were saved for the training process.
