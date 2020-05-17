import pandas as pd

read_file = pd.read_csv('credit_approval_data_set\crx.data')
read_file.to_csv ('credit_approval_data_set\credit_card_data.csv',index=False)