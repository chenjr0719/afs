import os
import pytest
import requests
import json



# Positive test
def test_upload_model(models_resource, test, v1_env):
    name = 'test_model.h5'
    with open(name, 'w') as f:
        f.write(str(test))
    models_resource.upload_model(name, accuracy=.123, loss=.123)
    if os.path.exists(name):
        os.remove(name)


# Positive test
def test_download_model(models_resource, test, v1_env):
    name = 'test_model.h5'
    try:
        models_resource.download_model(name, model_name=name)
        assert os.path.exists(name)

        with open(name, 'r') as f:
            content = f.read()
        print(content)
        assert str(test) == str(content)
    except Exception as e:
        print(e)
    finally:
        if os.path.exists(name):
            os.remove(name)


# Positive test
def test_get_latest_model_info(models_resource, v1_env):
    name = 'test_model.h5'
    model_info = models_resource.get_latest_model_info(name)
    assert 'evaluation_result' in model_info
    assert 'tags' in model_info


# Negative test
def test_model_accuracy(models_resource, test):
    name = 'test_model.h5'
    with open(name, 'w') as f:
        f.write(str(test))
    with pytest.raises(Exception):
        pytest.raises(
            models_resource.upload_model(name, accuracy=1.23, loss=.123))
    if os.path.exists(name):
        os.remove(name)


# Negative test
def test_model_naming_length(models_resource, test, v1_env):
    a = ['a' for i in range(100)]
    name = '.'.join(a)
    with open(name, 'w') as f:
        f.write(str(test))
    with pytest.raises(Exception):
        pytest.raises(
            models_resource.upload_model(name, accuracy=.123, loss=.123))
    if os.path.exists(name):
        os.remove(name)


# Negative test
def test_model_naming_rule(models_resource, test, v1_env):
    name = "adsfsf,s=.h5"
    with open(name, 'w') as f:
        f.write(str(test))
    with pytest.raises(Exception):
        pytest.raises(
            models_resource.upload_model(name, accuracy=.123, loss=.123))
    if os.path.exists(name):
        os.remove(name)


# # Negative test
# def test_model_limit(models_resource):
#     name = 'limit_model'
#     if not os.path.exists(name):
#         f = open(name, "wb")
#         # create a file 2G +1 bytes
#         f.seek((2 * 1024 * 1024 * 1024 + 1) - 1)
#         f.write(b"\0")
#         f.close()
#     with pytest.raises(Exception):
#         pytest.raises(
#             models_resource.upload_model(name, accuracy=.123, loss=.123))

