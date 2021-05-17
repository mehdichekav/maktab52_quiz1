import datetime

import jdatetime



now = datetime.datetime.today()
with open('test.txt', 'w') as opened_file:
    # opened_file.write()
    # fa_date = jdatetime.date(jdatetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S"))

    today = jdatetime.date.today()
    print('open by:', today)
# f.close()
# print('close by', today)

