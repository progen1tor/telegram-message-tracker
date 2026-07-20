import logging 
from constants import ALL_MSG_LOG_FILEPATH, TGT_MSG_LOG_FILEPATH, EXP_LOG_FILEPATH

# all messages 
all_messages_logger = logging.getLogger('all_messages')  
all_messages_handler = logging.FileHandler(ALL_MSG_LOG_FILEPATH, mode='a')  
all_messages_logger.setLevel(logging.INFO)
all_messages_logger.addHandler(all_messages_handler)

# targets 
target_messages_logger = logging.getLogger('target_messages')  
target_messages_handler = logging.FileHandler(TGT_MSG_LOG_FILEPATH, mode='a')  
target_messages_logger.setLevel(logging.INFO)
target_messages_logger.addHandler(target_messages_handler)

# errors 
exp_logger = logging.getLogger('tracker')  
exp_handler = logging.FileHandler(EXP_LOG_FILEPATH, mode='a')  
exp_logger.setLevel(logging.ERROR)
exp_logger.addHandler(exp_handler)