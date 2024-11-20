from pybit.unified_trading import HTTP
import time
session = HTTP(
    testnet=False,
    api_key="smOJZdsX25D1EYURGI",
    api_secret="kQjJ0R6X32FBwSzvR0bEOIpMknNVq0eLmCO1",
)
info,balance,availableToWithdraw1,availableToWithdraw2=0,0,0,0
def current_milli_time():
    return round(time.time() * 1000)
try:
    info = session.get_account_info(category="linear", symbol="BTCUSDT")
except Exception as e:
    print(f"An error occurred: {e}")
def Balance():
    res = '0'
    try:
        balance = session.get_wallet_balance(accountType="UNIFIED", symbol="USDT")
        res = balance['result']['list'][0]['coin'][1]['availableToWithdraw']
    except Exception as e:
        print(f"An error occurred: {e}")
    return res




time.sleep(4)
availableToWithdraw1 =  Balance()
sy='SOL-29NOV24'
qt = '0.04'
res =''
orderId = ''

t0 = current_milli_time()
try:
    res = session.place_order(
        category="linear",
        symbol=sy,
        side="Buy",
        orderType="Market",
        qty=qt)
    orderId = res['result']['orderId']
    #print('ID:'+orderId)
except Exception as e:
    print(f"An error occurred: {e}")
t1 = current_milli_time()
try:
    res = session.place_order(
        category="linear",
        symbol=sy,
        side="Sell",
        orderType="Market",
        qty=qt) 
    #print(res)
except Exception as e:
    print(f"An error occurred: {e}")
t2 = current_milli_time()
availableToWithdraw2 =  Balance()



print('Executing Time : '+str( (t1-t0) )+'ms + '+str(t2-t1)+'ms = '+str(t2-t0)+'ms')
print('Starting Balance: '+availableToWithdraw1+'USDT')
print('Ending Balance: '+availableToWithdraw1+'USDT')