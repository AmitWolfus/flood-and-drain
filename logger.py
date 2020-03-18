import datetime
import os


def get_file_name():
  return os.path.join(
      os.path.dirname(__file__),
      os.path.join('log_{}.txt'.format(
          datetime.datetime.now().strftime("%y_%m_%d"))))


def log(msg):
  with open(get_file_name(), 'a') as log_file:
    log_file.write('[{}]: {}\n'.format(
        datetime.datetime.now().strftime("%H:%M:%S"), msg))
    print(msg)
