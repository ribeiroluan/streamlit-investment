#Importing dependencies
import streamlit as st
import pandas as pd
from pandas_datareader import data as pdr
from datetime import date
import plotly.express as px

header = st.container()
parameters = st.container()
dataset = st.container()
results = st.container()

with header:
    st.title("_Lit_invest_ :chart_with_upwards_trend:")
    st.write("Esta é uma ferramenta onde você pode acompanhar o seu portfólio de investimentos e compará-lo com indíces de mercado de maneira prática e intuitiva.")

with parameters:
    st.write("## Parâmetros")
    st.write('Antes de te mostrar quanto dinheiro você ganhou (ou perdeu, rs), precisamos de algumas informações básicas: o **período no qual o investimento vai ser analisado** e a **composição da sua carteira de ações**.')
    daterange = st.date_input("Selecione o período analisado", [date(2022, 1, 1), date.today()])

    start_date = daterange[0]
    end_date = daterange[1]

    wallet = st.multiselect(
     'Selecione as ações que compõem sua carteira. Por enquanto, estão disponíveis as empresas que compõem o IBOVESPA',
     ('RRRP3', 'ALPA4', 'ABEV3', 'AMER3', 'ASAI3', 'AZUL4', 'B3SA3', 'BPAN4', 'BBSE3', 'BRML3',
      'BBDC3', 'BBDC4', 'BRAP4', 'BBAS3', 'BRKM5', 'BRFS3', 'BPAC11', 'CRFB3', 'CCRO3', 'CMIG4',
      'CIEL3', 'COGN3', 'CPLE6', 'CSAN3', 'CPFE3', 'CMIN3', 'CVCB3', 'CYRE3', 'DXCO3', 'ECOR3',
      'ELET3', 'ELET6', 'EMBR3', 'ENBR3', 'ENGI11', 'ENEV3', 'EGIE3', 'EQTL3', 'EZTC3', 'FLRY3',
      'GGBR4', 'GOAU4', 'GOLL4', 'NTCO3', 'SOMA3', 'HAPV3', 'HYPE3', 'IGTI11', 'IRBR3','ITSA4',
      'ITUB4', 'JBSS3', 'JHSF3', 'KLBN11', 'RENT3', 'LWSA3', 'LREN3', 'MGLU3', 'MRFG3', 'CASH3',
      'BEEF3', 'MRVE3', 'MULT3', 'PCAR3', 'PETR3', 'PETR4', 'PRIO3', 'PETZ3', 'POSI3', 'QUAL3',
      'RADL3', 'RDOR3', 'RAIL3', 'SBSP3', 'SANB11', 'CSNA3', 'SLCE3', 'SULA11', 'SUZB3', 'TAEE11',
      'VIVT3', 'TIMS3', 'TOTS3', 'UGPA3', 'USIM5', 'VALE3', 'VIIA3','VBBR3', 'WEGE3', 'YDUQ3'))

