from ccxt.base.types import Entry
_Dict = dict[str, object]
_List = list[object]


class ImplicitAPI:
    public_get_v1_time = publicGetV1Time = Entry[_Dict]('v1/time', 'public', 'GET', {'cost': 1})
    public_get_v1_tickers = publicGetV1Tickers = Entry[_List]('v1/tickers', 'public', 'GET', {'cost': 1})
    public_get_v1_pairs = publicGetV1Pairs = Entry[_List]('v1/pairs', 'public', 'GET', {'cost': 1})
    public_get_v1_orderbook_pair = publicGetV1OrderbookPair = Entry[_Dict]('v1/orderbook/{pair}', 'public', 'GET', {'cost': 1})
    public_get_v1_candles_pair = publicGetV1CandlesPair = Entry[_List]('v1/candles/{pair}', 'public', 'GET', {'cost': 1})
    public_get_v1_assets = publicGetV1Assets = Entry[_List]('v1/assets', 'public', 'GET', {'cost': 1})
    private_get_v1_account = privateGetV1Account = Entry[_Dict]('v1/account', 'private', 'GET', {'cost': 1})
    private_get_v1_account_balances = privateGetV1AccountBalances = Entry[_List]('v1/account/balances', 'private', 'GET', {'cost': 1})
    private_get_v1_account_orders = privateGetV1AccountOrders = Entry[_Dict]('v1/account/orders', 'private', 'GET', {'cost': 1})
    private_get_v1_account_orders_orderid = privateGetV1AccountOrdersOrderId = Entry[_Dict]('v1/account/orders/{orderId}', 'private', 'GET', {'cost': 1})
    private_get_v1_account_trades = privateGetV1AccountTrades = Entry[_Dict]('v1/account/trades', 'private', 'GET', {'cost': 1})
    private_get_v1_account_trades_tradeid = privateGetV1AccountTradesTradeId = Entry[_Dict]('v1/account/trades/{tradeId}', 'private', 'GET', {'cost': 1})
    private_post_v1_account_orders = privatePostV1AccountOrders = Entry[_Dict]('v1/account/orders', 'private', 'POST', {'cost': 1})
    private_delete_v1_account_orders_orderid = privateDeleteV1AccountOrdersOrderId = Entry[_Dict]('v1/account/orders/{orderId}', 'private', 'DELETE', {'cost': 1})
