.mode columns
.header on


SELECT price, price_types.name, price_date, MAX(p.id) FROM 
        prices p, 
        price_types, 
        tickers 
        where 
        p.ticker_id = tickers.id 
        and 
        price_type_id = price_types.id
        and 
        tickers.ticker = 'AAPL';

SELECT price, price_types.name, MAX(price_date), p.id FROM 
        prices p, 
        price_types, 
        tickers 
        where 
        p.ticker_id = tickers.id 
        and 
        price_type_id = price_types.id
        and 
        tickers.ticker = 'AAPL';
