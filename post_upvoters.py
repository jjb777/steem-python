from datetime import datetime
from steem import Steem
timestamp = datetime.now().strftime('%Y_%m_%d__%H-%M')
s = Steem()

# variables
ACCOUNT_NAME = 'jjb777'
POST_NAME = 'check-your-followers-with-steem-python'
# from https://steemd.com/
reward_balance = 689021.232 #steem
recent_payouts = 253293929348078529 #rshares
steem_price = 1.327

rshares_sdb_value = steem_price * (reward_balance / recent_payouts)

print(reward_balance)
print(recent_payouts)
print(rshares_sdb_value)

# start code
voters = s.get_active_votes(ACCOUNT_NAME, POST_NAME)

file = open('upvoters_post_{}_{}.html'.format(ACCOUNT_NAME, timestamp), 'w')
file.write('<html><body><table><tr><th>account</th><th>percent</th><th>upvote</th><th>time</th><tr>')
file.write('<h3>Upvoters of post <a href="https://steemit.com/@{}/" target="blank">{}</a> - {}</h3>'.format(ACCOUNT_NAME, ACCOUNT_NAME, POST_NAME, timestamp))

count_sdb = 0.0

for voter in voters:
    name = voter['voter']
    percent = voter['percent']
    rshares = voter['rshares']
    time = voter['time']
    current_sdb = float(rshares) * rshares_sdb_value
    count_sdb = count_sdb + current_sdb
    file.write('<tr><td><a href="https://steemit.com/@{}" target="blank">{}</a></td><td align="right">{}</td><td align="right">{}</td><td align="right">{}</td></tr>'.format(name, name, '{:10.2f}%'.format(percent/100), '{:10.3f} sdb'.format(current_sdb), time))

file.write('<tr><td></td><td></td><td>{:10.3f} sdb</td><td></td>'.format(count_sdb))
file.write('</table></body></html>')
file.close()


