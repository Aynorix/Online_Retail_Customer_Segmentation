# Online Retail Customer Segmentation

## 📌 Project Overview
This project performs customer segmentation on the **Online Retail II** dataset from the UCI Machine Learning Repository. The goal is to identify distinct customer groups based on their purchasing behavior using unsupervised machine learning techniques.

We utilize the **RFM (Recency, Frequency, Monetary)** framework to engineer features and compare two popular clustering algorithms: **K-Means** and **DBSCAN**.

## 📁 Project Structure
```text
online-retail-segmentation/
│
├── data/
│   ├── raw/               # Contains: online_retail_II.csv
│   └── processed/         # Contains: rfm_data.csv
│
├── src/
│   ├── utils.py           # Plot saving pipeline
│   └── preprocessing.py   # Cleaning and RFM engineering logic
│
├── notebooks/
│   ├── 01_eda.ipynb           # Exploratory Data Analysis
│   ├── 02_dim_reduction.ipynb # PCA & t-SNE Visualizations
│   ├── 03_clustering.ipynb    # K-Means & DBSCAN Implementation
│   └── 04_comparison.ipynb    # Model Performance & Result Analysis
│
├── plots/                 # Exported visualizations (PNG)
│   ├── eda/
│   ├── dim_reduction/
│   └── clustering/
│
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation