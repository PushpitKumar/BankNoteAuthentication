# BankNoteAuthentication

## Table of Contents
* Overview/Problem Statement
* Dataset
* File Structure
* Major Packages/Libraries Used
* Installation/Working Environment
* Building the Web App
* Model Deployment on Heroku Platform
* App Implementation
* Drawbacks and Future Scope
* Credits

### 1. Overview/Problem Statement
* Ever wondered whether the note given to you as change by the shopkeeper was real or fake? Or you returned empty handed when you went to deposit some money in the bank and your notes were rejected for being fake? This app will help you identify whether the note is authentic or not!
* This is a classification problem where we use ML algorithms such as LogisticRegression, SVM, KNN and more.

### 2. Dataset
* The dataset was taken from Machine Learning UCI repository and is available on Kaggle. 
* Data were extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used.
* The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained.
* Wavelet Transform tool were used to extract features from images.
* The dataset contains the following features: **Variance**, **Skewness**, **Curtosis**, **Additional Information** and **Class**.
* [Dateset Link](https://www.kaggle.com/vivekgediya/banknote-authenticationcsv)

### 3. File Structure
```
├── BankNote_Authentication.csv 
├── Dockerfile
├── Notebook.ipynb
├── Procfile
├── README.md
├── app.py
├── banknote.pkl
├── requirements.txt
```

### 4. Major Packages/Libraries Used
* pandas 
* numpy
* sci-kit learn
* matplotlib
* seaborn
* Flask
* flasgger
* gunicorn

### 5. Installation/Working Environment
Follow the instructions if you want to run the app from your local computer.
* The app is written using **Python 3.8.5**. You can download it from [here](https://www.python.org/downloads/).You can also download **Anaconda** which is a distribution of python from [here](https://www.anaconda.com/products/individual). I would recommend downloading anaconda since it is very useful as it comes with a lot of python libraries, Jupyter and Spyder IDE.
* Once you are done with the installation, you can clone this repository to your computer and install the required packages and libraries using the following line of code through the command prompt where your local environment is setup.
```
pip install -r requirements.txt
```
### 6. Building the Web App
* The web was developed using flask micro web framework which is written in python suitable for small scale projects such as this one. For more information you can check the offical flask website by clicking [here](https://flask.palletsprojects.com/en/2.0.x/)
* Flasgger was used to develop the basic UI of the webpage. It  is a Flask extension to extract OpenAPI-Specification from all Flask views registered in your API.
* Flasgger also comes with SwaggerUI embedded so you can access http://localhost:5000/apidocs and visualize and interact with your API resources. For more information on flasgger click [here](https://github.com/flasgger/flasgger)

### 7. Model Deployment on Heroku Platoform
* You will have to create a account in order to deploy the model. Login to your account and go to the deploy section.
* Connect to your github repository and deploy the model manually or through Heroku CLI.

![3](https://user-images.githubusercontent.com/83957848/119222443-06092480-bb12-11eb-8102-086761ded15b.JPG)

### 8. App Implementation  
* Link: [BankNoteAuthenticator](https://banknoteauthenticator99.herokuapp.com/apidocs)  
* The app asks for user to enter the details obtained by wavelet transform tool i.e variance, skewness, curtosis and entropy. Based on these input the banknote is authenticated. 

![1](https://user-images.githubusercontent.com/83957848/120903860-5205ae80-c666-11eb-90dc-5c0838f8b9ac.JPG)
![2](https://user-images.githubusercontent.com/83957848/120903864-6184f780-c666-11eb-9abc-ecc134a6bd68.JPG)
![3](https://user-images.githubusercontent.com/83957848/120903869-677ad880-c666-11eb-8a31-5fee94cee2c8.JPG)


### 10. Credits
I would like to thank [Krish Naik](https://github.com/krishnaik06) for hosting this problem statement on his youtube channel 
