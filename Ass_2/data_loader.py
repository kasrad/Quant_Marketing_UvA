#%%
#from user_agents import parse
import pandas as pd
from datetime import datetime
colnames = ['bid_id',
            'timestamp',
            'log_type',
            'ipinyou_id',
            'user_agent',
            'ip_address',
            'region_id',
            'city_id',
            'ad_exchange',
            'domain',
            'url',
            'anonymous_url_id',
            'ad_slot_id',
            'ad_slot_width',
            'ad_slot_height',
            'ad_slot_visibility',
            'ad_slot',
            'ad_slot_floor_price',
            'creative_id',
            'bidding_price',
            'paying_price',
            'key_page_url',
            'advertiser_id',
            'user_tags']

colnames_bid = colnames.copy()
colnames_bid.remove('log_type')
colnames_bid.remove('paying_price')
colnames_bid.remove('key_page_url')

#%%
def data_reader(address, colnames, verbose=False, fuck_parsing=True):
    '''
    Imports data with column names
    '''
    data = pd.read_csv(address, sep="\t", names=colnames)
<<<<<<< HEAD
#    data['user_tags'] = [[int(tag) for tag in entry.split(',')] \
#                         if entry != 'null' else None \
#                         for entry in data['user_tags']]
=======
    # data['user_tags'] = [[int(tag) for tag in entry.split(',')] \
    #                      if entry != 'null' else None \
    #                      for entry in data['user_tags']]
>>>>>>> fb225c681bac1bcc023101362bffa9ebecd844cd
    data['timestamp'] = [datetime.strptime(str(entry)[:-3], '%Y%m%d%H%M%S') \
                         for entry in data['timestamp']]
    if not fuck_parsing:
        print('parsing user agent data')
        if verbose:
            print('getting os')
        data = data.assign(os=[parse(str(user_agent)).os.family \
                            for user_agent in data.user_agent])
        if verbose:
            print('getting browser')
        data = data.assign(browser=[parse(str(user_agent)).browser.family
                                for user_agent in data.user_agent])
        if verbose:
            print('getting device')
        data = data.assign(device=[parse(str(user_agent)).device.family
                            for user_agent in data.user_agent])
    
    # print(data['timestamp'])
    return data
