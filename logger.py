import datetime
import os


def get_file_name():
  return os.path.join(
      os.path.dirname(__file__),
      os.path.join(f'log_{datetime.datetime.now().strftime("%y_%m_%d")}.txt'))


def log(msg):
  with open(get_file_name(), 'a') as log_file:
    log_file.write(
        f'[{datetime.datetime.now().strftime("%H:%M:%S")}]: {msg}\n')
    print(msg)
