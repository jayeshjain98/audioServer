import requests
import json
import os

#This method is required to change in case host address changed
def get_base_url():
     host_address = "localhost"      #To Be change with server address
     port = "8000"                   #To Be change with server port
    
     return "http://"+host_address+":"+port

url_map = {
    "insert" : "/savefile",
    "delete" : "/deletefile/{}/{}",
    "update" : "/updatefile/{}/{}",
    "get" : "/getfile/{}/{}",
    "get_special" : "/getfile/{}"
}
def get_api_url(operation, values=None):
    end_point = url_map[operation].format(values[0],values[1] if len(values) >1 else values[0] ) if values != None else url_map[operation]
    resource = get_base_url()+end_point  #No Change required
    return resource

def send_post_request(url=None,request_data=None,headers=None):
    return requests.post(url,json=request_data,headers=headers)

def send_delete_request(url=None,headers=None):

    return requests.delete(url,headers=headers)

def send_get_request(url=None,headers=None):
    return requests.get(url,headers=headers)

def send_update_request(url=None,request_data=None,headers=None):
    return requests.put(url,json=request_data,headers=headers)

def get_data(filename,file_path):
    resource_path=os.path.abspath(os.path.dirname(__file__))+file_path+filename
    file=open(resource_path,"r")
    input_data=file.read()
    return json.loads(input_data)

def get_file_list(file_path):
    resourse_path=os.path.abspath(os.path.dirname(__file__))+file_path
    return os.listdir(resourse_path)
                                  

