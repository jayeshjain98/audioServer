import json
import setup


file_path='/test_data/'

def test_get_api_success():
    #inserting for get
    filename = "create_api_for_success.json"
    request_data = setup.get_data(filename,file_path)
    headers = {'content-type': 'application/json'}
    service_url_upload = setup.get_api_url("insert")
    setup.send_post_request(service_url_upload,request_data,headers)
    
    
    service_url_get = setup.get_api_url("get", ("Audiobook", "2EB8AA08-AA98-11EA-B4AA-73B441D16381"))
    headers = {'content-type': 'application/json'}
    response = setup.send_get_request(service_url_get,headers)
    
    service_url_get = setup.get_api_url("get_special", ("Audiobook",))
    print(service_url_get)
    headers = {'content-type': 'application/json'}
    response_special = setup.send_get_request(service_url_get,headers)

    service_url_delete = setup.get_api_url("delete", ("Audiobook", "2EB8AA08-AA98-11EA-B4AA-73B441D16381"))
    headers = {'content-type': 'application/json'}
    setup.send_delete_request(service_url_delete,headers)

    assert response.status_code == 200
    assert response_special.status_code == 200

def test_delete_api_fail():
    service_url_get = setup.get_api_url("get", ("Audiobook", "2EB8AA08-AA98-11EA-73B441D16381"))
    headers = {'content-type': 'application/json'}
    response = setup.send_get_request(service_url_get,headers)
    
    
    assert response.status_code == 400

