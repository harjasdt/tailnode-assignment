# Python Intern Assignment
## Implementation
### Part A
First established a connection with Mongodb Atlas using URI and then created functions for making API calls to populate database, then started an infinite loop and took user inputs to perform the mentioned functionalities of creating users and posting data.After getting the required data it was inserted to the database and a success message is displayed.

### Part B
First established a connection with Mongodb Atlas using URI and then created functions for scraping data from the mentioned websites, then started a for loop for navigating to different pages for scraping data .After getting the required data the database is updated.


## How to use
### Step1. Cloning this repo
Run this either in gitbash terminal or VsCode terminal

```
git clone https://github.com/harjasdt/teachNote.git
```
### Step2. Installing and Creating virtual envirnoment
Install virtual envirnomen
```
pip install virtualenv
```


Create your virtual envirnoment
```
virtualenv teachnote_env 
```

Activate your env
```
cd teachnote_env
Scripts/activate
cd .. 
```

You should see teachnote_env written in brackets in the beginning of your terminal.

### Step3. Install requirements.txt
Now, inside your main folder install all the requirements using
```
pip -r install requirements.txt
```

### Step4. Adding your URI
-Go to https://account.mongodb.com/account/login <br>
-After logging in create your database<br>
-Now connect using python driver<br>
-Create you URI and replace it on places mentioned in the code


### Step5. Run Files
### Running part_A.py
 Expected output as on terminal for adding a user

 
![user](https://github.com/harjasdt/teachNote/assets/68768529/8d390336-e477-4fc8-b23f-676580ade3c0)


 Expected output as on terminal for posting the post data

 
![post](https://github.com/harjasdt/teachNote/assets/68768529/9d1b21fa-666f-47ee-a00f-4a23d0281984)


Changes reflected to your database


![parta](https://github.com/harjasdt/teachNote/assets/68768529/5ecbde0f-c357-4514-b998-b7cd1be45afb)
### Runningg part_B.py
Expected output as on terminal


![partb](https://github.com/harjasdt/teachNote/assets/68768529/a56b719a-58d0-4fef-bea0-a9df17bce646)

 Changes reflected to your database
 

![book](https://github.com/harjasdt/teachNote/assets/68768529/2e90f7f2-d587-48ea-a01b-7cd963f89e54)
