# -*- coding:utf-8 -*-
"""
Demonstrates how to use the background scheduler to schedule a job that executes on 3 second
intervals.
"""

from datetime import datetime
import time
import os

from apscheduler.schedulers.background import BackgroundScheduler

import pb,pe


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_cron_job(pb.run, day_of_week="1-5", hour='16',minute=30)
    scheduler.add_cron_job(pe.run, day_of_week="1-5", hour='16',minute=40)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
