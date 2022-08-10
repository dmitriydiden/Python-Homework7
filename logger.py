from datetime import datetime

def recording_logger(data_f, data_r):
    time = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        #file.write('{}; f_result; {}'.format(time, data_f))
        file.write('\n {}; f_result; {} = {}'.format(time, data_f, data_r))
def output_logger():
    path = 'log.csv'
    data = open(path, 'r')
    for line in data:
        print(line)
    data.close()
