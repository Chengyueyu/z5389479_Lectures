import yfinance as yf
def yf_prc_to_csv(tic, pth, start = None, end = None):
    df = yf.download(tic, start=start, end=end, ignore_tz=True)
    df.to_csv(pth)
if_name_ == "__main__"
tic = 'QAN.AX'
datadir = ''
pth = 'qan_stk_prc.csv'
yf_prc_to_csv(tic, pth)