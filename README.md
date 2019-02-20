# digit recognizer

This is a web application developed to detect and predict the handwritten digits written on a canvas and using tensorflow built model using softmax regression with ADAM Optimizer. The model is quite good and is able to predict majority of digits.

Here is the deployed application: https://re-digit.herokuapp.com/


<h1> Running the application on local machine </h1><br/>
Steps to follow are: <br/>
1. git clone https://github.com/prakass1/digitrecognizer.git<br/>
2. cd --working_git_dir--<br/>
3. Ensuring all the requirements are satisfied as per requirements.txt, run python app.py<br/>



<h1> How to contribute for future improvements ? </h1><br/>
1. Make a fork of the application<br/>
2. git clone the app. <br/>
    Example you could simply clone using git bash $git clone https://github.com/--username--/digitrecognizer.git<br/>
3. Make a new model, update it and build it using heroku.<br/>
<br/>
   Steps to build on heroku.<br/>
  1. First make an account at heroku.<br/>
  2. Download heroku cli for Windows/Linux/Mac<br/>
  3. Using bash,<br/>
  <code>
     cd working_dir #containing the .git file <br/>
     heroku create app_name <br/>
     git remote -v <br/>
     git push heroku master # Pushes the app to heroku master
  </code>
  
  Two important files that are necessary for herokus are:<br/>
  a. Procfile # says what to deploy. Can leave it as is<br/>
  b. requirements.txt  # If any new requirements needs to be added it goes here<br/>
