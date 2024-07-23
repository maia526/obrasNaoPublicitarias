import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

#Verificando se todos os arquivos contém as mesmas colunas
obrasNaoPublicitarias2002 = pd.read_csv(
                            "obras-nao-pub-brasileiras-2002.csv",
                            delimiter=";"                           
    )

listaNomesArquivos = ["obras-nao-pub-brasileiras-2003.csv",
                      "obras-nao-pub-brasileiras-2004.csv",
                      "obras-nao-pub-brasileiras-2005.csv",
                      "obras-nao-pub-brasileiras-2006.csv",
                      "obras-nao-pub-brasileiras-2007.csv",
                      "obras-nao-pub-brasileiras-2008.csv",
                      "obras-nao-pub-brasileiras-2009.csv",
                      "obras-nao-pub-brasileiras-2010.csv",
                      "obras-nao-pub-brasileiras-2011.csv",
                      "obras-nao-pub-brasileiras-2012.csv",
                      "obras-nao-pub-brasileiras-2013.csv",
                      "obras-nao-pub-brasileiras-2014.csv",
                      "obras-nao-pub-brasileiras-2015.csv",
                      "obras-nao-pub-brasileiras-2016.csv",
                      "obras-nao-pub-brasileiras-2017.csv",
                      "obras-nao-pub-brasileiras-2018.csv",
                      "obras-nao-pub-brasileiras-2019.csv",
                      "obras-nao-pub-brasileiras-2020.csv",
                      "obras-nao-pub-brasileiras-2021.csv",
                      "obras-nao-pub-brasileiras-2022.csv",
                      "obras-nao-pub-brasileiras-2023.csv",
                      "obras-nao-pub-brasileiras-2024.csv"]

tabelas = []
mesmasColunas = True;
for nome in listaNomesArquivos:
    obrasNaoPublicitarias = pd.read_csv(
                            nome,
                            delimiter=";"                           
    )
    mesmasColunas = obrasNaoPublicitarias2002.columns.equals(obrasNaoPublicitarias.columns)
    
    dataTabela = obrasNaoPublicitarias.loc[0, "DATA_EMISSAO_CPB"]
    ano = dataTabela.split("/")[-1]

    obrasNaoPublicitarias["ANO"] = ano
    tabelas.append(obrasNaoPublicitarias)


#produções seriadas (séries) ficaram mais frequentes recentemente?
freqPorAno = []
for tabela in tabelas:
    frequenciaAno = []
    
    contagem = tabela['ORGANIZACAO_TEMPORAL'].value_counts()
    totalSeriada = contagem.get("SERIADA", 0) + contagem.get("SERIADA EM MÚLTIPLAS TEMPORADAS", 0) + contagem.get("SERIADA EM TEMPORADA ÚNICA", 0) + contagem.get("SERIADA DE DURAÇÃO INDETERMINADA", 0)

    frequenciaAno.append(str(tabela.loc[0, "ANO"]))
    frequenciaAno.append(totalSeriada)
    
    freqPorAno.append(frequenciaAno)

    #print(contagem)
    #print("total: " + str(totalSeriada))
    #print("seriada: " + str(contagem.get("SERIADA", 0)))
    #print("multiplas: " + str(contagem.get("SERIADA EM MÚLTIPLAS TEMPORADAS", 0)))
    #print("unica: " + str(contagem.get("SERIADA EM TEMPORADA ÚNICA", 0)))
    #print("indeterminada: " + str(contagem.get("SERIADA DE DURAÇÃO INDETERMINADA", 0)))
    #print("\n------------------------------------------------------------------")

dataFrameFrequenciasPorAno = pd.DataFrame(freqPorAno, columns=['ANO', "FREQUENCIA"])
dataFrameFrequenciasPorAno.plot.bar(x='ANO', y='FREQUENCIA', rot=0, color='blue', legend=None)

# Adiciona títulos e rótulos aos eixos
plt.xlabel('Ano')
plt.ylabel('Qtd de produções seriadas')
plt.title('Produções seriadas por Ano')

# Exibe o gráfico
plt.show()

