import json
import setup


file_path='/test_data/'

def test_create_api_success():
    filename = "create_api_for_success.json"
    request_data = setup.get_data(filename,file_path)
    headers = {'content-type': 'application/json'}
    service_url_upload = setup.get_api_url("insert")
    response = setup.send_post_request(service_url_upload,request_data,headers)
    
    
    #for cleaning
    service_url_delete = setup.get_api_url("delete", ("Audiobook", "2EB8AA08-AA98-11EA-B4AA-73B441D16381"))
    headers = {'content-type': 'application/json'}
    print(service_url_delete)
    setup.send_delete_request(service_url_delete,headers)
    
    assert response.status_code == 200

def test_create_api_fail():
    filename = "create_api_for_fail.json"
    request_data = setup.get_data(filename,file_path)
    headers = {'content-type': 'application/json'}
    service_url_upload = setup.get_api_url("insert")
    response = setup.send_post_request(service_url_upload,request_data,headers)
    
    
    assert response.status_code == 400


def test_create_api_nopayload():
    headers = {'content-type': 'application/json'}
    service_url_upload = setup.get_api_url("insert")
    response = setup.send_post_request(service_url_upload,headers)

    assert response.status_code == 400
