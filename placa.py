import requests, os, time
def gt():
   print('\n\033[34;01mdeseja fazer uma nova consulta?\n1. sim\n2. sair\n\033[0;0m\n')
   df=input('>')
   if df == '1':
    placa()
   elif df == '2':
    print('\n\033[32;1mobrigado por usar os serviços do scorpion king\033[0;0m\n')
    exit()
   elif df != 1 and 2:
    print('\n\033[33;1mseleção invalida digite 1 ou 2\n')
    gt()
def placa():
 os.system('clear')
 print('\033[32;1m')
 print('\033[32;1m     ██╗███╗  ██╗███████╗ █████╗ ')
 time.sleep(0.1)      
 print('\033[32;1m     ██║████╗ ██║██╔════╝██╔══██╗')
 time.sleep(0.1)      
 print('\033[32;1m     ██║██╔██╗██║█████╗  ██║  ██║')
 time.sleep(0.1)      
 print('\033[32;1m     ██║██║╚████║██╔══╝  ██║  ██║')
 time.sleep(0.1)      
 print('\033[32;1m     ██║██║ ╚███║██║     ╚█████╔╝')
 time.sleep(0.1)      
 print('\033[32;1m     ╚═╝╚═╝  ╚══╝╚═╝      ╚════╝')
 time.sleep(0.1)      
 print('\033[32;1m')
 time.sleep(0.1)      
 print('\033[32;1m')
 time.sleep(0.1)      
 print('\033[32;1m██████╗ ██╗      █████╗  █████╗  █████╗') 
 time.sleep(0.1)      
 print('\033[32;1m██╔══██╗██║     ██╔══██╗██╔══██╗██╔══██╗')
 time.sleep(0.1)      
 print('\033[32;1m██████╔╝██║     ███████║██║  ╚═╝███████║')
 time.sleep(0.1)      
 print('\033[32;1m██╔═══╝ ██║     ██╔══██║██║  ██╗██╔══██║')
 time.sleep(0.1)      
 print('\033[32;1m██║     ███████╗██║  ██║╚█████╔╝██║  ██║')
 time.sleep(0.1)      
 print('\033[32;1m╚═╝     ╚══════╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝')
 print('')
 print('''\033[34;1m
 ____________________________________________
 |
 |---------- 1. consultar uma placa
 |---------- 2. ajuda
 |---------- 3. sair 
 |___________________________________________
 ''')
 s=input('\nDigite o que deseja fazer\n          >')
 if s == '1':
  print('\n\n\033[34;1mdigite a placa a ser consultada\033[0;0m\n')
  plac=input('\033[31;1m>')
  dados=requests.get(f'https://apicarros.com/v1/consulta/{plac}/json', verify=False).json()
  br=("\033[34;1m◆-▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱-◆\n◆-\n\033[34;1m◆-Modelo: \033[0;0m\033[37;1m{}\033[0;0m\n\033[34;1m◆-Ano: \033[0;0m\033[37;1m{}\033[0;0m\n\033[34;1m◆-Ano_Modelo: \033[0;0m\033[37;1m{}\033[0;0m\n\033[34;1m◆-Marca: \033[0;0m\33[37;1m{}\033[0;0m\n\033[34;1m◆-Cor: \033[0;0m\033[37;1m{}\033[0;0m\n\033[34;1m◆-Placa: \033[0;0m\033[37;1m{}\033[0;0m\n\033[34;1m◆-Cidade: \033[0;0m\033[37;1m{}\033[0;0m\n\033[34;1m◆-Estado: \033[0;0m\033[37;1m{}\033[0;0m\n\033[34;1m◆-Chassi: \033[0;0m\033[37;1m{}\033[0;0m\n\033[34;1m◆-Codigo_de_situacao: \033[0;0m\033[37;1m{}\033[0;0m\n\033[34;1m◆-Codigo_Retorno: \033[0;0m\033[37;1m{}\033[0;0m\n\033[34;1m◆-Data: \033[0;0m\033[37;1m{}\033[0;0m\n\033[34;1m◆-Data_Atualizacao_Alareme: \033[0;0m\033[37;1{}\033[0;0m\n\033[34;1m◆-Data_Atualizacao_Caracteristicas: \033[0;0m\033[37;1m{}\033[0;0m\n\033[34;1m◆-Data_Atualizacao_RouboFurto: \033[0;0m\033[37;1m{}\033[0;0m\n\033[34;1m◆-MenssagemDeRetorno: \033[0;0m\033[37;1m{}\033[0;0m\n\033[34;1m◆-Situacao: \033[0;0m\033[37;1m{}\033[0;0m\n\033[34;1m◆-\n\033[34;1m◆-▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱-◆\n".format(dados['modelo'],dados['ano'],dados['anoModelo'],dados['marca'],dados['cor'],dados['placa'],dados['municipio'],dados['uf'],dados['chassi'],dados['codigoSituacao'],dados['codigoRetorno'],dados['data'],dados['dataAtualizacaoAlarme'],dados['dataAtualizacaoCaracteristicasVeiculo'],dados['dataAtualizacaoRouboFurto'],dados['mensagemRetorno'],dados['situacao']))
  if 'error' not in 'modelo':
   print('\n\033[32;1m==>PLACA ENCONTRADA<==\033[0;0m\n')
   print(br) 
   gt()
  if 'plac' != 'placa':
   print('\033[33;1mplaca nao encontrada\033[0;0m\n')
   gt()
 if s == '2':
   print('\n\033[32;1mEssa é uma ferramenta bem simples na qual foi desenvolvida com o intuito de retornar determinadas informações a partir de uma placa veicular....a placa deve ser digitada com letras minusculas sem traços')
   gt()
 if s == '3':
   print('\033[32;1m\nObrigado por ultilizar os serviços do scorpion king\n')
   exit()
 if s != '1' and '2' and '3':
  print('\033[33;1mSeleção invalida\033[0;0m')
  time.sleep(3)
  placa()
os.system('clear')
print("\033[34;1m                    coded by:")
time.sleep(0.1)      
print("")
time.sleep(0.1)      
print("       ⟡ ━━━━━━━━ ⟡ ━━━━━━━━ ⟡ ━━━━━━━━ ⟡ ")
time.sleep(0.1)      
print("       ┃                                ┃")
time.sleep(0.1)       
print("       ┃      ✪   SCORPION KING   ✪    ┃")
time.sleep(0.1)      
print("       ┃                                ┃")
time.sleep(0.1)      
print("       ⟡ ━━━━━━━━ ⟡ ━━━━━━━━ ⟡ ━━━━━━━━ ⟡")  
print('')
time.sleep(5) 
os.system('clear')
placa()
