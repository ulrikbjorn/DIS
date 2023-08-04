
-- Investors
INSERT INTO public.investors(user_ID, password, name, balance) VALUES (3000, '$2b$12$Kwp8aa8YWiksx6ImKJJB5uboziQe5Dj29gHOlhHy8fYy98qMwz0DK', 'Sam Bankman-Fraud',400);
INSERT INTO public.investors(user_ID, password, name, balance) VALUES (3001, '$2b$12$Kwp8aa8YWiksx6ImKJJB5uboziQe5Dj29gHOlhHy8fYy98qMwz0DK', 'Keith Goll',800);
INSERT INTO public.investors(user_ID, password, name, balance) VALUES (3002, '$2b$12$Kwp8aa8YWiksx6ImKJJB5uboziQe5Dj29gHOlhHy8fYy98qMwz0DK', 'George Soras',10000);
INSERT INTO public.investors(user_ID, password, name, balance) VALUES (3003, '$2b$12$Kwp8aa8YWiksx6ImKJJB5uboziQe5Dj29gHOlhHy8fYy98qMwz0DK', 'Vladimir Tinov',3200);

-- Portfolios 
INSERT INTO public.portfolios(record_ID, user_ID, ticker_symbol, purchase_price, quantity) VALUES (0100, 3000, 'TSLA', 248, 100);
INSERT INTO public.portfolios(record_ID, user_ID, ticker_symbol, purchase_price, quantity) VALUES (0101, 3000, 'APPL', 110, 400);
INSERT INTO public.portfolios(record_ID, user_ID, ticker_symbol, purchase_price, quantity) VALUES (0102, 3000, 'MSFT', 300, 200);
INSERT INTO public.portfolios(record_ID, user_ID, ticker_symbol, purchase_price, quantity) VALUES (0103, 3000, 'NVDA', 400, 300);
INSERT INTO public.portfolios(record_ID, user_ID, ticker_symbol, purchase_price, quantity) VALUES (0104, 3000, 'META', 310, 50);
INSERT INTO public.portfolios(record_ID, user_ID, ticker_symbol, purchase_price, quantity) VALUES (0105, 3001, 'TSLA', 900, 10);
INSERT INTO public.portfolios(record_ID, user_ID, ticker_symbol, purchase_price, quantity) VALUES (0106, 3001, 'APPL', 500, 40);
INSERT INTO public.portfolios(record_ID, user_ID, ticker_symbol, purchase_price, quantity) VALUES (0107, 3001, 'MSFT', 600, 20);
INSERT INTO public.portfolios(record_ID, user_ID, ticker_symbol, purchase_price, quantity) VALUES (0108, 3002, 'TSLA', 710, 1000);
INSERT INTO public.portfolios(record_ID, user_ID, ticker_symbol, purchase_price, quantity) VALUES (0109, 3002, 'APPL', 180, 4000);
INSERT INTO public.portfolios(record_ID, user_ID, ticker_symbol, purchase_price, quantity) VALUES (0110, 3003, 'TSLA', 24, 10000);


-- Market
INSERT INTO public.market(ticker_symbol, current_price) VALUES ('TSLA', 259);
INSERT INTO public.market(ticker_symbol, current_price) VALUES ('APPL', 191);
INSERT INTO public.market(ticker_symbol, current_price) VALUES ('MSFT', 326);
INSERT INTO public.market(ticker_symbol, current_price) VALUES ('NVDA', 445);
INSERT INTO public.market(ticker_symbol, current_price) VALUES ('META', 313);

