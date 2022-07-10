from decouple import config
from crontab import CronTab

"""
This script will serve as a watcher script for any project.
It will make use of a cron job to run at the specified interval
"""

cron = CronTab(user=True)
command = config('CRON_COMMAND', default='')

if not command and command=='':
    print('No cron command specified')
    exit()

job = cron.new(
    command=config('COMMAND_TO_RUN')
    )

# Set the interval to run the script
hour = config('HOUR', default=0, cast=int)
minute = config('MINUTE', default=0, cast=int)

if hour == 0 and minute == 0:
    print('One of hour or minute is not set')
    exit()

frequency_command = (
    f"{minute} 0-23/{hour} * * *"
    if hour != 0
    else f"1-59/{minute} * * *"
)

job.setall(frequency_command)

job.dow.on('SAT','SUN')

job.run()