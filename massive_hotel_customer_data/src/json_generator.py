import json
import boto3
import datetime
import os, tempfile
from pathlib import Path
import random

def randomnumber(n):
    minimum = pow(10 , n-1)
    maximum = pow(10 , n) - 1
    return random.randint(minimum , maximum)

def generate_customer_data():
    customers = []

    for i in range(50):  # Generating data for 50 customers
        n = random.randint(1, 70)
        customer = {
            "id": n,
            "first_name": f"first_name_{n}",
            "middle_name": random.choice([None , f"middle_name_{n}"]), #middle can be null in some cases
            "last_name": f"last_name_{n}",
            "email": f"customer{n}@yahoo.com",
            "age": random.randint(18, 60),
            "created_at": str(datetime.datetime.utcnow()),
            "address": generate_address() , # Generating nested address data
            "phone_number": generate_phone_number(), #generate nested phonenumber data
            "updated_at": str(datetime.datetime.utcnow())
        }
        customers.append(customer)

    return customers

def generate_address():
    # List of city and country names
    cities = ['New York', 'London', 'Paris', 'Tokyo', 'Sydney' , 'Bangalore' , 'Colombo']
    countries = ['USA', 'UK', 'France', 'Japan', 'Australia' , 'India' , 'SriLanka']   
    city_index = random.randint(0, len(cities) - 1)

    return  {
        "streetAddress": f"{randomnumber(2)} Street",
        "city":  cities[city_index],
        "country":  countries[city_index],
        "postalCode": randomnumber(5)
    }

def generate_phone_number(): 
    phone_numbers =[]
    #types of phonenumbers
    type = ['mobile','fax','home','office']
    type_index = random.randint(1, len(type))

    for i in range(type_index):
        ph_no = []

        #Generate ranfom 10 digit number as phone number
        for n in range(1, 10): 
            ph_no.append(random.randint(0, 9)) 

        phone_number =  {
            "type": type[i],
            "number": int("".join(map(str, ph_no )))
        }
        phone_numbers.append(phone_number)

    return phone_numbers

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = 'massive-hotel-customer-data'
    upload_key = f"raw-data/customer_data_{str(datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))}.json"
 
    customer_data = generate_customer_data()
    
    try:
        with open("/tmp/customer_data.json", "w") as file:
            json.dump(customer_data, file, indent=2)
    except TypeError:
        print("Unable to serialize the object")

    # Upload the generated customer data JSON file back to S3
    s3.upload_file("/tmp/customer_data.json", bucket, upload_key)
