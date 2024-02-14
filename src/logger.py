import logging     #alternate code to make logs at same llevel with src
import os
from datetime import datetime

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Navigate up one level to the parent directory
parent_dir = os.path.dirname(script_dir)

# Define the path to the logs directory at the same level as src
logs_dir = os.path.join(parent_dir, "logs")

# Create the logs directory if it doesn't exist
os.makedirs(logs_dir, exist_ok=True)

LOG_FILE = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"

# Define the log file path using the current timestamp
LOG_FILE_PATH = os.path.join(logs_dir,LOG_FILE )

# Configure the logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ]%(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# # Log a message to indicate that logging has started
# if __name__== "__main__":
#     logging.info('Logging has started')





# import logging                      ###code executing but not making logs folder
# import os
# from datetime import datetime

# LOG_FILE = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"
# #logs_path = os.path.join(os.getcwd(),"logs")
# script_dir = os.path.dirname(os.path.abspath(__file__))
# logs_path = os.path.join(script_dir, "logs")

# os.makedirs(logs_path,exist_ok = True)


# LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)


# logging.basicConfig(
#     filename = LOG_FILE_PATH,
#     format = "[ %(asctime)s ]%(lineno)d %(name)s - %(levelname)s - %(message)s",
#     level = logging.INFO,

# )


# if __name__== "__main__":
#     logging.info('Logging has started')
    
    


