from important_functions import *
import json
import os

ligo_list_email = os.environ['LIGO_EMAIL']
ligo_list_password = os.environ['EMAIL_PASSWORD']


def get_email_list(file_loc = 'contact_all_BNS.json'):
    f = open( file_loc , "rb" )
    jsonObject = json.load(f)
    return jsonObject['email_list']

def email(contact_list_file_loc = 'contact_all_BNS.json', subject = None, body = None, files_to_attach = [], people_to_contact = []):
    
    email_list = get_email_list(file_loc = contact_list_file_loc)
    print(email_list)
    
    psu_email_receivers = ''
    texas_email_recievers = ''
    non_academic_email_receivers = ''
    
    if len(people_to_contact) == 0:
        people_to_contact = email_list.keys()
    
    
    for person in people_to_contact:
        address = email_list[person]
        if 'psu.edu' in address:
            
            psu_email_receivers+=str(email_list[person])+", "
        elif 'utexas.edu' in address:
            texas_email_recievers+=str(email_list[person])+', '
        else:
            non_academic_email_receivers+=str(email_list[person])+", "
            
    if psu_email_receivers[-2:] == ', ':
        psu_email_receivers = psu_email_receivers[:-2]
        
    if non_academic_email_receivers[-2:] == ', ':
        non_academic_email_receivers = non_academic_email_receivers[:-2]
    
    if texas_email_recievers[-2:] == ', ':
        texas_email_recievers = texas_email_recievers[:-2]
       
    all_email_recipients = []
    
    for i in psu_email_receivers:
        if len(i) > 0:
            all_email_recipients.append(i)
    for i in texas_email_recievers:
        if len(i) > 0:
            all_email_recipients.append(i)
    for i in non_academic_email_receivers:
        if len(i) > 0:
            all_email_recipients.append(i)
    
    
    print('all email recipients: '+str(all_email_recipients))
        
    if subject is None:
        subject = "LIGO HET Followup Test Email"
    if body is None:
        body = """This is just a test."""

    email_sender = ligo_list_email
    email_password = ligo_list_password
    send_email(email_sender = email_sender, email_password = email_password, all_email_recipients = all_email_recipients, files = files_to_attach, subject = subject, body = body)


