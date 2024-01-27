from env_colab_pass import passutil 
import os 

key_name = "FROM_ENV"
os.environ[key_name] = 'This key is from environment variable'
value = passutil.get_secret_value(key_name)
print(f"The value for {key_name} is: {value}")

key_name = "KEY_FROM_COLAB"
value = passutil.get_secret_value(key_name)
print(f"The value for {key_name} is: {value}")

key_name = "NEW_KEY"
value = passutil.get_secret_value(key_name)
print(f"The value for {key_name} is: {value}")
