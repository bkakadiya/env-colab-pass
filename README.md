# Env-colab-pass
Python package that check for key value in env and colab userdata. If key is not found then it will asks for it using getpass

If Colab has key but access is not granted then it will ask for access and use it.

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

## Read from keylab userdata
key_name = "KEY_FROM_COLAB"
value = passutil.get_secret_value(key_name)
print(f"The value for {key_name} is: {value}")

## ask for value for new key
key_name = "NEW_KEY"
value = passutil.get_secret_value(key_name)
print(f"The value for {key_name} is: {value}")  
```
