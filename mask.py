

##### frames = pd.read_excel('./Billboard Hot 100 Number Ones Database.xlsx', sheet_name=None)
df = frames['Data']
maska = df['Weeks at Number One'] == 13
maskb = df['Weeks at Number One'] > 5 
maskc = df['Artist'] == 'Michael Jackson'
maskd = df['Song'] == 'Not Like Us'
mask = maska | maskb
#### print(frames['Data Dictionary']['Category'].value_counts())
#### print(df['Weeks at Number One'].value_counts())
