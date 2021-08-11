import pandas as pd

# header=None - Option
iphone_df = pd.read_csv('Lotto.csv', index_col=0)


# iphone_df.loc[] row Data
# iphone_df[] colnum Data
# iphone_df['':''] slirasing colnum Data
# iphone_df.loc[:, '':''] slirasing colnum Data
#colnum
#print(iphone_df[['1', '2']])
#print(iphone_df.loc[:, '2'])
#print(iphone_df.[colnum])


hyundee_df = pd.read_csv('hyundee.csv')
samsong_df = pd.read_csv('samsong.csv')


frame_lst = {
    'day': hyundee_df['요일'],
    'hyundee': hyundee_df['문화생활비'],
    'samsong': samsong_df['문화생활비']
}





