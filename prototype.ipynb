{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "693ae819-af4d-4dd0-942e-29d5195a8166",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from pandas_datareader import data as pdr\n",
    "from datetime import date\n",
    "import plotly.express as px"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2a9ddc19-ba7d-47ef-8c9c-1caeaa5f6f78",
   "metadata": {},
   "source": [
    "## Parameters"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 371,
   "id": "2b999df8-7565-4dba-8dbe-5a4c40b7cc8d",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#Creating variables to store start and end date of analysis\n",
    "start_date = '2022-01-01'\n",
    "end_date = date.today()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 369,
   "id": "d5051950-775a-4a39-8504-c3846b9d365e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#We are going to store all the tickers for the companies in our investment portfolio in a variable named wallet. Later, we will iterate over this variable in order to pull our data\n",
    "wallet = ['CIEL3', 'BRFS3', 'BBDC4', 'ENEV3']"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d1a82569-0946-4f78-8c21-eda3b29a4640",
   "metadata": {
    "tags": []
   },
   "source": [
    "## First, let's pull data for our reference index (IBOVESPA)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 372,
   "id": "f47a7ab4-80bb-4bc0-9bf4-208647ed55c7",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Reading data using pandas datareader and cleaning column names\n",
    "ibov = pdr.DataReader(f'^BVSP', data_source='yahoo', start=start_date, end=end_date)\n",
    "ibov.reset_index(drop=False, inplace=True)\n",
    "ibov = ibov[['Date', 'Close']] #we are only interested in the closing prices\n",
    "ibov.rename(columns={'Date':'date', 'Close':'ibov_close'}, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 373,
   "id": "993128da-e77b-413e-a426-fbed2ed42426",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>date</th>\n",
       "      <th>ibov_close</th>\n",
       "      <th>ibov_cum_change</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2022-01-03</td>\n",
       "      <td>103922.00000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2022-01-04</td>\n",
       "      <td>103514.00000</td>\n",
       "      <td>-0.392602</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2022-01-05</td>\n",
       "      <td>101006.00000</td>\n",
       "      <td>-2.805951</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2022-01-06</td>\n",
       "      <td>101561.00000</td>\n",
       "      <td>-2.271896</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2022-01-07</td>\n",
       "      <td>102719.00000</td>\n",
       "      <td>-1.157599</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>121</th>\n",
       "      <td>2022-06-28</td>\n",
       "      <td>100591.00000</td>\n",
       "      <td>-3.205289</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>122</th>\n",
       "      <td>2022-06-29</td>\n",
       "      <td>99622.00000</td>\n",
       "      <td>-4.137719</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>123</th>\n",
       "      <td>2022-06-30</td>\n",
       "      <td>98542.00000</td>\n",
       "      <td>-5.176960</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>124</th>\n",
       "      <td>2022-07-01</td>\n",
       "      <td>98954.00000</td>\n",
       "      <td>-4.780508</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>125</th>\n",
       "      <td>2022-07-04</td>\n",
       "      <td>98784.09375</td>\n",
       "      <td>-4.944002</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>126 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "          date    ibov_close  ibov_cum_change\n",
       "0   2022-01-03  103922.00000         0.000000\n",
       "1   2022-01-04  103514.00000        -0.392602\n",
       "2   2022-01-05  101006.00000        -2.805951\n",
       "3   2022-01-06  101561.00000        -2.271896\n",
       "4   2022-01-07  102719.00000        -1.157599\n",
       "..         ...           ...              ...\n",
       "121 2022-06-28  100591.00000        -3.205289\n",
       "122 2022-06-29   99622.00000        -4.137719\n",
       "123 2022-06-30   98542.00000        -5.176960\n",
       "124 2022-07-01   98954.00000        -4.780508\n",
       "125 2022-07-04   98784.09375        -4.944002\n",
       "\n",
       "[126 rows x 3 columns]"
      ]
     },
     "execution_count": 373,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Creating the cumulative change column. This way, we can easily compare performance across multiple companies\n",
    "reference = ibov.at[0,\"ibov_close\"]\n",
    "ibov['ibov_cum_change'] = ibov['ibov_close'].apply(lambda x: (x-reference)*100/reference)\n",
    "ibov"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "476292ab-fafa-44c3-a6e8-5f2b54bcd93f",
   "metadata": {
    "tags": []
   },
   "source": [
    "## Now, let's pull data for our investment portfolio"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 374,
   "id": "71d500d5-18fe-472b-a1fa-b2e14114708e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>date</th>\n",
       "      <th>CIEL3_close</th>\n",
       "      <th>CIEL3_cum_change</th>\n",
       "      <th>BRFS3_close</th>\n",
       "      <th>BRFS3_cum_change</th>\n",
       "      <th>BBDC4_close</th>\n",
       "      <th>BBDC4_cum_change</th>\n",
       "      <th>ENEV3_close</th>\n",
       "      <th>ENEV3_cum_change</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2022-01-03</td>\n",
       "      <td>2.19</td>\n",
       "      <td>0.0</td>\n",
       "      <td>23.219999</td>\n",
       "      <td>0.0</td>\n",
       "      <td>17.9</td>\n",
       "      <td>0.0</td>\n",
       "      <td>13.44</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2022-01-04</td>\n",
       "      <td>2.12</td>\n",
       "      <td>-3.196355</td>\n",
       "      <td>22.42</td>\n",
       "      <td>-3.445303</td>\n",
       "      <td>18.0</td>\n",
       "      <td>0.558661</td>\n",
       "      <td>12.91</td>\n",
       "      <td>-3.943451</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2022-01-05</td>\n",
       "      <td>2.11</td>\n",
       "      <td>-3.652975</td>\n",
       "      <td>22.700001</td>\n",
       "      <td>-2.239443</td>\n",
       "      <td>17.872726</td>\n",
       "      <td>-0.152364</td>\n",
       "      <td>12.4</td>\n",
       "      <td>-7.738095</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2022-01-06</td>\n",
       "      <td>2.06</td>\n",
       "      <td>-5.936078</td>\n",
       "      <td>24.299999</td>\n",
       "      <td>4.651163</td>\n",
       "      <td>18.127272</td>\n",
       "      <td>1.269676</td>\n",
       "      <td>12.21</td>\n",
       "      <td>-9.151783</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2022-01-07</td>\n",
       "      <td>2.05</td>\n",
       "      <td>-6.392699</td>\n",
       "      <td>24.6</td>\n",
       "      <td>5.943157</td>\n",
       "      <td>18.390909</td>\n",
       "      <td>2.742512</td>\n",
       "      <td>11.93</td>\n",
       "      <td>-11.235114</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>121</th>\n",
       "      <td>2022-06-28</td>\n",
       "      <td>3.85</td>\n",
       "      <td>75.799078</td>\n",
       "      <td>14.48</td>\n",
       "      <td>-37.639966</td>\n",
       "      <td>17.91</td>\n",
       "      <td>0.055867</td>\n",
       "      <td>15.35</td>\n",
       "      <td>14.211316</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>122</th>\n",
       "      <td>2022-06-29</td>\n",
       "      <td>3.78</td>\n",
       "      <td>72.602734</td>\n",
       "      <td>14.14</td>\n",
       "      <td>-39.104217</td>\n",
       "      <td>17.6</td>\n",
       "      <td>-1.675973</td>\n",
       "      <td>14.97</td>\n",
       "      <td>11.383934</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>123</th>\n",
       "      <td>2022-06-30</td>\n",
       "      <td>3.75</td>\n",
       "      <td>71.232872</td>\n",
       "      <td>13.59</td>\n",
       "      <td>-41.472866</td>\n",
       "      <td>17.200001</td>\n",
       "      <td>-3.910608</td>\n",
       "      <td>14.77</td>\n",
       "      <td>9.89584</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>124</th>\n",
       "      <td>2022-07-01</td>\n",
       "      <td>3.93</td>\n",
       "      <td>79.452053</td>\n",
       "      <td>14.28</td>\n",
       "      <td>-38.501291</td>\n",
       "      <td>17.33</td>\n",
       "      <td>-3.184356</td>\n",
       "      <td>15.14</td>\n",
       "      <td>12.648816</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>125</th>\n",
       "      <td>2022-07-04</td>\n",
       "      <td>3.87</td>\n",
       "      <td>76.712319</td>\n",
       "      <td>14.72</td>\n",
       "      <td>-36.606371</td>\n",
       "      <td>17.15</td>\n",
       "      <td>-4.189944</td>\n",
       "      <td>14.83</td>\n",
       "      <td>10.342265</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>126 rows × 9 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "          date CIEL3_close CIEL3_cum_change BRFS3_close BRFS3_cum_change  \\\n",
       "0   2022-01-03        2.19              0.0   23.219999              0.0   \n",
       "1   2022-01-04        2.12        -3.196355       22.42        -3.445303   \n",
       "2   2022-01-05        2.11        -3.652975   22.700001        -2.239443   \n",
       "3   2022-01-06        2.06        -5.936078   24.299999         4.651163   \n",
       "4   2022-01-07        2.05        -6.392699        24.6         5.943157   \n",
       "..         ...         ...              ...         ...              ...   \n",
       "121 2022-06-28        3.85        75.799078       14.48       -37.639966   \n",
       "122 2022-06-29        3.78        72.602734       14.14       -39.104217   \n",
       "123 2022-06-30        3.75        71.232872       13.59       -41.472866   \n",
       "124 2022-07-01        3.93        79.452053       14.28       -38.501291   \n",
       "125 2022-07-04        3.87        76.712319       14.72       -36.606371   \n",
       "\n",
       "    BBDC4_close BBDC4_cum_change ENEV3_close ENEV3_cum_change  \n",
       "0          17.9              0.0       13.44              0.0  \n",
       "1          18.0         0.558661       12.91        -3.943451  \n",
       "2     17.872726        -0.152364        12.4        -7.738095  \n",
       "3     18.127272         1.269676       12.21        -9.151783  \n",
       "4     18.390909         2.742512       11.93       -11.235114  \n",
       "..          ...              ...         ...              ...  \n",
       "121       17.91         0.055867       15.35        14.211316  \n",
       "122        17.6        -1.675973       14.97        11.383934  \n",
       "123   17.200001        -3.910608       14.77          9.89584  \n",
       "124       17.33        -3.184356       15.14        12.648816  \n",
       "125       17.15        -4.189944       14.83        10.342265  \n",
       "\n",
       "[126 rows x 9 columns]"
      ]
     },
     "execution_count": 374,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_holder = []\n",
    "\n",
    "for stock in wallet:\n",
    "    #Reading data and cleaning column names\n",
    "    temp_df = pdr.DataReader(f'{stock}.SA', data_source='yahoo', start=start_date, end=end_date)\n",
    "    temp_df.reset_index(drop=False, inplace=True)\n",
    "    temp_df = temp_df[['Date', 'Close']]\n",
    "    temp_df.rename(columns={'Date':'date', 'Close':f'{stock}_close'}, inplace=True)\n",
    "    \n",
    "    #Creating the cumulative change column\n",
    "    reference = temp_df.at[0,f'{stock}_close']\n",
    "    temp_df[f'{stock}_cum_change'] = temp_df[f'{stock}_close'].apply(lambda x: (x-reference)*100/reference)\n",
    "    \n",
    "    #Appending our temporary dataframe to our empty list, which will be later concatenated\n",
    "    df_holder.append(temp_df)\n",
    "    \n",
    "#Lastly, lets concat our temp dataframes dropping duplicates - date column\n",
    "wallet_df = pd.concat(df_holder, axis=1).T.drop_duplicates().T\n",
    "wallet_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 375,
   "id": "0f59d7fd-ac3e-48a8-92c8-1a2f0fce4c1c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>date</th>\n",
       "      <th>ibov_close</th>\n",
       "      <th>ibov_cum_change</th>\n",
       "      <th>CIEL3_close</th>\n",
       "      <th>CIEL3_cum_change</th>\n",
       "      <th>BRFS3_close</th>\n",
       "      <th>BRFS3_cum_change</th>\n",
       "      <th>BBDC4_close</th>\n",
       "      <th>BBDC4_cum_change</th>\n",
       "      <th>ENEV3_close</th>\n",
       "      <th>ENEV3_cum_change</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2022-01-03</td>\n",
       "      <td>103922.00000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>2.19</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>23.219999</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>17.900000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>13.44</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2022-01-04</td>\n",
       "      <td>103514.00000</td>\n",
       "      <td>-0.392602</td>\n",
       "      <td>2.12</td>\n",
       "      <td>-3.196355</td>\n",
       "      <td>22.420000</td>\n",
       "      <td>-3.445303</td>\n",
       "      <td>18.000000</td>\n",
       "      <td>0.558661</td>\n",
       "      <td>12.91</td>\n",
       "      <td>-3.943451</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2022-01-05</td>\n",
       "      <td>101006.00000</td>\n",
       "      <td>-2.805951</td>\n",
       "      <td>2.11</td>\n",
       "      <td>-3.652975</td>\n",
       "      <td>22.700001</td>\n",
       "      <td>-2.239443</td>\n",
       "      <td>17.872726</td>\n",
       "      <td>-0.152364</td>\n",
       "      <td>12.40</td>\n",
       "      <td>-7.738095</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2022-01-06</td>\n",
       "      <td>101561.00000</td>\n",
       "      <td>-2.271896</td>\n",
       "      <td>2.06</td>\n",
       "      <td>-5.936078</td>\n",
       "      <td>24.299999</td>\n",
       "      <td>4.651163</td>\n",
       "      <td>18.127272</td>\n",
       "      <td>1.269676</td>\n",
       "      <td>12.21</td>\n",
       "      <td>-9.151783</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2022-01-07</td>\n",
       "      <td>102719.00000</td>\n",
       "      <td>-1.157599</td>\n",
       "      <td>2.05</td>\n",
       "      <td>-6.392699</td>\n",
       "      <td>24.600000</td>\n",
       "      <td>5.943157</td>\n",
       "      <td>18.390909</td>\n",
       "      <td>2.742512</td>\n",
       "      <td>11.93</td>\n",
       "      <td>-11.235114</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>121</th>\n",
       "      <td>2022-06-28</td>\n",
       "      <td>100591.00000</td>\n",
       "      <td>-3.205289</td>\n",
       "      <td>3.85</td>\n",
       "      <td>75.799078</td>\n",
       "      <td>14.480000</td>\n",
       "      <td>-37.639966</td>\n",
       "      <td>17.910000</td>\n",
       "      <td>0.055867</td>\n",
       "      <td>15.35</td>\n",
       "      <td>14.211316</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>122</th>\n",
       "      <td>2022-06-29</td>\n",
       "      <td>99622.00000</td>\n",
       "      <td>-4.137719</td>\n",
       "      <td>3.78</td>\n",
       "      <td>72.602734</td>\n",
       "      <td>14.140000</td>\n",
       "      <td>-39.104217</td>\n",
       "      <td>17.600000</td>\n",
       "      <td>-1.675973</td>\n",
       "      <td>14.97</td>\n",
       "      <td>11.383934</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>123</th>\n",
       "      <td>2022-06-30</td>\n",
       "      <td>98542.00000</td>\n",
       "      <td>-5.176960</td>\n",
       "      <td>3.75</td>\n",
       "      <td>71.232872</td>\n",
       "      <td>13.590000</td>\n",
       "      <td>-41.472866</td>\n",
       "      <td>17.200001</td>\n",
       "      <td>-3.910608</td>\n",
       "      <td>14.77</td>\n",
       "      <td>9.895840</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>124</th>\n",
       "      <td>2022-07-01</td>\n",
       "      <td>98954.00000</td>\n",
       "      <td>-4.780508</td>\n",
       "      <td>3.93</td>\n",
       "      <td>79.452053</td>\n",
       "      <td>14.280000</td>\n",
       "      <td>-38.501291</td>\n",
       "      <td>17.330000</td>\n",
       "      <td>-3.184356</td>\n",
       "      <td>15.14</td>\n",
       "      <td>12.648816</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>125</th>\n",
       "      <td>2022-07-04</td>\n",
       "      <td>98784.09375</td>\n",
       "      <td>-4.944002</td>\n",
       "      <td>3.87</td>\n",
       "      <td>76.712319</td>\n",
       "      <td>14.720000</td>\n",
       "      <td>-36.606371</td>\n",
       "      <td>17.150000</td>\n",
       "      <td>-4.189944</td>\n",
       "      <td>14.83</td>\n",
       "      <td>10.342265</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>126 rows × 11 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "          date    ibov_close  ibov_cum_change  CIEL3_close  CIEL3_cum_change  \\\n",
       "0   2022-01-03  103922.00000         0.000000         2.19          0.000000   \n",
       "1   2022-01-04  103514.00000        -0.392602         2.12         -3.196355   \n",
       "2   2022-01-05  101006.00000        -2.805951         2.11         -3.652975   \n",
       "3   2022-01-06  101561.00000        -2.271896         2.06         -5.936078   \n",
       "4   2022-01-07  102719.00000        -1.157599         2.05         -6.392699   \n",
       "..         ...           ...              ...          ...               ...   \n",
       "121 2022-06-28  100591.00000        -3.205289         3.85         75.799078   \n",
       "122 2022-06-29   99622.00000        -4.137719         3.78         72.602734   \n",
       "123 2022-06-30   98542.00000        -5.176960         3.75         71.232872   \n",
       "124 2022-07-01   98954.00000        -4.780508         3.93         79.452053   \n",
       "125 2022-07-04   98784.09375        -4.944002         3.87         76.712319   \n",
       "\n",
       "     BRFS3_close  BRFS3_cum_change  BBDC4_close  BBDC4_cum_change  \\\n",
       "0      23.219999          0.000000    17.900000          0.000000   \n",
       "1      22.420000         -3.445303    18.000000          0.558661   \n",
       "2      22.700001         -2.239443    17.872726         -0.152364   \n",
       "3      24.299999          4.651163    18.127272          1.269676   \n",
       "4      24.600000          5.943157    18.390909          2.742512   \n",
       "..           ...               ...          ...               ...   \n",
       "121    14.480000        -37.639966    17.910000          0.055867   \n",
       "122    14.140000        -39.104217    17.600000         -1.675973   \n",
       "123    13.590000        -41.472866    17.200001         -3.910608   \n",
       "124    14.280000        -38.501291    17.330000         -3.184356   \n",
       "125    14.720000        -36.606371    17.150000         -4.189944   \n",
       "\n",
       "     ENEV3_close  ENEV3_cum_change  \n",
       "0          13.44          0.000000  \n",
       "1          12.91         -3.943451  \n",
       "2          12.40         -7.738095  \n",
       "3          12.21         -9.151783  \n",
       "4          11.93        -11.235114  \n",
       "..           ...               ...  \n",
       "121        15.35         14.211316  \n",
       "122        14.97         11.383934  \n",
       "123        14.77          9.895840  \n",
       "124        15.14         12.648816  \n",
       "125        14.83         10.342265  \n",
       "\n",
       "[126 rows x 11 columns]"
      ]
     },
     "execution_count": 375,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Finally, let's merge the index dataframe with our wallet dataframe\n",
    "final_df = pd.merge(ibov, wallet_df, on='date')\n",
    "final_df.iloc[:,1:].apply(pd.to_numeric)\n",
    "for column in final_df.columns:\n",
    "    if column not in ['date']:\n",
    "        final_df[column] = final_df[column].astype(float)\n",
    "final_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 376,
   "id": "e95b9477-699d-4140-963b-c1874c2d3c61",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>date</th>\n",
       "      <th>ibov_close</th>\n",
       "      <th>ibov_cum_change</th>\n",
       "      <th>CIEL3_close</th>\n",
       "      <th>CIEL3_cum_change</th>\n",
       "      <th>BRFS3_close</th>\n",
       "      <th>BRFS3_cum_change</th>\n",
       "      <th>BBDC4_close</th>\n",
       "      <th>BBDC4_cum_change</th>\n",
       "      <th>ENEV3_close</th>\n",
       "      <th>ENEV3_cum_change</th>\n",
       "      <th>total_cum_change</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2022-01-03</td>\n",
       "      <td>103922.00000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>2.19</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>23.219999</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>17.900000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>13.44</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2022-01-04</td>\n",
       "      <td>103514.00000</td>\n",
       "      <td>-0.392602</td>\n",
       "      <td>2.12</td>\n",
       "      <td>-3.196355</td>\n",
       "      <td>22.420000</td>\n",
       "      <td>-3.445303</td>\n",
       "      <td>18.000000</td>\n",
       "      <td>0.558661</td>\n",
       "      <td>12.91</td>\n",
       "      <td>-3.943451</td>\n",
       "      <td>-2.506612</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2022-01-05</td>\n",
       "      <td>101006.00000</td>\n",
       "      <td>-2.805951</td>\n",
       "      <td>2.11</td>\n",
       "      <td>-3.652975</td>\n",
       "      <td>22.700001</td>\n",
       "      <td>-2.239443</td>\n",
       "      <td>17.872726</td>\n",
       "      <td>-0.152364</td>\n",
       "      <td>12.40</td>\n",
       "      <td>-7.738095</td>\n",
       "      <td>-3.445719</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2022-01-06</td>\n",
       "      <td>101561.00000</td>\n",
       "      <td>-2.271896</td>\n",
       "      <td>2.06</td>\n",
       "      <td>-5.936078</td>\n",
       "      <td>24.299999</td>\n",
       "      <td>4.651163</td>\n",
       "      <td>18.127272</td>\n",
       "      <td>1.269676</td>\n",
       "      <td>12.21</td>\n",
       "      <td>-9.151783</td>\n",
       "      <td>-2.291755</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2022-01-07</td>\n",
       "      <td>102719.00000</td>\n",
       "      <td>-1.157599</td>\n",
       "      <td>2.05</td>\n",
       "      <td>-6.392699</td>\n",
       "      <td>24.600000</td>\n",
       "      <td>5.943157</td>\n",
       "      <td>18.390909</td>\n",
       "      <td>2.742512</td>\n",
       "      <td>11.93</td>\n",
       "      <td>-11.235114</td>\n",
       "      <td>-2.235536</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>121</th>\n",
       "      <td>2022-06-28</td>\n",
       "      <td>100591.00000</td>\n",
       "      <td>-3.205289</td>\n",
       "      <td>3.85</td>\n",
       "      <td>75.799078</td>\n",
       "      <td>14.480000</td>\n",
       "      <td>-37.639966</td>\n",
       "      <td>17.910000</td>\n",
       "      <td>0.055867</td>\n",
       "      <td>15.35</td>\n",
       "      <td>14.211316</td>\n",
       "      <td>13.106574</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>122</th>\n",
       "      <td>2022-06-29</td>\n",
       "      <td>99622.00000</td>\n",
       "      <td>-4.137719</td>\n",
       "      <td>3.78</td>\n",
       "      <td>72.602734</td>\n",
       "      <td>14.140000</td>\n",
       "      <td>-39.104217</td>\n",
       "      <td>17.600000</td>\n",
       "      <td>-1.675973</td>\n",
       "      <td>14.97</td>\n",
       "      <td>11.383934</td>\n",
       "      <td>10.801619</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>123</th>\n",
       "      <td>2022-06-30</td>\n",
       "      <td>98542.00000</td>\n",
       "      <td>-5.176960</td>\n",
       "      <td>3.75</td>\n",
       "      <td>71.232872</td>\n",
       "      <td>13.590000</td>\n",
       "      <td>-41.472866</td>\n",
       "      <td>17.200001</td>\n",
       "      <td>-3.910608</td>\n",
       "      <td>14.77</td>\n",
       "      <td>9.895840</td>\n",
       "      <td>8.936310</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>124</th>\n",
       "      <td>2022-07-01</td>\n",
       "      <td>98954.00000</td>\n",
       "      <td>-4.780508</td>\n",
       "      <td>3.93</td>\n",
       "      <td>79.452053</td>\n",
       "      <td>14.280000</td>\n",
       "      <td>-38.501291</td>\n",
       "      <td>17.330000</td>\n",
       "      <td>-3.184356</td>\n",
       "      <td>15.14</td>\n",
       "      <td>12.648816</td>\n",
       "      <td>12.603805</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>125</th>\n",
       "      <td>2022-07-04</td>\n",
       "      <td>98784.09375</td>\n",
       "      <td>-4.944002</td>\n",
       "      <td>3.87</td>\n",
       "      <td>76.712319</td>\n",
       "      <td>14.720000</td>\n",
       "      <td>-36.606371</td>\n",
       "      <td>17.150000</td>\n",
       "      <td>-4.189944</td>\n",
       "      <td>14.83</td>\n",
       "      <td>10.342265</td>\n",
       "      <td>11.564567</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>126 rows × 12 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "          date    ibov_close  ibov_cum_change  CIEL3_close  CIEL3_cum_change  \\\n",
       "0   2022-01-03  103922.00000         0.000000         2.19          0.000000   \n",
       "1   2022-01-04  103514.00000        -0.392602         2.12         -3.196355   \n",
       "2   2022-01-05  101006.00000        -2.805951         2.11         -3.652975   \n",
       "3   2022-01-06  101561.00000        -2.271896         2.06         -5.936078   \n",
       "4   2022-01-07  102719.00000        -1.157599         2.05         -6.392699   \n",
       "..         ...           ...              ...          ...               ...   \n",
       "121 2022-06-28  100591.00000        -3.205289         3.85         75.799078   \n",
       "122 2022-06-29   99622.00000        -4.137719         3.78         72.602734   \n",
       "123 2022-06-30   98542.00000        -5.176960         3.75         71.232872   \n",
       "124 2022-07-01   98954.00000        -4.780508         3.93         79.452053   \n",
       "125 2022-07-04   98784.09375        -4.944002         3.87         76.712319   \n",
       "\n",
       "     BRFS3_close  BRFS3_cum_change  BBDC4_close  BBDC4_cum_change  \\\n",
       "0      23.219999          0.000000    17.900000          0.000000   \n",
       "1      22.420000         -3.445303    18.000000          0.558661   \n",
       "2      22.700001         -2.239443    17.872726         -0.152364   \n",
       "3      24.299999          4.651163    18.127272          1.269676   \n",
       "4      24.600000          5.943157    18.390909          2.742512   \n",
       "..           ...               ...          ...               ...   \n",
       "121    14.480000        -37.639966    17.910000          0.055867   \n",
       "122    14.140000        -39.104217    17.600000         -1.675973   \n",
       "123    13.590000        -41.472866    17.200001         -3.910608   \n",
       "124    14.280000        -38.501291    17.330000         -3.184356   \n",
       "125    14.720000        -36.606371    17.150000         -4.189944   \n",
       "\n",
       "     ENEV3_close  ENEV3_cum_change  total_cum_change  \n",
       "0          13.44          0.000000          0.000000  \n",
       "1          12.91         -3.943451         -2.506612  \n",
       "2          12.40         -7.738095         -3.445719  \n",
       "3          12.21         -9.151783         -2.291755  \n",
       "4          11.93        -11.235114         -2.235536  \n",
       "..           ...               ...               ...  \n",
       "121        15.35         14.211316         13.106574  \n",
       "122        14.97         11.383934         10.801619  \n",
       "123        14.77          9.895840          8.936310  \n",
       "124        15.14         12.648816         12.603805  \n",
       "125        14.83         10.342265         11.564567  \n",
       "\n",
       "[126 rows x 12 columns]"
      ]
     },
     "execution_count": 376,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Computing total change\n",
    "total_change_columns = [column for column in final_df.columns if \"change\" in column and column not in ['ibov_cum_change', 'total_cum_change']]\n",
    "final_df['total_cum_change'] = final_df[total_change_columns].mean(axis=1)\n",
    "final_df"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4dfa7657-eaf3-4223-8e3d-9dd8faadb65b",
   "metadata": {
    "tags": []
   },
   "source": [
    "## Investment results"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 378,
   "id": "3ad242db-ec1d-41fa-8b9f-baaa708dca9b",
   "metadata": {},
   "outputs": [],
   "source": [
    "changes = [final_df[column] for column in final_df.columns if \"change\" in column and column not in ['ibov_cum_change','total_cum_change']]\n",
    "changes = pd.concat(changes, axis=1)\n",
    "changes_results = changes.iloc[-1].sort_values(ascending=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 379,
   "id": "95a67dde-767e-4c6b-8a8f-e26c12651a6e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A ação do seu portfólio que teve melhor desempenho no período foi a CIEL3, com um rendimento de 76.71%.\n"
     ]
    }
   ],
   "source": [
    "print(f'A ação do seu portfólio que teve melhor desempenho no período foi a {changes_results.index[0].split(\"_\")[0]}, com um rendimento de {round(changes_results[0],2)}%.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 380,
   "id": "7578b388-419d-463b-8c80-7058f908f1ff",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A ação do seu portfólio que teve pior desempenho no período foi a BRFS3, com um rendimento de -36.61%.\n"
     ]
    }
   ],
   "source": [
    "print(f'A ação do seu portfólio que teve pior desempenho no período foi a {changes_results.index[-1].split(\"_\")[0]}, com um rendimento de {round(changes_results[-1],2)}%.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 381,
   "id": "0851c391-53b0-4c87-a0a1-cf029b4c57fc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "O seu portfólio teve um desempenho médio de 11.56% no período, 16.51% comparado ao Ibovespa.\n"
     ]
    }
   ],
   "source": [
    "print(f'O seu portfólio teve um desempenho médio de {round(final_df[\"total_cum_change\"].iloc[-1],2)}% no período, {round(final_df[\"total_cum_change\"].iloc[-1]-final_df[\"ibov_cum_change\"].iloc[-1],2)}% comparado ao Ibovespa.')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ca568df8-3d11-455c-ae0f-beac3c94e382",
   "metadata": {
    "tags": []
   },
   "source": [
    "## Visualizing data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 382,
   "id": "acbab9b7-2bb4-46d1-af21-343ecebb5962",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "hovertemplate": "variable=CIEL3_close<br>date=%{x}<br>value=%{y}<extra></extra>",
         "legendgroup": "CIEL3_close",
         "line": {
          "color": "#636efa",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines",
         "name": "CIEL3_close",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "2022-01-03T00:00:00",
          "2022-01-04T00:00:00",
          "2022-01-05T00:00:00",
          "2022-01-06T00:00:00",
          "2022-01-07T00:00:00",
          "2022-01-10T00:00:00",
          "2022-01-11T00:00:00",
          "2022-01-12T00:00:00",
          "2022-01-13T00:00:00",
          "2022-01-14T00:00:00",
          "2022-01-17T00:00:00",
          "2022-01-18T00:00:00",
          "2022-01-19T00:00:00",
          "2022-01-20T00:00:00",
          "2022-01-21T00:00:00",
          "2022-01-24T00:00:00",
          "2022-01-25T00:00:00",
          "2022-01-26T00:00:00",
          "2022-01-27T00:00:00",
          "2022-01-28T00:00:00",
          "2022-01-31T00:00:00",
          "2022-02-01T00:00:00",
          "2022-02-02T00:00:00",
          "2022-02-03T00:00:00",
          "2022-02-04T00:00:00",
          "2022-02-07T00:00:00",
          "2022-02-08T00:00:00",
          "2022-02-09T00:00:00",
          "2022-02-10T00:00:00",
          "2022-02-11T00:00:00",
          "2022-02-14T00:00:00",
          "2022-02-15T00:00:00",
          "2022-02-16T00:00:00",
          "2022-02-17T00:00:00",
          "2022-02-18T00:00:00",
          "2022-02-21T00:00:00",
          "2022-02-22T00:00:00",
          "2022-02-23T00:00:00",
          "2022-02-24T00:00:00",
          "2022-02-25T00:00:00",
          "2022-03-02T00:00:00",
          "2022-03-03T00:00:00",
          "2022-03-04T00:00:00",
          "2022-03-07T00:00:00",
          "2022-03-08T00:00:00",
          "2022-03-09T00:00:00",
          "2022-03-10T00:00:00",
          "2022-03-11T00:00:00",
          "2022-03-14T00:00:00",
          "2022-03-15T00:00:00",
          "2022-03-16T00:00:00",
          "2022-03-17T00:00:00",
          "2022-03-18T00:00:00",
          "2022-03-21T00:00:00",
          "2022-03-22T00:00:00",
          "2022-03-23T00:00:00",
          "2022-03-24T00:00:00",
          "2022-03-25T00:00:00",
          "2022-03-28T00:00:00",
          "2022-03-29T00:00:00",
          "2022-03-30T00:00:00",
          "2022-03-31T00:00:00",
          "2022-04-01T00:00:00",
          "2022-04-04T00:00:00",
          "2022-04-05T00:00:00",
          "2022-04-06T00:00:00",
          "2022-04-07T00:00:00",
          "2022-04-08T00:00:00",
          "2022-04-11T00:00:00",
          "2022-04-12T00:00:00",
          "2022-04-13T00:00:00",
          "2022-04-14T00:00:00",
          "2022-04-18T00:00:00",
          "2022-04-19T00:00:00",
          "2022-04-20T00:00:00",
          "2022-04-22T00:00:00",
          "2022-04-25T00:00:00",
          "2022-04-26T00:00:00",
          "2022-04-27T00:00:00",
          "2022-04-28T00:00:00",
          "2022-04-29T00:00:00",
          "2022-05-02T00:00:00",
          "2022-05-03T00:00:00",
          "2022-05-04T00:00:00",
          "2022-05-05T00:00:00",
          "2022-05-06T00:00:00",
          "2022-05-09T00:00:00",
          "2022-05-10T00:00:00",
          "2022-05-11T00:00:00",
          "2022-05-12T00:00:00",
          "2022-05-13T00:00:00",
          "2022-05-16T00:00:00",
          "2022-05-17T00:00:00",
          "2022-05-18T00:00:00",
          "2022-05-19T00:00:00",
          "2022-05-20T00:00:00",
          "2022-05-23T00:00:00",
          "2022-05-24T00:00:00",
          "2022-05-25T00:00:00",
          "2022-05-26T00:00:00",
          "2022-05-27T00:00:00",
          "2022-05-30T00:00:00",
          "2022-05-31T00:00:00",
          "2022-06-01T00:00:00",
          "2022-06-02T00:00:00",
          "2022-06-03T00:00:00",
          "2022-06-06T00:00:00",
          "2022-06-07T00:00:00",
          "2022-06-08T00:00:00",
          "2022-06-09T00:00:00",
          "2022-06-10T00:00:00",
          "2022-06-13T00:00:00",
          "2022-06-14T00:00:00",
          "2022-06-15T00:00:00",
          "2022-06-17T00:00:00",
          "2022-06-20T00:00:00",
          "2022-06-21T00:00:00",
          "2022-06-22T00:00:00",
          "2022-06-23T00:00:00",
          "2022-06-24T00:00:00",
          "2022-06-27T00:00:00",
          "2022-06-28T00:00:00",
          "2022-06-29T00:00:00",
          "2022-06-30T00:00:00",
          "2022-07-01T00:00:00",
          "2022-07-04T00:00:00"
         ],
         "xaxis": "x",
         "y": [
          2.190000057220459,
          2.119999885559082,
          2.109999895095825,
          2.059999942779541,
          2.049999952316284,
          2.009999990463257,
          2.0799999237060547,
          2.0299999713897705,
          2.0199999809265137,
          2.0199999809265137,
          2.119999885559082,
          2.049999952316284,
          2.0799999237060547,
          2.140000104904175,
          2.069999933242798,
          2.049999952316284,
          2.180000066757202,
          2.190000057220459,
          2.1500000953674316,
          2.2799999713897705,
          2.299999952316284,
          2.299999952316284,
          2.3299999237060547,
          2.190000057220459,
          2.3299999237060547,
          2.3399999141693115,
          2.319999933242798,
          2.309999942779541,
          2.380000114440918,
          2.319999933242798,
          2.380000114440918,
          2.369999885559082,
          2.490000009536743,
          2.5199999809265137,
          2.8299999237060547,
          2.6600000858306885,
          2.609999895095825,
          2.5999999046325684,
          2.6500000953674316,
          2.569999933242798,
          2.4700000286102295,
          2.5999999046325684,
          2.4700000286102295,
          2.2899999618530273,
          2.4200000762939453,
          2.5199999809265137,
          2.509999990463257,
          2.490000009536743,
          2.440000057220459,
          2.569999933242798,
          2.490000009536743,
          2.5,
          2.680000066757202,
          2.700000047683716,
          2.690000057220459,
          2.7100000381469727,
          2.8299999237060547,
          2.890000104904175,
          2.859999895095825,
          2.930000066757202,
          2.9800000190734863,
          3.109999895095825,
          3.359999895095825,
          3.3499999046325684,
          3.25,
          3.240000009536743,
          3.299999952316284,
          3.4200000762939453,
          3.4700000286102295,
          3.609999895095825,
          3.5899999141693115,
          3.5799999237060547,
          3.6500000953674316,
          3.569999933242798,
          3.5199999809265137,
          3.440000057220459,
          3.509999990463257,
          3.380000114440918,
          3.440000057220459,
          3.609999895095825,
          3.4000000953674316,
          3.319999933242798,
          3.4200000762939453,
          3.4200000762939453,
          3.119999885559082,
          3.109999895095825,
          3.0799999237060547,
          3.109999895095825,
          3.059999942779541,
          3.180000066757202,
          3.25,
          3.319999933242798,
          3.380000114440918,
          3.380000114440918,
          3.450000047683716,
          3.549999952316284,
          3.640000104904175,
          3.6500000953674316,
          3.630000114440918,
          4.039999961853027,
          3.990000009536743,
          3.930000066757202,
          3.950000047683716,
          3.9800000190734863,
          3.950000047683716,
          3.950000047683716,
          3.9700000286102295,
          3.799999952316284,
          3.7699999809265137,
          3.759999990463257,
          3.7799999713897705,
          3.8299999237060547,
          3.7799999713897705,
          3.940000057220459,
          3.8499999046325684,
          3.799999952316284,
          3.9000000953674316,
          3.940000057220459,
          3.950000047683716,
          3.859999895095825,
          3.859999895095825,
          3.8499999046325684,
          3.7799999713897705,
          3.75,
          3.930000066757202,
          3.869999885559082
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "variable=BRFS3_close<br>date=%{x}<br>value=%{y}<extra></extra>",
         "legendgroup": "BRFS3_close",
         "line": {
          "color": "#EF553B",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines",
         "name": "BRFS3_close",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "2022-01-03T00:00:00",
          "2022-01-04T00:00:00",
          "2022-01-05T00:00:00",
          "2022-01-06T00:00:00",
          "2022-01-07T00:00:00",
          "2022-01-10T00:00:00",
          "2022-01-11T00:00:00",
          "2022-01-12T00:00:00",
          "2022-01-13T00:00:00",
          "2022-01-14T00:00:00",
          "2022-01-17T00:00:00",
          "2022-01-18T00:00:00",
          "2022-01-19T00:00:00",
          "2022-01-20T00:00:00",
          "2022-01-21T00:00:00",
          "2022-01-24T00:00:00",
          "2022-01-25T00:00:00",
          "2022-01-26T00:00:00",
          "2022-01-27T00:00:00",
          "2022-01-28T00:00:00",
          "2022-01-31T00:00:00",
          "2022-02-01T00:00:00",
          "2022-02-02T00:00:00",
          "2022-02-03T00:00:00",
          "2022-02-04T00:00:00",
          "2022-02-07T00:00:00",
          "2022-02-08T00:00:00",
          "2022-02-09T00:00:00",
          "2022-02-10T00:00:00",
          "2022-02-11T00:00:00",
          "2022-02-14T00:00:00",
          "2022-02-15T00:00:00",
          "2022-02-16T00:00:00",
          "2022-02-17T00:00:00",
          "2022-02-18T00:00:00",
          "2022-02-21T00:00:00",
          "2022-02-22T00:00:00",
          "2022-02-23T00:00:00",
          "2022-02-24T00:00:00",
          "2022-02-25T00:00:00",
          "2022-03-02T00:00:00",
          "2022-03-03T00:00:00",
          "2022-03-04T00:00:00",
          "2022-03-07T00:00:00",
          "2022-03-08T00:00:00",
          "2022-03-09T00:00:00",
          "2022-03-10T00:00:00",
          "2022-03-11T00:00:00",
          "2022-03-14T00:00:00",
          "2022-03-15T00:00:00",
          "2022-03-16T00:00:00",
          "2022-03-17T00:00:00",
          "2022-03-18T00:00:00",
          "2022-03-21T00:00:00",
          "2022-03-22T00:00:00",
          "2022-03-23T00:00:00",
          "2022-03-24T00:00:00",
          "2022-03-25T00:00:00",
          "2022-03-28T00:00:00",
          "2022-03-29T00:00:00",
          "2022-03-30T00:00:00",
          "2022-03-31T00:00:00",
          "2022-04-01T00:00:00",
          "2022-04-04T00:00:00",
          "2022-04-05T00:00:00",
          "2022-04-06T00:00:00",
          "2022-04-07T00:00:00",
          "2022-04-08T00:00:00",
          "2022-04-11T00:00:00",
          "2022-04-12T00:00:00",
          "2022-04-13T00:00:00",
          "2022-04-14T00:00:00",
          "2022-04-18T00:00:00",
          "2022-04-19T00:00:00",
          "2022-04-20T00:00:00",
          "2022-04-22T00:00:00",
          "2022-04-25T00:00:00",
          "2022-04-26T00:00:00",
          "2022-04-27T00:00:00",
          "2022-04-28T00:00:00",
          "2022-04-29T00:00:00",
          "2022-05-02T00:00:00",
          "2022-05-03T00:00:00",
          "2022-05-04T00:00:00",
          "2022-05-05T00:00:00",
          "2022-05-06T00:00:00",
          "2022-05-09T00:00:00",
          "2022-05-10T00:00:00",
          "2022-05-11T00:00:00",
          "2022-05-12T00:00:00",
          "2022-05-13T00:00:00",
          "2022-05-16T00:00:00",
          "2022-05-17T00:00:00",
          "2022-05-18T00:00:00",
          "2022-05-19T00:00:00",
          "2022-05-20T00:00:00",
          "2022-05-23T00:00:00",
          "2022-05-24T00:00:00",
          "2022-05-25T00:00:00",
          "2022-05-26T00:00:00",
          "2022-05-27T00:00:00",
          "2022-05-30T00:00:00",
          "2022-05-31T00:00:00",
          "2022-06-01T00:00:00",
          "2022-06-02T00:00:00",
          "2022-06-03T00:00:00",
          "2022-06-06T00:00:00",
          "2022-06-07T00:00:00",
          "2022-06-08T00:00:00",
          "2022-06-09T00:00:00",
          "2022-06-10T00:00:00",
          "2022-06-13T00:00:00",
          "2022-06-14T00:00:00",
          "2022-06-15T00:00:00",
          "2022-06-17T00:00:00",
          "2022-06-20T00:00:00",
          "2022-06-21T00:00:00",
          "2022-06-22T00:00:00",
          "2022-06-23T00:00:00",
          "2022-06-24T00:00:00",
          "2022-06-27T00:00:00",
          "2022-06-28T00:00:00",
          "2022-06-29T00:00:00",
          "2022-06-30T00:00:00",
          "2022-07-01T00:00:00",
          "2022-07-04T00:00:00"
         ],
         "xaxis": "x",
         "y": [
          23.219999313354492,
          22.420000076293945,
          22.700000762939453,
          24.299999237060547,
          24.600000381469727,
          23.520000457763672,
          23.219999313354492,
          23.84000015258789,
          24.010000228881836,
          24.299999237060547,
          24.75,
          23.31999969482422,
          23.709999084472656,
          23.360000610351562,
          22.690000534057617,
          23.459999084472656,
          23.25,
          22.81999969482422,
          23.100000381469727,
          22.850000381469727,
          22.329999923706055,
          21.6299991607666,
          19.950000762939453,
          19.850000381469727,
          18.75,
          18.3700008392334,
          18.350000381469727,
          18.899999618530273,
          19.139999389648438,
          18.809999465942383,
          18.959999084472656,
          19,
          19,
          18.950000762939453,
          18.81999969482422,
          18.34000015258789,
          19.350000381469727,
          18.459999084472656,
          17.34000015258789,
          16.709999084472656,
          16.520000457763672,
          16.020000457763672,
          15.430000305175781,
          14.359999656677246,
          15.369999885559082,
          16.540000915527344,
          15.90999984741211,
          15.430000305175781,
          15.25,
          15.470000267028809,
          16.239999771118164,
          16.59000015258789,
          16.799999237060547,
          16.6299991607666,
          17.229999542236328,
          16.56999969482422,
          16.969999313354492,
          17,
          17.389999389648438,
          18.170000076293945,
          18.15999984741211,
          18.59000015258789,
          18.84000015258789,
          18.3700008392334,
          17.850000381469727,
          17.860000610351562,
          17.81999969482422,
          17.440000534057617,
          16.200000762939453,
          15.899999618530273,
          15.779999732971191,
          15.229999542236328,
          15.25,
          15.289999961853027,
          14.760000228881836,
          14.510000228881836,
          13.979999542236328,
          13.4399995803833,
          13.9399995803833,
          13.989999771118164,
          13.579999923706055,
          13.279999732971191,
          13.369999885559082,
          13.65999984741211,
          12.770000457763672,
          11.989999771118164,
          12.319999694824219,
          12.579999923706055,
          12.390000343322754,
          12.579999923706055,
          13.880000114440918,
          13.930000305175781,
          14.3100004196167,
          13.579999923706055,
          13.449999809265137,
          13.569999694824219,
          14.229999542236328,
          14.350000381469727,
          14.220000267028809,
          14.529999732971191,
          15.229999542236328,
          15.050000190734863,
          15.649999618530273,
          15.34000015258789,
          15.40999984741211,
          15.199999809265137,
          15.149999618530273,
          15.149999618530273,
          14.890000343322754,
          14.960000038146973,
          15,
          13.899999618530273,
          13.15999984741211,
          12.979999542236328,
          12.829999923706055,
          12.430000305175781,
          12.470000267028809,
          13.069999694824219,
          14.09000015258789,
          14.539999961853027,
          14.760000228881836,
          14.479999542236328,
          14.140000343322754,
          13.59000015258789,
          14.279999732971191,
          14.720000267028809
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "variable=BBDC4_close<br>date=%{x}<br>value=%{y}<extra></extra>",
         "legendgroup": "BBDC4_close",
         "line": {
          "color": "#00cc96",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines",
         "name": "BBDC4_close",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "2022-01-03T00:00:00",
          "2022-01-04T00:00:00",
          "2022-01-05T00:00:00",
          "2022-01-06T00:00:00",
          "2022-01-07T00:00:00",
          "2022-01-10T00:00:00",
          "2022-01-11T00:00:00",
          "2022-01-12T00:00:00",
          "2022-01-13T00:00:00",
          "2022-01-14T00:00:00",
          "2022-01-17T00:00:00",
          "2022-01-18T00:00:00",
          "2022-01-19T00:00:00",
          "2022-01-20T00:00:00",
          "2022-01-21T00:00:00",
          "2022-01-24T00:00:00",
          "2022-01-25T00:00:00",
          "2022-01-26T00:00:00",
          "2022-01-27T00:00:00",
          "2022-01-28T00:00:00",
          "2022-01-31T00:00:00",
          "2022-02-01T00:00:00",
          "2022-02-02T00:00:00",
          "2022-02-03T00:00:00",
          "2022-02-04T00:00:00",
          "2022-02-07T00:00:00",
          "2022-02-08T00:00:00",
          "2022-02-09T00:00:00",
          "2022-02-10T00:00:00",
          "2022-02-11T00:00:00",
          "2022-02-14T00:00:00",
          "2022-02-15T00:00:00",
          "2022-02-16T00:00:00",
          "2022-02-17T00:00:00",
          "2022-02-18T00:00:00",
          "2022-02-21T00:00:00",
          "2022-02-22T00:00:00",
          "2022-02-23T00:00:00",
          "2022-02-24T00:00:00",
          "2022-02-25T00:00:00",
          "2022-03-02T00:00:00",
          "2022-03-03T00:00:00",
          "2022-03-04T00:00:00",
          "2022-03-07T00:00:00",
          "2022-03-08T00:00:00",
          "2022-03-09T00:00:00",
          "2022-03-10T00:00:00",
          "2022-03-11T00:00:00",
          "2022-03-14T00:00:00",
          "2022-03-15T00:00:00",
          "2022-03-16T00:00:00",
          "2022-03-17T00:00:00",
          "2022-03-18T00:00:00",
          "2022-03-21T00:00:00",
          "2022-03-22T00:00:00",
          "2022-03-23T00:00:00",
          "2022-03-24T00:00:00",
          "2022-03-25T00:00:00",
          "2022-03-28T00:00:00",
          "2022-03-29T00:00:00",
          "2022-03-30T00:00:00",
          "2022-03-31T00:00:00",
          "2022-04-01T00:00:00",
          "2022-04-04T00:00:00",
          "2022-04-05T00:00:00",
          "2022-04-06T00:00:00",
          "2022-04-07T00:00:00",
          "2022-04-08T00:00:00",
          "2022-04-11T00:00:00",
          "2022-04-12T00:00:00",
          "2022-04-13T00:00:00",
          "2022-04-14T00:00:00",
          "2022-04-18T00:00:00",
          "2022-04-19T00:00:00",
          "2022-04-20T00:00:00",
          "2022-04-22T00:00:00",
          "2022-04-25T00:00:00",
          "2022-04-26T00:00:00",
          "2022-04-27T00:00:00",
          "2022-04-28T00:00:00",
          "2022-04-29T00:00:00",
          "2022-05-02T00:00:00",
          "2022-05-03T00:00:00",
          "2022-05-04T00:00:00",
          "2022-05-05T00:00:00",
          "2022-05-06T00:00:00",
          "2022-05-09T00:00:00",
          "2022-05-10T00:00:00",
          "2022-05-11T00:00:00",
          "2022-05-12T00:00:00",
          "2022-05-13T00:00:00",
          "2022-05-16T00:00:00",
          "2022-05-17T00:00:00",
          "2022-05-18T00:00:00",
          "2022-05-19T00:00:00",
          "2022-05-20T00:00:00",
          "2022-05-23T00:00:00",
          "2022-05-24T00:00:00",
          "2022-05-25T00:00:00",
          "2022-05-26T00:00:00",
          "2022-05-27T00:00:00",
          "2022-05-30T00:00:00",
          "2022-05-31T00:00:00",
          "2022-06-01T00:00:00",
          "2022-06-02T00:00:00",
          "2022-06-03T00:00:00",
          "2022-06-06T00:00:00",
          "2022-06-07T00:00:00",
          "2022-06-08T00:00:00",
          "2022-06-09T00:00:00",
          "2022-06-10T00:00:00",
          "2022-06-13T00:00:00",
          "2022-06-14T00:00:00",
          "2022-06-15T00:00:00",
          "2022-06-17T00:00:00",
          "2022-06-20T00:00:00",
          "2022-06-21T00:00:00",
          "2022-06-22T00:00:00",
          "2022-06-23T00:00:00",
          "2022-06-24T00:00:00",
          "2022-06-27T00:00:00",
          "2022-06-28T00:00:00",
          "2022-06-29T00:00:00",
          "2022-06-30T00:00:00",
          "2022-07-01T00:00:00",
          "2022-07-04T00:00:00"
         ],
         "xaxis": "x",
         "y": [
          17.899999618530273,
          18,
          17.872726440429688,
          18.12727165222168,
          18.39090919494629,
          18.454544067382812,
          18.4818172454834,
          18.3454532623291,
          18.672727584838867,
          18.972726821899414,
          19.081817626953125,
          19.42727279663086,
          19.18181800842285,
          19.16363525390625,
          18.96363639831543,
          19.363636016845703,
          20.136362075805664,
          20.154544830322266,
          20.254545211791992,
          20.545454025268555,
          20.727272033691406,
          20.799999237060547,
          20.409090042114258,
          20.709089279174805,
          20.8454532623291,
          20.77272605895996,
          20.654544830322266,
          18.881818771362305,
          19.154544830322266,
          19.218181610107422,
          19.245454788208008,
          19.263635635375977,
          19.490909576416016,
          19.263635635375977,
          19.372726440429688,
          19.14545440673828,
          19.07272720336914,
          18.9818172454834,
          18.409090042114258,
          18.5,
          18.30908966064453,
          18.64545440673828,
          18.10909080505371,
          17.64545440673828,
          17.872726440429688,
          19.01818084716797,
          18.899999618530273,
          18.818180084228516,
          18.954544067382812,
          18.909090042114258,
          19.18181800842285,
          19.254545211791992,
          19.209089279174805,
          19.66363525390625,
          19.909090042114258,
          19.781818389892578,
          20.07272720336914,
          20.254545211791992,
          20.154544830322266,
          20.51818084716797,
          20.39090919494629,
          20.200000762939453,
          19.9818172454834,
          19.881818771362305,
          19.327272415161133,
          19.227272033691406,
          19.30908966064453,
          19.527271270751953,
          19.5,
          19.327272415161133,
          19.527271270751953,
          19.4818172454834,
          19.827272415161133,
          19.56999969482422,
          19.5,
          19.219999313354492,
          19.100000381469727,
          18.280000686645508,
          18.389999389648438,
          18.219999313354492,
          17.979999542236328,
          17.969999313354492,
          18.06999969482422,
          18.329999923706055,
          17.729999542236328,
          18.100000381469727,
          18.3700008392334,
          18.549999237060547,
          18.8700008392334,
          18.989999771118164,
          19.209999084472656,
          19.530000686645508,
          19.93000030517578,
          19.559999465942383,
          19.40999984741211,
          19.670000076293945,
          19.989999771118164,
          20.40999984741211,
          20.18000030517578,
          20.290000915527344,
          20.579999923706055,
          20.3799991607666,
          20.5,
          20.1299991607666,
          20.030000686645508,
          19.90999984741211,
          19.93000030517578,
          19.760000228881836,
          19.40999984741211,
          19.399999618530273,
          19.110000610351562,
          18.829999923706055,
          18.639999389648438,
          18.770000457763672,
          18.479999542236328,
          18.969999313354492,
          18.639999389648438,
          18.559999465942383,
          18.06999969482422,
          17.920000076293945,
          18.170000076293945,
          17.90999984741211,
          17.600000381469727,
          17.200000762939453,
          17.329999923706055,
          17.149999618530273
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "variable=ENEV3_close<br>date=%{x}<br>value=%{y}<extra></extra>",
         "legendgroup": "ENEV3_close",
         "line": {
          "color": "#ab63fa",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines",
         "name": "ENEV3_close",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "2022-01-03T00:00:00",
          "2022-01-04T00:00:00",
          "2022-01-05T00:00:00",
          "2022-01-06T00:00:00",
          "2022-01-07T00:00:00",
          "2022-01-10T00:00:00",
          "2022-01-11T00:00:00",
          "2022-01-12T00:00:00",
          "2022-01-13T00:00:00",
          "2022-01-14T00:00:00",
          "2022-01-17T00:00:00",
          "2022-01-18T00:00:00",
          "2022-01-19T00:00:00",
          "2022-01-20T00:00:00",
          "2022-01-21T00:00:00",
          "2022-01-24T00:00:00",
          "2022-01-25T00:00:00",
          "2022-01-26T00:00:00",
          "2022-01-27T00:00:00",
          "2022-01-28T00:00:00",
          "2022-01-31T00:00:00",
          "2022-02-01T00:00:00",
          "2022-02-02T00:00:00",
          "2022-02-03T00:00:00",
          "2022-02-04T00:00:00",
          "2022-02-07T00:00:00",
          "2022-02-08T00:00:00",
          "2022-02-09T00:00:00",
          "2022-02-10T00:00:00",
          "2022-02-11T00:00:00",
          "2022-02-14T00:00:00",
          "2022-02-15T00:00:00",
          "2022-02-16T00:00:00",
          "2022-02-17T00:00:00",
          "2022-02-18T00:00:00",
          "2022-02-21T00:00:00",
          "2022-02-22T00:00:00",
          "2022-02-23T00:00:00",
          "2022-02-24T00:00:00",
          "2022-02-25T00:00:00",
          "2022-03-02T00:00:00",
          "2022-03-03T00:00:00",
          "2022-03-04T00:00:00",
          "2022-03-07T00:00:00",
          "2022-03-08T00:00:00",
          "2022-03-09T00:00:00",
          "2022-03-10T00:00:00",
          "2022-03-11T00:00:00",
          "2022-03-14T00:00:00",
          "2022-03-15T00:00:00",
          "2022-03-16T00:00:00",
          "2022-03-17T00:00:00",
          "2022-03-18T00:00:00",
          "2022-03-21T00:00:00",
          "2022-03-22T00:00:00",
          "2022-03-23T00:00:00",
          "2022-03-24T00:00:00",
          "2022-03-25T00:00:00",
          "2022-03-28T00:00:00",
          "2022-03-29T00:00:00",
          "2022-03-30T00:00:00",
          "2022-03-31T00:00:00",
          "2022-04-01T00:00:00",
          "2022-04-04T00:00:00",
          "2022-04-05T00:00:00",
          "2022-04-06T00:00:00",
          "2022-04-07T00:00:00",
          "2022-04-08T00:00:00",
          "2022-04-11T00:00:00",
          "2022-04-12T00:00:00",
          "2022-04-13T00:00:00",
          "2022-04-14T00:00:00",
          "2022-04-18T00:00:00",
          "2022-04-19T00:00:00",
          "2022-04-20T00:00:00",
          "2022-04-22T00:00:00",
          "2022-04-25T00:00:00",
          "2022-04-26T00:00:00",
          "2022-04-27T00:00:00",
          "2022-04-28T00:00:00",
          "2022-04-29T00:00:00",
          "2022-05-02T00:00:00",
          "2022-05-03T00:00:00",
          "2022-05-04T00:00:00",
          "2022-05-05T00:00:00",
          "2022-05-06T00:00:00",
          "2022-05-09T00:00:00",
          "2022-05-10T00:00:00",
          "2022-05-11T00:00:00",
          "2022-05-12T00:00:00",
          "2022-05-13T00:00:00",
          "2022-05-16T00:00:00",
          "2022-05-17T00:00:00",
          "2022-05-18T00:00:00",
          "2022-05-19T00:00:00",
          "2022-05-20T00:00:00",
          "2022-05-23T00:00:00",
          "2022-05-24T00:00:00",
          "2022-05-25T00:00:00",
          "2022-05-26T00:00:00",
          "2022-05-27T00:00:00",
          "2022-05-30T00:00:00",
          "2022-05-31T00:00:00",
          "2022-06-01T00:00:00",
          "2022-06-02T00:00:00",
          "2022-06-03T00:00:00",
          "2022-06-06T00:00:00",
          "2022-06-07T00:00:00",
          "2022-06-08T00:00:00",
          "2022-06-09T00:00:00",
          "2022-06-10T00:00:00",
          "2022-06-13T00:00:00",
          "2022-06-14T00:00:00",
          "2022-06-15T00:00:00",
          "2022-06-17T00:00:00",
          "2022-06-20T00:00:00",
          "2022-06-21T00:00:00",
          "2022-06-22T00:00:00",
          "2022-06-23T00:00:00",
          "2022-06-24T00:00:00",
          "2022-06-27T00:00:00",
          "2022-06-28T00:00:00",
          "2022-06-29T00:00:00",
          "2022-06-30T00:00:00",
          "2022-07-01T00:00:00",
          "2022-07-04T00:00:00"
         ],
         "xaxis": "x",
         "y": [
          13.4399995803833,
          12.90999984741211,
          12.399999618530273,
          12.210000038146973,
          11.930000305175781,
          11.960000038146973,
          12.119999885559082,
          12.510000228881836,
          12.170000076293945,
          12.699999809265137,
          12.609999656677246,
          12.550000190734863,
          12.90999984741211,
          12.9399995803833,
          12.930000305175781,
          12.75,
          12.890000343322754,
          13.069999694824219,
          13.199999809265137,
          12.670000076293945,
          13.210000038146973,
          13.260000228881836,
          13.220000267028809,
          13.359999656677246,
          13.329999923706055,
          13.069999694824219,
          13.079999923706055,
          13.460000038146973,
          13.470000267028809,
          13.40999984741211,
          13.359999656677246,
          13.680000305175781,
          14.010000228881836,
          13.880000114440918,
          13.65999984741211,
          13.390000343322754,
          13.59000015258789,
          13.430000305175781,
          13.5600004196167,
          13.470000267028809,
          13.479999542236328,
          13.15999984741211,
          12.789999961853027,
          12.229999542236328,
          12.479999542236328,
          12.989999771118164,
          12.5,
          11.979999542236328,
          11.930000305175781,
          12.029999732971191,
          12.149999618530273,
          12.649999618530273,
          13.880000114440918,
          13.390000343322754,
          14.279999732971191,
          14.489999771118164,
          15.100000381469727,
          15.25,
          14.979999542236328,
          15.300000190734863,
          14.890000343322754,
          14.779999732971191,
          15.050000190734863,
          14.8100004196167,
          14.649999618530273,
          14.770000457763672,
          14.8100004196167,
          15.40999984741211,
          15.3100004196167,
          15.479999542236328,
          15.390000343322754,
          15.5600004196167,
          14.899999618530273,
          14.869999885559082,
          14.6899995803833,
          14.149999618530273,
          14.329999923706055,
          13.90999984741211,
          13.739999771118164,
          13.850000381469727,
          13.720000267028809,
          13.369999885559082,
          13.489999771118164,
          14.050000190734863,
          13.479999542236328,
          13.5600004196167,
          13.079999923706055,
          13.220000267028809,
          12.970000267028809,
          13.260000228881836,
          13.600000381469727,
          14.300000190734863,
          14.4399995803833,
          14.460000038146973,
          14.729999542236328,
          14.84000015258789,
          14.470000267028809,
          14.770000457763672,
          14.920000076293945,
          15.449999809265137,
          15.34000015258789,
          15.539999961853027,
          15.579999923706055,
          15.319999694824219,
          14.850000381469727,
          14.699999809265137,
          14.510000228881836,
          14.1899995803833,
          14.369999885559082,
          14.34000015258789,
          14.369999885559082,
          13.949999809265137,
          13.640000343322754,
          14.180000305175781,
          14.539999961853027,
          14.680000305175781,
          14.850000381469727,
          14.869999885559082,
          14.369999885559082,
          14.359999656677246,
          15.1899995803833,
          15.350000381469727,
          14.970000267028809,
          14.770000457763672,
          15.140000343322754,
          14.829999923706055
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "autosize": true,
        "legend": {
         "title": {
          "text": "variable"
         },
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "xaxis": {
         "anchor": "y",
         "autorange": true,
         "domain": [
          0,
          1
         ],
         "range": [
          "2022-01-03",
          "2022-07-04"
         ],
         "title": {
          "text": "date"
         },
         "type": "date"
        },
        "yaxis": {
         "anchor": "x",
         "autorange": true,
         "domain": [
          0,
          1
         ],
         "range": [
          0.7466666566001046,
          26.01333333386315
         ],
         "title": {
          "text": "value"
         },
         "type": "linear"
        }
       }
      },
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABpIAAAFoCAYAAABUsGgGAAAAAXNSR0IArs4c6QAAIABJREFUeF7snQd4XNWZ/t977zR1yUWW5F5xAwPGxNQQTCgGEgIJCSl/CAlxSHbTCCyEEJJlCWBC2m7CEhZSNgQC2UBC6CV0TDHNgBuustVsSVafdu/9P98ZzXg0Gkkzmhlpynv86JmZe88595zfdzzlvuf7Ps22bRssJEACJEACJEACJEACJEACJEACJEACJEACJEACJEACJEACJEACJBBDQKOQxDVBAiRAAiRAAiRAAiRAAiRAAiRAAiRAAiRAAiRAAiRAAiRAAiQQjwCFJK4LEiABEiABEiABEiABEiABEiABEiABEiABEiABEiABEiABEiCBuAQoJHFhkAAJkAAJkAAJkAAJkAAJkAAJkAAJkAAJkAAJkAAJkAAJkAAJUEjiGiABEiABEiABEiABEiABEiABEiABEiABEiABEiABEiABEiABEkicAD2SEmfFmiRAAiRAAiRAAiRAAiRAAiRAAiRAAiRAAiRAAiRAAiRAAiRQUAQoJBWUuTlZEiABEiABEiABEiABEiABEiABEiABEiABEiABEiABEiABEkicAIWkxFmxJgmQAAmQAAmQAAmQAAmQAAmQAAmQAAmQAAmQAAmQAAmQAAkUFAEKSQVlbk6WBEiABEiABEiABEiABEiABEiABEiABEiABEiABEiABEiABBInQCEpcVasSQIkQAIkQAIkQAIkQAIkQAIkQAIkQAIkQAIkQAIkQAIkQAIFRYBCUkGZm5MlARIgARIgARIgARIgARIgARIgARIgARIgARIgARIgARIggcQJUEhKnBVrkgAJkAAJkAAJkAAJkAAJkAAJkAAJkAAJkAAJkAAJkAAJkEBBEaCQVFDm5mRJgARIgARIgARIgARIgARIgARIgARIgARIgARIgARIgARIIHECFJISZ8WaJEACJEACJEACJEACJEACJEACJEACJEACJEACJEACJEACJFBQBCgkFZS5OVkSIAESIAESIAESIAESIAESIAESIAESIAESIAESIAESIAESSJwAhaTEWbEmCZAACZAACZAACZAACZAACZAACZAACZAACZAACZAACZAACRQUAQpJBWVuTpYESIAESIAESIAESIAESIAESIAESIAESIAESIAESIAESIAEEidAISlxVqxJAiRAAiRAAiRAAiRAAiRAAiRAAiRAAiRAAiRAAiRAAiRAAgVFgEJSQZmbkyUBEiABEiABEiABEiABEiABEiABEiABEiABEiABEiABEiCBxAlQSEqcFWuSAAmQAAmQAAmQAAmQAAmQAAmQAAmQAAmQAAmQAAmQAAmQQEERoJBUUObmZEmABEiABEiABEiABEiABEiABEiABEiABEiABEiABEiABEggcQIUkhJnxZokQAIkQAIkQAIkQAIkQAIkQAIkQAIkQAIkQAIkQAIkQAIkUFAEKCQVlLk5WRIgARIgARIgARIgARIgARIgARIgARIgARIgARIgARIgARJInACFpMRZsSYJkAAJkAAJkAAJkAAJkAAJkAAJkAAJkAAJkAAJkAAJkAAJFBQBCkkFZW5OlgRIgARIgARIgARIgARIgARIgARIgARIgARIgARIgARIgAQSJ0AhKXFWrEkCJEACJEACJEACJEACJEACJEACJEACJEACJEACJEACJEACBUWAQlJBmZuTJQESIAESIAESIAESIAESIAESIAESIAESIAESIAESIAESIIHECVBISpwVa5IACZAACZAACZAACZAACZAACZAACZAACZAACZAACZAACZBAQRGgkFRQ5uZkSYAESIAESIAESIAESIAESIAESIAESIAESIAESIAESIAESCBxAhSSEmfFmiRAAiRAAiRAAiRAAiRAAiRAAiRAAiRAAiRAAiRAAiRAAiRQUAQoJBWUuTlZEiABEiABEiABEiABEiABEiABEiABEiABEiABEiABEiABEkicAIWkxFmxJgmQAAmQAAmQAAmQAAmQAAmQAAmQAAmQAAmQAAmQAAmQAAkUFAEKSQVlbk6WBEiABEiABEiABEiABEiABEiABEiABEiABEiABEiABEiABBInQCEpcVasSQIkQAIkQAIkQAIkQAIkQAIkQAIkQAIkQAIkQAIkQAIkQAIFRYBCUkGZm5MlARIgARIgARIgARIgARIgARIgARIgARIgARIgARIgARIggcQJUEhKnBVrkgAJkAAJkAAJkAAJkAAJkAAJkAAJkAAJkAAJkAAJkAAJkEBBEaCQVFDm5mRJgARIgARIgARIgARIgARIgARIgARIgARIgARIgARIgARIIHECFJISZ8WaJEACJEACJEACJEACJEACJEACJEACJEACJEACJEACJEACJFBQBCgkFZS5OVkSIAESIAESIAESIAESIAESIAESIAESIAESIAESIAESIAESSJwAhaTEWbEmCZAACZAACZAACZAACZAACZAACZAACZAACZAACZAACZAACRQUAQpJBWVuTpYESIAESIAESIAESIAESIAESIAESIAESIAESIAESIAESIAEEidAISlxVqxJAiRAAiRAAiRAAiRAAiRAAiRAAiRAAiRAAiRAAiRAAiRAAgVFgEJSQZmbkyUBEiABEiABEiABEiABEiABEiABEiABEiABEiABEiABEiCBxAlQSEqcFWuSAAmQAAmQAAmQAAmQAAmQAAmQAAmQAAmQAAmQAAmQAAmQQEERoJBUUObmZEmABEiABEiABEiABEiABEiABEiABEiABEiABEiABEiABEggcQIUkhJnxZokQAIkQAIkQAIkQAIkQAIkQAIkQAIkQAIkQAIkQAIkQAIkUFAEKCQVlLk5WRIgARIgARIgARIgARIgARIgARIgARIgARIgARIgARIgARJInACFpMRZsSYJkAAJkAAJkAAJkAAJkAAJkAAJkAAJkAAJkAAJkAAJkAAJFBQBCkkFZW5OlgRIgARIgARIgARIgARIgARIgARIgARIgARIgARIgARIgAQSJ0AhKXFWrEkCJEACJEACJEACJEACJEACJEACJEACJEACJEACJEACJEACBUWAQlJBmZuTJQESIAESIAESIAESIAESIAESIAESIAESIAESIAESIAESIIHECVBISpwVa5IACZAACZAACZAACZAACZAACZAACZAACZAACZAACZAACZBAQRGgkFRQ5uZkSYAESIAESIAESIAESIAESIAESIAESIAESIAESIAESIAESCBxAhSSEmfFmiRAAiRAAiRAAiRAAiRAAiRAAiRAAiRAAiRAAiRAAiRAAiRQUAQoJBWUuTlZEiABEiABEiABEiABEiABEiABEiABEiABEiABEiABEiABEkicAIWkxFmxJgmQAAmQAAmQAAmQAAmQAAmQAAmQAAmQAAmQAAmQAAmQAAkUFAEKSQVlbk6WBEiABEiABEiABEiABEiABEiABEiABEiABEiABEiABEiABBInQCEpcVasSQIkQAIkQAIkQAIkQAIkQAIkQAIkQAIkQAIkQAIkQAIkQAIFRYBCUkGZm5MlARIgARIgARIgARIgARIg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",
      "text/html": [
       "<div>                            <div id=\"7b431a1c-1eb0-4306-bf5c-dac783d7ffa6\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"7b431a1c-1eb0-4306-bf5c-dac783d7ffa6\")) {                    Plotly.newPlot(                        \"7b431a1c-1eb0-4306-bf5c-dac783d7ffa6\",                        [{\"hovertemplate\":\"variable=CIEL3_close<br>date=%{x}<br>value=%{y}<extra></extra>\",\"legendgroup\":\"CIEL3_close\",\"line\":{\"color\":\"#636efa\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"lines\",\"name\":\"CIEL3_close\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"2022-01-03T00:00:00\",\"2022-01-04T00:00:00\",\"2022-01-05T00:00:00\",\"2022-01-06T00:00:00\",\"2022-01-07T00:00:00\",\"2022-01-10T00:00:00\",\"2022-01-11T00:00:00\",\"2022-01-12T00:00:00\",\"2022-01-13T00:00:00\",\"2022-01-14T00:00:00\",\"2022-01-17T00:00:00\",\"2022-01-18T00:00:00\",\"2022-01-19T00:00:00\",\"2022-01-20T00:00:00\",\"2022-01-21T00:00:00\",\"2022-01-24T00:00:00\",\"2022-01-25T00:00:00\",\"2022-01-26T00:00:00\",\"2022-01-27T00:00:00\",\"2022-01-28T00:00:00\",\"2022-01-31T00:00:00\",\"2022-02-01T00:00:00\",\"2022-02-02T00:00:00\",\"2022-02-03T00:00:00\",\"2022-02-04T00:00:00\",\"2022-02-07T00:00:00\",\"2022-02-08T00:00:00\",\"2022-02-09T00:00:00\",\"2022-02-10T00:00:00\",\"2022-02-11T00:00:00\",\"2022-02-14T00:00:00\",\"2022-02-15T00:00:00\",\"2022-02-16T00:00:00\",\"2022-02-17T00:00:00\",\"2022-02-18T00:00:00\",\"2022-02-21T00:00:00\",\"2022-02-22T00:00:00\",\"2022-02-23T00:00:00\",\"2022-02-24T00:00:00\",\"2022-02-25T00:00:00\",\"2022-03-02T00:00:00\",\"2022-03-03T00:00:00\",\"2022-03-04T00:00:00\",\"2022-03-07T00:00:00\",\"2022-03-08T00:00:00\",\"2022-03-09T00:00:00\",\"2022-03-10T00:00:00\",\"2022-03-11T00:00:00\",\"2022-03-14T00:00:00\",\"2022-03-15T00:00:00\",\"2022-03-16T00:00:00\",\"2022-03-17T00:00:00\",\"2022-03-18T00:00:00\",\"2022-03-21T00:00:00\",\"2022-03-22T00:00:00\",\"2022-03-23T00:00:00\",\"2022-03-24T00:00:00\",\"2022-03-25T00:00:00\",\"2022-03-28T00:00:00\",\"2022-03-29T00:00:00\",\"2022-03-30T00:00:00\",\"2022-03-31T00:00:00\",\"2022-04-01T00:00:00\",\"2022-04-04T00:00:00\",\"2022-04-05T00:00:00\",\"2022-04-06T00:00:00\",\"2022-04-07T00:00:00\",\"2022-04-08T00:00:00\",\"2022-04-11T00:00:00\",\"2022-04-12T00:00:00\",\"2022-04-13T00:00:00\",\"2022-04-14T00:00:00\",\"2022-04-18T00:00:00\",\"2022-04-19T00:00:00\",\"2022-04-20T00:00:00\",\"2022-04-22T00:00:00\",\"2022-04-25T00:00:00\",\"2022-04-26T00:00:00\",\"2022-04-27T00:00:00\",\"2022-04-28T00:00:00\",\"2022-04-29T00:00:00\",\"2022-05-02T00:00:00\",\"2022-05-03T00:00:00\",\"2022-05-04T00:00:00\",\"2022-05-05T00:00:00\",\"2022-05-06T00:00:00\",\"2022-05-09T00:00:00\",\"2022-05-10T00:00:00\",\"2022-05-11T00:00:00\",\"2022-05-12T00:00:00\",\"2022-05-13T00:00:00\",\"2022-05-16T00:00:00\",\"2022-05-17T00:00:00\",\"2022-05-18T00:00:00\",\"2022-05-19T00:00:00\",\"2022-05-20T00:00:00\",\"2022-05-23T00:00:00\",\"2022-05-24T00:00:00\",\"2022-05-25T00:00:00\",\"2022-05-26T00:00:00\",\"2022-05-27T00:00:00\",\"2022-05-30T00:00:00\",\"2022-05-31T00:00:00\",\"2022-06-01T00:00:00\",\"2022-06-02T00:00:00\",\"2022-06-03T00:00:00\",\"2022-06-06T00:00:00\",\"2022-06-07T00:00:00\",\"2022-06-08T00:00:00\",\"2022-06-09T00:00:00\",\"2022-06-10T00:00:00\",\"2022-06-13T00:00:00\",\"2022-06-14T00:00:00\",\"2022-06-15T00:00:00\",\"2022-06-17T00:00:00\",\"2022-06-20T00:00:00\",\"2022-06-21T00:00:00\",\"2022-06-22T00:00:00\",\"2022-06-23T00:00:00\",\"2022-06-24T00:00:00\",\"2022-06-27T00:00:00\",\"2022-06-28T00:00:00\",\"2022-06-29T00:00:00\",\"2022-06-30T00:00:00\",\"2022-07-01T00:00:00\",\"2022-07-04T00:00:00\"],\"xaxis\":\"x\",\"y\":[2.190000057220459,2.119999885559082,2.109999895095825,2.059999942779541,2.049999952316284,2.009999990463257,2.0799999237060547,2.0299999713897705,2.0199999809265137,2.0199999809265137,2.119999885559082,2.049999952316284,2.0799999237060547,2.140000104904175,2.069999933242798,2.049999952316284,2.180000066757202,2.190000057220459,2.1500000953674316,2.2799999713897705,2.299999952316284,2.299999952316284,2.3299999237060547,2.190000057220459,2.3299999237060547,2.3399999141693115,2.319999933242798,2.309999942779541,2.380000114440918,2.319999933242798,2.380000114440918,2.369999885559082,2.490000009536743,2.5199999809265137,2.8299999237060547,2.6600000858306885,2.609999895095825,2.5999999046325684,2.6500000953674316,2.569999933242798,2.4700000286102295,2.5999999046325684,2.4700000286102295,2.2899999618530273,2.4200000762939453,2.5199999809265137,2.509999990463257,2.490000009536743,2.440000057220459,2.569999933242798,2.490000009536743,2.5,2.680000066757202,2.700000047683716,2.690000057220459,2.7100000381469727,2.8299999237060547,2.890000104904175,2.859999895095825,2.930000066757202,2.9800000190734863,3.109999895095825,3.359999895095825,3.3499999046325684,3.25,3.240000009536743,3.299999952316284,3.4200000762939453,3.4700000286102295,3.609999895095825,3.5899999141693115,3.5799999237060547,3.6500000953674316,3.569999933242798,3.5199999809265137,3.440000057220459,3.509999990463257,3.380000114440918,3.440000057220459,3.609999895095825,3.4000000953674316,3.319999933242798,3.4200000762939453,3.4200000762939453,3.119999885559082,3.109999895095825,3.0799999237060547,3.109999895095825,3.059999942779541,3.180000066757202,3.25,3.319999933242798,3.380000114440918,3.380000114440918,3.450000047683716,3.549999952316284,3.640000104904175,3.6500000953674316,3.630000114440918,4.039999961853027,3.990000009536743,3.930000066757202,3.950000047683716,3.9800000190734863,3.950000047683716,3.950000047683716,3.9700000286102295,3.799999952316284,3.7699999809265137,3.759999990463257,3.7799999713897705,3.8299999237060547,3.7799999713897705,3.940000057220459,3.8499999046325684,3.799999952316284,3.9000000953674316,3.940000057220459,3.950000047683716,3.859999895095825,3.859999895095825,3.8499999046325684,3.7799999713897705,3.75,3.930000066757202,3.869999885559082],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"variable=BRFS3_close<br>date=%{x}<br>value=%{y}<extra></extra>\",\"legendgroup\":\"BRFS3_close\",\"line\":{\"color\":\"#EF553B\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"lines\",\"name\":\"BRFS3_close\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"2022-01-03T00:00:00\",\"2022-01-04T00:00:00\",\"2022-01-05T00:00:00\",\"2022-01-06T00:00:00\",\"2022-01-07T00:00:00\",\"2022-01-10T00:00:00\",\"2022-01-11T00:00:00\",\"2022-01-12T00:00:00\",\"2022-01-13T00:00:00\",\"2022-01-14T00:00:00\",\"2022-01-17T00:00:00\",\"2022-01-18T00:00:00\",\"2022-01-19T00:00:00\",\"2022-01-20T00:00:00\",\"2022-01-21T00:00:00\",\"2022-01-24T00:00:00\",\"2022-01-25T00:00:00\",\"2022-01-26T00:00:00\",\"2022-01-27T00:00:00\",\"2022-01-28T00:00:00\",\"2022-01-31T00:00:00\",\"2022-02-01T00:00:00\",\"2022-02-02T00:00:00\",\"2022-02-03T00:00:00\",\"2022-02-04T00:00:00\",\"2022-02-07T00:00:00\",\"2022-02-08T00:00:00\",\"2022-02-09T00:00:00\",\"2022-02-10T00:00:00\",\"2022-02-11T00:00:00\",\"2022-02-14T00:00:00\",\"2022-02-15T00:00:00\",\"2022-02-16T00:00:00\",\"2022-02-17T00:00:00\",\"2022-02-18T00:00:00\",\"2022-02-21T00:00:00\",\"2022-02-22T00:00:00\",\"2022-02-23T00:00:00\",\"2022-02-24T00:00:00\",\"2022-02-25T00:00:00\",\"2022-03-02T00:00:00\",\"2022-03-03T00:00:00\",\"2022-03-04T00:00:00\",\"2022-03-07T00:00:00\",\"2022-03-08T00:00:00\",\"2022-03-09T00:00:00\",\"2022-03-10T00:00:00\",\"2022-03-11T00:00:00\",\"2022-03-14T00:00:00\",\"2022-03-15T00:00:00\",\"2022-03-16T00:00:00\",\"2022-03-17T00:00:00\",\"2022-03-18T00:00:00\",\"2022-03-21T00:00:00\",\"2022-03-22T00:00:00\",\"2022-03-23T00:00:00\",\"2022-03-24T00:00:00\",\"2022-03-25T00:00:00\",\"2022-03-28T00:00:00\",\"2022-03-29T00:00:00\",\"2022-03-30T00:00:00\",\"2022-03-31T00:00:00\",\"2022-04-01T00:00:00\",\"2022-04-04T00:00:00\",\"2022-04-05T00:00:00\",\"2022-04-06T00:00:00\",\"2022-04-07T00:00:00\",\"2022-04-08T00:00:00\",\"2022-04-11T00:00:00\",\"2022-04-12T00:00:00\",\"2022-04-13T00:00:00\",\"2022-04-14T00:00:00\",\"2022-04-18T00:00:00\",\"2022-04-19T00:00:00\",\"2022-04-20T00:00:00\",\"2022-04-22T00:00:00\",\"2022-04-25T00:00:00\",\"2022-04-26T00:00:00\",\"2022-04-27T00:00:00\",\"2022-04-28T00:00:00\",\"2022-04-29T00:00:00\",\"2022-05-02T00:00:00\",\"2022-05-03T00:00:00\",\"2022-05-04T00:00:00\",\"2022-05-05T00:00:00\",\"2022-05-06T00:00:00\",\"2022-05-09T00:00:00\",\"2022-05-10T00:00:00\",\"2022-05-11T00:00:00\",\"2022-05-12T00:00:00\",\"2022-05-13T00:00:00\",\"2022-05-16T00:00:00\",\"2022-05-17T00:00:00\",\"2022-05-18T00:00:00\",\"2022-05-19T00:00:00\",\"2022-05-20T00:00:00\",\"2022-05-23T00:00:00\",\"2022-05-24T00:00:00\",\"2022-05-25T00:00:00\",\"2022-05-26T00:00:00\",\"2022-05-27T00:00:00\",\"2022-05-30T00:00:00\",\"2022-05-31T00:00:00\",\"2022-06-01T00:00:00\",\"2022-06-02T00:00:00\",\"2022-06-03T00:00:00\",\"2022-06-06T00:00:00\",\"2022-06-07T00:00:00\",\"2022-06-08T00:00:00\",\"2022-06-09T00:00:00\",\"2022-06-10T00:00:00\",\"2022-06-13T00:00:00\",\"2022-06-14T00:00:00\",\"2022-06-15T00:00:00\",\"2022-06-17T00:00:00\",\"2022-06-20T00:00:00\",\"2022-06-21T00:00:00\",\"2022-06-22T00:00:00\",\"2022-06-23T00:00:00\",\"2022-06-24T00:00:00\",\"2022-06-27T00:00:00\",\"2022-06-28T00:00:00\",\"2022-06-29T00:00:00\",\"2022-06-30T00:00:00\",\"2022-07-01T00:00:00\",\"2022-07-04T00:00:00\"],\"xaxis\":\"x\",\"y\":[23.219999313354492,22.420000076293945,22.700000762939453,24.299999237060547,24.600000381469727,23.520000457763672,23.219999313354492,23.84000015258789,24.010000228881836,24.299999237060547,24.75,23.31999969482422,23.709999084472656,23.360000610351562,22.690000534057617,23.459999084472656,23.25,22.81999969482422,23.100000381469727,22.850000381469727,22.329999923706055,21.6299991607666,19.950000762939453,19.850000381469727,18.75,18.3700008392334,18.350000381469727,18.899999618530273,19.139999389648438,18.809999465942383,18.959999084472656,19.0,19.0,18.950000762939453,18.81999969482422,18.34000015258789,19.350000381469727,18.459999084472656,17.34000015258789,16.709999084472656,16.520000457763672,16.020000457763672,15.430000305175781,14.359999656677246,15.369999885559082,16.540000915527344,15.90999984741211,15.430000305175781,15.25,15.470000267028809,16.239999771118164,16.59000015258789,16.799999237060547,16.6299991607666,17.229999542236328,16.56999969482422,16.969999313354492,17.0,17.389999389648438,18.170000076293945,18.15999984741211,18.59000015258789,18.84000015258789,18.3700008392334,17.850000381469727,17.860000610351562,17.81999969482422,17.440000534057617,16.200000762939453,15.899999618530273,15.779999732971191,15.229999542236328,15.25,15.289999961853027,14.760000228881836,14.510000228881836,13.979999542236328,13.4399995803833,13.9399995803833,13.989999771118164,13.579999923706055,13.279999732971191,13.369999885559082,13.65999984741211,12.770000457763672,11.989999771118164,12.319999694824219,12.579999923706055,12.390000343322754,12.579999923706055,13.880000114440918,13.930000305175781,14.3100004196167,13.579999923706055,13.449999809265137,13.569999694824219,14.229999542236328,14.350000381469727,14.220000267028809,14.529999732971191,15.229999542236328,15.050000190734863,15.649999618530273,15.34000015258789,15.40999984741211,15.199999809265137,15.149999618530273,15.149999618530273,14.890000343322754,14.960000038146973,15.0,13.899999618530273,13.15999984741211,12.979999542236328,12.829999923706055,12.430000305175781,12.470000267028809,13.069999694824219,14.09000015258789,14.539999961853027,14.760000228881836,14.479999542236328,14.140000343322754,13.59000015258789,14.279999732971191,14.720000267028809],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"variable=BBDC4_close<br>date=%{x}<br>value=%{y}<extra></extra>\",\"legendgroup\":\"BBDC4_close\",\"line\":{\"color\":\"#00cc96\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"lines\",\"name\":\"BBDC4_close\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"2022-01-03T00:00:00\",\"2022-01-04T00:00:00\",\"2022-01-05T00:00:00\",\"2022-01-06T00:00:00\",\"2022-01-07T00:00:00\",\"2022-01-10T00:00:00\",\"2022-01-11T00:00:00\",\"2022-01-12T00:00:00\",\"2022-01-13T00:00:00\",\"2022-01-14T00:00:00\",\"2022-01-17T00:00:00\",\"2022-01-18T00:00:00\",\"2022-01-19T00:00:00\",\"2022-01-20T00:00:00\",\"2022-01-21T00:00:00\",\"2022-01-24T00:00:00\",\"2022-01-25T00:00:00\",\"2022-01-26T00:00:00\",\"2022-01-27T00:00:00\",\"2022-01-28T00:00:00\",\"2022-01-31T00:00:00\",\"2022-02-01T00:00:00\",\"2022-02-02T00:00:00\",\"2022-02-03T00:00:00\",\"2022-02-04T00:00:00\",\"2022-02-07T00:00:00\",\"2022-02-08T00:00:00\",\"2022-02-09T00:00:00\",\"2022-02-10T00:00:00\",\"2022-02-11T00:00:00\",\"2022-02-14T00:00:00\",\"2022-02-15T00:00:00\",\"2022-02-16T00:00:00\",\"2022-02-17T00:00:00\",\"2022-02-18T00:00:00\",\"2022-02-21T00:00:00\",\"2022-02-22T00:00:00\",\"2022-02-23T00:00:00\",\"2022-02-24T00:00:00\",\"2022-02-25T00:00:00\",\"2022-03-02T00:00:00\",\"2022-03-03T00:00:00\",\"2022-03-04T00:00:00\",\"2022-03-07T00:00:00\",\"2022-03-08T00:00:00\",\"2022-03-09T00:00:00\",\"2022-03-10T00:00:00\",\"2022-03-11T00:00:00\",\"2022-03-14T00:00:00\",\"2022-03-15T00:00:00\",\"2022-03-16T00:00:00\",\"2022-03-17T00:00:00\",\"2022-03-18T00:00:00\",\"2022-03-21T00:00:00\",\"2022-03-22T00:00:00\",\"2022-03-23T00:00:00\",\"2022-03-24T00:00:00\",\"2022-03-25T00:00:00\",\"2022-03-28T00:00:00\",\"2022-03-29T00:00:00\",\"2022-03-30T00:00:00\",\"2022-03-31T00:00:00\",\"2022-04-01T00:00:00\",\"2022-04-04T00:00:00\",\"2022-04-05T00:00:00\",\"2022-04-06T00:00:00\",\"2022-04-07T00:00:00\",\"2022-04-08T00:00:00\",\"2022-04-11T00:00:00\",\"2022-04-12T00:00:00\",\"2022-04-13T00:00:00\",\"2022-04-14T00:00:00\",\"2022-04-18T00:00:00\",\"2022-04-19T00:00:00\",\"2022-04-20T00:00:00\",\"2022-04-22T00:00:00\",\"2022-04-25T00:00:00\",\"2022-04-26T00:00:00\",\"2022-04-27T00:00:00\",\"2022-04-28T00:00:00\",\"2022-04-29T00:00:00\",\"2022-05-02T00:00:00\",\"2022-05-03T00:00:00\",\"2022-05-04T00:00:00\",\"2022-05-05T00:00:00\",\"2022-05-06T00:00:00\",\"2022-05-09T00:00:00\",\"2022-05-10T00:00:00\",\"2022-05-11T00:00:00\",\"2022-05-12T00:00:00\",\"2022-05-13T00:00:00\",\"2022-05-16T00:00:00\",\"2022-05-17T00:00:00\",\"2022-05-18T00:00:00\",\"2022-05-19T00:00:00\",\"2022-05-20T00:00:00\",\"2022-05-23T00:00:00\",\"2022-05-24T00:00:00\",\"2022-05-25T00:00:00\",\"2022-05-26T00:00:00\",\"2022-05-27T00:00:00\",\"2022-05-30T00:00:00\",\"2022-05-31T00:00:00\",\"2022-06-01T00:00:00\",\"2022-06-02T00:00:00\",\"2022-06-03T00:00:00\",\"2022-06-06T00:00:00\",\"2022-06-07T00:00:00\",\"2022-06-08T00:00:00\",\"2022-06-09T00:00:00\",\"2022-06-10T00:00:00\",\"2022-06-13T00:00:00\",\"2022-06-14T00:00:00\",\"2022-06-15T00:00:00\",\"2022-06-17T00:00:00\",\"2022-06-20T00:00:00\",\"2022-06-21T00:00:00\",\"2022-06-22T00:00:00\",\"2022-06-23T00:00:00\",\"2022-06-24T00:00:00\",\"2022-06-27T00:00:00\",\"2022-06-28T00:00:00\",\"2022-06-29T00:00:00\",\"2022-06-30T00:00:00\",\"2022-07-01T00:00:00\",\"2022-07-04T00:00:00\"],\"xaxis\":\"x\",\"y\":[17.899999618530273,18.0,17.872726440429688,18.12727165222168,18.39090919494629,18.454544067382812,18.4818172454834,18.3454532623291,18.672727584838867,18.972726821899414,19.081817626953125,19.42727279663086,19.18181800842285,19.16363525390625,18.96363639831543,19.363636016845703,20.136362075805664,20.154544830322266,20.254545211791992,20.545454025268555,20.727272033691406,20.799999237060547,20.409090042114258,20.709089279174805,20.8454532623291,20.77272605895996,20.654544830322266,18.881818771362305,19.154544830322266,19.218181610107422,19.245454788208008,19.263635635375977,19.490909576416016,19.263635635375977,19.372726440429688,19.14545440673828,19.07272720336914,18.9818172454834,18.409090042114258,18.5,18.30908966064453,18.64545440673828,18.10909080505371,17.64545440673828,17.872726440429688,19.01818084716797,18.899999618530273,18.818180084228516,18.954544067382812,18.909090042114258,19.18181800842285,19.254545211791992,19.209089279174805,19.66363525390625,19.909090042114258,19.781818389892578,20.07272720336914,20.254545211791992,20.154544830322266,20.51818084716797,20.39090919494629,20.200000762939453,19.9818172454834,19.881818771362305,19.327272415161133,19.227272033691406,19.30908966064453,19.527271270751953,19.5,19.327272415161133,19.527271270751953,19.4818172454834,19.827272415161133,19.56999969482422,19.5,19.219999313354492,19.100000381469727,18.280000686645508,18.389999389648438,18.219999313354492,17.979999542236328,17.969999313354492,18.06999969482422,18.329999923706055,17.729999542236328,18.100000381469727,18.3700008392334,18.549999237060547,18.8700008392334,18.989999771118164,19.209999084472656,19.530000686645508,19.93000030517578,19.559999465942383,19.40999984741211,19.670000076293945,19.989999771118164,20.40999984741211,20.18000030517578,20.290000915527344,20.579999923706055,20.3799991607666,20.5,20.1299991607666,20.030000686645508,19.90999984741211,19.93000030517578,19.760000228881836,19.40999984741211,19.399999618530273,19.110000610351562,18.829999923706055,18.639999389648438,18.770000457763672,18.479999542236328,18.969999313354492,18.639999389648438,18.559999465942383,18.06999969482422,17.920000076293945,18.170000076293945,17.90999984741211,17.600000381469727,17.200000762939453,17.329999923706055,17.149999618530273],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"variable=ENEV3_close<br>date=%{x}<br>value=%{y}<extra></extra>\",\"legendgroup\":\"ENEV3_close\",\"line\":{\"color\":\"#ab63fa\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"lines\",\"name\":\"ENEV3_close\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"2022-01-03T00:00:00\",\"2022-01-04T00:00:00\",\"2022-01-05T00:00:00\",\"2022-01-06T00:00:00\",\"2022-01-07T00:00:00\",\"2022-01-10T00:00:00\",\"2022-01-11T00:00:00\",\"2022-01-12T00:00:00\",\"2022-01-13T00:00:00\",\"2022-01-14T00:00:00\",\"2022-01-17T00:00:00\",\"2022-01-18T00:00:00\",\"2022-01-19T00:00:00\",\"2022-01-20T00:00:00\",\"2022-01-21T00:00:00\",\"2022-01-24T00:00:00\",\"2022-01-25T00:00:00\",\"2022-01-26T00:00:00\",\"2022-01-27T00:00:00\",\"2022-01-28T00:00:00\",\"2022-01-31T00:00:00\",\"2022-02-01T00:00:00\",\"2022-02-02T00:00:00\",\"2022-02-03T00:00:00\",\"2022-02-04T00:00:00\",\"2022-02-07T00:00:00\",\"2022-02-08T00:00:00\",\"2022-02-09T00:00:00\",\"2022-02-10T00:00:00\",\"2022-02-11T00:00:00\",\"2022-02-14T00:00:00\",\"2022-02-15T00:00:00\",\"2022-02-16T00:00:00\",\"2022-02-17T00:00:00\",\"2022-02-18T00:00:00\",\"2022-02-21T00:00:00\",\"2022-02-22T00:00:00\",\"2022-02-23T00:00:00\",\"2022-02-24T00:00:00\",\"2022-02-25T00:00:00\",\"2022-03-02T00:00:00\",\"2022-03-03T00:00:00\",\"2022-03-04T00:00:00\",\"2022-03-07T00:00:00\",\"2022-03-08T00:00:00\",\"2022-03-09T00:00:00\",\"2022-03-10T00:00:00\",\"2022-03-11T00:00:00\",\"2022-03-14T00:00:00\",\"2022-03-15T00:00:00\",\"2022-03-16T00:00:00\",\"2022-03-17T00:00:00\",\"2022-03-18T00:00:00\",\"2022-03-21T00:00:00\",\"2022-03-22T00:00:00\",\"2022-03-23T00:00:00\",\"2022-03-24T00:00:00\",\"2022-03-25T00:00:00\",\"2022-03-28T00:00:00\",\"2022-03-29T00:00:00\",\"2022-03-30T00:00:00\",\"2022-03-31T00:00:00\",\"2022-04-01T00:00:00\",\"2022-04-04T00:00:00\",\"2022-04-05T00:00:00\",\"2022-04-06T00:00:00\",\"2022-04-07T00:00:00\",\"2022-04-08T00:00:00\",\"2022-04-11T00:00:00\",\"2022-04-12T00:00:00\",\"2022-04-13T00:00:00\",\"2022-04-14T00:00:00\",\"2022-04-18T00:00:00\",\"2022-04-19T00:00:00\",\"2022-04-20T00:00:00\",\"2022-04-22T00:00:00\",\"2022-04-25T00:00:00\",\"2022-04-26T00:00:00\",\"2022-04-27T00:00:00\",\"2022-04-28T00:00:00\",\"2022-04-29T00:00:00\",\"2022-05-02T00:00:00\",\"2022-05-03T00:00:00\",\"2022-05-04T00:00:00\",\"2022-05-05T00:00:00\",\"2022-05-06T00:00:00\",\"2022-05-09T00:00:00\",\"2022-05-10T00:00:00\",\"2022-05-11T00:00:00\",\"2022-05-12T00:00:00\",\"2022-05-13T00:00:00\",\"2022-05-16T00:00:00\",\"2022-05-17T00:00:00\",\"2022-05-18T00:00:00\",\"2022-05-19T00:00:00\",\"2022-05-20T00:00:00\",\"2022-05-23T00:00:00\",\"2022-05-24T00:00:00\",\"2022-05-25T00:00:00\",\"2022-05-26T00:00:00\",\"2022-05-27T00:00:00\",\"2022-05-30T00:00:00\",\"2022-05-31T00:00:00\",\"2022-06-01T00:00:00\",\"2022-06-02T00:00:00\",\"2022-06-03T00:00:00\",\"2022-06-06T00:00:00\",\"2022-06-07T00:00:00\",\"2022-06-08T00:00:00\",\"2022-06-09T00:00:00\",\"2022-06-10T00:00:00\",\"2022-06-13T00:00:00\",\"2022-06-14T00:00:00\",\"2022-06-15T00:00:00\",\"2022-06-17T00:00:00\",\"2022-06-20T00:00:00\",\"2022-06-21T00:00:00\",\"2022-06-22T00:00:00\",\"2022-06-23T00:00:00\",\"2022-06-24T00:00:00\",\"2022-06-27T00:00:00\",\"2022-06-28T00:00:00\",\"2022-06-29T00:00:00\",\"2022-06-30T00:00:00\",\"2022-07-01T00:00:00\",\"2022-07-04T00:00:00\"],\"xaxis\":\"x\",\"y\":[13.4399995803833,12.90999984741211,12.399999618530273,12.210000038146973,11.930000305175781,11.960000038146973,12.119999885559082,12.510000228881836,12.170000076293945,12.699999809265137,12.609999656677246,12.550000190734863,12.90999984741211,12.9399995803833,12.930000305175781,12.75,12.890000343322754,13.069999694824219,13.199999809265137,12.670000076293945,13.210000038146973,13.260000228881836,13.220000267028809,13.359999656677246,13.329999923706055,13.069999694824219,13.079999923706055,13.460000038146973,13.470000267028809,13.40999984741211,13.359999656677246,13.680000305175781,14.010000228881836,13.880000114440918,13.65999984741211,13.390000343322754,13.59000015258789,13.430000305175781,13.5600004196167,13.470000267028809,13.479999542236328,13.15999984741211,12.789999961853027,12.229999542236328,12.479999542236328,12.989999771118164,12.5,11.979999542236328,11.930000305175781,12.029999732971191,12.149999618530273,12.649999618530273,13.880000114440918,13.390000343322754,14.279999732971191,14.489999771118164,15.100000381469727,15.25,14.979999542236328,15.300000190734863,14.890000343322754,14.779999732971191,15.050000190734863,14.8100004196167,14.649999618530273,14.770000457763672,14.8100004196167,15.40999984741211,15.3100004196167,15.479999542236328,15.390000343322754,15.5600004196167,14.899999618530273,14.869999885559082,14.6899995803833,14.149999618530273,14.329999923706055,13.90999984741211,13.739999771118164,13.850000381469727,13.720000267028809,13.369999885559082,13.489999771118164,14.050000190734863,13.479999542236328,13.5600004196167,13.079999923706055,13.220000267028809,12.970000267028809,13.260000228881836,13.600000381469727,14.300000190734863,14.4399995803833,14.460000038146973,14.729999542236328,14.84000015258789,14.470000267028809,14.770000457763672,14.920000076293945,15.449999809265137,15.34000015258789,15.539999961853027,15.579999923706055,15.319999694824219,14.850000381469727,14.699999809265137,14.510000228881836,14.1899995803833,14.369999885559082,14.34000015258789,14.369999885559082,13.949999809265137,13.640000343322754,14.180000305175781,14.539999961853027,14.680000305175781,14.850000381469727,14.869999885559082,14.369999885559082,14.359999656677246,15.1899995803833,15.350000381469727,14.970000267028809,14.770000457763672,15.140000343322754,14.829999923706055],\"yaxis\":\"y\",\"type\":\"scatter\"}],                        {\"template\":{\"data\":{\"histogram2dcontour\":[{\"type\":\"histogram2dcontour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"choropleth\":[{\"type\":\"choropleth\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"histogram2d\":[{\"type\":\"histogram2d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmap\":[{\"type\":\"heatmap\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmapgl\":[{\"type\":\"heatmapgl\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"contourcarpet\":[{\"type\":\"contourcarpet\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"contour\":[{\"type\":\"contour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"surface\":[{\"type\":\"surface\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"mesh3d\":[{\"type\":\"mesh3d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"parcoords\":[{\"type\":\"parcoords\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolargl\":[{\"type\":\"scatterpolargl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"scattergeo\":[{\"type\":\"scattergeo\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolar\":[{\"type\":\"scatterpolar\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"scattergl\":[{\"type\":\"scattergl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatter3d\":[{\"type\":\"scatter3d\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattermapbox\":[{\"type\":\"scattermapbox\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterternary\":[{\"type\":\"scatterternary\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattercarpet\":[{\"type\":\"scattercarpet\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}]},\"layout\":{\"autotypenumbers\":\"strict\",\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"hovermode\":\"closest\",\"hoverlabel\":{\"align\":\"left\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"bgcolor\":\"#E5ECF6\",\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"ternary\":{\"bgcolor\":\"#E5ECF6\",\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]]},\"xaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"yaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"geo\":{\"bgcolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"subunitcolor\":\"white\",\"showland\":true,\"showlakes\":true,\"lakecolor\":\"white\"},\"title\":{\"x\":0.05},\"mapbox\":{\"style\":\"light\"}}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"date\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"value\"}},\"legend\":{\"title\":{\"text\":\"variable\"},\"tracegroupgap\":0},\"margin\":{\"t\":60}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('7b431a1c-1eb0-4306-bf5c-dac783d7ffa6');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig = px.line(final_df, x='date', y=[column for column in final_df.columns if \"close\" in column and \"ibov\" not in column])\n",
    "fig.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 383,
   "id": "650aedce-3a23-4fca-afc4-3a961052c6e4",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "hovertemplate": "variable=ibov_cum_change<br>date=%{x}<br>value=%{y}<extra></extra>",
         "legendgroup": "ibov_cum_change",
         "line": {
          "color": "#636efa",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines",
         "name": "ibov_cum_change",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "visible": true,
         "x": [
          "2022-01-03T00:00:00",
          "2022-01-04T00:00:00",
          "2022-01-05T00:00:00",
          "2022-01-06T00:00:00",
          "2022-01-07T00:00:00",
          "2022-01-10T00:00:00",
          "2022-01-11T00:00:00",
          "2022-01-12T00:00:00",
          "2022-01-13T00:00:00",
          "2022-01-14T00:00:00",
          "2022-01-17T00:00:00",
          "2022-01-18T00:00:00",
          "2022-01-19T00:00:00",
          "2022-01-20T00:00:00",
          "2022-01-21T00:00:00",
          "2022-01-24T00:00:00",
          "2022-01-25T00:00:00",
          "2022-01-26T00:00:00",
          "2022-01-27T00:00:00",
          "2022-01-28T00:00:00",
          "2022-01-31T00:00:00",
          "2022-02-01T00:00:00",
          "2022-02-02T00:00:00",
          "2022-02-03T00:00:00",
          "2022-02-04T00:00:00",
          "2022-02-07T00:00:00",
          "2022-02-08T00:00:00",
          "2022-02-09T00:00:00",
          "2022-02-10T00:00:00",
          "2022-02-11T00:00:00",
          "2022-02-14T00:00:00",
          "2022-02-15T00:00:00",
          "2022-02-16T00:00:00",
          "2022-02-17T00:00:00",
          "2022-02-18T00:00:00",
          "2022-02-21T00:00:00",
          "2022-02-22T00:00:00",
          "2022-02-23T00:00:00",
          "2022-02-24T00:00:00",
          "2022-02-25T00:00:00",
          "2022-03-02T00:00:00",
          "2022-03-03T00:00:00",
          "2022-03-04T00:00:00",
          "2022-03-07T00:00:00",
          "2022-03-08T00:00:00",
          "2022-03-09T00:00:00",
          "2022-03-10T00:00:00",
          "2022-03-11T00:00:00",
          "2022-03-14T00:00:00",
          "2022-03-15T00:00:00",
          "2022-03-16T00:00:00",
          "2022-03-17T00:00:00",
          "2022-03-18T00:00:00",
          "2022-03-21T00:00:00",
          "2022-03-22T00:00:00",
          "2022-03-23T00:00:00",
          "2022-03-24T00:00:00",
          "2022-03-25T00:00:00",
          "2022-03-28T00:00:00",
          "2022-03-29T00:00:00",
          "2022-03-30T00:00:00",
          "2022-03-31T00:00:00",
          "2022-04-01T00:00:00",
          "2022-04-04T00:00:00",
          "2022-04-05T00:00:00",
          "2022-04-06T00:00:00",
          "2022-04-07T00:00:00",
          "2022-04-08T00:00:00",
          "2022-04-11T00:00:00",
          "2022-04-12T00:00:00",
          "2022-04-13T00:00:00",
          "2022-04-14T00:00:00",
          "2022-04-18T00:00:00",
          "2022-04-19T00:00:00",
          "2022-04-20T00:00:00",
          "2022-04-22T00:00:00",
          "2022-04-25T00:00:00",
          "2022-04-26T00:00:00",
          "2022-04-27T00:00:00",
          "2022-04-28T00:00:00",
          "2022-04-29T00:00:00",
          "2022-05-02T00:00:00",
          "2022-05-03T00:00:00",
          "2022-05-04T00:00:00",
          "2022-05-05T00:00:00",
          "2022-05-06T00:00:00",
          "2022-05-09T00:00:00",
          "2022-05-10T00:00:00",
          "2022-05-11T00:00:00",
          "2022-05-12T00:00:00",
          "2022-05-13T00:00:00",
          "2022-05-16T00:00:00",
          "2022-05-17T00:00:00",
          "2022-05-18T00:00:00",
          "2022-05-19T00:00:00",
          "2022-05-20T00:00:00",
          "2022-05-23T00:00:00",
          "2022-05-24T00:00:00",
          "2022-05-25T00:00:00",
          "2022-05-26T00:00:00",
          "2022-05-27T00:00:00",
          "2022-05-30T00:00:00",
          "2022-05-31T00:00:00",
          "2022-06-01T00:00:00",
          "2022-06-02T00:00:00",
          "2022-06-03T00:00:00",
          "2022-06-06T00:00:00",
          "2022-06-07T00:00:00",
          "2022-06-08T00:00:00",
          "2022-06-09T00:00:00",
          "2022-06-10T00:00:00",
          "2022-06-13T00:00:00",
          "2022-06-14T00:00:00",
          "2022-06-15T00:00:00",
          "2022-06-17T00:00:00",
          "2022-06-20T00:00:00",
          "2022-06-21T00:00:00",
          "2022-06-22T00:00:00",
          "2022-06-23T00:00:00",
          "2022-06-24T00:00:00",
          "2022-06-27T00:00:00",
          "2022-06-28T00:00:00",
          "2022-06-29T00:00:00",
          "2022-06-30T00:00:00",
          "2022-07-01T00:00:00",
          "2022-07-04T00:00:00"
         ],
         "xaxis": "x",
         "y": [
          0,
          -0.39260214391562903,
          -2.8059506168087602,
          -2.2718962298647063,
          -1.157598968457112,
          -1.90238832970882,
          -0.13760320240180135,
          1.697426916341102,
          1.5473143319027733,
          2.8925540309077964,
          2.6654606339369913,
          2.501876407305479,
          3.9366063008795056,
          4.984507611477839,
          4.830545986412886,
          3.685456399992302,
          5.699466907873212,
          7.362252458574701,
          8.076249494813418,
          7.270837743692384,
          8.146494486249303,
          8.876849945151172,
          7.928061430688401,
          7.480610457843382,
          8.0088912838475,
          7.769288504840168,
          7.998306422124285,
          8.216739477685186,
          9.080849098362233,
          9.28581051172995,
          9.5119416485441,
          10.332749562171628,
          10.834087103789381,
          9.24347106483709,
          8.512153345778565,
          7.508516002386405,
          8.631473605203903,
          7.78083562672004,
          7.380535401551163,
          8.87203864436789,
          10.827351282692788,
          10.819653201439541,
          10.153769173033622,
          7.38149766170782,
          7.0062162006119975,
          9.601431843113104,
          9.373376185985643,
          7.496968880506533,
          5.779334500875657,
          4.846904409076037,
          6.918650526356306,
          8.808529474028598,
          10.959180924154655,
          11.771328496372279,
          12.84617309135698,
          13.02419122033833,
          14.559958430361233,
          14.586901714747599,
          14.256846481014607,
          15.484690440907604,
          15.721406439444968,
          15.470256538557765,
          16.98196724466427,
          16.70291179923404,
          14.398298724043032,
          13.766093801120071,
          14.376166740439945,
          13.85654625584573,
          12.53921210138373,
          11.763630415119032,
          12.374665614595562,
          11.79730952060199,
          11.320990743057292,
          10.714766844364043,
          10.028675352668348,
          6.885933681030004,
          6.5077654394642135,
          4.129058332210697,
          5.2221858701718595,
          5.770674159465753,
          3.80477665941764,
          2.6144608456342255,
          2.5076499682454148,
          4.255114412732627,
          1.3298435364985277,
          1.1672215700236717,
          -0.6466388252728007,
          -0.7813552472046342,
          0.4570735744115779,
          1.6993514366544138,
          2.8887049902811723,
          4.148303535343816,
          4.683320182444525,
          2.237254864225092,
          2.9666480629703047,
          4.393679875291084,
          6.181559246357845,
          6.407690383171994,
          6.406728123015339,
          7.667288928234638,
          7.717326456380747,
          6.84166971382383,
          7.148630703797078,
          7.157291045206982,
          8.151305787032582,
          6.909027924789746,
          6.027597621292893,
          5.915975443120802,
          4.278208656492369,
          3.0522892169126847,
          1.5001635842266314,
          -1.2740324474124824,
          -1.7888416312234177,
          -1.072920074671388,
          -3.9423798618194414,
          -3.915436577433075,
          -4.077096283751275,
          -4.233944689286195,
          -5.62152383518408,
          -5.051865822443756,
          -3.038817574719501,
          -3.205288581820981,
          -4.1377186736206,
          -5.17695964280903,
          -4.780508458266777,
          -4.944002473008602
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "variable=CIEL3_cum_change<br>date=%{x}<br>value=%{y}<extra></extra>",
         "legendgroup": "CIEL3_cum_change",
         "line": {
          "color": "#EF553B",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines",
         "name": "CIEL3_cum_change",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "visible": true,
         "x": [
          "2022-01-03T00:00:00",
          "2022-01-04T00:00:00",
          "2022-01-05T00:00:00",
          "2022-01-06T00:00:00",
          "2022-01-07T00:00:00",
          "2022-01-10T00:00:00",
          "2022-01-11T00:00:00",
          "2022-01-12T00:00:00",
          "2022-01-13T00:00:00",
          "2022-01-14T00:00:00",
          "2022-01-17T00:00:00",
          "2022-01-18T00:00:00",
          "2022-01-19T00:00:00",
          "2022-01-20T00:00:00",
          "2022-01-21T00:00:00",
          "2022-01-24T00:00:00",
          "2022-01-25T00:00:00",
          "2022-01-26T00:00:00",
          "2022-01-27T00:00:00",
          "2022-01-28T00:00:00",
          "2022-01-31T00:00:00",
          "2022-02-01T00:00:00",
          "2022-02-02T00:00:00",
          "2022-02-03T00:00:00",
          "2022-02-04T00:00:00",
          "2022-02-07T00:00:00",
          "2022-02-08T00:00:00",
          "2022-02-09T00:00:00",
          "2022-02-10T00:00:00",
          "2022-02-11T00:00:00",
          "2022-02-14T00:00:00",
          "2022-02-15T00:00:00",
          "2022-02-16T00:00:00",
          "2022-02-17T00:00:00",
          "2022-02-18T00:00:00",
          "2022-02-21T00:00:00",
          "2022-02-22T00:00:00",
          "2022-02-23T00:00:00",
          "2022-02-24T00:00:00",
          "2022-02-25T00:00:00",
          "2022-03-02T00:00:00",
          "2022-03-03T00:00:00",
          "2022-03-04T00:00:00",
          "2022-03-07T00:00:00",
          "2022-03-08T00:00:00",
          "2022-03-09T00:00:00",
          "2022-03-10T00:00:00",
          "2022-03-11T00:00:00",
          "2022-03-14T00:00:00",
          "2022-03-15T00:00:00",
          "2022-03-16T00:00:00",
          "2022-03-17T00:00:00",
          "2022-03-18T00:00:00",
          "2022-03-21T00:00:00",
          "2022-03-22T00:00:00",
          "2022-03-23T00:00:00",
          "2022-03-24T00:00:00",
          "2022-03-25T00:00:00",
          "2022-03-28T00:00:00",
          "2022-03-29T00:00:00",
          "2022-03-30T00:00:00",
          "2022-03-31T00:00:00",
          "2022-04-01T00:00:00",
          "2022-04-04T00:00:00",
          "2022-04-05T00:00:00",
          "2022-04-06T00:00:00",
          "2022-04-07T00:00:00",
          "2022-04-08T00:00:00",
          "2022-04-11T00:00:00",
          "2022-04-12T00:00:00",
          "2022-04-13T00:00:00",
          "2022-04-14T00:00:00",
          "2022-04-18T00:00:00",
          "2022-04-19T00:00:00",
          "2022-04-20T00:00:00",
          "2022-04-22T00:00:00",
          "2022-04-25T00:00:00",
          "2022-04-26T00:00:00",
          "2022-04-27T00:00:00",
          "2022-04-28T00:00:00",
          "2022-04-29T00:00:00",
          "2022-05-02T00:00:00",
          "2022-05-03T00:00:00",
          "2022-05-04T00:00:00",
          "2022-05-05T00:00:00",
          "2022-05-06T00:00:00",
          "2022-05-09T00:00:00",
          "2022-05-10T00:00:00",
          "2022-05-11T00:00:00",
          "2022-05-12T00:00:00",
          "2022-05-13T00:00:00",
          "2022-05-16T00:00:00",
          "2022-05-17T00:00:00",
          "2022-05-18T00:00:00",
          "2022-05-19T00:00:00",
          "2022-05-20T00:00:00",
          "2022-05-23T00:00:00",
          "2022-05-24T00:00:00",
          "2022-05-25T00:00:00",
          "2022-05-26T00:00:00",
          "2022-05-27T00:00:00",
          "2022-05-30T00:00:00",
          "2022-05-31T00:00:00",
          "2022-06-01T00:00:00",
          "2022-06-02T00:00:00",
          "2022-06-03T00:00:00",
          "2022-06-06T00:00:00",
          "2022-06-07T00:00:00",
          "2022-06-08T00:00:00",
          "2022-06-09T00:00:00",
          "2022-06-10T00:00:00",
          "2022-06-13T00:00:00",
          "2022-06-14T00:00:00",
          "2022-06-15T00:00:00",
          "2022-06-17T00:00:00",
          "2022-06-20T00:00:00",
          "2022-06-21T00:00:00",
          "2022-06-22T00:00:00",
          "2022-06-23T00:00:00",
          "2022-06-24T00:00:00",
          "2022-06-27T00:00:00",
          "2022-06-28T00:00:00",
          "2022-06-29T00:00:00",
          "2022-06-30T00:00:00",
          "2022-07-01T00:00:00",
          "2022-07-04T00:00:00"
         ],
         "xaxis": "x",
         "y": [
          0,
          -3.1963547868679485,
          -3.6529753440358235,
          -5.936078129875197,
          -6.3926986870430715,
          -8.21918091571457,
          -5.022837015539448,
          -7.3059398013788215,
          -7.762560358546696,
          -7.762560358546696,
          -3.1963547868679485,
          -6.3926986870430715,
          -5.022837015539448,
          -2.283102785839374,
          -5.4794575727073225,
          -6.3926986870430715,
          -0.45662055716787475,
          0,
          -1.826482228671499,
          4.1095850145108725,
          5.0228261288466225,
          5.0228261288466225,
          6.392687800350247,
          0,
          6.392687800350247,
          6.8493083575181215,
          5.9360672431823716,
          5.479446686014497,
          8.675801472882446,
          5.9360672431823716,
          8.675801472882446,
          8.219170029021745,
          13.698627601729068,
          15.068489273232693,
          29.223737432129635,
          21.461187960275765,
          19.178074287743566,
          18.72145373057569,
          21.004567403107888,
          17.351592059072065,
          12.78538648739332,
          18.72145373057569,
          12.78538648739332,
          4.566205571678748,
          10.502283701553944,
          15.068489273232693,
          14.611868716064818,
          13.698627601729068,
          11.415524815889695,
          17.351592059072065,
          13.698627601729068,
          14.155248158896942,
          22.374429074611513,
          23.287670188947263,
          22.83104963177939,
          23.744290746115137,
          29.223737432129635,
          31.963471661829708,
          30.59359910363326,
          33.78995389050121,
          36.073056676340585,
          42.009123919522956,
          53.424648735412646,
          52.96802817824477,
          48.40182260656603,
          47.94520204939815,
          50.6849253924054,
          56.16438296511272,
          58.4474857509521,
          64.84017355130234,
          63.926932436966595,
          63.47031187979872,
          66.66666666666667,
          63.01369132263084,
          60.73058853679147,
          57.07762407944847,
          60.27396797962359,
          54.33790073644122,
          57.07762407944847,
          64.84017355130234,
          55.251141850776975,
          51.59816650674115,
          56.16438296511272,
          56.16438296511272,
          42.46574447669083,
          42.009123919522956,
          40.63926224801933,
          42.009123919522956,
          39.72602113368358,
          45.2054787063909,
          48.40182260656603,
          51.59816650674115,
          54.33790073644122,
          54.33790073644122,
          57.53424463661634,
          62.10045020829509,
          66.21004610949879,
          66.66666666666667,
          65.75342555233092,
          84.47487928290661,
          82.19177649706724,
          79.45205315405998,
          80.36529426839573,
          81.73515593989936,
          80.36529426839573,
          80.36529426839573,
          81.27853538273149,
          73.51597502418478,
          72.14611335268117,
          71.68949279551329,
          72.60273390984904,
          74.88583669568841,
          72.60273390984904,
          79.90867371122786,
          75.79907781002416,
          73.51597502418478,
          78.08219148255635,
          79.90867371122786,
          80.36529426839573,
          76.25569836719204,
          76.25569836719204,
          75.79907781002416,
          72.60273390984904,
          71.23287223834541,
          79.45205315405998,
          76.7123189243599
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "variable=BRFS3_cum_change<br>date=%{x}<br>value=%{y}<extra></extra>",
         "legendgroup": "BRFS3_cum_change",
         "line": {
          "color": "#00cc96",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines",
         "name": "BRFS3_cum_change",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "visible": true,
         "x": [
          "2022-01-03T00:00:00",
          "2022-01-04T00:00:00",
          "2022-01-05T00:00:00",
          "2022-01-06T00:00:00",
          "2022-01-07T00:00:00",
          "2022-01-10T00:00:00",
          "2022-01-11T00:00:00",
          "2022-01-12T00:00:00",
          "2022-01-13T00:00:00",
          "2022-01-14T00:00:00",
          "2022-01-17T00:00:00",
          "2022-01-18T00:00:00",
          "2022-01-19T00:00:00",
          "2022-01-20T00:00:00",
          "2022-01-21T00:00:00",
          "2022-01-24T00:00:00",
          "2022-01-25T00:00:00",
          "2022-01-26T00:00:00",
          "2022-01-27T00:00:00",
          "2022-01-28T00:00:00",
          "2022-01-31T00:00:00",
          "2022-02-01T00:00:00",
          "2022-02-02T00:00:00",
          "2022-02-03T00:00:00",
          "2022-02-04T00:00:00",
          "2022-02-07T00:00:00",
          "2022-02-08T00:00:00",
          "2022-02-09T00:00:00",
          "2022-02-10T00:00:00",
          "2022-02-11T00:00:00",
          "2022-02-14T00:00:00",
          "2022-02-15T00:00:00",
          "2022-02-16T00:00:00",
          "2022-02-17T00:00:00",
          "2022-02-18T00:00:00",
          "2022-02-21T00:00:00",
          "2022-02-22T00:00:00",
          "2022-02-23T00:00:00",
          "2022-02-24T00:00:00",
          "2022-02-25T00:00:00",
          "2022-03-02T00:00:00",
          "2022-03-03T00:00:00",
          "2022-03-04T00:00:00",
          "2022-03-07T00:00:00",
          "2022-03-08T00:00:00",
          "2022-03-09T00:00:00",
          "2022-03-10T00:00:00",
          "2022-03-11T00:00:00",
          "2022-03-14T00:00:00",
          "2022-03-15T00:00:00",
          "2022-03-16T00:00:00",
          "2022-03-17T00:00:00",
          "2022-03-18T00:00:00",
          "2022-03-21T00:00:00",
          "2022-03-22T00:00:00",
          "2022-03-23T00:00:00",
          "2022-03-24T00:00:00",
          "2022-03-25T00:00:00",
          "2022-03-28T00:00:00",
          "2022-03-29T00:00:00",
          "2022-03-30T00:00:00",
          "2022-03-31T00:00:00",
          "2022-04-01T00:00:00",
          "2022-04-04T00:00:00",
          "2022-04-05T00:00:00",
          "2022-04-06T00:00:00",
          "2022-04-07T00:00:00",
          "2022-04-08T00:00:00",
          "2022-04-11T00:00:00",
          "2022-04-12T00:00:00",
          "2022-04-13T00:00:00",
          "2022-04-14T00:00:00",
          "2022-04-18T00:00:00",
          "2022-04-19T00:00:00",
          "2022-04-20T00:00:00",
          "2022-04-22T00:00:00",
          "2022-04-25T00:00:00",
          "2022-04-26T00:00:00",
          "2022-04-27T00:00:00",
          "2022-04-28T00:00:00",
          "2022-04-29T00:00:00",
          "2022-05-02T00:00:00",
          "2022-05-03T00:00:00",
          "2022-05-04T00:00:00",
          "2022-05-05T00:00:00",
          "2022-05-06T00:00:00",
          "2022-05-09T00:00:00",
          "2022-05-10T00:00:00",
          "2022-05-11T00:00:00",
          "2022-05-12T00:00:00",
          "2022-05-13T00:00:00",
          "2022-05-16T00:00:00",
          "2022-05-17T00:00:00",
          "2022-05-18T00:00:00",
          "2022-05-19T00:00:00",
          "2022-05-20T00:00:00",
          "2022-05-23T00:00:00",
          "2022-05-24T00:00:00",
          "2022-05-25T00:00:00",
          "2022-05-26T00:00:00",
          "2022-05-27T00:00:00",
          "2022-05-30T00:00:00",
          "2022-05-31T00:00:00",
          "2022-06-01T00:00:00",
          "2022-06-02T00:00:00",
          "2022-06-03T00:00:00",
          "2022-06-06T00:00:00",
          "2022-06-07T00:00:00",
          "2022-06-08T00:00:00",
          "2022-06-09T00:00:00",
          "2022-06-10T00:00:00",
          "2022-06-13T00:00:00",
          "2022-06-14T00:00:00",
          "2022-06-15T00:00:00",
          "2022-06-17T00:00:00",
          "2022-06-20T00:00:00",
          "2022-06-21T00:00:00",
          "2022-06-22T00:00:00",
          "2022-06-23T00:00:00",
          "2022-06-24T00:00:00",
          "2022-06-27T00:00:00",
          "2022-06-28T00:00:00",
          "2022-06-29T00:00:00",
          "2022-06-30T00:00:00",
          "2022-07-01T00:00:00",
          "2022-07-04T00:00:00"
         ],
         "xaxis": "x",
         "y": [
          0,
          -3.4453025870696052,
          -2.2394425744705897,
          4.651162599668621,
          5.943157230506704,
          1.2919946308380825,
          0,
          2.6701156656659246,
          3.4022434921993794,
          4.651162599668621,
          6.589150438801091,
          0.4306648769460275,
          2.1102488613612964,
          0.6029341134241616,
          -2.282509883590123,
          1.0335907761208816,
          0.12920192735860053,
          -1.7226512935348026,
          -0.516791280935787,
          -1.5934493661762021,
          -3.832900154896099,
          -6.847546079268985,
          -14.082681512115155,
          -14.513346389061184,
          -19.250643606968872,
          -20.887160282264606,
          -20.973294900503674,
          -18.604650398674483,
          -17.5710596225536,
          -18.992247966500976,
          -18.34625475820659,
          -18.173985521728454,
          -18.173985521728454,
          -18.389313853076814,
          -18.949180657381444,
          -21.016362209623207,
          -16.66666255954201,
          -20.49957092868742,
          -25.322994550584866,
          -28.036177525370324,
          -28.85443175589354,
          -31.007747926374368,
          -33.548661664681696,
          -38.156761062355436,
          -33.807061412274244,
          -28.76829713765447,
          -31.48148011243993,
          -33.548661664681696,
          -34.32385680033468,
          -33.37639653532821,
          -30.060291768492554,
          -28.55296880630611,
          -27.64857995754383,
          -28.380707784077284,
          -25.796726736650427,
          -28.63910342454518,
          -26.916452131010377,
          -26.787250203651777,
          -25.107666219236506,
          -21.74849003615666,
          -21.791557345276196,
          -19.939704124382793,
          -18.863046039142375,
          -20.887160282264606,
          -23.126611070984502,
          -23.08354376186497,
          -23.255812998343103,
          -24.89232967363884,
          -30.232552790721382,
          -31.524547421559465,
          -32.041342809619906,
          -34.409991418573746,
          -34.32385680033468,
          -34.151591670981205,
          -36.43410566169598,
          -37.51076374693639,
          -39.79328184477583,
          -42.11886314461013,
          -39.9655469741293,
          -39.75021453565629,
          -41.51593313831063,
          -42.80792366202405,
          -42.42032609419756,
          -41.17140287960367,
          -45.00430303449976,
          -48.36347921757961,
          -46.94229087363224,
          -45.822565479272285,
          -46.640823816920154,
          -45.822565479272285,
          -40.2239426145972,
          -40.008610176124186,
          -38.372089393703796,
          -41.51593313831063,
          -42.0757958354906,
          -41.55900044743016,
          -38.71662375953541,
          -38.19982426435031,
          -38.759686961530285,
          -37.42463323582198,
          -34.409991418573746,
          -35.185182447102086,
          -32.60120550679988,
          -33.936259232508185,
          -33.63479628292076,
          -34.539189238807694,
          -34.75452167728071,
          -34.75452167728071,
          -35.87424296451601,
          -35.572780014928576,
          -35.4005148855751,
          -40.13781210348279,
          -43.3247190500845,
          -44.09991418573748,
          -44.745907394031875,
          -46.46855868756668,
          -46.29629355821319,
          -43.71231661791099,
          -39.319549658710265,
          -37.38156592670244,
          -36.43410566169598,
          -37.63996567429499,
          -39.104217220237246,
          -41.47286582919109,
          -38.501291321062396,
          -36.60637079104946
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "variable=BBDC4_cum_change<br>date=%{x}<br>value=%{y}<extra></extra>",
         "legendgroup": "BBDC4_cum_change",
         "line": {
          "color": "#ab63fa",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines",
         "name": "BBDC4_cum_change",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "visible": true,
         "x": [
          "2022-01-03T00:00:00",
          "2022-01-04T00:00:00",
          "2022-01-05T00:00:00",
          "2022-01-06T00:00:00",
          "2022-01-07T00:00:00",
          "2022-01-10T00:00:00",
          "2022-01-11T00:00:00",
          "2022-01-12T00:00:00",
          "2022-01-13T00:00:00",
          "2022-01-14T00:00:00",
          "2022-01-17T00:00:00",
          "2022-01-18T00:00:00",
          "2022-01-19T00:00:00",
          "2022-01-20T00:00:00",
          "2022-01-21T00:00:00",
          "2022-01-24T00:00:00",
          "2022-01-25T00:00:00",
          "2022-01-26T00:00:00",
          "2022-01-27T00:00:00",
          "2022-01-28T00:00:00",
          "2022-01-31T00:00:00",
          "2022-02-01T00:00:00",
          "2022-02-02T00:00:00",
          "2022-02-03T00:00:00",
          "2022-02-04T00:00:00",
          "2022-02-07T00:00:00",
          "2022-02-08T00:00:00",
          "2022-02-09T00:00:00",
          "2022-02-10T00:00:00",
          "2022-02-11T00:00:00",
          "2022-02-14T00:00:00",
          "2022-02-15T00:00:00",
          "2022-02-16T00:00:00",
          "2022-02-17T00:00:00",
          "2022-02-18T00:00:00",
          "2022-02-21T00:00:00",
          "2022-02-22T00:00:00",
          "2022-02-23T00:00:00",
          "2022-02-24T00:00:00",
          "2022-02-25T00:00:00",
          "2022-03-02T00:00:00",
          "2022-03-03T00:00:00",
          "2022-03-04T00:00:00",
          "2022-03-07T00:00:00",
          "2022-03-08T00:00:00",
          "2022-03-09T00:00:00",
          "2022-03-10T00:00:00",
          "2022-03-11T00:00:00",
          "2022-03-14T00:00:00",
          "2022-03-15T00:00:00",
          "2022-03-16T00:00:00",
          "2022-03-17T00:00:00",
          "2022-03-18T00:00:00",
          "2022-03-21T00:00:00",
          "2022-03-22T00:00:00",
          "2022-03-23T00:00:00",
          "2022-03-24T00:00:00",
          "2022-03-25T00:00:00",
          "2022-03-28T00:00:00",
          "2022-03-29T00:00:00",
          "2022-03-30T00:00:00",
          "2022-03-31T00:00:00",
          "2022-04-01T00:00:00",
          "2022-04-04T00:00:00",
          "2022-04-05T00:00:00",
          "2022-04-06T00:00:00",
          "2022-04-07T00:00:00",
          "2022-04-08T00:00:00",
          "2022-04-11T00:00:00",
          "2022-04-12T00:00:00",
          "2022-04-13T00:00:00",
          "2022-04-14T00:00:00",
          "2022-04-18T00:00:00",
          "2022-04-19T00:00:00",
          "2022-04-20T00:00:00",
          "2022-04-22T00:00:00",
          "2022-04-25T00:00:00",
          "2022-04-26T00:00:00",
          "2022-04-27T00:00:00",
          "2022-04-28T00:00:00",
          "2022-04-29T00:00:00",
          "2022-05-02T00:00:00",
          "2022-05-03T00:00:00",
          "2022-05-04T00:00:00",
          "2022-05-05T00:00:00",
          "2022-05-06T00:00:00",
          "2022-05-09T00:00:00",
          "2022-05-10T00:00:00",
          "2022-05-11T00:00:00",
          "2022-05-12T00:00:00",
          "2022-05-13T00:00:00",
          "2022-05-16T00:00:00",
          "2022-05-17T00:00:00",
          "2022-05-18T00:00:00",
          "2022-05-19T00:00:00",
          "2022-05-20T00:00:00",
          "2022-05-23T00:00:00",
          "2022-05-24T00:00:00",
          "2022-05-25T00:00:00",
          "2022-05-26T00:00:00",
          "2022-05-27T00:00:00",
          "2022-05-30T00:00:00",
          "2022-05-31T00:00:00",
          "2022-06-01T00:00:00",
          "2022-06-02T00:00:00",
          "2022-06-03T00:00:00",
          "2022-06-06T00:00:00",
          "2022-06-07T00:00:00",
          "2022-06-08T00:00:00",
          "2022-06-09T00:00:00",
          "2022-06-10T00:00:00",
          "2022-06-13T00:00:00",
          "2022-06-14T00:00:00",
          "2022-06-15T00:00:00",
          "2022-06-17T00:00:00",
          "2022-06-20T00:00:00",
          "2022-06-21T00:00:00",
          "2022-06-22T00:00:00",
          "2022-06-23T00:00:00",
          "2022-06-24T00:00:00",
          "2022-06-27T00:00:00",
          "2022-06-28T00:00:00",
          "2022-06-29T00:00:00",
          "2022-06-30T00:00:00",
          "2022-07-01T00:00:00",
          "2022-07-04T00:00:00"
         ],
         "xaxis": "x",
         "y": [
          0,
          0.5586613608986063,
          -0.1523641267140165,
          1.2696761929320477,
          2.7425116585355718,
          3.098013746762702,
          3.2503778734767184,
          2.4885678954858172,
          4.316916104895652,
          5.99288953201229,
          6.602335383289175,
          8.532252573455567,
          7.1609967441877815,
          7.059417107852043,
          5.9421050416340115,
          8.176739829649255,
          12.493645278965728,
          12.595224915301465,
          13.15388627620007,
          14.77907521293843,
          15.794818298399905,
          16.201115532584495,
          14.01726523494753,
          15.693238662064166,
          16.455048640055068,
          16.04875140587048,
          15.388521064215315,
          5.4850233170711435,
          7.008632617473765,
          7.364145361280076,
          7.516509487994092,
          7.6180784687506495,
          8.887765317261879,
          7.6180784687506495,
          8.227524320027534,
          6.957848127095486,
          6.551550892910896,
          6.043674022390569,
          2.8440806392921285,
          3.3519575098124563,
          2.285419278393522,
          4.1645519781816365,
          1.168107212175491,
          -1.4220403196460643,
          -0.1523641267140165,
          6.246822639482864,
          5.586592297827701,
          5.129499917685651,
          5.891309895676552,
          5.637376788205978,
          7.1609967441877815,
          7.567293978372371,
          7.313350215322616,
          9.852713256765893,
          11.223969086033678,
          10.512954254000238,
          12.138143190738596,
          13.15388627620007,
          12.595224915301465,
          14.626711086224415,
          13.915696254190973,
          12.84916867835122,
          11.630266320218269,
          11.071615614898844,
          7.97359121255696,
          7.414929851658354,
          7.872011576221222,
          9.090903278774991,
          8.938549807640157,
          7.97359121255696,
          9.090903278774991,
          8.836970171304419,
          10.766887361470811,
          9.329609563595428,
          8.938549807640157,
          7.374300128239896,
          6.703915019624913,
          2.1229110402988676,
          2.7374289472660713,
          1.7877078304121952,
          0.4469269576030488,
          0.39105975595527,
          0.9497211168538763,
          2.40223639295858,
          -0.9497211168538763,
          1.1173227217972126,
          2.6257051995496954,
          3.631282862472169,
          5.419001348463546,
          6.089386457078528,
          7.318432926592116,
          9.106151412583493,
          11.340786200598737,
          9.273742361947647,
          8.43575564838933,
          9.888270924494034,
          11.675978754906229,
          14.02234794621703,
          12.737434275055662,
          13.351962837602047,
          14.972069063070906,
          13.854746341273694,
          14.525142105467857,
          12.458098266816767,
          11.899447561497343,
          11.22905179730318,
          11.340786200598737,
          10.391065083744861,
          8.43575564838933,
          8.37988844674155,
          6.759782221272692,
          5.1955325418724305,
          4.134077021722996,
          4.860339987564939,
          3.240223106516899,
          5.97765205378297,
          4.134077021722996,
          3.687150064119948,
          0.9497211168538763,
          0.11173440329555753,
          1.5083824777524826,
          0.055867201647778766,
          -1.6759734271166375,
          -3.9106082151318815,
          -3.18435590486912,
          -4.189944223370775
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "variable=ENEV3_cum_change<br>date=%{x}<br>value=%{y}<extra></extra>",
         "legendgroup": "ENEV3_cum_change",
         "line": {
          "color": "#FFA15A",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines",
         "name": "ENEV3_cum_change",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "visible": true,
         "x": [
          "2022-01-03T00:00:00",
          "2022-01-04T00:00:00",
          "2022-01-05T00:00:00",
          "2022-01-06T00:00:00",
          "2022-01-07T00:00:00",
          "2022-01-10T00:00:00",
          "2022-01-11T00:00:00",
          "2022-01-12T00:00:00",
          "2022-01-13T00:00:00",
          "2022-01-14T00:00:00",
          "2022-01-17T00:00:00",
          "2022-01-18T00:00:00",
          "2022-01-19T00:00:00",
          "2022-01-20T00:00:00",
          "2022-01-21T00:00:00",
          "2022-01-24T00:00:00",
          "2022-01-25T00:00:00",
          "2022-01-26T00:00:00",
          "2022-01-27T00:00:00",
          "2022-01-28T00:00:00",
          "2022-01-31T00:00:00",
          "2022-02-01T00:00:00",
          "2022-02-02T00:00:00",
          "2022-02-03T00:00:00",
          "2022-02-04T00:00:00",
          "2022-02-07T00:00:00",
          "2022-02-08T00:00:00",
          "2022-02-09T00:00:00",
          "2022-02-10T00:00:00",
          "2022-02-11T00:00:00",
          "2022-02-14T00:00:00",
          "2022-02-15T00:00:00",
          "2022-02-16T00:00:00",
          "2022-02-17T00:00:00",
          "2022-02-18T00:00:00",
          "2022-02-21T00:00:00",
          "2022-02-22T00:00:00",
          "2022-02-23T00:00:00",
          "2022-02-24T00:00:00",
          "2022-02-25T00:00:00",
          "2022-03-02T00:00:00",
          "2022-03-03T00:00:00",
          "2022-03-04T00:00:00",
          "2022-03-07T00:00:00",
          "2022-03-08T00:00:00",
          "2022-03-09T00:00:00",
          "2022-03-10T00:00:00",
          "2022-03-11T00:00:00",
          "2022-03-14T00:00:00",
          "2022-03-15T00:00:00",
          "2022-03-16T00:00:00",
          "2022-03-17T00:00:00",
          "2022-03-18T00:00:00",
          "2022-03-21T00:00:00",
          "2022-03-22T00:00:00",
          "2022-03-23T00:00:00",
          "2022-03-24T00:00:00",
          "2022-03-25T00:00:00",
          "2022-03-28T00:00:00",
          "2022-03-29T00:00:00",
          "2022-03-30T00:00:00",
          "2022-03-31T00:00:00",
          "2022-04-01T00:00:00",
          "2022-04-04T00:00:00",
          "2022-04-05T00:00:00",
          "2022-04-06T00:00:00",
          "2022-04-07T00:00:00",
          "2022-04-08T00:00:00",
          "2022-04-11T00:00:00",
          "2022-04-12T00:00:00",
          "2022-04-13T00:00:00",
          "2022-04-14T00:00:00",
          "2022-04-18T00:00:00",
          "2022-04-19T00:00:00",
          "2022-04-20T00:00:00",
          "2022-04-22T00:00:00",
          "2022-04-25T00:00:00",
          "2022-04-26T00:00:00",
          "2022-04-27T00:00:00",
          "2022-04-28T00:00:00",
          "2022-04-29T00:00:00",
          "2022-05-02T00:00:00",
          "2022-05-03T00:00:00",
          "2022-05-04T00:00:00",
          "2022-05-05T00:00:00",
          "2022-05-06T00:00:00",
          "2022-05-09T00:00:00",
          "2022-05-10T00:00:00",
          "2022-05-11T00:00:00",
          "2022-05-12T00:00:00",
          "2022-05-13T00:00:00",
          "2022-05-16T00:00:00",
          "2022-05-17T00:00:00",
          "2022-05-18T00:00:00",
          "2022-05-19T00:00:00",
          "2022-05-20T00:00:00",
          "2022-05-23T00:00:00",
          "2022-05-24T00:00:00",
          "2022-05-25T00:00:00",
          "2022-05-26T00:00:00",
          "2022-05-27T00:00:00",
          "2022-05-30T00:00:00",
          "2022-05-31T00:00:00",
          "2022-06-01T00:00:00",
          "2022-06-02T00:00:00",
          "2022-06-03T00:00:00",
          "2022-06-06T00:00:00",
          "2022-06-07T00:00:00",
          "2022-06-08T00:00:00",
          "2022-06-09T00:00:00",
          "2022-06-10T00:00:00",
          "2022-06-13T00:00:00",
          "2022-06-14T00:00:00",
          "2022-06-15T00:00:00",
          "2022-06-17T00:00:00",
          "2022-06-20T00:00:00",
          "2022-06-21T00:00:00",
          "2022-06-22T00:00:00",
          "2022-06-23T00:00:00",
          "2022-06-24T00:00:00",
          "2022-06-27T00:00:00",
          "2022-06-28T00:00:00",
          "2022-06-29T00:00:00",
          "2022-06-30T00:00:00",
          "2022-07-01T00:00:00",
          "2022-07-04T00:00:00"
         ],
         "xaxis": "x",
         "y": [
          0,
          -3.9434505172512524,
          -7.738095195858385,
          -9.151782594038215,
          -11.235114005594747,
          -11.011901699732936,
          -9.821426607414917,
          -6.919638248046298,
          -9.44940136711772,
          -5.505950849866468,
          -6.17559486324317,
          -6.622019474966794,
          -3.9434505172512524,
          -3.7202382113894403,
          -3.794637582815867,
          -5.13392560956927,
          -4.092256355895372,
          -2.752975424933234,
          -1.7857126384770274,
          -5.72916315572828,
          -1.7113061712593347,
          -1.3392809309621374,
          -1.636899704041642,
          -0.5952375461590091,
          -0.818449852020821,
          -2.752975424933234,
          -2.6785689577155414,
          0.1488129344353854,
          0.2232194016530781,
          -0.22321230586181187,
          -0.5952375461590091,
          1.7857197342682938,
          4.241076386122023,
          3.2738135996658166,
          1.6369067998329083,
          -0.37201814450593107,
          1.116075720891592,
          -0.07439937142642647,
          0.89286341502978,
          0.2232194016530781,
          0.2976187730795046,
          -2.0833314115565322,
          -4.836306836489766,
          -9.002976755394096,
          -7.142857649699376,
          -3.3482129710922433,
          -6.994044715263991,
          -10.863095861088816,
          -11.235114005594747,
          -10.49107062079162,
          -9.598214301553105,
          -5.877976090163665,
          3.2738135996658166,
          -0.37201814450593107,
          6.250001330460862,
          7.812501663076078,
          12.351196822277606,
          13.467265447377931,
          11.458333407247826,
          13.83929068767513,
          10.78869648966239,
          9.970239541850303,
          11.979171581980408,
          10.193458943503382,
          9.002976755394096,
          9.895840170423876,
          10.193458943503382,
          14.657740539695949,
          13.913697154892821,
          15.178571618637266,
          14.50893470105183,
          15.773816260587541,
          10.863095861088816,
          10.639883555227005,
          9.3005955284736,
          5.282738544004656,
          6.6220265707580594,
          3.4970259055276287,
          2.2321443459919177,
          3.0506012938040046,
          2.0833385073477984,
          -0.5208310789413164,
          0.3720252402971973,
          4.538695159201527,
          0.2976187730795046,
          0.89286341502978,
          -2.6785689577155414,
          -1.636899704041642,
          -3.497018809736362,
          -1.3392809309621374,
          1.1904821881092846,
          6.398814264896248,
          7.440476422778881,
          7.589289357214266,
          9.598214301553105,
          10.416671249365193,
          7.663695824431959,
          9.895840170423876,
          11.011908795524201,
          14.955359312775455,
          14.136909460754634,
          15.625003326152155,
          15.92262209923166,
          13.988096526319248,
          10.491077716582886,
          9.375001995691294,
          7.961314597511463,
          5.580357317084161,
          6.919645343837565,
          6.696433037975752,
          6.919645343837565,
          3.794644678607133,
          1.4881009611887892,
          5.505957945657734,
          8.184526903373275,
          9.226196157047175,
          10.491077716582886,
          10.639883555227005,
          6.919645343837565,
          6.845238876619872,
          13.020833739863042,
          14.211315927972326,
          11.3839340358214,
          9.895840170423876,
          12.64881559535711,
          10.3422647821475
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "variable=total_cum_change<br>date=%{x}<br>value=%{y}<extra></extra>",
         "legendgroup": "total_cum_change",
         "line": {
          "color": "#19d3f3",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines",
         "name": "total_cum_change",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "visible": true,
         "x": [
          "2022-01-03T00:00:00",
          "2022-01-04T00:00:00",
          "2022-01-05T00:00:00",
          "2022-01-06T00:00:00",
          "2022-01-07T00:00:00",
          "2022-01-10T00:00:00",
          "2022-01-11T00:00:00",
          "2022-01-12T00:00:00",
          "2022-01-13T00:00:00",
          "2022-01-14T00:00:00",
          "2022-01-17T00:00:00",
          "2022-01-18T00:00:00",
          "2022-01-19T00:00:00",
          "2022-01-20T00:00:00",
          "2022-01-21T00:00:00",
          "2022-01-24T00:00:00",
          "2022-01-25T00:00:00",
          "2022-01-26T00:00:00",
          "2022-01-27T00:00:00",
          "2022-01-28T00:00:00",
          "2022-01-31T00:00:00",
          "2022-02-01T00:00:00",
          "2022-02-02T00:00:00",
          "2022-02-03T00:00:00",
          "2022-02-04T00:00:00",
          "2022-02-07T00:00:00",
          "2022-02-08T00:00:00",
          "2022-02-09T00:00:00",
          "2022-02-10T00:00:00",
          "2022-02-11T00:00:00",
          "2022-02-14T00:00:00",
          "2022-02-15T00:00:00",
          "2022-02-16T00:00:00",
          "2022-02-17T00:00:00",
          "2022-02-18T00:00:00",
          "2022-02-21T00:00:00",
          "2022-02-22T00:00:00",
          "2022-02-23T00:00:00",
          "2022-02-24T00:00:00",
          "2022-02-25T00:00:00",
          "2022-03-02T00:00:00",
          "2022-03-03T00:00:00",
          "2022-03-04T00:00:00",
          "2022-03-07T00:00:00",
          "2022-03-08T00:00:00",
          "2022-03-09T00:00:00",
          "2022-03-10T00:00:00",
          "2022-03-11T00:00:00",
          "2022-03-14T00:00:00",
          "2022-03-15T00:00:00",
          "2022-03-16T00:00:00",
          "2022-03-17T00:00:00",
          "2022-03-18T00:00:00",
          "2022-03-21T00:00:00",
          "2022-03-22T00:00:00",
          "2022-03-23T00:00:00",
          "2022-03-24T00:00:00",
          "2022-03-25T00:00:00",
          "2022-03-28T00:00:00",
          "2022-03-29T00:00:00",
          "2022-03-30T00:00:00",
          "2022-03-31T00:00:00",
          "2022-04-01T00:00:00",
          "2022-04-04T00:00:00",
          "2022-04-05T00:00:00",
          "2022-04-06T00:00:00",
          "2022-04-07T00:00:00",
          "2022-04-08T00:00:00",
          "2022-04-11T00:00:00",
          "2022-04-12T00:00:00",
          "2022-04-13T00:00:00",
          "2022-04-14T00:00:00",
          "2022-04-18T00:00:00",
          "2022-04-19T00:00:00",
          "2022-04-20T00:00:00",
          "2022-04-22T00:00:00",
          "2022-04-25T00:00:00",
          "2022-04-26T00:00:00",
          "2022-04-27T00:00:00",
          "2022-04-28T00:00:00",
          "2022-04-29T00:00:00",
          "2022-05-02T00:00:00",
          "2022-05-03T00:00:00",
          "2022-05-04T00:00:00",
          "2022-05-05T00:00:00",
          "2022-05-06T00:00:00",
          "2022-05-09T00:00:00",
          "2022-05-10T00:00:00",
          "2022-05-11T00:00:00",
          "2022-05-12T00:00:00",
          "2022-05-13T00:00:00",
          "2022-05-16T00:00:00",
          "2022-05-17T00:00:00",
          "2022-05-18T00:00:00",
          "2022-05-19T00:00:00",
          "2022-05-20T00:00:00",
          "2022-05-23T00:00:00",
          "2022-05-24T00:00:00",
          "2022-05-25T00:00:00",
          "2022-05-26T00:00:00",
          "2022-05-27T00:00:00",
          "2022-05-30T00:00:00",
          "2022-05-31T00:00:00",
          "2022-06-01T00:00:00",
          "2022-06-02T00:00:00",
          "2022-06-03T00:00:00",
          "2022-06-06T00:00:00",
          "2022-06-07T00:00:00",
          "2022-06-08T00:00:00",
          "2022-06-09T00:00:00",
          "2022-06-10T00:00:00",
          "2022-06-13T00:00:00",
          "2022-06-14T00:00:00",
          "2022-06-15T00:00:00",
          "2022-06-17T00:00:00",
          "2022-06-20T00:00:00",
          "2022-06-21T00:00:00",
          "2022-06-22T00:00:00",
          "2022-06-23T00:00:00",
          "2022-06-24T00:00:00",
          "2022-06-27T00:00:00",
          "2022-06-28T00:00:00",
          "2022-06-29T00:00:00",
          "2022-06-30T00:00:00",
          "2022-07-01T00:00:00",
          "2022-07-04T00:00:00"
         ],
         "xaxis": "x",
         "y": [
          0,
          -2.50661163257255,
          -3.4457193102697037,
          -2.2917554828281856,
          -2.235535950898886,
          -3.7102685594616807,
          -2.8984714373694116,
          -2.266723622068344,
          -2.373200532142346,
          -0.6561147691830633,
          0.9548840429947867,
          -1.0129501779020675,
          0.0762395181895944,
          0.41475255601184746,
          -1.4036249993698253,
          -0.5790734227105512,
          2.01849257331527,
          2.029899549208357,
          2.256225032028939,
          2.8915119263862055,
          3.818359525272774,
          3.2592786627999986,
          1.172592954785245,
          0.14616368171099337,
          0.6946607453539055,
          -0.18551898595230953,
          -0.5818188877053824,
          -1.872841865288364,
          -0.4158515326360781,
          -1.478811916975085,
          -0.6872953358722654,
          -0.13775432242194147,
          2.163370945846129,
          1.8927668721430861,
          5.034746973652158,
          1.7576639333105284,
          2.544759585501011,
          1.0477893632131032,
          -0.14537077328876738,
          -1.7773521387081812,
          -3.371501804256798,
          -2.5512684072933935,
          -6.107868700400663,
          -11.003893141429211,
          -7.649999871783423,
          -2.7002995490077897,
          -4.569265953452851,
          -6.3959075015889475,
          -7.063034023590795,
          -5.219624577210447,
          -4.699720431032203,
          -3.177100689800116,
          1.3282532330140286,
          1.0969143792824854,
          3.627073327905876,
          3.357660809661568,
          6.699156328533865,
          7.949343295438984,
          7.3848728017365115,
          10.126866407061023,
          9.746473018729437,
          11.222207003835422,
          14.542760149617237,
          13.336485613595597,
          10.562944875883145,
          10.543107077403851,
          11.373645728446723,
          13.755174277486205,
          12.766794980690923,
          14.116947240234277,
          13.871356901793376,
          13.417776723279232,
          13.493198272222903,
          12.207898192618018,
          10.633907052802313,
          8.055974751189158,
          8.451656931307685,
          4.459743634414396,
          5.520412599644288,
          7.482067034965563,
          4.066368544354298,
          2.165117880432763,
          3.7664508070165583,
          5.4834779094172905,
          -0.7976652253958263,
          -1.0860422903074152,
          -1.588973095944689,
          -0.45476460032970045,
          -1.2482050361273473,
          1.0332546883087512,
          4.171698776667558,
          6.773630502024177,
          8.68676849152876,
          7.421249829323126,
          8.373104687767045,
          10.21159798368104,
          11.708274232325392,
          13.096257629739316,
          12.685770415345125,
          18.839392049365532,
          19.222690900579757,
          18.436655093595938,
          19.552963241573842,
          18.5612728751318,
          17.2802558158888,
          16.607539705645628,
          16.456528625890247,
          13.683218936933276,
          12.906817845098015,
          12.798258566325504,
          12.72041164734605,
          10.934550453171298,
          8.725048210669081,
          11.543764364678264,
          10.619480106470615,
          10.562816136862063,
          11.60276316566226,
          12.630847678165956,
          12.228777767594227,
          11.457776430101257,
          13.587702230777897,
          13.106573816337317,
          10.801619324579137,
          8.936309591111577,
          12.603805380871393,
          11.564567173021794
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "autosize": true,
        "legend": {
         "title": {
          "text": "variable"
         },
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "xaxis": {
         "anchor": "y",
         "autorange": true,
         "domain": [
          0,
          1
         ],
         "range": [
          "2022-01-03",
          "2022-07-04"
         ],
         "title": {
          "text": "date"
         },
         "type": "date"
        },
        "yaxis": {
         "anchor": "x",
         "autorange": true,
         "domain": [
          0,
          1
         ],
         "range": [
          -55.743388023162176,
          91.85478808848919
         ],
         "title": {
          "text": "value"
         },
         "type": "linear"
        }
       }
      },
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABpIAAAFoCAYAAABUsGgGAAAAAXNSR0IArs4c6QAAIABJREFUeF7s3QeYXFXB//HfnbIlvZGyqSRACkEIEQj6ShVRiihKgBcVCIS8FAWCQUIRIiWBGEARMEQQXvUPBF4UkaggVZAAApGWUNLJppFetkz7P+cuM8zOlpm7M3dm7sz3Po9PsjvnnHvO55yNM/vjnGvFYrGYuBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBIEbAIklgTCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACrQkQJLEuEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEWhUgSGJhIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIECSxBhBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBDIXYEdS5laURAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQTKSoAgqaymm8EigAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAApkLECRlbkVJBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQKCsBAiSymq6GSwCCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAgggkLkAQVLmVpREAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBMpKgCCprKabwSKAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACmQsQJGVuRUkEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAoKwECJLKaroZLAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCQuQBBUuZWlEQAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEykqAIKmsppvBIoAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAKZCxAkZW5FSQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEECgrAQIkspquhksAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIJC5AEFS5laURAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQTKSoAgqaymm8EigAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAApkLECRlbkVJBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQKCsBAiSymq6GSwCCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAgggkLkAQVLmVpREAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBMpKgCCprKabwSKAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACmQsQJGVuRUkEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAoKwECJLKaroZLAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCQuQBBUuZWlEQAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEykqAIKmsppvBIoAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAKZCxAkZW5FSQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEECgrAQIkspquhksAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIJC5AEFS5laURAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQTKSoAgqaymm8EigAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAApkLECRlbkVJBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQKCsBAiSymq6GSwCCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAgggkLkAQVLmVpREAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBMpKgCCprKabwSKAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACmQsQJGVuRUkEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAoKwECJLKaroZLAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCQuQBBUuZWlEQAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEykqAIKmsppvBIoAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAKZCxAkZW5FSQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEECgrAQIkspquhksAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIJC5AEFS5laURAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQTKSoAgqaymm8EigAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAApkLECRlbkVJBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQKCsBAiS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",
      "text/html": [
       "<div>                            <div id=\"fb32890c-dc1f-43a8-acb3-39023e878873\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"fb32890c-dc1f-43a8-acb3-39023e878873\")) {                    Plotly.newPlot(                        \"fb32890c-dc1f-43a8-acb3-39023e878873\",                        [{\"hovertemplate\":\"variable=ibov_cum_change<br>date=%{x}<br>value=%{y}<extra></extra>\",\"legendgroup\":\"ibov_cum_change\",\"line\":{\"color\":\"#636efa\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"lines\",\"name\":\"ibov_cum_change\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"2022-01-03T00:00:00\",\"2022-01-04T00:00:00\",\"2022-01-05T00:00:00\",\"2022-01-06T00:00:00\",\"2022-01-07T00:00:00\",\"2022-01-10T00:00:00\",\"2022-01-11T00:00:00\",\"2022-01-12T00:00:00\",\"2022-01-13T00:00:00\",\"2022-01-14T00:00:00\",\"2022-01-17T00:00:00\",\"2022-01-18T00:00:00\",\"2022-01-19T00:00:00\",\"2022-01-20T00:00:00\",\"2022-01-21T00:00:00\",\"2022-01-24T00:00:00\",\"2022-01-25T00:00:00\",\"2022-01-26T00:00:00\",\"2022-01-27T00:00:00\",\"2022-01-28T00:00:00\",\"2022-01-31T00:00:00\",\"2022-02-01T00:00:00\",\"2022-02-02T00:00:00\",\"2022-02-03T00:00:00\",\"2022-02-04T00:00:00\",\"2022-02-07T00:00:00\",\"2022-02-08T00:00:00\",\"2022-02-09T00:00:00\",\"2022-02-10T00:00:00\",\"2022-02-11T00:00:00\",\"2022-02-14T00:00:00\",\"2022-02-15T00:00:00\",\"2022-02-16T00:00:00\",\"2022-02-17T00:00:00\",\"2022-02-18T00:00:00\",\"2022-02-21T00:00:00\",\"2022-02-22T00:00:00\",\"2022-02-23T00:00:00\",\"2022-02-24T00:00:00\",\"2022-02-25T00:00:00\",\"2022-03-02T00:00:00\",\"2022-03-03T00:00:00\",\"2022-03-04T00:00:00\",\"2022-03-07T00:00:00\",\"2022-03-08T00:00:00\",\"2022-03-09T00:00:00\",\"2022-03-10T00:00:00\",\"2022-03-11T00:00:00\",\"2022-03-14T00:00:00\",\"2022-03-15T00:00:00\",\"2022-03-16T00:00:00\",\"2022-03-17T00:00:00\",\"2022-03-18T00:00:00\",\"2022-03-21T00:00:00\",\"2022-03-22T00:00:00\",\"2022-03-23T00:00:00\",\"2022-03-24T00:00:00\",\"2022-03-25T00:00:00\",\"2022-03-28T00:00:00\",\"2022-03-29T00:00:00\",\"2022-03-30T00:00:00\",\"2022-03-31T00:00:00\",\"2022-04-01T00:00:00\",\"2022-04-04T00:00:00\",\"2022-04-05T00:00:00\",\"2022-04-06T00:00:00\",\"2022-04-07T00:00:00\",\"2022-04-08T00:00:00\",\"2022-04-11T00:00:00\",\"2022-04-12T00:00:00\",\"2022-04-13T00:00:00\",\"2022-04-14T00:00:00\",\"2022-04-18T00:00:00\",\"2022-04-19T00:00:00\",\"2022-04-20T00:00:00\",\"2022-04-22T00:00:00\",\"2022-04-25T00:00:00\",\"2022-04-26T00:00:00\",\"2022-04-27T00:00:00\",\"2022-04-28T00:00:00\",\"2022-04-29T00:00:00\",\"2022-05-02T00:00:00\",\"2022-05-03T00:00:00\",\"2022-05-04T00:00:00\",\"2022-05-05T00:00:00\",\"2022-05-06T00:00:00\",\"2022-05-09T00:00:00\",\"2022-05-10T00:00:00\",\"2022-05-11T00:00:00\",\"2022-05-12T00:00:00\",\"2022-05-13T00:00:00\",\"2022-05-16T00:00:00\",\"2022-05-17T00:00:00\",\"2022-05-18T00:00:00\",\"2022-05-19T00:00:00\",\"2022-05-20T00:00:00\",\"2022-05-23T00:00:00\",\"2022-05-24T00:00:00\",\"2022-05-25T00:00:00\",\"2022-05-26T00:00:00\",\"2022-05-27T00:00:00\",\"2022-05-30T00:00:00\",\"2022-05-31T00:00:00\",\"2022-06-01T00:00:00\",\"2022-06-02T00:00:00\",\"2022-06-03T00:00:00\",\"2022-06-06T00:00:00\",\"2022-06-07T00:00:00\",\"2022-06-08T00:00:00\",\"2022-06-09T00:00:00\",\"2022-06-10T00:00:00\",\"2022-06-13T00:00:00\",\"2022-06-14T00:00:00\",\"2022-06-15T00:00:00\",\"2022-06-17T00:00:00\",\"2022-06-20T00:00:00\",\"2022-06-21T00:00:00\",\"2022-06-22T00:00:00\",\"2022-06-23T00:00:00\",\"2022-06-24T00:00:00\",\"2022-06-27T00:00:00\",\"2022-06-28T00:00:00\",\"2022-06-29T00:00:00\",\"2022-06-30T00:00:00\",\"2022-07-01T00:00:00\",\"2022-07-04T00:00:00\"],\"xaxis\":\"x\",\"y\":[0.0,-0.39260214391562903,-2.8059506168087602,-2.2718962298647063,-1.157598968457112,-1.90238832970882,-0.13760320240180135,1.697426916341102,1.5473143319027733,2.8925540309077964,2.6654606339369913,2.501876407305479,3.9366063008795056,4.984507611477839,4.830545986412886,3.685456399992302,5.699466907873212,7.362252458574701,8.076249494813418,7.270837743692384,8.146494486249303,8.876849945151172,7.928061430688401,7.480610457843382,8.0088912838475,7.769288504840168,7.998306422124285,8.216739477685186,9.080849098362233,9.28581051172995,9.5119416485441,10.332749562171628,10.834087103789381,9.24347106483709,8.512153345778565,7.508516002386405,8.631473605203903,7.78083562672004,7.380535401551163,8.87203864436789,10.827351282692788,10.819653201439541,10.153769173033622,7.38149766170782,7.0062162006119975,9.601431843113104,9.373376185985643,7.496968880506533,5.779334500875657,4.846904409076037,6.918650526356306,8.808529474028598,10.959180924154655,11.771328496372279,12.84617309135698,13.02419122033833,14.559958430361233,14.586901714747599,14.256846481014607,15.484690440907604,15.721406439444968,15.470256538557765,16.98196724466427,16.70291179923404,14.398298724043032,13.766093801120071,14.376166740439945,13.85654625584573,12.53921210138373,11.763630415119032,12.374665614595562,11.79730952060199,11.320990743057292,10.714766844364043,10.028675352668348,6.885933681030004,6.5077654394642135,4.129058332210697,5.2221858701718595,5.770674159465753,3.80477665941764,2.6144608456342255,2.5076499682454148,4.255114412732627,1.3298435364985277,1.1672215700236717,-0.6466388252728007,-0.7813552472046342,0.4570735744115779,1.6993514366544138,2.8887049902811723,4.148303535343816,4.683320182444525,2.237254864225092,2.9666480629703047,4.393679875291084,6.181559246357845,6.407690383171994,6.406728123015339,7.667288928234638,7.717326456380747,6.84166971382383,7.148630703797078,7.157291045206982,8.151305787032582,6.909027924789746,6.027597621292893,5.915975443120802,4.278208656492369,3.0522892169126847,1.5001635842266314,-1.2740324474124824,-1.7888416312234177,-1.072920074671388,-3.9423798618194414,-3.915436577433075,-4.077096283751275,-4.233944689286195,-5.62152383518408,-5.051865822443756,-3.038817574719501,-3.205288581820981,-4.1377186736206,-5.17695964280903,-4.780508458266777,-4.944002473008602],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"variable=CIEL3_cum_change<br>date=%{x}<br>value=%{y}<extra></extra>\",\"legendgroup\":\"CIEL3_cum_change\",\"line\":{\"color\":\"#EF553B\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"lines\",\"name\":\"CIEL3_cum_change\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"2022-01-03T00:00:00\",\"2022-01-04T00:00:00\",\"2022-01-05T00:00:00\",\"2022-01-06T00:00:00\",\"2022-01-07T00:00:00\",\"2022-01-10T00:00:00\",\"2022-01-11T00:00:00\",\"2022-01-12T00:00:00\",\"2022-01-13T00:00:00\",\"2022-01-14T00:00:00\",\"2022-01-17T00:00:00\",\"2022-01-18T00:00:00\",\"2022-01-19T00:00:00\",\"2022-01-20T00:00:00\",\"2022-01-21T00:00:00\",\"2022-01-24T00:00:00\",\"2022-01-25T00:00:00\",\"2022-01-26T00:00:00\",\"2022-01-27T00:00:00\",\"2022-01-28T00:00:00\",\"2022-01-31T00:00:00\",\"2022-02-01T00:00:00\",\"2022-02-02T00:00:00\",\"2022-02-03T00:00:00\",\"2022-02-04T00:00:00\",\"2022-02-07T00:00:00\",\"2022-02-08T00:00:00\",\"2022-02-09T00:00:00\",\"2022-02-10T00:00:00\",\"2022-02-11T00:00:00\",\"2022-02-14T00:00:00\",\"2022-02-15T00:00:00\",\"2022-02-16T00:00:00\",\"2022-02-17T00:00:00\",\"2022-02-18T00:00:00\",\"2022-02-21T00:00:00\",\"2022-02-22T00:00:00\",\"2022-02-23T00:00:00\",\"2022-02-24T00:00:00\",\"2022-02-25T00:00:00\",\"2022-03-02T00:00:00\",\"2022-03-03T00:00:00\",\"2022-03-04T00:00:00\",\"2022-03-07T00:00:00\",\"2022-03-08T00:00:00\",\"2022-03-09T00:00:00\",\"2022-03-10T00:00:00\",\"2022-03-11T00:00:00\",\"2022-03-14T00:00:00\",\"2022-03-15T00:00:00\",\"2022-03-16T00:00:00\",\"2022-03-17T00:00:00\",\"2022-03-18T00:00:00\",\"2022-03-21T00:00:00\",\"2022-03-22T00:00:00\",\"2022-03-23T00:00:00\",\"2022-03-24T00:00:00\",\"2022-03-25T00:00:00\",\"2022-03-28T00:00:00\",\"2022-03-29T00:00:00\",\"2022-03-30T00:00:00\",\"2022-03-31T00:00:00\",\"2022-04-01T00:00:00\",\"2022-04-04T00:00:00\",\"2022-04-05T00:00:00\",\"2022-04-06T00:00:00\",\"2022-04-07T00:00:00\",\"2022-04-08T00:00:00\",\"2022-04-11T00:00:00\",\"2022-04-12T00:00:00\",\"2022-04-13T00:00:00\",\"2022-04-14T00:00:00\",\"2022-04-18T00:00:00\",\"2022-04-19T00:00:00\",\"2022-04-20T00:00:00\",\"2022-04-22T00:00:00\",\"2022-04-25T00:00:00\",\"2022-04-26T00:00:00\",\"2022-04-27T00:00:00\",\"2022-04-28T00:00:00\",\"2022-04-29T00:00:00\",\"2022-05-02T00:00:00\",\"2022-05-03T00:00:00\",\"2022-05-04T00:00:00\",\"2022-05-05T00:00:00\",\"2022-05-06T00:00:00\",\"2022-05-09T00:00:00\",\"2022-05-10T00:00:00\",\"2022-05-11T00:00:00\",\"2022-05-12T00:00:00\",\"2022-05-13T00:00:00\",\"2022-05-16T00:00:00\",\"2022-05-17T00:00:00\",\"2022-05-18T00:00:00\",\"2022-05-19T00:00:00\",\"2022-05-20T00:00:00\",\"2022-05-23T00:00:00\",\"2022-05-24T00:00:00\",\"2022-05-25T00:00:00\",\"2022-05-26T00:00:00\",\"2022-05-27T00:00:00\",\"2022-05-30T00:00:00\",\"2022-05-31T00:00:00\",\"2022-06-01T00:00:00\",\"2022-06-02T00:00:00\",\"2022-06-03T00:00:00\",\"2022-06-06T00:00:00\",\"2022-06-07T00:00:00\",\"2022-06-08T00:00:00\",\"2022-06-09T00:00:00\",\"2022-06-10T00:00:00\",\"2022-06-13T00:00:00\",\"2022-06-14T00:00:00\",\"2022-06-15T00:00:00\",\"2022-06-17T00:00:00\",\"2022-06-20T00:00:00\",\"2022-06-21T00:00:00\",\"2022-06-22T00:00:00\",\"2022-06-23T00:00:00\",\"2022-06-24T00:00:00\",\"2022-06-27T00:00:00\",\"2022-06-28T00:00:00\",\"2022-06-29T00:00:00\",\"2022-06-30T00:00:00\",\"2022-07-01T00:00:00\",\"2022-07-04T00:00:00\"],\"xaxis\":\"x\",\"y\":[0.0,-3.1963547868679485,-3.6529753440358235,-5.936078129875197,-6.3926986870430715,-8.21918091571457,-5.022837015539448,-7.3059398013788215,-7.762560358546696,-7.762560358546696,-3.1963547868679485,-6.3926986870430715,-5.022837015539448,-2.283102785839374,-5.4794575727073225,-6.3926986870430715,-0.45662055716787475,0.0,-1.826482228671499,4.1095850145108725,5.0228261288466225,5.0228261288466225,6.392687800350247,0.0,6.392687800350247,6.8493083575181215,5.9360672431823716,5.479446686014497,8.675801472882446,5.9360672431823716,8.675801472882446,8.219170029021745,13.698627601729068,15.068489273232693,29.223737432129635,21.461187960275765,19.178074287743566,18.72145373057569,21.004567403107888,17.351592059072065,12.78538648739332,18.72145373057569,12.78538648739332,4.566205571678748,10.502283701553944,15.068489273232693,14.611868716064818,13.698627601729068,11.415524815889695,17.351592059072065,13.698627601729068,14.155248158896942,22.374429074611513,23.287670188947263,22.83104963177939,23.744290746115137,29.223737432129635,31.963471661829708,30.59359910363326,33.78995389050121,36.073056676340585,42.009123919522956,53.424648735412646,52.96802817824477,48.40182260656603,47.94520204939815,50.6849253924054,56.16438296511272,58.4474857509521,64.84017355130234,63.926932436966595,63.47031187979872,66.66666666666667,63.01369132263084,60.73058853679147,57.07762407944847,60.27396797962359,54.33790073644122,57.07762407944847,64.84017355130234,55.251141850776975,51.59816650674115,56.16438296511272,56.16438296511272,42.46574447669083,42.009123919522956,40.63926224801933,42.009123919522956,39.72602113368358,45.2054787063909,48.40182260656603,51.59816650674115,54.33790073644122,54.33790073644122,57.53424463661634,62.10045020829509,66.21004610949879,66.66666666666667,65.75342555233092,84.47487928290661,82.19177649706724,79.45205315405998,80.36529426839573,81.73515593989936,80.36529426839573,80.36529426839573,81.27853538273149,73.51597502418478,72.14611335268117,71.68949279551329,72.60273390984904,74.88583669568841,72.60273390984904,79.90867371122786,75.79907781002416,73.51597502418478,78.08219148255635,79.90867371122786,80.36529426839573,76.25569836719204,76.25569836719204,75.79907781002416,72.60273390984904,71.23287223834541,79.45205315405998,76.7123189243599],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"variable=BRFS3_cum_change<br>date=%{x}<br>value=%{y}<extra></extra>\",\"legendgroup\":\"BRFS3_cum_change\",\"line\":{\"color\":\"#00cc96\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"lines\",\"name\":\"BRFS3_cum_change\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"2022-01-03T00:00:00\",\"2022-01-04T00:00:00\",\"2022-01-05T00:00:00\",\"2022-01-06T00:00:00\",\"2022-01-07T00:00:00\",\"2022-01-10T00:00:00\",\"2022-01-11T00:00:00\",\"2022-01-12T00:00:00\",\"2022-01-13T00:00:00\",\"2022-01-14T00:00:00\",\"2022-01-17T00:00:00\",\"2022-01-18T00:00:00\",\"2022-01-19T00:00:00\",\"2022-01-20T00:00:00\",\"2022-01-21T00:00:00\",\"2022-01-24T00:00:00\",\"2022-01-25T00:00:00\",\"2022-01-26T00:00:00\",\"2022-01-27T00:00:00\",\"2022-01-28T00:00:00\",\"2022-01-31T00:00:00\",\"2022-02-01T00:00:00\",\"2022-02-02T00:00:00\",\"2022-02-03T00:00:00\",\"2022-02-04T00:00:00\",\"2022-02-07T00:00:00\",\"2022-02-08T00:00:00\",\"2022-02-09T00:00:00\",\"2022-02-10T00:00:00\",\"2022-02-11T00:00:00\",\"2022-02-14T00:00:00\",\"2022-02-15T00:00:00\",\"2022-02-16T00:00:00\",\"2022-02-17T00:00:00\",\"2022-02-18T00:00:00\",\"2022-02-21T00:00:00\",\"2022-02-22T00:00:00\",\"2022-02-23T00:00:00\",\"2022-02-24T00:00:00\",\"2022-02-25T00:00:00\",\"2022-03-02T00:00:00\",\"2022-03-03T00:00:00\",\"2022-03-04T00:00:00\",\"2022-03-07T00:00:00\",\"2022-03-08T00:00:00\",\"2022-03-09T00:00:00\",\"2022-03-10T00:00:00\",\"2022-03-11T00:00:00\",\"2022-03-14T00:00:00\",\"2022-03-15T00:00:00\",\"2022-03-16T00:00:00\",\"2022-03-17T00:00:00\",\"2022-03-18T00:00:00\",\"2022-03-21T00:00:00\",\"2022-03-22T00:00:00\",\"2022-03-23T00:00:00\",\"2022-03-24T00:00:00\",\"2022-03-25T00:00:00\",\"2022-03-28T00:00:00\",\"2022-03-29T00:00:00\",\"2022-03-30T00:00:00\",\"2022-03-31T00:00:00\",\"2022-04-01T00:00:00\",\"2022-04-04T00:00:00\",\"2022-04-05T00:00:00\",\"2022-04-06T00:00:00\",\"2022-04-07T00:00:00\",\"2022-04-08T00:00:00\",\"2022-04-11T00:00:00\",\"2022-04-12T00:00:00\",\"2022-04-13T00:00:00\",\"2022-04-14T00:00:00\",\"2022-04-18T00:00:00\",\"2022-04-19T00:00:00\",\"2022-04-20T00:00:00\",\"2022-04-22T00:00:00\",\"2022-04-25T00:00:00\",\"2022-04-26T00:00:00\",\"2022-04-27T00:00:00\",\"2022-04-28T00:00:00\",\"2022-04-29T00:00:00\",\"2022-05-02T00:00:00\",\"2022-05-03T00:00:00\",\"2022-05-04T00:00:00\",\"2022-05-05T00:00:00\",\"2022-05-06T00:00:00\",\"2022-05-09T00:00:00\",\"2022-05-10T00:00:00\",\"2022-05-11T00:00:00\",\"2022-05-12T00:00:00\",\"2022-05-13T00:00:00\",\"2022-05-16T00:00:00\",\"2022-05-17T00:00:00\",\"2022-05-18T00:00:00\",\"2022-05-19T00:00:00\",\"2022-05-20T00:00:00\",\"2022-05-23T00:00:00\",\"2022-05-24T00:00:00\",\"2022-05-25T00:00:00\",\"2022-05-26T00:00:00\",\"2022-05-27T00:00:00\",\"2022-05-30T00:00:00\",\"2022-05-31T00:00:00\",\"2022-06-01T00:00:00\",\"2022-06-02T00:00:00\",\"2022-06-03T00:00:00\",\"2022-06-06T00:00:00\",\"2022-06-07T00:00:00\",\"2022-06-08T00:00:00\",\"2022-06-09T00:00:00\",\"2022-06-10T00:00:00\",\"2022-06-13T00:00:00\",\"2022-06-14T00:00:00\",\"2022-06-15T00:00:00\",\"2022-06-17T00:00:00\",\"2022-06-20T00:00:00\",\"2022-06-21T00:00:00\",\"2022-06-22T00:00:00\",\"2022-06-23T00:00:00\",\"2022-06-24T00:00:00\",\"2022-06-27T00:00:00\",\"2022-06-28T00:00:00\",\"2022-06-29T00:00:00\",\"2022-06-30T00:00:00\",\"2022-07-01T00:00:00\",\"2022-07-04T00:00:00\"],\"xaxis\":\"x\",\"y\":[0.0,-3.4453025870696052,-2.2394425744705897,4.651162599668621,5.943157230506704,1.2919946308380825,0.0,2.6701156656659246,3.4022434921993794,4.651162599668621,6.589150438801091,0.4306648769460275,2.1102488613612964,0.6029341134241616,-2.282509883590123,1.0335907761208816,0.12920192735860053,-1.7226512935348026,-0.516791280935787,-1.5934493661762021,-3.832900154896099,-6.847546079268985,-14.082681512115155,-14.513346389061184,-19.250643606968872,-20.887160282264606,-20.973294900503674,-18.604650398674483,-17.5710596225536,-18.992247966500976,-18.34625475820659,-18.173985521728454,-18.173985521728454,-18.389313853076814,-18.949180657381444,-21.016362209623207,-16.66666255954201,-20.49957092868742,-25.322994550584866,-28.036177525370324,-28.85443175589354,-31.007747926374368,-33.548661664681696,-38.156761062355436,-33.807061412274244,-28.76829713765447,-31.48148011243993,-33.548661664681696,-34.32385680033468,-33.37639653532821,-30.060291768492554,-28.55296880630611,-27.64857995754383,-28.380707784077284,-25.796726736650427,-28.63910342454518,-26.916452131010377,-26.787250203651777,-25.107666219236506,-21.74849003615666,-21.791557345276196,-19.939704124382793,-18.863046039142375,-20.887160282264606,-23.126611070984502,-23.08354376186497,-23.255812998343103,-24.89232967363884,-30.232552790721382,-31.524547421559465,-32.041342809619906,-34.409991418573746,-34.32385680033468,-34.151591670981205,-36.43410566169598,-37.51076374693639,-39.79328184477583,-42.11886314461013,-39.9655469741293,-39.75021453565629,-41.51593313831063,-42.80792366202405,-42.42032609419756,-41.17140287960367,-45.00430303449976,-48.36347921757961,-46.94229087363224,-45.822565479272285,-46.640823816920154,-45.822565479272285,-40.2239426145972,-40.008610176124186,-38.372089393703796,-41.51593313831063,-42.0757958354906,-41.55900044743016,-38.71662375953541,-38.19982426435031,-38.759686961530285,-37.42463323582198,-34.409991418573746,-35.185182447102086,-32.60120550679988,-33.936259232508185,-33.63479628292076,-34.539189238807694,-34.75452167728071,-34.75452167728071,-35.87424296451601,-35.572780014928576,-35.4005148855751,-40.13781210348279,-43.3247190500845,-44.09991418573748,-44.745907394031875,-46.46855868756668,-46.29629355821319,-43.71231661791099,-39.319549658710265,-37.38156592670244,-36.43410566169598,-37.63996567429499,-39.104217220237246,-41.47286582919109,-38.501291321062396,-36.60637079104946],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"variable=BBDC4_cum_change<br>date=%{x}<br>value=%{y}<extra></extra>\",\"legendgroup\":\"BBDC4_cum_change\",\"line\":{\"color\":\"#ab63fa\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"lines\",\"name\":\"BBDC4_cum_change\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"2022-01-03T00:00:00\",\"2022-01-04T00:00:00\",\"2022-01-05T00:00:00\",\"2022-01-06T00:00:00\",\"2022-01-07T00:00:00\",\"2022-01-10T00:00:00\",\"2022-01-11T00:00:00\",\"2022-01-12T00:00:00\",\"2022-01-13T00:00:00\",\"2022-01-14T00:00:00\",\"2022-01-17T00:00:00\",\"2022-01-18T00:00:00\",\"2022-01-19T00:00:00\",\"2022-01-20T00:00:00\",\"2022-01-21T00:00:00\",\"2022-01-24T00:00:00\",\"2022-01-25T00:00:00\",\"2022-01-26T00:00:00\",\"2022-01-27T00:00:00\",\"2022-01-28T00:00:00\",\"2022-01-31T00:00:00\",\"2022-02-01T00:00:00\",\"2022-02-02T00:00:00\",\"2022-02-03T00:00:00\",\"2022-02-04T00:00:00\",\"2022-02-07T00:00:00\",\"2022-02-08T00:00:00\",\"2022-02-09T00:00:00\",\"2022-02-10T00:00:00\",\"2022-02-11T00:00:00\",\"2022-02-14T00:00:00\",\"2022-02-15T00:00:00\",\"2022-02-16T00:00:00\",\"2022-02-17T00:00:00\",\"2022-02-18T00:00:00\",\"2022-02-21T00:00:00\",\"2022-02-22T00:00:00\",\"2022-02-23T00:00:00\",\"2022-02-24T00:00:00\",\"2022-02-25T00:00:00\",\"2022-03-02T00:00:00\",\"2022-03-03T00:00:00\",\"2022-03-04T00:00:00\",\"2022-03-07T00:00:00\",\"2022-03-08T00:00:00\",\"2022-03-09T00:00:00\",\"2022-03-10T00:00:00\",\"2022-03-11T00:00:00\",\"2022-03-14T00:00:00\",\"2022-03-15T00:00:00\",\"2022-03-16T00:00:00\",\"2022-03-17T00:00:00\",\"2022-03-18T00:00:00\",\"2022-03-21T00:00:00\",\"2022-03-22T00:00:00\",\"2022-03-23T00:00:00\",\"2022-03-24T00:00:00\",\"2022-03-25T00:00:00\",\"2022-03-28T00:00:00\",\"2022-03-29T00:00:00\",\"2022-03-30T00:00:00\",\"2022-03-31T00:00:00\",\"2022-04-01T00:00:00\",\"2022-04-04T00:00:00\",\"2022-04-05T00:00:00\",\"2022-04-06T00:00:00\",\"2022-04-07T00:00:00\",\"2022-04-08T00:00:00\",\"2022-04-11T00:00:00\",\"2022-04-12T00:00:00\",\"2022-04-13T00:00:00\",\"2022-04-14T00:00:00\",\"2022-04-18T00:00:00\",\"2022-04-19T00:00:00\",\"2022-04-20T00:00:00\",\"2022-04-22T00:00:00\",\"2022-04-25T00:00:00\",\"2022-04-26T00:00:00\",\"2022-04-27T00:00:00\",\"2022-04-28T00:00:00\",\"2022-04-29T00:00:00\",\"2022-05-02T00:00:00\",\"2022-05-03T00:00:00\",\"2022-05-04T00:00:00\",\"2022-05-05T00:00:00\",\"2022-05-06T00:00:00\",\"2022-05-09T00:00:00\",\"2022-05-10T00:00:00\",\"2022-05-11T00:00:00\",\"2022-05-12T00:00:00\",\"2022-05-13T00:00:00\",\"2022-05-16T00:00:00\",\"2022-05-17T00:00:00\",\"2022-05-18T00:00:00\",\"2022-05-19T00:00:00\",\"2022-05-20T00:00:00\",\"2022-05-23T00:00:00\",\"2022-05-24T00:00:00\",\"2022-05-25T00:00:00\",\"2022-05-26T00:00:00\",\"2022-05-27T00:00:00\",\"2022-05-30T00:00:00\",\"2022-05-31T00:00:00\",\"2022-06-01T00:00:00\",\"2022-06-02T00:00:00\",\"2022-06-03T00:00:00\",\"2022-06-06T00:00:00\",\"2022-06-07T00:00:00\",\"2022-06-08T00:00:00\",\"2022-06-09T00:00:00\",\"2022-06-10T00:00:00\",\"2022-06-13T00:00:00\",\"2022-06-14T00:00:00\",\"2022-06-15T00:00:00\",\"2022-06-17T00:00:00\",\"2022-06-20T00:00:00\",\"2022-06-21T00:00:00\",\"2022-06-22T00:00:00\",\"2022-06-23T00:00:00\",\"2022-06-24T00:00:00\",\"2022-06-27T00:00:00\",\"2022-06-28T00:00:00\",\"2022-06-29T00:00:00\",\"2022-06-30T00:00:00\",\"2022-07-01T00:00:00\",\"2022-07-04T00:00:00\"],\"xaxis\":\"x\",\"y\":[0.0,0.5586613608986063,-0.1523641267140165,1.2696761929320477,2.7425116585355718,3.098013746762702,3.2503778734767184,2.4885678954858172,4.316916104895652,5.99288953201229,6.602335383289175,8.532252573455567,7.1609967441877815,7.059417107852043,5.9421050416340115,8.176739829649255,12.493645278965728,12.595224915301465,13.15388627620007,14.77907521293843,15.794818298399905,16.201115532584495,14.01726523494753,15.693238662064166,16.455048640055068,16.04875140587048,15.388521064215315,5.4850233170711435,7.008632617473765,7.364145361280076,7.516509487994092,7.6180784687506495,8.887765317261879,7.6180784687506495,8.227524320027534,6.957848127095486,6.551550892910896,6.043674022390569,2.8440806392921285,3.3519575098124563,2.285419278393522,4.1645519781816365,1.168107212175491,-1.4220403196460643,-0.1523641267140165,6.246822639482864,5.586592297827701,5.129499917685651,5.891309895676552,5.637376788205978,7.1609967441877815,7.567293978372371,7.313350215322616,9.852713256765893,11.223969086033678,10.512954254000238,12.138143190738596,13.15388627620007,12.595224915301465,14.626711086224415,13.915696254190973,12.84916867835122,11.630266320218269,11.071615614898844,7.97359121255696,7.414929851658354,7.872011576221222,9.090903278774991,8.938549807640157,7.97359121255696,9.090903278774991,8.836970171304419,10.766887361470811,9.329609563595428,8.938549807640157,7.374300128239896,6.703915019624913,2.1229110402988676,2.7374289472660713,1.7877078304121952,0.4469269576030488,0.39105975595527,0.9497211168538763,2.40223639295858,-0.9497211168538763,1.1173227217972126,2.6257051995496954,3.631282862472169,5.419001348463546,6.089386457078528,7.318432926592116,9.106151412583493,11.340786200598737,9.273742361947647,8.43575564838933,9.888270924494034,11.675978754906229,14.02234794621703,12.737434275055662,13.351962837602047,14.972069063070906,13.854746341273694,14.525142105467857,12.458098266816767,11.899447561497343,11.22905179730318,11.340786200598737,10.391065083744861,8.43575564838933,8.37988844674155,6.759782221272692,5.1955325418724305,4.134077021722996,4.860339987564939,3.240223106516899,5.97765205378297,4.134077021722996,3.687150064119948,0.9497211168538763,0.11173440329555753,1.5083824777524826,0.055867201647778766,-1.6759734271166375,-3.9106082151318815,-3.18435590486912,-4.189944223370775],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"variable=ENEV3_cum_change<br>date=%{x}<br>value=%{y}<extra></extra>\",\"legendgroup\":\"ENEV3_cum_change\",\"line\":{\"color\":\"#FFA15A\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"lines\",\"name\":\"ENEV3_cum_change\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"2022-01-03T00:00:00\",\"2022-01-04T00:00:00\",\"2022-01-05T00:00:00\",\"2022-01-06T00:00:00\",\"2022-01-07T00:00:00\",\"2022-01-10T00:00:00\",\"2022-01-11T00:00:00\",\"2022-01-12T00:00:00\",\"2022-01-13T00:00:00\",\"2022-01-14T00:00:00\",\"2022-01-17T00:00:00\",\"2022-01-18T00:00:00\",\"2022-01-19T00:00:00\",\"2022-01-20T00:00:00\",\"2022-01-21T00:00:00\",\"2022-01-24T00:00:00\",\"2022-01-25T00:00:00\",\"2022-01-26T00:00:00\",\"2022-01-27T00:00:00\",\"2022-01-28T00:00:00\",\"2022-01-31T00:00:00\",\"2022-02-01T00:00:00\",\"2022-02-02T00:00:00\",\"2022-02-03T00:00:00\",\"2022-02-04T00:00:00\",\"2022-02-07T00:00:00\",\"2022-02-08T00:00:00\",\"2022-02-09T00:00:00\",\"2022-02-10T00:00:00\",\"2022-02-11T00:00:00\",\"2022-02-14T00:00:00\",\"2022-02-15T00:00:00\",\"2022-02-16T00:00:00\",\"2022-02-17T00:00:00\",\"2022-02-18T00:00:00\",\"2022-02-21T00:00:00\",\"2022-02-22T00:00:00\",\"2022-02-23T00:00:00\",\"2022-02-24T00:00:00\",\"2022-02-25T00:00:00\",\"2022-03-02T00:00:00\",\"2022-03-03T00:00:00\",\"2022-03-04T00:00:00\",\"2022-03-07T00:00:00\",\"2022-03-08T00:00:00\",\"2022-03-09T00:00:00\",\"2022-03-10T00:00:00\",\"2022-03-11T00:00:00\",\"2022-03-14T00:00:00\",\"2022-03-15T00:00:00\",\"2022-03-16T00:00:00\",\"2022-03-17T00:00:00\",\"2022-03-18T00:00:00\",\"2022-03-21T00:00:00\",\"2022-03-22T00:00:00\",\"2022-03-23T00:00:00\",\"2022-03-24T00:00:00\",\"2022-03-25T00:00:00\",\"2022-03-28T00:00:00\",\"2022-03-29T00:00:00\",\"2022-03-30T00:00:00\",\"2022-03-31T00:00:00\",\"2022-04-01T00:00:00\",\"2022-04-04T00:00:00\",\"2022-04-05T00:00:00\",\"2022-04-06T00:00:00\",\"2022-04-07T00:00:00\",\"2022-04-08T00:00:00\",\"2022-04-11T00:00:00\",\"2022-04-12T00:00:00\",\"2022-04-13T00:00:00\",\"2022-04-14T00:00:00\",\"2022-04-18T00:00:00\",\"2022-04-19T00:00:00\",\"2022-04-20T00:00:00\",\"2022-04-22T00:00:00\",\"2022-04-25T00:00:00\",\"2022-04-26T00:00:00\",\"2022-04-27T00:00:00\",\"2022-04-28T00:00:00\",\"2022-04-29T00:00:00\",\"2022-05-02T00:00:00\",\"2022-05-03T00:00:00\",\"2022-05-04T00:00:00\",\"2022-05-05T00:00:00\",\"2022-05-06T00:00:00\",\"2022-05-09T00:00:00\",\"2022-05-10T00:00:00\",\"2022-05-11T00:00:00\",\"2022-05-12T00:00:00\",\"2022-05-13T00:00:00\",\"2022-05-16T00:00:00\",\"2022-05-17T00:00:00\",\"2022-05-18T00:00:00\",\"2022-05-19T00:00:00\",\"2022-05-20T00:00:00\",\"2022-05-23T00:00:00\",\"2022-05-24T00:00:00\",\"2022-05-25T00:00:00\",\"2022-05-26T00:00:00\",\"2022-05-27T00:00:00\",\"2022-05-30T00:00:00\",\"2022-05-31T00:00:00\",\"2022-06-01T00:00:00\",\"2022-06-02T00:00:00\",\"2022-06-03T00:00:00\",\"2022-06-06T00:00:00\",\"2022-06-07T00:00:00\",\"2022-06-08T00:00:00\",\"2022-06-09T00:00:00\",\"2022-06-10T00:00:00\",\"2022-06-13T00:00:00\",\"2022-06-14T00:00:00\",\"2022-06-15T00:00:00\",\"2022-06-17T00:00:00\",\"2022-06-20T00:00:00\",\"2022-06-21T00:00:00\",\"2022-06-22T00:00:00\",\"2022-06-23T00:00:00\",\"2022-06-24T00:00:00\",\"2022-06-27T00:00:00\",\"2022-06-28T00:00:00\",\"2022-06-29T00:00:00\",\"2022-06-30T00:00:00\",\"2022-07-01T00:00:00\",\"2022-07-04T00:00:00\"],\"xaxis\":\"x\",\"y\":[0.0,-3.9434505172512524,-7.738095195858385,-9.151782594038215,-11.235114005594747,-11.011901699732936,-9.821426607414917,-6.919638248046298,-9.44940136711772,-5.505950849866468,-6.17559486324317,-6.622019474966794,-3.9434505172512524,-3.7202382113894403,-3.794637582815867,-5.13392560956927,-4.092256355895372,-2.752975424933234,-1.7857126384770274,-5.72916315572828,-1.7113061712593347,-1.3392809309621374,-1.636899704041642,-0.5952375461590091,-0.818449852020821,-2.752975424933234,-2.6785689577155414,0.1488129344353854,0.2232194016530781,-0.22321230586181187,-0.5952375461590091,1.7857197342682938,4.241076386122023,3.2738135996658166,1.6369067998329083,-0.37201814450593107,1.116075720891592,-0.07439937142642647,0.89286341502978,0.2232194016530781,0.2976187730795046,-2.0833314115565322,-4.836306836489766,-9.002976755394096,-7.142857649699376,-3.3482129710922433,-6.994044715263991,-10.863095861088816,-11.235114005594747,-10.49107062079162,-9.598214301553105,-5.877976090163665,3.2738135996658166,-0.37201814450593107,6.250001330460862,7.812501663076078,12.351196822277606,13.467265447377931,11.458333407247826,13.83929068767513,10.78869648966239,9.970239541850303,11.979171581980408,10.193458943503382,9.002976755394096,9.895840170423876,10.193458943503382,14.657740539695949,13.913697154892821,15.178571618637266,14.50893470105183,15.773816260587541,10.863095861088816,10.639883555227005,9.3005955284736,5.282738544004656,6.6220265707580594,3.4970259055276287,2.2321443459919177,3.0506012938040046,2.0833385073477984,-0.5208310789413164,0.3720252402971973,4.538695159201527,0.2976187730795046,0.89286341502978,-2.6785689577155414,-1.636899704041642,-3.497018809736362,-1.3392809309621374,1.1904821881092846,6.398814264896248,7.440476422778881,7.589289357214266,9.598214301553105,10.416671249365193,7.663695824431959,9.895840170423876,11.011908795524201,14.955359312775455,14.136909460754634,15.625003326152155,15.92262209923166,13.988096526319248,10.491077716582886,9.375001995691294,7.961314597511463,5.580357317084161,6.919645343837565,6.696433037975752,6.919645343837565,3.794644678607133,1.4881009611887892,5.505957945657734,8.184526903373275,9.226196157047175,10.491077716582886,10.639883555227005,6.919645343837565,6.845238876619872,13.020833739863042,14.211315927972326,11.3839340358214,9.895840170423876,12.64881559535711,10.3422647821475],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"variable=total_cum_change<br>date=%{x}<br>value=%{y}<extra></extra>\",\"legendgroup\":\"total_cum_change\",\"line\":{\"color\":\"#19d3f3\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"lines\",\"name\":\"total_cum_change\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[\"2022-01-03T00:00:00\",\"2022-01-04T00:00:00\",\"2022-01-05T00:00:00\",\"2022-01-06T00:00:00\",\"2022-01-07T00:00:00\",\"2022-01-10T00:00:00\",\"2022-01-11T00:00:00\",\"2022-01-12T00:00:00\",\"2022-01-13T00:00:00\",\"2022-01-14T00:00:00\",\"2022-01-17T00:00:00\",\"2022-01-18T00:00:00\",\"2022-01-19T00:00:00\",\"2022-01-20T00:00:00\",\"2022-01-21T00:00:00\",\"2022-01-24T00:00:00\",\"2022-01-25T00:00:00\",\"2022-01-26T00:00:00\",\"2022-01-27T00:00:00\",\"2022-01-28T00:00:00\",\"2022-01-31T00:00:00\",\"2022-02-01T00:00:00\",\"2022-02-02T00:00:00\",\"2022-02-03T00:00:00\",\"2022-02-04T00:00:00\",\"2022-02-07T00:00:00\",\"2022-02-08T00:00:00\",\"2022-02-09T00:00:00\",\"2022-02-10T00:00:00\",\"2022-02-11T00:00:00\",\"2022-02-14T00:00:00\",\"2022-02-15T00:00:00\",\"2022-02-16T00:00:00\",\"2022-02-17T00:00:00\",\"2022-02-18T00:00:00\",\"2022-02-21T00:00:00\",\"2022-02-22T00:00:00\",\"2022-02-23T00:00:00\",\"2022-02-24T00:00:00\",\"2022-02-25T00:00:00\",\"2022-03-02T00:00:00\",\"2022-03-03T00:00:00\",\"2022-03-04T00:00:00\",\"2022-03-07T00:00:00\",\"2022-03-08T00:00:00\",\"2022-03-09T00:00:00\",\"2022-03-10T00:00:00\",\"2022-03-11T00:00:00\",\"2022-03-14T00:00:00\",\"2022-03-15T00:00:00\",\"2022-03-16T00:00:00\",\"2022-03-17T00:00:00\",\"2022-03-18T00:00:00\",\"2022-03-21T00:00:00\",\"2022-03-22T00:00:00\",\"2022-03-23T00:00:00\",\"2022-03-24T00:00:00\",\"2022-03-25T00:00:00\",\"2022-03-28T00:00:00\",\"2022-03-29T00:00:00\",\"2022-03-30T00:00:00\",\"2022-03-31T00:00:00\",\"2022-04-01T00:00:00\",\"2022-04-04T00:00:00\",\"2022-04-05T00:00:00\",\"2022-04-06T00:00:00\",\"2022-04-07T00:00:00\",\"2022-04-08T00:00:00\",\"2022-04-11T00:00:00\",\"2022-04-12T00:00:00\",\"2022-04-13T00:00:00\",\"2022-04-14T00:00:00\",\"2022-04-18T00:00:00\",\"2022-04-19T00:00:00\",\"2022-04-20T00:00:00\",\"2022-04-22T00:00:00\",\"2022-04-25T00:00:00\",\"2022-04-26T00:00:00\",\"2022-04-27T00:00:00\",\"2022-04-28T00:00:00\",\"2022-04-29T00:00:00\",\"2022-05-02T00:00:00\",\"2022-05-03T00:00:00\",\"2022-05-04T00:00:00\",\"2022-05-05T00:00:00\",\"2022-05-06T00:00:00\",\"2022-05-09T00:00:00\",\"2022-05-10T00:00:00\",\"2022-05-11T00:00:00\",\"2022-05-12T00:00:00\",\"2022-05-13T00:00:00\",\"2022-05-16T00:00:00\",\"2022-05-17T00:00:00\",\"2022-05-18T00:00:00\",\"2022-05-19T00:00:00\",\"2022-05-20T00:00:00\",\"2022-05-23T00:00:00\",\"2022-05-24T00:00:00\",\"2022-05-25T00:00:00\",\"2022-05-26T00:00:00\",\"2022-05-27T00:00:00\",\"2022-05-30T00:00:00\",\"2022-05-31T00:00:00\",\"2022-06-01T00:00:00\",\"2022-06-02T00:00:00\",\"2022-06-03T00:00:00\",\"2022-06-06T00:00:00\",\"2022-06-07T00:00:00\",\"2022-06-08T00:00:00\",\"2022-06-09T00:00:00\",\"2022-06-10T00:00:00\",\"2022-06-13T00:00:00\",\"2022-06-14T00:00:00\",\"2022-06-15T00:00:00\",\"2022-06-17T00:00:00\",\"2022-06-20T00:00:00\",\"2022-06-21T00:00:00\",\"2022-06-22T00:00:00\",\"2022-06-23T00:00:00\",\"2022-06-24T00:00:00\",\"2022-06-27T00:00:00\",\"2022-06-28T00:00:00\",\"2022-06-29T00:00:00\",\"2022-06-30T00:00:00\",\"2022-07-01T00:00:00\",\"2022-07-04T00:00:00\"],\"xaxis\":\"x\",\"y\":[0.0,-2.50661163257255,-3.4457193102697037,-2.2917554828281856,-2.235535950898886,-3.7102685594616807,-2.8984714373694116,-2.266723622068344,-2.373200532142346,-0.6561147691830633,0.9548840429947867,-1.0129501779020675,0.0762395181895944,0.41475255601184746,-1.4036249993698253,-0.5790734227105512,2.01849257331527,2.029899549208357,2.256225032028939,2.8915119263862055,3.818359525272774,3.2592786627999986,1.172592954785245,0.14616368171099337,0.6946607453539055,-0.18551898595230953,-0.5818188877053824,-1.872841865288364,-0.4158515326360781,-1.478811916975085,-0.6872953358722654,-0.13775432242194147,2.163370945846129,1.8927668721430861,5.034746973652158,1.7576639333105284,2.544759585501011,1.0477893632131032,-0.14537077328876738,-1.7773521387081812,-3.371501804256798,-2.5512684072933935,-6.107868700400663,-11.003893141429211,-7.649999871783423,-2.7002995490077897,-4.569265953452851,-6.3959075015889475,-7.063034023590795,-5.219624577210447,-4.699720431032203,-3.177100689800116,1.3282532330140286,1.0969143792824854,3.627073327905876,3.357660809661568,6.699156328533865,7.949343295438984,7.3848728017365115,10.126866407061023,9.746473018729437,11.222207003835422,14.542760149617237,13.336485613595597,10.562944875883145,10.543107077403851,11.373645728446723,13.755174277486205,12.766794980690923,14.116947240234277,13.871356901793376,13.417776723279232,13.493198272222903,12.207898192618018,10.633907052802313,8.055974751189158,8.451656931307685,4.459743634414396,5.520412599644288,7.482067034965563,4.066368544354298,2.165117880432763,3.7664508070165583,5.4834779094172905,-0.7976652253958263,-1.0860422903074152,-1.588973095944689,-0.45476460032970045,-1.2482050361273473,1.0332546883087512,4.171698776667558,6.773630502024177,8.68676849152876,7.421249829323126,8.373104687767045,10.21159798368104,11.708274232325392,13.096257629739316,12.685770415345125,18.839392049365532,19.222690900579757,18.436655093595938,19.552963241573842,18.5612728751318,17.2802558158888,16.607539705645628,16.456528625890247,13.683218936933276,12.906817845098015,12.798258566325504,12.72041164734605,10.934550453171298,8.725048210669081,11.543764364678264,10.619480106470615,10.562816136862063,11.60276316566226,12.630847678165956,12.228777767594227,11.457776430101257,13.587702230777897,13.106573816337317,10.801619324579137,8.936309591111577,12.603805380871393,11.564567173021794],\"yaxis\":\"y\",\"type\":\"scatter\"}],                        {\"template\":{\"data\":{\"histogram2dcontour\":[{\"type\":\"histogram2dcontour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"choropleth\":[{\"type\":\"choropleth\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"histogram2d\":[{\"type\":\"histogram2d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmap\":[{\"type\":\"heatmap\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmapgl\":[{\"type\":\"heatmapgl\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"contourcarpet\":[{\"type\":\"contourcarpet\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"contour\":[{\"type\":\"contour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"surface\":[{\"type\":\"surface\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"mesh3d\":[{\"type\":\"mesh3d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"parcoords\":[{\"type\":\"parcoords\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolargl\":[{\"type\":\"scatterpolargl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"scattergeo\":[{\"type\":\"scattergeo\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolar\":[{\"type\":\"scatterpolar\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"scattergl\":[{\"type\":\"scattergl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatter3d\":[{\"type\":\"scatter3d\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattermapbox\":[{\"type\":\"scattermapbox\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterternary\":[{\"type\":\"scatterternary\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattercarpet\":[{\"type\":\"scattercarpet\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}]},\"layout\":{\"autotypenumbers\":\"strict\",\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"hovermode\":\"closest\",\"hoverlabel\":{\"align\":\"left\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"bgcolor\":\"#E5ECF6\",\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"ternary\":{\"bgcolor\":\"#E5ECF6\",\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]]},\"xaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"yaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"geo\":{\"bgcolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"subunitcolor\":\"white\",\"showland\":true,\"showlakes\":true,\"lakecolor\":\"white\"},\"title\":{\"x\":0.05},\"mapbox\":{\"style\":\"light\"}}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"date\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"value\"}},\"legend\":{\"title\":{\"text\":\"variable\"},\"tracegroupgap\":0},\"margin\":{\"t\":60}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('fb32890c-dc1f-43a8-acb3-39023e878873');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig = px.line(final_df, x='date', y=[column for column in final_df.columns if \"change\" in column])\n",
    "fig.show()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "sfds_kernel",
   "language": "python",
   "name": "sfds_kernel"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
