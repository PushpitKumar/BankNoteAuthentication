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
* Docker Implementation
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

### 9. Docker Implementation

![4](https://user-images.githubusercontent.com/83957848/120937919-fbfc3e00-c72d-11eb-8eb0-2760b6f3155e.JPG)

* Dockerizing is the process of packing, deploying, and running applications using Docker containers.
* Docker is an open source tool that ships your application with all the necessary functionalities as one package. You can use Docker to pack your application with everything you need to run the application (such as libraries) and ship it as one package - a container.
* Containers are created from images that specify their precise contents. Dockerizing is a big hit nowadays. All the big names use it - Google, VMware, or Amazon support it.
* You can know more about Docker by clicking [here](https://www.docker.com/) and download it on your computer.
* This is the first time i have implemented docker on a app. If you would also like to dockerize the app, you need to run the commands in a dockerfile via CLI.
* The following commands are written in Dockerfile:
 1. From - This command is used to get the base image which we can get from dockerhub. 
 2. COPY - This command tells the computer to copy the files from local directory to the user root folder in docker.
 3. EXPOSE - This command mentions the port number to be used.
 4. WORKDIR - The command used to tell our file location in docker
 5. RUN pip install -r reuirements.txt
 6. CMD python app.py
* Now to build the docker image, go to your file directory in command prompt and run the following command, where 'api_name' is the name you want to give to your app:
```
docker build -t 'api_name'
```
* The process will take some time to execute and some compatibility issue of various libraries might arise which you will have to fix manually in requirements.txt
* Now, you can see your containerized application by running the following command:
```
docker ps
```
This will show details such as Container ID, Image Name, Commands, Status, Ports, etc.
* Now to run your application via docker, write the following command, provided you used 5000 as port number:
```
docker run -p 5000:5000 'api_name'
```

### 9. Drawbacks and Future Scope
* The ML model assumes you have the wavelet transform tool in order to extract the features to check the authenticity of the banknotes.
* An image classifer would be more reliable for this problem statement.
* Features can be scaled to get more accurate results.
* The app's front end has room for improvement.

### 10. Credits
I would like to thank [Krish Naik](https://github.com/krishnaik06) for hosting this problem statement on his youtube channel, whose work was taken as inspiration for successful completion of this project.
