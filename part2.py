#==========================================#
#atençao: essa parte tem palavras,palavroes#
pt-br_palavras = """
FDP,Filha da p__a
KRL,caralh_
Olá,um tipo de oi
bem
os,o,as,a,s
você,vc,vocês,vcs
corpo
cabeça
mãos,direita,esquerda
barriga
cintura
pernas,direita,esquerda
1234567890
@#$_&-+()/*"':;!?
~`|•√π÷×§∆£¢€¥^°={}\%©®™✓[]
abreviado,abreviados,abreviadas
arquivo,arquivos,arquivas,arquiva,png,jpeg,mp3,mp4,img,vid
q,w,ëėēèéêę,r,t,y,ūùúüû,īïįìíî,ºōøœöòôõó,p,äåæªáãàâ,s,d,f,g,h,j,k,l,z,x,ćçčc,v,b,n,m
"""
#=========================#
#Api data                 #
#=========================#
clockai_api_version = 1.0.0
texto_saudacao = "Olá!"
api_extern_cpu_ip = "serverhub.com/clockai/api_extern_cpu_ip/files/api_extern_cpu_ip.bin"
ia_name = "nomedasuaiaaqui"
ia_vox = "seuaudiodevoz.mp3"
ia_logo = "nomedoarquivodelogo.png"
ia_chat_aperance = "dark"
#=========================#
#Ui chat                  #
#=========================#
import time

if:
    time.sleep(9)
    print("Conectado carregando...")
time.sleep(9)
system("clear")
else:
    time.sleep(9)
    print("Erro a se conectar a 'ClockIA'") 
    time.sleep(9)
    
    system("clear")   
 #=========================##=========================#
 #=========================##=========================#
 test_number = 1 + 9
 test_number_eval = eval(test_number)
 number2_api_test = 1 + 1 -1 -1 1 + 1
 number2_api_test_eval = eval(number2_api_test)
dados_para_api = {
    "comando": "CALCULAR",
    "formula_descritiva": "Subtraia o valor do desconto do preço total.",
    "detalhes": "O desconto é de 10%"
}

# A sua API receberia essa estrutura e buscaria o valor da chave 'formula_descritiva'.
instrucao_para_processamento = dados_para_api["formula_descritiva"]

print(f"Instrução enviada: {instrucao_para_processamento}")
(x * 2 for x in lista)
print(*lista)
#============================#
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
# URL da API Externa que você quer consumir
API_EXTERNA_URL = "https://jsonplaceholder.typicode.com/clockai/main"


@app.route('/', methods=['GET'])
def homepage():
    return "Servidor Python rodando! Acesse /dados_externos para ver o resultado da API."

if __name__ == '__main__':
    # Roda o servidor na porta 5000
    app.run(debug=True)
    # Continuação do arquivo app.py

@app.route('/dados_externos', methods=['GET'])
def buscar_dados_da_api():
    try:
        # 1. Faz a requisição GET para a API externa
        response = requests.get(API_EXTERNA_URL)
        
        # 2. Verifica se a requisição foi bem-sucedida (código 200)
        response.raise_for_status() 
        
        # 3. Converte a resposta JSON em um dicionário Python
        dados = response.json()
        
        # 4. Retorna os dados como JSON para quem acessou seu servidor
        return jsonify({
            "status": "sucesso",
            "dados": dados,
            "mensagem": "Dados obtidos da API externa com sucesso!"
        })

    except requests.exceptions.RequestException as e:
        # Lida com erros de conexão ou HTTP
        return jsonify({
            "status": "erro",
            "mensagem": f"Erro ao conectar com a API externa: {e}"
        }), 500 # Retorna um código de status HTTP 500 (Erro Interno do Servidor)
  #===========#
  info = {
      "ClockAI_version": "1.0.0"
  }     
