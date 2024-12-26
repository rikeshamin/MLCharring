![Python](https://img.shields.io/badge/Python-blue?logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-blue?logo=postgresql&logoColor=white)
![Structural Engineering](https://img.shields.io/badge/Structural%20Engineering-brightgreen)
![Optimization](https://img.shields.io/badge/Bayesian%20Optimization-orange)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-yellow?logo=machine-learning&logoColor=white)
![Statistics](https://img.shields.io/badge/Statistics-lightgrey?logo=chart-bar&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)

# Predicting the Average Charring Rate of Mass Timber Using Data-Driven Methods for Structural Calculations

MLCharring is a collection of data-driven models developed to predict the charring rate of timber in fire scenarios, providing assistance for structural engineering calculations. The dataset, [VAQT](https://zenodo.org/records/14238389) , aggregates timber furnace tests conducted in an ISO 834 fire environment, offering a robust foundation for training advanced statistical and machine learning models. These models are designed to accurately estimate the average charring rate of mass timber, supporting fire-safe and efficient structural design practices in the built environment. 

--- 
## Setting up VAQT on your local machine

Follow these steps to set up the VAQT dataset:

1. [Download VAQT](https://zenodo.org/records/14238389) from Zenodo. 
2. Install Microsoft Access or migrate to open database platform (e.g., PostgreSQL, MySQL)
3. Open the `Timber Charring fe` file. 
4. Navigate to the `External Data` tab and select:
     - `New Data Source` -> `From Database` -> `Access`.
5. Choose `Link to data source...` and select the `Timber Charring be` file.
6. In the dialog box,  press `SELECT ALL` and then click `OK`.
7. **VAQT is now linked and ready to usee**

---
## Running models locally

1. Ensure Python is installed and set up a virtual environment. Guidance can be found here:
   - [Python Installation Guide](https://www.python.org/downloads/)
   - [Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
2. Run `pip install -r requirements.txt` to install all dependencies. 
3. Ensure the model `statistical_model.pkl` is in the same directory as `ml_charring_statistical.py`.
4. Execute the script using:
   ```bash
   python ml_charring_statistical.py
   ```
6. Provide the input dataset to the model. 
7. The terminal will output the predicted charring rates(s):
   ```bash
   Charring Rate: [0.71605273]
   ``` 

If you encounter any problems, please create an issue directly in this repository or email [myself](rikamin95@gmail.com) or [Prof. Guillermo Rein](g.rein@imperial.ac.uk).

---

### Additional Resources:
- [Publication DOI](https://doi.org/10.1007/s10694-024-01593-x)
- [Hazelab - Imperial College London](https://www.imperial.ac.uk/hazelab)
--- 
### To Do (when i have some more time):
* Update VAQT compatability to open databases 
* Upload deep learning models (currently on my own server)
* Implement MLOps for containerization and deployment (Docker and Kubernetes)
---




