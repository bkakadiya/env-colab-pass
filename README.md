# Env-colab-pass
Python package that check for key value in env and colab userdata. If key is not found then it will asks for it using getpass

If Colab has key but access is not granted, then it will ask for access and use it.

This utility will simplify keeping secret out of sample Jupyter Notebook provided that sample can be run on Google colab as well. 

[Demo](media/demo.webm)

# Usage 

## Install package
```
pip install env-colab-pass
```

## Import module 
```
from env_colab_pass import passutil 
```

## To get the value of a env variable / colab user data / ask user 

```
passutil.get_secret_value(key_name)
```

## Few more examples
```

## Read env variable
key_name = "TEMP"
value = passutil.get_secret_value(key_name)
print(f"The value for {key_name} is: {value}")

## Read from colab userdata
key_name = "KEY_FROM_COLAB"
value = passutil.get_secret_value(key_name)
print(f"The value for {key_name} is: {value}")

### This will ask to grant access to colab userdata
key_name = "ANOTHER_KEY_NO_ACCESS"
value = passutil.get_secret_value(key_name)
print(f"The value for {key_name} is: {value}")

## ask user for value for new key, that is not found in env and on colab userdata
key_name = "NEW_KEY"
value = passutil.get_secret_value(key_name)
print(f"The value for {key_name} is: {value}") 
```

## Colab notebook
Try out on [Google Colab notebook](https://colab.research.google.com/github/bkakadiya/env-colab-pass/blob/main/tests/colab_userdata_getpass.ipynb) 