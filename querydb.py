from sqlalchemy import create_engine
import pymysql
import pandas as pd

def main():
 db_connection_str = 'mysql+pymysql://xxuser:welcome1@127.0.0.1/sampledb'
 db_connection = create_engine(db_connection_str)
 pd.set_option('display.expand_frame_repr', True)
#df = pd.read_sql("show tables", con=db_connection)
#print(type(df))
 print('---PRINT XXIBM_PRODUCT_CATALOGUE -----')
#print(df)
#display(df)
 df = pd.read_sql("select * from XXIBM_PRODUCT_CATALOGUE limit 10", con=db_connection)
 print(df.to_string())
#print(df.column_name)
#dbConnection.close()
<<<<<<< HEAD
 print('---PRINT XXXIBM_PRODUCT_PRICING -----')
 df = pd.read_sql("select * from XXIBM_PRODUCT_PRICING limit 10", con=db_connection)
 print(df.to_string())
 print('---PRINT XXXIBM_PRODUCT_SKU -----')
 df = pd.read_sql("select * from XXIBM_PRODUCT_SKU limit 10", con=db_connection)
 print(df.to_string())
 print('---PRINT XXIBM_PRODUCT_STYLE -----')
 df = pd.read_sql("select * from XXIBM_PRODUCT_STYLE limit 10", con=db_connection)
 print(df.to_string())
if __name__ == '__main__':
    main()
=======
print('---PRINT XXXIBM_PRODUCT_PRICING -----')
df = pd.read_sql("select * from XXIBM_PRODUCT_PRICING limit 10", con=db_connection)
print(df.to_string())
print('---PRINT XXXIBM_PRODUCT_SKU -----')
df = pd.read_sql("select * from XXIBM_PRODUCT_SKU limit 10", con=db_connection)
print(df.to_string())
print('---PRINT XXIBM_PRODUCT_STYLE -----')
df = pd.read_sql("select * from XXIBM_PRODUCT_STYLE limit 10", con=db_connection)
print(df.to_string())
>>>>>>> 25e66a6dfda8617d640b0b12404df62f1f23787a
