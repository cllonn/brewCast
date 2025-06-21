# BrewCast  
**Forecasting Success in the Coffee Business**

BrewCast is a predictive machine learning solution developed to assist small coffee shop owners in forecasting successful business days. By leveraging weather patterns and historical sales data, BrewCast empowers data-driven decisions for resource optimization, marketing timing, and staffing.

---

## Project Summary

**Meet Maryam**, an aspiring coffee shop owner navigating the challenges of demand forecasting, resource planning, and staffing. BrewCast helps her predict successful sales days using a blend of environmental (weather) and temporal (time/date) factors.

With over **600 days of real-world data**, BrewCast was trained to classify business days as successful or not, helping Maryam plan proactively instead of reactively.

---

## Objectives

- Develop a predictive ML model to identify profitable business days.
- Provide actionable insights to optimize:
  - **Staffing**
  - **Inventory**
  - **Promotion timing**
- Enhance efficiency and profitability for small businesses.

---

## Model & Methodology

### 🔢 Dataset Features
- `date`  
- `avg_temperature`  
- `humidity`  
- `rain`  
- `weekend`  
- `number_of_customers`  
- `coffee_ordered`  

> Data sources:  
> - Internal coffee shop sales (over 2 years)  
> - Weather data from NMC & Weather Underground

### Preprocessing
- Removed holidays, Ramadan, and shop-closed days
- Handled missing values and outliers
- Aligned and merged timestamped datasets
- One-hot encoding for categorical features
- Normalization for numerical values

### Model Selection
- **Random Forest Classifier**  
- Chosen for its ability to handle non-linear relationships and interpretability

### Evaluation
- **98.5% validation accuracy**
- Evaluated using accuracy and feature importance
- Top features: temperature, rain, weekend flag, and customer count

---

## Results

- Achieved **98%+ accuracy** on validation data
- Visualized key trees for interpretability
- Enabled **real-time predictions** for resource planning
- Suggested offer timings and staff scheduling based on forecast

---

## Business Impact

BrewCast helps small businesses:
- Anticipate peak days for promotions
- Avoid overstaffing on slow days
- Make inventory decisions with confidence

---

## Tech Stack

| Area              | Tools Used              |
|------------------|-------------------------|
| Data Preprocessing | Python (pandas, NumPy) |
| Machine Learning | RandomForestClassifier (sklearn) |
| Visualization    | matplotlib, seaborn     |
| Dataset Sources  | CSV + API-based weather data |

---

## Visuals

### Poster  
![BrewCast Poster](assets/brewcast_poster.png)

### System Overview  
![Model Diagram](assets/brewcast_diagram.png)

> *(Ensure the images are added to an `assets/` folder in your repo)*

---

## Files in This Repo
- `brewcast_ppt.pdf` – Full presentation
- `brewcastposter.pdf` – Final project poster
- `coffee_shop_sales_dataset_updated.csv` – Cleaned dataset
- `model_training.ipynb` – ML model training and evaluation

---

## Authors

- **Sara Almarzooqi** – Model Evaluation & Data Collection
- **Saleha Alameri** – Data Collection & Cleaning  
- **Safa Baalfaqih** – Model Evaluation & Testing

---

## Future Enhancements

- Deploy model as a web-based dashboard or mobile app
- Integrate live weather API for real-time predictions
- Expand to support other F&B businesses

---

## References

- UAE National Meteorological Center (NMC)
- Weather Underground API
- Scikit-learn documentation

---

## Links

- [Presentation PDF](./BrewCastppt.pdf)  
- [Poster PDF](./BrewcastPoster.pdf)  
- [Dataset CSV](./coffee_shop_sales_dataset_updated.csv)

---

