from dotenv import load_dotenv
import os

load_dotenv()

# Access the environment variables
mlflow_username = os.getenv('MLFLOW_TRACKING_USERNAME')
mlflow_pswd = os.getenv('MLFLOW_TRACKING_PASSWORD')

print(mlflow_username)  # Should print 'vinu0404'
print(mlflow_pswd)  # Should print the password or None if not set
 