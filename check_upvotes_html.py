from datetime import datetime
from steem import Steem
from steem.account import Account
s = Steem()

# variables
ACCOUNT_NAME = 'jjb777'
a = Account(ACCOUNT_NAME)
HISTORY_LIMIT = 100
timestamp = datetime.now().strftime('%Y_%m_%d__%H-%M')

# start code
history_events = a.get_account_history(index=-1, limit=HISTORY_LIMIT, filter_by=['vote'], raw_output=True)

file = open('check_upvotes_{}_{}.html'.format(ACCOUNT_NAME, timestamp), 'w')
file.write('<html><body>')
file.write('<h3>Check upvotes for comments and posts for account - {} - {}</h3>'.format(ACCOUNT_NAME, timestamp))
file.write('<table><tr><th>user</th><th>post</th><th>time</th><tr>')

for event in history_events:
  operation = event[1]['op'][0]
  name = event[1]['op'][1]['voter']
  link = event[1]['op'][1]['permlink']
  time = event[1]['timestamp']
  if (name != ACCOUNT_NAME):
    file.write('<tr><td><a href="https://steemit.com/@{}" target="blank">{}</a></td><td align="left"><a href="https://steemit.com/@{}/{}" target="blank">{}</a></td><td align="tight">{}</td></tr>'.format(name, name, ACCOUNT_NAME, link, link, time))

file.write('</table></body></html>')
file.close()



