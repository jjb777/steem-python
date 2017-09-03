from datetime import datetime
from steem import Steem
from steem.converter import Converter

# variables and constants
ACCOUNT_NAME = 'jjb777'
FOLLOWER_SHOW_LIMIT = 1000
dict = {} # dictionary to tmp store accounts
timestamp = datetime.now().strftime('%Y_%m_%d__%H-%M')
s = Steem()

# helper methods
def get_account_from_map(account):
  a = dict.get(account, '')
  if a == '': 
    a = s.get_account(account)
    dict[account] = a
  return a

def get_sp(account):
  a = get_account_from_map(account)
  return round(Converter().vests_to_sp(int(a['vesting_shares'].split('.')[0])))

def get_vp(account):
  a = get_account_from_map(account)
  return '{0:.2f}%'.format(int(a['voting_power'])/100)

# start code
followers = s.get_followers(ACCOUNT_NAME, '', 'blog', FOLLOWER_SHOW_LIMIT)
file = open('followers_{}_{}.html'.format(ACCOUNT_NAME, timestamp), 'w')
file.write('<html><body><table><tr><th>account</th><th>SP</th><th>VP</th><tr>')
file.write('<h3>Followers of <a href="https://steemit.com/@{}" target="blank">{}</a> - {}</h3>'.format(ACCOUNT_NAME, ACCOUNT_NAME, timestamp))

for follower in followers:
  name = follower['follower']
  file.write('<tr><td><a href="https://steemit.com/@{}" target="blank">{}</a></td><td align="right">{}</td><td align="right">{}</td></tr>'.format(name, name, get_sp(name), get_vp(name)))

file.write('</table></body></html>')
file.close()

