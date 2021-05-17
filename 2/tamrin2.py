import datetime

import jdatetime



now = datetime.datetime.today()
with open('test.txt', 'w') as opened_file:


    today = jdatetime.date.today()
    print('open by:', today)


