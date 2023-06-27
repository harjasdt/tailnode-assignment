#importing for mongo db
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

#importing for data scraping
import requests

#uri connects you to  mongodb atlas
uri ="mongodb+srv://teachnode:teachnode@teachnode.3o5abt1.mongodb.net/?retryWrites=true&w=majority"

# Set the Stable API version when creating a new client
client = MongoClient(uri, server_api=ServerApi('1'))
                          
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

#creating a new database if does not already exists
mydb = client["teachdatabase"]

#creating collections 
mycol = mydb["user"]
myposts = mydb["post"]

print("Available collections are:-")
print(mydb.list_collection_names())

# Helper functions
def fetch_users(limit):
    url = f'https://dummyapi.io/data/v1/user?limit={limit}'
    headers = {'app-id': "649a79dafa3b5819daf98597"}  # Replace 'your_app_id' with your actual app_id

    response = requests.get(url, headers=headers)
    users_data = response.json().get('data')
    
    return users_data
    

def fetch_posts(user_id):

    url = 'https://dummyapi.io/data/v1/user/{}/post'
    headers = {'app-id': '649a79dafa3b5819daf98597'}  # Replace 'your_app_id' with your actual app_id, or you can use mine aswell , i don't mind!

   
    response = requests.get(url.format(user_id), headers=headers)
    posts_data = response.json().get('data')

    x = myposts.insert_many(posts_data)
    

def insert_users(number):

    # for inserting users
    mylist=fetch_users(3) 
    x = mycol.insert_many(mylist)
    print("\nUsers Created !!!!\n\n")

def upload_posts():
    for x in mycol.find({},{"_id":0,"id":1}):
        fetch_posts(x['id'])
    print("\nPosts Uploaded !!!!\n\n")

# Min Program Starts
while True:
    print('''
    Enter you choice:-
    1>Insert users
    2>Upload Posts
    ''')
    option=int(input("What would you like to do?  "))

    if(option==1):
        number=int(input("How many Users would you like to upload? "))
        insert_users(number)
    elif(option==2):
        upload_posts()



