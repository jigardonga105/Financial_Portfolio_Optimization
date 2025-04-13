index = [
    '^NSEI', # NIFTY 50
    '^NSEBANK', # NIFTY BANK
    '^CNXIT', # NIFTY IT
    '^BSESN', # S&P BSE SENSEX
    'NIFTY_MIDCAP_100.NS',
    '^CNXPSUBANK',
    '^CNXAUTO',
    'NIFTY_FIN_SERVICE.NS'
]

share_name = [
    "ADANIENT.NS", "ASIANPAINT.NS", "AXISBANK.NS", "BAJAJ-AUTO.NS", "BAJFINANCE.NS", 
    "BAJAJFINSV.NS", "BHARTIARTL.NS", "BPCL.NS", "BRITANNIA.NS", "CIPLA.NS", 
    "COALINDIA.NS", "DIVISLAB.NS", "DRREDDY.NS", "EICHERMOT.NS", "GRASIM.NS", 
    "HCLTECH.NS", "HDFCBANK.NS", "HDFCLIFE.NS", "HEROMOTOCO.NS", "HINDALCO.NS", 
    "HINDUNILVR.NS", "ICICIBANK.NS", "ITC.NS", "INDUSINDBK.NS", "INFY.NS", 
    "JSWSTEEL.NS", "KOTAKBANK.NS", "LT.NS", "M&M.NS", "MARUTI.NS", 
    "NESTLEIND.NS", "NTPC.NS", "ONGC.NS", "POWERGRID.NS", "RELIANCE.NS", 
    "SBILIFE.NS", "SBIN.NS", "SUNPHARMA.NS", "TCS.NS", "TATACONSUM.NS", 
    "TATAMOTORS.NS", "TATASTEEL.NS", "TECHM.NS", "TITAN.NS", "ULTRACEMCO.NS", 
    "UPL.NS", "WIPRO.NS", "APOLLOHOSP.NS", "ADANIPORTS.NS", "JSWENERGY.NS"
]

mutual_funds = [
    '0P00005WL6.BO',
    'UTINEXT50.BO',
    '0P0000MLHH.BO',
    '0P0000KV39.BO',
    '0P00009J3K.BO',
    '0P0001BAB5.BO',
    '0P0001EI18.BO',
    '0P0001BA1R.BO',
    '0P00005WEY.BO',
    '0P0000XUXL.BO',
    '0P0000XUYZ.BO',
    '0P0000XW8D.BO',
    '0P0000XVER.BO',
    '0P0000XUYS.BO',
    '0P0000XW7I.BO',
    '0P0000U3OG.BO',
    'SETFGOLD.NS',
    'BSLGOLDETF.NS'
]

index = {
    '^NSEI': 'NIFTY 50',
    '^NSEBANK': 'NIFTY BANK',
    '^CNXIT': 'NIFTY IT',
    '^BSESN': 'S&P BSE SENSEX',
    'NIFTY_MIDCAP_100.NS': 'NIFTY MIDCAP 100',
    '^CNXPSUBANK': 'NIFTY PSU BANK',
    '^CNXAUTO': 'NIFTY AUTO',
    'NIFTY_FIN_SERVICE.NS': 'NIFTY FIN SERVICE'
}

mutual_funds_names = {
    '0P00005WL6.BO': 'UTI Nifty 50 Index Fund',
    'UTINEXT50.BO': 'UTI-Nifty Next 50 Exchange Traded Fund',
    '0P0000MLHH.BO': 'Axis Bluechip Fund Gr',
    '0P0000KV39.BO': 'SBI Small Cap Fund Reg Gr',
    '0P00009J3K.BO': 'HDFC Mid-Cap Opportunities Gr',
    '0P0001BAB5.BO': 'ICICI Prudential Equity & Debt Fund',
    '0P0001EI18.BO': 'HDFC Hybrid Eq Dir Gr',
    '0P0001BA1R.BO': 'Edelweiss Balanced Advantage Fund',
    '0P00005WEY.BO': 'SBI Equity Hybrid Fund',
    '0P0000XUXL.BO': 'Axis Banking & PSU Debt Dir Gr',
    '0P0000XUYZ.BO': 'ICICI Pru Short Term Dir Gr',
    '0P0000XW8D.BO': 'HDFC Corporate Bond Dir Gr',
    '0P0000XVER.BO': 'Nippon India Liquid Dir Gr',
    '0P0000XUYS.BO': 'ICICI Pru Nifty Next 50 Index Dir Gr',
    '0P0000XW7I.BO': 'HDFC Gold Dir Gr',
    '0P0000U3OG.BO': 'ICICI Prudential Regular Gold Savings Fund(FOF) Growth',
    'SETFGOLD.NS': 'SBI Gold ETF',
    'BSLGOLDETF.NS': 'Aditya Birla Sun Life Gold ETF'
}

fd_data = {
    "Bank Name": [
        "ICICI Bank", 
        "HDFC Bank", 
        "Axis Bank", 
        "Bank of Baroda", 
        "State Bank of India", 
        "Bank Of India", 
        "Equitas small finance bank", 
        "AU small finance bank"
    ],
    "Return Rate for Adults (%)": [6.7, 6.6, 6.7, 6.85, 6.8, 6.8, 7.0, 7.25],
    "Return Rate for Senior Citizens (%)": [7.2, 7.1, 7.2, 7.35, 7.3, 7.3, 7.2, 7.75]
}

index_features = ['High_Low_Change', 'Daily_Range', 'MACD', 'ATR', 'Rolling_Std_Dev']
mutual_funds_features = ['Percent_Change_In_Price', 'High_Low_Change', 'RSI', 'Daily_Range', 'Close_Low_Ratio', 'MACD', 'ATR', 'Rolling_Std_Dev']
gold_bond_features = ['Percent_Change_In_Price', 'High_Low_Change', 'RSI', 'MACD', 'ATR', 'Rolling_Std_Dev', 'High_Open_Change']