with dataset:
    st.write("## Dados das empresas da sua carteira")

    if len(wallet) > 0:
        st.write("A partir das informações fornecidas, conseguimos gerar uma tabela com os preços diários de fechamento da sua carteira de ações.")
        
        st.write("A tabela é sempre composta pelos seguintes dados:")
        st.write("- `date` dia em que aquelas condições de mercado foram observadas; \n - `ibov_close` cotação de fechamento do índice Bovespa; \n - `ibov_cum_change` diferença percentual entre a cotação de fechamento do dia e a cotação de fechamento do primeiro dia do intervalo selecionado; \n - `TICKER_close` preço de fechamento da ação. Essa coluna vai se repetir para todas as ações da sua carteira; \n - `TICKER_cum_change` diferença percentual do preço de fechamento da ação no dia e o preço de fechamento do primeiro dia do intervalo selecionado. Essa coluna vai se repetir para todas as ações da sua carteira; \n - `total_cum_change` média de diferença percentual da sua carteira. Considera que todas as ações tem pesos iguais na sua carteira, o que pode não ser verdadeiro.")



        #First, let's pull data for our reference index (IBOVESPA)

        #Reading data using pandas datareader and cleaning column names
        ibov = pdr.DataReader(f'^BVSP', data_source='yahoo', start=start_date, end=end_date)
        ibov.reset_index(drop=False, inplace=True)
        ibov = ibov[['Date', 'Close']] #we are only interested in the closing prices
        ibov.rename(columns={'Date':'date', 'Close':'ibov_close'}, inplace=True)

        #Creating the cumulative change column. This way, we can easily compare performance across multiple companies
        reference = ibov.at[0,"ibov_close"]
        ibov['ibov_cum_change'] = ibov['ibov_close'].apply(lambda x: (x-reference)*100/reference)

        #----------------------------

        #Now, let's pull data for our investment portfolio

        df_holder = []

        for stock in wallet:
            #Reading data and cleaning column names
            temp_df = pdr.DataReader(f'{stock}.SA', data_source='yahoo', start=start_date, end=end_date)
            temp_df.reset_index(drop=False, inplace=True)
            temp_df = temp_df[['Date', 'Close']]
            temp_df.rename(columns={'Date':'date', 'Close':f'{stock}_close'}, inplace=True)
            
            #Creating the cumulative change column
            reference = temp_df.at[0,f'{stock}_close']
            temp_df[f'{stock}_cum_change'] = temp_df[f'{stock}_close'].apply(lambda x: (x-reference)*100/reference)
            
            #Appending our temporary dataframe to our empty list, which will be later concatenated
            df_holder.append(temp_df)
            
        #Lastly, lets concat our temp dataframes dropping duplicates - date column
        wallet_df = pd.concat(df_holder, axis=1).T.drop_duplicates().T

        #Finally, let's merge the index dataframe with our wallet dataframe
        final_df = pd.merge(ibov, wallet_df, on='date')
        final_df.iloc[:,1:].apply(pd.to_numeric)
        for column in final_df.columns:
            if column not in ['date']:
                final_df[column] = final_df[column].astype(float)

        #----------------------------

        #Computing total change
        total_change_columns = [column for column in final_df.columns if "change" in column and column not in ['ibov_cum_change', 'total_cum_change']]
        final_df['total_cum_change'] = final_df[total_change_columns].mean(axis=1)

        #----------------------------   
        #Displaying and downloading data

        st.write(final_df)

        @st.cache #THIS NEEDS TO BE FIXED
        def convert_df(df):
            return df.to_csv().encode('utf-8')

        csv = convert_df(final_df)

        st.download_button(
             label="Faça o download dos seus dados no formato csv",
             data=csv,
             file_name='meus_dados_financeiros.csv',
             mime='text/csv',
         )

    else:
        st.write(":warning: Selecione as ações da sua carteira antes de iniciarmos!")

with results:
    st.write("## Seus resultados")

    if len(wallet) > 0:
        st.write("**Principais indicadores**")
        st.write("Abaixo é possível ver a melhor e pior ação da sua carteira, o seu rendimento médio e como sua carteira se compara com o Ibovespa no período.")

        changes = [final_df[column] for column in final_df.columns if "change" in column and column not in ['ibov_cum_change','total_cum_change']]
        changes = pd.concat(changes, axis=1)
        changes_results = changes.iloc[-1].sort_values(ascending=False)

        col1, col2, col3, col4 = st.columns(4)
        col1.metric(f'Melhor ({changes_results.index[0].split("_")[0]})', f'{round(changes_results[0],2)}%')
        col2.metric(f'Pior ({changes_results.index[-1].split("_")[0]})', f'{round(changes_results[-1],2)}%')
        col3.metric(f'Médio', f'{round(final_df["total_cum_change"].iloc[-1],2)}%')
        col4.metric(f'Carteira vs Ibovespa', f'{round(final_df["total_cum_change"].iloc[-1]-final_df["ibov_cum_change"].iloc[-1],2)}%')
    
        st.write("**Evolução das cotações das empresas da sua carteira no período analisado**")
        st.write("O gráfico é interativo: fique à vontade para brincar com ele!")
        fig = px.line(final_df, x='date', y=[column for column in final_df.columns if "close" in column and "ibov" not in column])
        st.plotly_chart(fig, use_container_width=False)

        st.write("**Desempenho da sua carteira em comparaçao com o Ibovespa**")
        st.write("O gráfico é interativo: fique à vontade para brincar com ele!")
        fig2 = px.line(final_df, x='date', y=[column for column in final_df.columns if "change" in column])
        st.plotly_chart(fig2, use_container_width=False)


    else:
        st.write(":warning: Selecione as ações da sua carteira antes de iniciarmos!")