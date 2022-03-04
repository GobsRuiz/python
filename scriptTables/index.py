# Imports
import pandas as pd
import os.path





# <1>
# Function to be performed
def functionToBePerfomed():
  userValue = 0
  modules = {
    1: mod019_v3,
  }



  # Text that will be displayed on the screen
  print("===============================")
  print("Escolha o módulo")
  print("===============================")
  print("1 - Estrutura: mod019_v3")
  print("2 - Estrutura: cantacom_n_mod072_aereas_100_V2;")
  print("3 - Estrutura: canta_destinos_vitrine_novo_modelo_estrutura;")
  print("4 - Estrutura: canta_mod050_estrutura; Obs: Valores apenas para Clube Smiles")
  print("5 - CANTACOM_100MILHAS-SMILESANDMONEY-VERTICAL_V1")
  print("===============================")
  


  # Ask the user to enter a value, verify that it is a number and that this typed option exists
  while (isinstance(userValue, str) or not userValue in modules):
    try:
      userValue = int(input("Digite um número: "))
      print("===============================")

      if(not userValue in modules):
        print("===============================")
        print("Essa opção não existe! Escolha uma das opções acima!")
        print("===============================")
    except:
      print("===============================")
      print("Ops, digite um número!")
      print("===============================")

  

  def runFuncion():
    modules[userValue]()
  runFuncion()
# </1>





# <Other functions>
# Check excel file
def checkExcelFile():
  # Check if the file exists or if the filename is wrong
  if(not os.path.exists('./planilha.xlsx')):
    print("Arquivo do excel não encontrado. O nome do arquivo tem que ser: 'planilha' e estar na raiz da pasta.")
    print("========================================================") 
    exit()
  
  # Check if the table/worksheet name is correct
  try: 
      # 
      table = pd.read_excel('./planilha.xlsx', sheet_name='LP')
  except:
      print("O nome da tabela está errado. O nome da tabela tem que ser: 'LP'")
      print("========================================================")
      exit()

  return table



# Table adjustments - Removing rows without values
def tableAdjustments(table, column, numericColumns):
    # Removing rows that do not contain values
    if column != "":  
        for i in range(table.shape[0]):
            if pd.isna(table[column][i]):
                table = table.drop(labels=i, axis=0) 

    # Criar nova tabela
    newTable = pd.DataFrame(table)

    # Resetar o index da nova tabela
    newTable.reset_index(inplace=True, drop=True)

    # Change the type of number tables
    for i in range(len(numericColumns)):
      if numericColumns[i] in newTable.columns:
        newTable = newTable.astype({numericColumns[i]: 'int64'})
    
    return newTable



# Function that inserts code into a txt file
def insertResultInFile(cod): 
    # Codigo.txt is the file where all the js code will be inserted
    file = open('codigo.txt', 'w', encoding='utf-8')
    file.writelines(cod)
    file.close()



# Message
def message():
    print("Pronto! O código está no arquivo codigo.txt")
    print("========================================================") 

# </Other functions>





# Funcões de cada módulo
def mod019_v3():
  # Check excel file
  table = checkExcelFile()

  # Table adjustment
  try:
      newTable = tableAdjustments(table, 1, ['DE', 1, '1.1']);
  except:
      print("Ops, ERRO!!!")
      print("========================================================")
      return


functionToBePerfomed()