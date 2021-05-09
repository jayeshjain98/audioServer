import json
import setup


file_path='/test_data/'

def test_update_api_success():
    #inserting for update
    filename = "create_api_for_success.json"
    request_data = setup.get_data(filename,file_path)
    headers = {'content-type': 'application/json'}
    service_url_upload = setup.get_api_url("insert")
    setup.send_post_request(service_url_upload,request_data,headers)
    
    
    service_url_update = setup.get_api_url("update", ("Audiobook", "2EB8AA08-AA98-11EA-B4AA-73B441D16381"))
    headers = {'content-type': 'application/json'}
    request_data['audioMetadata']["audiobook_title"] = "updated"
    response = setup.send_update_request(service_url_update,request_data,headers)

    #for cleaning
    service_url_delete = setup.get_api_url("delete", ("Audiobook", "2EB8AA08-AA98-11EA-B4AA-73B441D16381"))
    headers = {'content-type': 'application/json'}
    setup.send_delete_request(service_url_delete,headers)
    
    assert response.status_code == 200

def test_update_api_fail():
    filename = "create_api_for_success.json"
    request_data = setup.get_data(filename,file_path)
    headers = {'content-type': 'application/json'}
    service_url_upload = setup.get_api_url("insert")
    setup.send_post_request(service_url_upload,request_data,headers)

    service_url_update = setup.get_api_url("update", ("Song", "2EB8AA08-AA98-11EA-B4AA-73B441D16381"))
    print(service_url_update)
    headers = {'content-type': 'application/json'}
    request_data['audioMetadata']["audiobook_title"] = "updated"
    response = setup.send_update_request(service_url_update,request_data,headers)
    
    #for cleaning
    service_url_delete = setup.get_api_url("delete", ("Audiobook", "2EB8AA08-AA98-11EA-B4AA-73B441D16381"))
    headers = {'content-type': 'application/json'}
    setup.send_delete_request(service_url_delete,headers)
    
    assert response.status_code == 400


def test_update_api_norecord():
    filename = "create_api_for_success.json"
    request_data = setup.get_data(filename,file_path)
    service_url_update = setup.get_api_url("update", ("Audiobook", "2EB8AA08-AA98-11EA-B4AA-73B441D16385"))
    headers = {'content-type': 'application/json'}
    response = setup.send_update_request(service_url_update,request_data,headers)

    assert response.status_code == 400