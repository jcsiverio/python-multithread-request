import requests
import json
import _thread
import time

access_token = "Bearer eyJraWQiOiJTVFNHQ0JpbnRyYW5ldCIsInR5cCI6IkpXVCIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJjaWJnZGZvcmZlbzAwMDEiLCJuYmYiOjE2NTYzNDMyNTgsImlzcyI6IlNUU0dDQmludHJhbmV0IiwiZXhwIjoxNjU2MzQ2ODYzLCJpYXQiOjE2NTYzNDMyNjMsImp0aSI6ImI2MDE5MDU3LWRkMmItNGU2Yy04YWVjLWZhYzYwMDdhZmQ3OCJ9.zVXs2ttUByZHcCtH68vbgK3AIWVXKQTHRfd6kyVUMKsWpr-syXOP9thoDihw8OCTrZBqEUzzHykIlsRoLyHCf3pJ9tc35SMDqGHZXe2ij_0UR7gWUMvwqiSkuAIBONLGvv_SPjqRqrT1Jox1s85p00PSF4iWTco6HVQLWB_YHtB3ayUVGWF8Bb0GKKN6adL3CmdYMvy_wMfeZCcuBmjdZhoD0wg0atzD9hcuA7Z42v8AmH4fAr2Y0RzP9ck3mDzK7vUGsBCy2Hb-EwhavWVSUKMzuLEZlOvgDciS54Tn4qNRzXdBLv3NAfTmUFtjDtmPb76ZGfe5eujwDICfQzFBRw" 

