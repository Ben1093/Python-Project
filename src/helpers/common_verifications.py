def verify_status_code(response_data, expected_data):
    assert response_data.status_code == expected_data,"Expected status code is" + str(expected_data)

def verify_json_key_for_not_null(key):
    assert key != 0, "key not equal to zero" + key
    assert key > 0, "Key greater than zero"

def verify_response_key_should_not_be_none(key):
    assert key is not None

def verify_response_headers_content_type(actual_content_type, expected_content_type):
    actual_content_type = actual_content_type.headers.get("Content-Type")
    assert actual_content_type == expected_content_type, "unexpected Content-Type" + str(expected_content_type)

def verify_response_headers_cookies():
    actual_cookies

def verify_response_time(actual_time, expected_time):
    assert actual_time == expected_time, "unexpected response time" + str(expected_time)

def verify_status_code_for_post(response_data, expected_data):
    assert response_data == expected_data, "unexpected status code for post" + str(expected_data)

