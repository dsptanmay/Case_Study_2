import csv_ver
import pickle_ver
import questionary
import subprocess as sp
sp.run('pip install --upgrade tabulate', shell=True)
sp.run('pip install --upgrade questionary', shell=True)
option = ['CSV Version', 'Pickle Version']
question = questionary.select('Choose from one of the options below: ', option)
response = question.ask()
if response == option[0]:
    csv_ver.main()
elif response == option[1]:
    pickle_ver.main()
