# Gerenciador Barbearia

O domínio escolhido para o projeto da disciplina de Banco de Dados II foi uma Barbearia, que consiste na ideia de Gerenciar o agendamento entre Cliente e Funcionário e o serviço que será prestado. 

## Instruções para a compilação e execução da aplicação

### Requisitos da Aplicação
 - PostgreSQL
 - Python
 - Visual Studio Code ou qualquer outro editor de texto
 
### Faça uma Copia do Repositório para sua máquina
 - Clique em Code
 - Copie o link HTTPS para fazer o git clone
 - Ou Clique em Download ZIP
 - Clique com o direito no arquivo ZIP na pasta que o arquivo se encontra e em extrair o conteúdo do arquivo
 
<img width="647" alt="downloadcodigo" src="https://user-images.githubusercontent.com/40742096/234862519-9636623a-8f7e-43ad-a2ea-b51270b67b9f.png">
 
### Criando o Banco de Dados
 - Abrir o pgAdmin
  
![pgAdmin4](https://user-images.githubusercontent.com/40742096/234708693-a42f522f-7b08-465e-8a85-72db77a24c84.png)

 - Clique com o direito em Databases, selecione Create > Database

![image](https://user-images.githubusercontent.com/40742096/234709548-f7b55ae7-0d09-421c-96d4-cbd02a5e56f0.png)

 - Nomeie o banco como db_barbearia e clique em Save.

![image](https://user-images.githubusercontent.com/40742096/234709747-0dab4b09-2c35-4146-ac7a-416de6dfbc60.png)

 - Clique em Databases
 - Clique com o direito em db_barbearia e selecione Query Tool
 
 ![Captura de tela 2023-04-26 184940](https://user-images.githubusercontent.com/40742096/234866485-4594de66-46e9-4867-a6f2-d7cf22258c04.png)
 
 - Copie o Contéudo do arquivo db_barbearia.sql ou araste o arquivo dentro da Query Tool
 
 <img width="101" alt="Captura de tela 2023-04-27 095141" src="https://user-images.githubusercontent.com/40742096/234867528-dfd0b4c6-23ac-4585-9079-84a1ccdca151.png">
 
 - Clique em Executar
 
<img width="614" alt="Captura de tela 2023-04-26 185058" src="https://user-images.githubusercontent.com/40742096/234868331-ae2e6ceb-7201-48fe-8b7a-87a101b58c37.png">

### Executando e Compilando

 - Abrir o editor Visual Studio Code
 - Clique em File > Open Folder
 - Selecione a pasta que o repositório foi baixado

 ![image](https://user-images.githubusercontent.com/40742096/234871150-09680baa-2230-43e6-a564-9051bbf617e1.png)
 
 - Abrir o arquivo main.py
 - Altere os campos user, password e port de acesso ao banco
 
![image](https://user-images.githubusercontent.com/40742096/234873670-ddbc0e68-a9a5-44e0-923c-0b832934b5f8.png)

- Abrir o terminal do VS Code
- Digite o comando `pip install -r requirements.txt` no terminal para instalar as dependências do Python necessarias para a execução da aplicação 

<img width="329" alt="Captura de tela 2023-04-27 101915" src="https://user-images.githubusercontent.com/40742096/234874199-859f3652-04a1-4d55-a60d-a79a280607ea.png">

- Digite o comando `python main.py` no terminal para executar a aplicação

![image](https://user-images.githubusercontent.com/40742096/234876020-611febe0-8430-4e22-99a9-6116a634acf9.png)



