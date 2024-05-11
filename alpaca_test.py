from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.requests import LimitOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce, QueryOrderStatus
from alpaca.trading.requests import GetOrdersRequest
from alpaca.data.live import StockDataStream

# STREAMING REAL TIME DATA
# stream = StockDataStream("PKZ6T3RIGREDXK18Z645", "4QZGfg3kFqAcWh97AkLfgBbYU70czxo0xIuZ3Gh3")
# async def handle_quote(data):
#     print(data)


# stream.subscribe_trades(handle_quote, "AAPL")
# stream.run()

trading_client = TradingClient("PKZ6T3RIGREDXK18Z645", "4QZGfg3kFqAcWh97AkLfgBbYU70czxo0xIuZ3Gh3")

# Printing the details

# print(trading_client.get_account().account_number)
# print(trading_client.get_account().buying_power)


# BUYING THE STOCK
# MARKET ORDER

# market_order_data = MarketOrderRequest(
#     symbol = "SPY",
#     qty = 1,
#     side = OrderSide.BUY,
#     time_in_force = TimeInForce.DAY
# )

# market_order = trading_client.submit_order(market_order_data)
# print(market_order)



# LIMIT ORDER

limit_order_data = LimitOrderRequest(
    symbol = "SPY",
    qty = 1,
    side = OrderSide.BUY,
    time_in_force = TimeInForce.DAY,
    limit_price = 499.72
)

limit_order = trading_client.submit_order(limit_order_data)
print(limit_order)




# CANCELLING  AND MANAGING LIMIT ORDER
# request_params = GetOrdersRequest(
#     status=QueryOrderStatus.OPEN,
# )

# orders = trading_client.get_orders(request_params)
# # print(orders)

# for order in orders:
#     trading_client.cancel_order_by_id(order.id)





# POSITIONS
# positions = trading_client.get_all_positions()
# print(positions)
# for position in positions:
#     print(position.symbol, position.current_price)




# CANCELLING  ALL ORDERS 

# trading_client.close_all_positions(True)




# For Getting Historical Stock trade data

# from alpaca.data import StockHistoricalDataClient, StockTradesRequest
# from datetime import datetime


# data_client = StockHistoricalDataClient("PKZ6T3RIGREDXK18Z645", "4QZGfg3kFqAcWh97AkLfgBbYU70czxo0xIuZ3Gh3")

# request_params = StockTradesRequest(
#     symbol_or_symbols = "AAPL",
#     start = datetime(2024, 1, 30, 14, 30),
#     end = datetime(2024, 1, 30, 14, 45 )
# )

# trades = data_client.get_stock_trades(request_params)
# # print(trades)


# for trades in trades.data["AAPL"]:
#     print(trades)
#     break



