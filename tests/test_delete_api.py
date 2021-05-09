import json
import setup


file_path='/test_data/'

def test_delete_api_success():
    #inserting for delete
    filename = "create_api_for_success.json"
    request_data = setup.get_data(filename,file_path)
    headers = {'content-type': 'application/json'}
    service_url_upload = setup.get_api_url("insert")
    setup.send_post_request(service_url_upload,request_data,headers)
    
    
    service_url_delete = setup.get_api_url("delete", ("Audiobook", "2EB8AA08-AA98-11EA-B4AA-73B441D16381"))
    headers = {'content-type': 'application/json'}
    response = setup.send_delete_request(service_url_delete,headers)
    
    assert response.status_code == 200

def test_delete_api_fail():
    service_url_delete = setup.get_api_url("delete", ("Audiobook", "2EB8AA08-AA98-11EA-73B441D16381"))
    headers = {'content-type': 'application/json'}
    response = setup.send_delete_request(service_url_delete,headers)
    
    
    assert response.status_code == 400


def test_delete_api_norecord():
    service_url_delete = setup.get_api_url("delete", ("Audiobook", "2EB8AA08-AA98-11EA-B4AA-73B441D16385"))
    headers = {'content-type': 'application/json'}
    response = setup.send_delete_request(service_url_delete,headers)

    assert response.status_code == 200