def first_request():
    print ("First request: %s" % ( time.ctime(time.time()) ))
    url = "http://localhost:8080/fenergo/"
    
    payload = json.dumps({
      "sourceSystem": "Conpend",
      "requestID": "123456",
      "entityCode": "0049",
      "subentityCode": "LON",
      "onboardingSubentityCode": "LON",
      "personId": "CUST20200619003",
      "parentID": "1234",
      "associationType": "Vice President",
      "fullName": "Tania Valentina Díaz González",
      "dateOfBirth": "",
      "countryNationalityCode": "VE",
      "countryOriginCode": "VE",
      "countryResidenceCode": "VE",
      "documentCode": "12345677XX",
      "documentTypeCode": "PASS",
      "address": "Calle 103, 14a-53, Bogotá, 811, Colombia",
      "personType": "Financial Institutions",
      "businessIndustry": "Hotels",
      "glcs": "1234",
      "riskLevelDeclared": "M",
      "pepDeclared": "Relevant",
      "adverseMediaDeclared": "Confirmed",
      "action": "On-boarding",
      "systemAcquisitionDate": "",
      "systemLoadDate": ""
    })
    headers = {
      'X-IBM-Client-Id': '59186730-668f-4605-b526-7c1f9dd187ef',
      'scope': 'paymentscreening.read',
      'Authorization': access_token,
      'Content-Type': 'application/json',
      'Cookie': 'JSESSIONID=5E6908483DDF3DD5876B447A746E6B27'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(" -> " + "First request ends: %s" % ( time.ctime(time.time()) ) + " -> " + response.text)

def second_request():
    print ("Second request: %s" % ( time.ctime(time.time()) )) 
    url = "http://localhost:8080/fenergo/"
    payload = json.dumps({
      "sourceSystem": "Fenergo",
      "requestID": "123456",
      "entityCode": "0049",
      "subentityCode": "SLB",
      "onboardingSubentityCode": "SLB",
      "personId": "42472",
      "parentID": "42472",
      "associationType": "Vice President",
      "fullName": "INDIGO GROUP SAS",
      "dateOfBirth": "1984-02-22",
      "countryNationalityCode": "CH",
      "countryOriginCode": "NJ",
      "countryResidenceCode": "NJ",
      "documentCode": "12345677XX",
      "documentTypeCode": "PASS",
      "address": "Calle 103, 14a-53 , Bogotá, 811, Colombia",
      "personType": "Financial Institutions",
      "businessIndustry": "Hotels",
      "glcs": "1234",
      "riskLevelDeclared": "L",
      "pepDeclared": "Relevant",
      "adverseMediaDeclared": "Confirmed",
      "action": "On-boarding",
      "systemAcquisitionDate": "1999-02-01",
      "systemLoadDate": "1999-02-01"
    })
    headers = {
      'X-IBM-Client-Id': '59186730-668f-4605-b526-7c1f9dd187ef',
      'scope': 'paymentscreening.read',
      'Authorization': access_token,
      'Content-Type': 'application/json',
      'Cookie': 'JSESSIONID=C5F5616CF7B8F014741DB6C417B6AE1B'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(" -> " + "Second request ends: %s" % ( time.ctime(time.time()) ) + " -> " + response.text)

def third_request():
    print ("Third request: %s" % ( time.ctime(time.time()) )) 
    url = "http://localhost:8080/fenergo/"
    payload = json.dumps({
      "sourceSystem": "Fenergo",
      "requestID": "123456",
      "entityCode": "0049",
      "subentityCode": "LON",
      "onboardingSubentityCode": "LON",
      "personId": "42472",
      "parentID": "42472",
      "associationType": "Vice President",
      "fullName": "INDIGO GROUP SAS",
      "dateOfBirth": "1984-02-22",
      "countryNationalityCode": "CH",
      "countryOriginCode": "NJ",
      "countryResidenceCode": "NJ",
      "documentCode": "12345677XX",
      "documentTypeCode": "PASS",
      "address": "Calle 103, 14a-53 , Bogotá, 811, Colombia",
      "personType": "Financial Institutions",
      "businessIndustry": "Hotels",
      "glcs": "1234",
      "riskLevelDeclared": "L",
      "pepDeclared": "Relevant",
      "adverseMediaDeclared": "Confirmed",
      "action": "On-boarding",
      "systemAcquisitionDate": "1999-02-01",
      "systemLoadDate": "1999-02-01"
    })
    headers = {
      'X-IBM-Client-Id': '59186730-668f-4605-b526-7c1f9dd187ef',
      'scope': 'paymentscreening.read',
      'Authorization': access_token,
      'Content-Type': 'application/json',
      'Cookie': 'JSESSIONID=C5F5616CF7B8F014741DB6C417B6AE1B'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(" -> " + "Third request ends: %s" % ( time.ctime(time.time()) ) + " -> " + response.text)    

def fourth_request():
    print ("Fourth request: %s" % ( time.ctime(time.time()) )) 
    url = "http://localhost:8080/fenergo/"
    payload = json.dumps({
      "sourceSystem": "Fenergo",
      "requestID": "123456",
      "entityCode": "0049",
      "subentityCode": "LON",
      "onboardingSubentityCode": "LON",
      "personId": "42472",
      "parentID": "42472",
      "associationType": "Vice President",
      "fullName": "INDIGO GROUP SAS",
      "dateOfBirth": "1984-02-22",
      "countryNationalityCode": "CH",
      "countryOriginCode": "NJ",
      "countryResidenceCode": "NJ",
      "documentCode": "12345677XX",
      "documentTypeCode": "PASS",
      "address": "Calle 103, 14a-53 , Bogotá, 811, Colombia",
      "personType": "Financial Institutions",
      "businessIndustry": "Hotels",
      "glcs": "1234",
      "riskLevelDeclared": "L",
      "pepDeclared": "Relevant",
      "adverseMediaDeclared": "Confirmed",
      "action": "On-boarding",
      "systemAcquisitionDate": "1999-02-01",
      "systemLoadDate": "1999-02-01"
    })
    headers = {
      'X-IBM-Client-Id': '59186730-668f-4605-b526-7c1f9dd187ef',
      'scope': 'paymentscreening.read',
      'Authorization': access_token,
      'Content-Type': 'application/json',
      'Cookie': 'JSESSIONID=C5F5616CF7B8F014741DB6C417B6AE1B'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(" -> " + "Fourth request ends: %s" % ( time.ctime(time.time()) ) + " -> " + response.text)
    
def fifth_request():
    print ("Fifth request: %s" % ( time.ctime(time.time()) )) 
    url = "http://localhost:8080/fenergo/"
    payload = json.dumps({
      "sourceSystem": "Conpend",
      "requestID": "123456",
      "entityCode": "0049",
      "subentityCode": "PAR",
      "onboardingSubentityCode": "PAR",
      "personId": "CUST20200619003",
      "parentID": "1234",
      "associationType": "Vice President",
      "fullName": "Tania Valentina Díaz González",
      "dateOfBirth": "",
      "countryNationalityCode": "VE",
      "countryOriginCode": "VE",
      "countryResidenceCode": "VE",
      "documentCode": "12345677XX",
      "documentTypeCode": "PASS",
      "address": "Calle 103, 14a-53, Bogotá, 811, Colombia",
      "personType": "Financial Institutions",
      "businessIndustry": "Hotels",
      "glcs": "1234",
      "riskLevelDeclared": "M",
      "pepDeclared": "Relevant",
      "adverseMediaDeclared": "Confirmed",
      "action": "On-boarding",
      "systemAcquisitionDate": "",
      "systemLoadDate": ""
    })
    headers = {
      'X-IBM-Client-Id': '59186730-668f-4605-b526-7c1f9dd187ef',
      'scope': 'paymentscreening.read',
      'Authorization': access_token,
      'Content-Type': 'application/json',
      'Cookie': 'JSESSIONID=5E6908483DDF3DD5876B447A746E6B27'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(" -> " + "Fifth request ends: %s" % ( time.ctime(time.time()) ) + " -> " + response.text)
    
def sixth_request():
    print ("Third request: %s" % ( time.ctime(time.time()) )) 
    url = "http://localhost:8080/fenergo/"
    payload = json.dumps({
      "sourceSystem": "Fenergo",
      "requestID": "123456",
      "entityCode": "0049",
      "subentityCode": "LON",
      "onboardingSubentityCode": "LON",
      "personId": "42472",
      "parentID": "42472",
      "associationType": "Vice President",
      "fullName": "INDIGO GROUP SAS",
      "dateOfBirth": "1984-02-22",
      "countryNationalityCode": "CH",
      "countryOriginCode": "NJ",
      "countryResidenceCode": "NJ",
      "documentCode": "12345677XX",
      "documentTypeCode": "PASS",
      "address": "Calle 103, 14a-53 , Bogotá, 811, Colombia",
      "personType": "Financial Institutions",
      "businessIndustry": "Hotels",
      "glcs": "1234",
      "riskLevelDeclared": "L",
      "pepDeclared": "Relevant",
      "adverseMediaDeclared": "Confirmed",
      "action": "On-boarding",
      "systemAcquisitionDate": "1999-02-01",
      "systemLoadDate": "1999-02-01"
    })
    headers = {
      'X-IBM-Client-Id': '59186730-668f-4605-b526-7c1f9dd187ef',
      'scope': 'paymentscreening.read',
      'Authorization': access_token,
      'Content-Type': 'application/json',
      'Cookie': 'JSESSIONID=C5F5616CF7B8F014741DB6C417B6AE1B'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(" -> " + "Sixth request ends: %s" % ( time.ctime(time.time()) ) + " -> " + response.text)  

def seventh_request():
    print ("Fifth request: %s" % ( time.ctime(time.time()) )) 
    url = "http://localhost:8080/fenergo/"
    payload = json.dumps({
      "sourceSystem": "Conpend",
      "requestID": "123456",
      "entityCode": "0049",
      "subentityCode": "PAR",
      "onboardingSubentityCode": "PAR",
      "personId": "CUST20200619003",
      "parentID": "1234",
      "associationType": "Vice President",
      "fullName": "Tania Valentina Díaz González",
      "dateOfBirth": "",
      "countryNationalityCode": "VE",
      "countryOriginCode": "VE",
      "countryResidenceCode": "VE",
      "documentCode": "12345677XX",
      "documentTypeCode": "PASS",
      "address": "Calle 103, 14a-53, Bogotá, 811, Colombia",
      "personType": "Financial Institutions",
      "businessIndustry": "Hotels",
      "glcs": "1234",
      "riskLevelDeclared": "M",
      "pepDeclared": "Relevant",
      "adverseMediaDeclared": "Confirmed",
      "action": "On-boarding",
      "systemAcquisitionDate": "",
      "systemLoadDate": ""
    })
    headers = {
      'X-IBM-Client-Id': '59186730-668f-4605-b526-7c1f9dd187ef',
      'scope': 'paymentscreening.read',
      'Authorization': access_token,
      'Content-Type': 'application/json',
      'Cookie': 'JSESSIONID=5E6908483DDF3DD5876B447A746E6B27'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(" -> " + "Seventh request ends: %s" % ( time.ctime(time.time()) ) + " -> " + response.text)
    

# Create two threads as follows
try:
    _thread.start_new_thread( fourth_request, () )

    #time.sleep(1)
    _thread.start_new_thread( first_request, () )
    #time.sleep(1)
    _thread.start_new_thread( second_request, () )
    #time.sleep(1)


    #time.sleep(1)
    _thread.start_new_thread( third_request, () )
    _thread.start_new_thread( fifth_request, () )
    _thread.start_new_thread( sixth_request, () )    
except:
    print ("Error: unable to start thread")

while 1:
    pass
