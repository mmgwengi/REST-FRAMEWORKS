# REST-FRAMEWORKS
1.	Create machine learning model
Linear regression() from sklearn is used to predict CO2 emission from vehicles. See the full model in Regression_CO2_emission.py. The Pickle module is used to save the model as model.pkl- (Pickle model is used for serializing and de-serialization python object structures. The process converts any python object to byte streams (0s and 1s)). This is the file that will later be used to predict the output when new data is provided in the web-app.
2.	Develop your web-app using Flask and integrate your model in the app, save as app.py. 
3.	Deploy your web-app in Heroku Cloud Platform by running app.py in command prompt. Get the URL and paste to browser
4.	Enter required values to predict emission.
Files
-	 FuelConsumption.csv — CO2 dataset
-	 mlmodel.py —machine learning code
-	model.pkl — This is the file we obtained after running Regression_CO2_emission.py file. It is present in the same directory
-	app.py — Flask application
-	templates — This folder contains ‘index.html’ file. This is mandatory in Flask while rendering templates. All HTML files are placed under this folder.
-	static — This folder contains the “css” folder. The static folder in Flask application is meant to hold the CSS and JavaScript files.

