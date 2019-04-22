from quantdata.db.mongo import Mongo
import tushare as ts
import quantdata.cons as ct
from datetime import datetime

ts.set_token(ct.DATA_YES_TOKEN)
st = ts.Market()
#today = datetime.strftime("20160507","%Y%m%d")
df = st.MktEqud(tradeDate="20160506",field="ticker,PB")
df['ticker'] = df['ticker'].map(lambda x: str(x).zfill(6))
df.to_csv("/tmp/pb2.csv")