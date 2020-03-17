#!/usr/bin/env python3
import os
import json
import pump
import schedule
import time
import datetime
import smtplib
from emailer import notify
import logger

RELAY_PIN = 7


def get_schedule():
  schedule_path = os.path.join(os.path.dirname(__file__), 'schedule.json')
  with open(schedule_path, 'r', encoding='utf-8') as schedule_file:
    return json.loads(schedule_file.read())


def flood():
  pump.start()
  logger.log('Flooding system')
  notify(
      'Flooding hydro garden',
      f'Hydro garden flooding starting at {datetime.datetime.now().strftime("%H:%M:%S")}'
  )


def drain():
  pump.stop()
  logger.log('Draining system')
  notify(
      'Draining hydro garden',
      f'Hydro garden draining at {datetime.datetime.now().strftime("%H:%M:%S")}'
  )


def main():
  pump.init(RELAY_PIN)
  time_table = get_schedule()
  logger.log('SYSTEM BOOTING')
  notify(
      'Ebb and flow system starting',
      f'Ebb and flow system starting at {datetime.datetime.now().strftime("%H:%M:%S")} with the following schedule:\n{json.dumps(time_table)}'
  )
  for sched in time_table:
    schedule.every().day.at(sched["start"]).do(flood)
    schedule.every().day.at(sched["end"]).do(drain)
    start_time = datetime.datetime.strptime(sched["start"], '%H:%M').time()
    end_time = datetime.datetime.strptime(sched["end"], '%H:%M').time()
    start = datetime.datetime.now().replace(
        hour=start_time.hour, minute=start_time.minute, second=0)
    end = datetime.datetime.now().replace(
        hour=end_time.hour, minute=end_time.minute, second=0)
    now = datetime.datetime.now()
    if (start < now < end):
      flood()

  while True:
    schedule.run_pending()
    time.sleep(1)


if __name__ == '__main__':
  main()