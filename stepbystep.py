### Project - Diamond price prediction

# End to End ML project Setup
import os
os.chdir("C:/Users/y0vwts9/OneDrive - Deere & Co/Y0VWTS9/Python/ML Project/Diamond Price Prediction1")
# pwd

# =============================================================================
# ## Open vs code from cmd
# # cd
# # code .
# =============================================================================

# Create a new environment for new project
#https://medium.com/@apremgeorge/using-conda-python-environments-with-spyder-ide-and-jupyter-notebooks-in-windows-4e0a905aaac5

### Type below code in powershell

# =============================================================================
# cd "C:/Users/y0vwts9/OneDrive - Deere & Co/Y0VWTS9/Python/ML Project/Diamond Price Prediction1"
# conda env list
# conda create -p venv python==3.8
# =============================================================================

# Entire project will refer this "venv" environment

# To activate this environment, use
#
#     $ conda activate "C:\Users\y0vwts9\OneDrive - Deere & Co\Y0VWTS9\Python\ML Project\Diamond Price Prediction1\venv"
#
# To deactivate an active environment, use
#
#     $ conda deactivate

# =============================================================================
# conda activate venv/   #works if wd already set
# pip install -r requirements.txt
# =============================================================================

# Create setup.py
# Create src with __init__.py
# =============================================================================
# python setup.py install
# =============================================================================

# a package will be created

#or

# Write "-e ." in requirements.txt   #to trigger setup.py from requirements
# Now execute "pip install -r requirements.txt"
# It will first install the packages and then run the setup.py file

# cls -- to clear the screen

######################################
# Project Github setup
# Download git cli 
# or
#conda install -c anaconda git  #installed in conda powershell
# git init
# git version
# git config -h

# Create a new repository
# =============================================================================
# echo "# DiamondPricePrediction1" >> README.md
# git init

#create two files README.md & .gitignore
# Add below code to it
# =============================================================================
# # Requirements
# venv/
# =============================================================================

# git add README.md or use git add .
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/FUZZZZI/DiamondPricePrediction1.git
# git push -u origin main
# =============================================================================

# Push an existing repository from the command line
# =============================================================================
# git remote add origin https://github.com/FUZZZZI/DiamondPricePrediction1.git
# git branch -M main
# git push -u origin main
# =============================================================================

# now copy the code form new .gitignore file to our file and replace the existing text
# To upload/refresh it, follow the steps
# git add .
# git commit -m "second commit"
# git push -u origin main

#########################################
# Creating Project structure
# Create new folders
# 1. artifacts: pickle file, models, dataset, intermediate files, whatever you want to save in HDD, preprocessed data, FE files
# 2. notebooks: EDA, FE, model training in jupyter
    # a. data: file
# 3. src (already created): Entire end to end ML project modules

# In Jupyter notebook EDA -> FE -> FS -> Model Training -> Model Hyperparameter tuning -> Deployment of models
# In industry, this process is not one time so it should be automated so create pipelines
# 1. Training Pipelines (generally triggers in every 20days, 30 days)
# 2. Prediction Pipelines

# Training Pipelines Components:
    # 1. Data Ingestion: Reading datasets from source (SQL, MongoDB, Api, etc.)
    # 2. Data Transformation: Handling Null, missing, outliers, data transformation, creating a pipeline for FE
    # 3. Model Trainer: train with multiple models
    # 4. Model Evaluation: 

# Prediction Pipelines:
    # Api exposed to the same model deployed in cloud

# Create two folders in src
# components
    # __init__.py
    # data_ingestion.py
    # data_transformation.py
    # model_trainer.py
# pipelines
    # __init__.py
    # training_pipeline.py
    # prediction_pipeline.py

# Create utils.py file: contains all common functionalities required for the project (creating pickle file, read the csv, uploading file to database, read file from database)

# Create logger.py & exception.py

# upload the changes to github   
#Note: artifacts & notebooks are empty folders so not uploaded, git ignore ignores them

#######################################
# Project Logging & Exception Handling
# These will be generic to the project

#######################################
# EDA, FE & Model Training
# Include the csv file in data folder & create EDA and Model training.ipynb files in jupyter

# conda install -c conda-forge jupyter_contrib_nbextensions -- for collapsible codes in jupyter
# pip install ipykernel  --- helps to open code in Jupyter from ipynb created in vscode