#=============#Copyrhigt (C)
#ClockAI API  #members:Enzo,fernanda,chagas LLC,Francenir
#=============#
input()       #Alimentar A API para responder
dados_para_treinamento = """
A inteligência artificial tem o potencial de transformar
o futuro de maneira inédita. No entanto, sua
implementação requer considerações éticas sérias
sobre privacidade, viés algorítmico e impacto no emprego.

Este é um bloco de texto muito longo que contém todas
as palavras e letras que você deseja armazenar.
Qualquer ENTER que você apertar aqui será
mantido como uma quebra de linha na variável.

Você pode colocar parágrafos, artigos inteiros,
ou qualquer dado textual extenso aqui dentro.
"""
tipos_de_oi = """
olá,oi,olá como vai?
"""
# 1. Definir o Gerador (G) e o Discriminador (D)
# G = Rede neural (ex: convolucional) que mapeia ruído aleatório para imagem
# D = Rede neural (ex: convolucional) que classifica imagem como real ou falsa

# 2. Loop de Treinamento
for epoch in range(num_epochs):
    for real_images in dataloader: # Carregar um lote de imagens reais

        # A. Treinar o Discriminador
        # Gerar imagens falsas
        noise = gerar_ruido_aleatorio()
        fake_images = G(noise)

        # Classificar imagens reais e falsas
        pred_real = D(real_images)
        pred_fake = D(fake_images.detach()) # Detach para não calcular gradientes no Gerador

        # Calcular perda do Discriminador (quer que pred_real seja 1 e pred_fake seja 0)
        loss_D = calcular_perda_discriminador(pred_real, pred_fake)

        # Otimizar o Discriminador
        otimizador_D.zero_grad()
        loss_D.backward()
        otimizador_D.step()

        # B. Treinar o Gerador
        # Gerar novas imagens falsas
        noise = gerar_ruido_aleatorio()
        fake_images = G(noise)

        # Classificar as novas imagens falsas com o Discriminador
        pred_fake_para_G = D(fake_images)

        # Calcular perda do Gerador (quer que D classifique fake_images como 1/real)
        loss_G = calcular_perda_gerador(pred_fake_para_G)

        # Otimizar o Gerador
        otimizador_G.zero_grad()
        loss_G.backward()
        otimizador_G.step()

    # C. Opcional: Salvar imagens geradas periodicamente para monitorar o progresso
    if epoch % save_interval == 0:
        gerar_e_salvar_imagens_exemplo(G)
 
 pt-br = """
 África
América
Antártida
Ásia
Europa
Oceania
Rondônia
Acre
Amazonas
Roraima
Pará
Amapá
Tocantins
Maranhão
Piauí
Ceará
Rio Grande do Norte
Paraíba
Pernambuco
Alagoas
Sergipe
Bahia
Minas Gerais
Espírito Santo
Rio de Janeiro
São Paulo
Paraná
Santa Catarina
Rio Grande do Sul
Mato Grosso do Sul
Mato Grosso
Goiás
Distrito Federal
Alta Floresta D'Oeste
Ariquemes
Cabixi
Cacoal
Cerejeiras
Teixeirópolis
Colorado do Oeste
Corumbiara
Costa Marques
Espigão D'Oeste
Guajará-Mirim
Jaru
Ji-Paraná
Machadinho D'Oeste
Nova Brasilândia D'Oeste
Theobroma
Rio dos Bois
Rio Sono
Sampaio
Sandolândia
Santa Fé do Araguaia
Santa Maria do Tocantins
Santa Rita do Tocantins
Santa Rosa do Tocantins
Santa Tereza do Tocantins
Santa Terezinha do Tocantins
São Bento do Tocantins
São Félix do Tocantins
São Miguel do Tocantins
São Salvador do Tocantins
São Sebastião do Tocantins
São Valério
Silvanópolis
Sítio Novo do Tocantins
Sucupira
Taguatinga
Ouro Preto do Oeste
Pimenta Bueno
Porto Velho
Presidente Médici
Rio Crespo
Rolim de Moura
Taipas do Tocantins
Talismã
Santa Luzia D'Oeste
Vilhena
São Miguel do Guaporé
Nova Mamoré
Alvorada D'Oeste
Alto Alegre dos Parecis
Alto Paraíso
Buritis
Vale do Paraíso
Novo Horizonte do Oeste
Acrelândia
Assis Brasil
Brasiléia
Bujari
Capixaba
Cruzeiro do Sul
Epitaciolândia
Feijó
Jordão
Mâncio Lima
Manoel Urbano
Marechal Thaumaturgo
Plácido de Castro
Porto Walter
Rio Branco
Rodrigues Alves
Santa Rosa do Purus
Senador Guiomard
Sena Madureira
Tarauacá
Xapuri
Porto Acre
Cacaulândia
Campo Novo de Rondônia
Candeias do Jamari
Alvarães
Amaturá
Anamã
Anori
Apuí
Atalaia do Norte
Autazes
Barcelos
Barreirinha
Benjamin Constant
Beruri
Boa Vista do Ramos
Boca do Acre
Borba
Caapiranga
Canutama
Carauari
Careiro
Careiro da Várzea
Coari
Codajás
Eirunepé
Envira
Fonte Boa
Guajará
Humaitá
Ipixuna
Iranduba
Itacoatiara
Itamarati
Itapiranga
Japurá
Juruá
Jutaí
Lábrea
Manacapuru
Manaquiri
Castanheiras
Chupinguaia
Cujubim
Governador Jorge Teixeira
Itapuã do Oeste
Ministro Andreazza
Mirante da Serra
Monte Negro
Nova União
Parecis
Pimenteiras do Oeste
Manaus
Manicoré
Maraã
Maués
Nhamundá
Nova Olinda do Norte
Primavera de Rondônia
São Felipe D'Oeste
São Francisco do Guaporé
Seringueiras
Novo Airão
Novo Aripuanã
Parintins
Pauini
Urupá
Vale do Anari
Presidente Figueiredo
Rio Preto da Eva
Santa Isabel do Rio Negro
Santo Antônio do Içá
São Gabriel da Cachoeira
São Paulo de Olivença
São Sebastião do Uatumã
Silves
Tabatinga
Tapauá
Tefé
Tonantins
Uarini
Urucará
Urucurituba
Amajari
Alto Alegre
Boa Vista
Bonfim
Cantá
Caracaraí
Caroebe
Iracema
Mucajaí
Normandia
Pacaraima
Rorainópolis
São João da Baliza
Palmas
Tocantínia
Tocantinópolis
Tupirama
Tupiratins
Wanderlândia
Xambioá
Açailândia
Itagibá
São Luiz
Uiramutã
Abaetetuba
Abel Figueiredo
Acará
Afuá
Água Azul do Norte
Alenquer
Almeirim
Altamira
Anajás
Ananindeua
Anapu
Augusto Corrêa
Aurora do Pará
Aveiro
Bagre
Baião
Bannach
Barcarena
Belém
Belterra
Lagoa de Pedras
Benevides
Bom Jesus do Tocantins
Bonito
Bragança
Brasil Novo
Isaías Coelho
Itagimirim
Itaguaçu da Bahia
Brejo Grande do Araguaia
Joaquim Pires
Lagoa de Velhos
Itaju do Colônia
Itajuípe
Itamaraju
Itamari
Itambé
Itanagra
Itanhém
São Fidélis
São Gonçalo
São João da Barra
São João de Meriti
São José de Ubá
São José do Vale do Rio Preto
São Pedro da Aldeia
São Sebastião do Alto
Sapucaia
Saquarema
Breu Branco
Breves
Bujaru
Cachoeira do Piriá
Cachoeira do Arari
Cametá
Canaã dos Carajás
Capanema
Capitão Poço
Castanhal
Chaves
Livramento de Nossa Senhora
Luís Eduardo Magalhães
Macajuba
Macarani
Macaúbas
Macururé
Seropédica
Silva Jardim
Sumidouro
Colares
Conceição do Araguaia
Concórdia do Pará
Cumaru do Norte
Curionópolis
Igarapé-Açu
Igarapé-Miri
Inhangapi
Ipixuna do Pará
Irituia
Itaituba
Curralinho
Curuá
Curuçá
Dom Eliseu
Itupiranga
Jacareacanga
Tanguá
Eldorado do Carajás
Faro
Floresta do Araguaia
Garrafão do Norte
Goianésia do Pará
Gurupá
Teresópolis
Trajano de Moraes
Três Rios
Valença
Varre-Sai
Vassouras
Volta Redonda
Adamantina
Adolfo
Aguaí
Jacundá
Águas da Prata
Juruti
Nova Timboteua
Limoeiro do Ajuru
Mãe do Rio
Novo Progresso
Novo Repartimento
Óbidos
Oeiras do Pará
Oriximiná
Ourém
Ourilândia do Norte
Pacajá
Lajes
Pinhalzinho
Magalhães Barata
Marabá
Maracanã
Marapanim
Santa Luzia do Pará
Santa Maria das Barreiras
Santa Maria do Pará
Santana do Araguaia
Santarém
Santarém Novo
Marituba
Medicilândia
Melgaço
Mocajuba
Moju
Mojuí dos Campos
Monte Alegre
Muaná
Nova Esperança do Piriá
Piquerobi
Piquete
Piracaia
Piracicaba
Nova Ipixuna
Piraju
Pirajuí
Pirangi
Pirapora do Bom Jesus
Pirapozinho
Pirassununga
Piratininga
Pitangueiras
Planalto
Platina
Poá
Saudades
Palestina do Pará
Paragominas
Parauapebas
Pau D'Arco
Peixe-Boi
Rafard
Rancharia
Redenção da Serra
Regente Feijó
Reginópolis
Registro
Restinga
Ribeira
Ribeirão Bonito
Ribeirão Branco
Ribeirão Corrente
Piçarra
Placas
Ponta de Pedras
Portel
Porto de Moz
Prainha
São Julião
Primavera
Quatipuru
Redenção
Rio Maria
Rondon do Pará
Rurópolis
Salinópolis
Santo Antônio do Tauá
São Caetano de Odivelas
São Lourenço do Piauí
Ribeirão Pires
Salvaterra
Tucuruí
Ulianópolis
Uruará
Belágua
Ribeirão Preto
Riversul
Santa Bárbara do Pará
Vigia
Santa Cruz do Arari
Santa Izabel do Pará
São Domingos do Araguaia
São Domingos do Capim
São Félix do Xingu
São Francisco do Pará
São Geraldo do Araguaia
Viseu
Vitória do Xingu
Afonso Cunha
Água Doce do Maranhão
Alcântara
Cidelândia
Codó
São João da Ponta
São João de Pirabas
Alvorada
Ananás
Angico
Aparecida do Rio Negro
Aragominas
Araguacema
Araguaçu
Araguaína
Araguanã
Araguatins
Arapoema
Arraias
Augustinópolis
Aurora do Tocantins
Axixá do Tocantins
Babaçulândia
Bandeirantes do Tocantins
Barra do Ouro
Barrolândia
Bernardo Sayão
Bom Jesus do Tocantins
Brasilândia do Tocantins
Brejinho de Nazaré
Buriti do Tocantins
Cachoeirinha
Campos Lindos
Cariri do Tocantins
Carmolândia
Carrasco Bonito
Caseara
Centenário
Chapada de Areia
Chapada da Natividade
Colinas do Tocantins
Combinado
Conceição do Tocantins
São João do Araguaia
São Miguel do Guamá
Couto Magalhães
Cristalândia
Crixás do Tocantins
Darcinópolis
Dianópolis
Divinópolis do Tocantins
Dois Irmãos do Tocantins
Dueré
Esperantina
Fátima
Figueirópolis
Filadélfia
Formoso do Araguaia
Tabocão
Goianorte
Goiatins
Guaraí
Gurupi
Ipueiras
Itacajá
Itaguatins
Itapiratins
Itaporã do Tocantins
Jaú do Tocantins
Juarina
Lagoa da Confusão
Lagoa do Tocantins
Lajeado
Lavandeira
Lizarda
Luzinópolis
Marianópolis do Tocantins
Mateiros
Maurilândia do Tocantins
Miracema do Tocantins
Miranorte
Monte do Carmo
Monte Santo do Tocantins
São Sebastião da Boa Vista
Palmeiras do Tocantins
Muricilândia
Natividade
Sapucaia
Senador José Porfírio
Soure
Tailândia
Terra Alta
Nazaré
Nova Olinda
Nova Rosalândia
Novo Acordo
Novo Alegre
Novo Jardim
Oliveira de Fátima
Palmeirante
Palmeirópolis
Paraíso do Tocantins
Paranã
Pau D'Arco
Pedro Afonso
Peixe
Pequizeiro
Colméia
Pindorama do Tocantins
Piraquê
Pium
Ponte Alta do Bom Jesus
Ponte Alta do Tocantins
Porto Alegre do Tocantins
Porto Nacional
Praia Norte
Presidente Kennedy
Pugmil
Recursolândia
Riachinho
Rio da Conceição
Terra Santa
Tomé-Açu
Tracuateua
Trairão
Tucumã
Xinguara
Serra do Navio
Amapá
Pedra Branca do Amapari
Calçoene
Cutias
Ferreira Gomes
Itaubal
Laranjal do Jari
Macapá
Mazagão
Oiapoque
Porto Grande
Pracuúba
Santana
Tartarugalzinho
Vitória do Jari
Abreulândia
Aguiarnópolis
Aliança do Tocantins
Almas
Aldeias Altas
Altamira do Maranhão
Alto Alegre do Maranhão
Alto Alegre do Pindaré
Alto Parnaíba
Rifaina
Rincão
Amapá do Maranhão
Amarante do Maranhão
Anajatuba
Anapurus
Apicum-Açu
Araguanã
Araioses
Arame
Arari
Rinópolis
Rio Claro
Rio das Pedras
Rio Grande da Serra
Axixá
Bacabal
Riolândia
Schroeder
Seara
Serra Alta
Siderópolis
Sombrio
Bacabeira
Bacuri
Bacurituba
Balsas
Barão de Grajaú
Barra do Corda
Barreirinhas
Lajes Pintadas
São Carlos
Sul Brasil
Taió
Tangará
Tigrinhos
Tijucas
Bela Vista do Maranhão
Benedito Leite
Gonçalves Dias
Sebastianópolis do Sul
Serra Azul
Serrana
Serra Negra
Sertãozinho
Bequimão
Bernardo do Mearim
Sete Barras
Timbé do Sul
Timbó
Boa Vista do Gurupi
Bom Jardim
Bom Jesus das Selvas
Bom Lugar
Brejo
Brejo de Areia
Buriti
Buriti Bravo
Buriticupu
Buritirana
Cachoeira Grande
Cajapió
Cajari
Campestre do Maranhão
Cândido Mendes
Cantanhede
Tanabi
Tapiraí
Tapiratiba
Timbó Grande
Três Barras
Treviso
Treze de Maio
Treze Tílias
Trombudo Central
Tubarão
Tunápolis
Turvo
União do Oeste
Urubici
Urupema
Urussanga
Vargeão
Vargem
Capinzal do Norte
Carolina
Carutapera
Caxias
Cedral
Central do Maranhão
Centro do Guilherme
Centro Novo do Maranhão
Chapadinha
Coelho Neto
Colinas
Conceição do Lago-Açu
Coroatá
Cururupu
Davinópolis
Junco do Maranhão
Turmalina
Ubarana
Ubatuba
Dom Pedro
Duque Bacelar
Esperantinópolis
Estreito
Feira Nova do Maranhão
Fernando Falcão
Formosa da Serra Negra
Fortaleza dos Nogueiras
Fortuna
Godofredo Viana
Vista Serrana
Governador Archer
Governador Edison Lobão
Magalhães de Almeida
Maracaçumé
Governador Eugênio Barros
Marajá do Sena
Lagoinha do Piauí
Diamante
Governador Luiz Rocha
Governador Newton Bello
Governador Nunes Freire
Dona Inês
Ubirajara
Uchoa
Vargem Bonita
Vidal Ramos
Videira
Vitor Meireles
Witmarsum
Graça Aranha
Grajaú
Guimarães
Humberto de Campos
Icatu
Paraibano
Parnarama
Passagem Franca
Xanxerê
Xavantina
Igarapé do Meio
Lucrécia
Xaxim
Igarapé Grande
Imperatriz
Itaipava do Grajaú
Itapecuru Mirim
Itinga do Maranhão
Jatobá
Jenipapo dos Vieiras
João Lisboa
Joselândia
Zortéa
Lago da Pedra
Lago do Junco
Lago Verde
Lagoa do Mato
Balneário Rincão
Aceguá
Água Santa
Agudo
Ajuricaba
Alecrim
Alegrete
Alegria
Almirante Tamandaré do Sul
Alpestre
Alto Alegre
Inocência
Itaporã
Itaquiraí
Ivinhema
Japorã
Jaraguari
Lago dos Rodrigues
Lagoa Grande do Maranhão
Lajeado Novo
Jardim
Jateí
Juti
Buriti Alegre
Buriti de Goiás
Lima Campos
Loreto
Peritoró
Pindaré-Mirim
Pinheiro
Luís Domingues
Sambaíba
Maranhãozinho
Mata Roma
Matinha
Matões
Matões do Norte
Milagres do Maranhão
Mirador
Santa Luzia
Miranda do Norte
Mirinzal
Monção
Montes Altos
Morros
Nina Rodrigues
Nova Colinas
Júlio Borges
Nova Iorque
Nova Olinda do Maranhão
Santa Luzia do Paruá
Santa Quitéria do Maranhão
Alto Feliz
Alvorada
Amaral Ferrador
Ametista do Sul
Olho d'Água das Cunhãs
Olinda Nova do Maranhão
Paço do Lumiar
André da Rocha
Palmeirândia
Luís Gomes
Arroio do Padre
Pastos Bons
Paulino Neves
Paulo Ramos
Pedreiras
Pedro do Rosário
Penalva
Peri Mirim
Arroio dos Ratos
Arroio do Tigre
Arroio Grande
Pio XII
Santana do Maranhão
Santo Amaro do Maranhão
Pirapemas
Poção de Pedras
Porto Franco
Porto Rico do Maranhão
Presidente Dutra
Presidente Juscelino
Presidente Médici
Presidente Sarney
Presidente Vargas
Primeira Cruz
Raposa
Riachão
Ribamar Fiquene
Rosário
Santa Filomena do Maranhão
Santa Helena
Santa Inês
Santa Rita
Senador Alexandre Costa
Santo Antônio dos Lopes
Senador La Rocque
Serrano do Maranhão
Sítio Novo
Sucupira do Norte
Sucupira do Riachão
Tasso Fragoso
São Benedito do Rio Preto
São Bento
São Bernardo
São Domingos do Azeitão
São Domingos do Maranhão
São Félix de Balsas
Tuntum
Turiaçu
Turilândia
Tutóia
Urbano Santos
Vargem Grande
Viana
Vila Nova dos Martírios
Vitória do Mearim
Vitorino Freire
Zé Doca
Acauã
São Francisco do Brejão
São Francisco do Maranhão
São João Batista
São João do Carú
São João do Paraíso
São João do Soter
São João dos Patos
São José de Ribamar
São José dos Basílios
São Luís
São Luís Gonzaga do Maranhão
São Mateus do Maranhão
São Pedro da Água Branca
São Pedro dos Crentes
São Raimundo das Mangabeiras
São Raimundo do Doca Bezerra
São Roberto
São Vicente Ferrer
Alegrete do Piauí
Alto Longá
Satubinha
Timbiras
Timon
Trizidela do Vale
Tufilândia
Agricolândia
Água Branca
Alagoinha do Piauí
Altos
Pedro Avelino
Alvorada do Gurguéia
Barro Duro
Amarante
Batalha
Olho d'Água do Borges
Angical do Piauí
Anísio de Abreu
Antônio Almeida
Aroazes
Aroeiras do Itaim
Campinas do Piauí
Arraial
Assunção do Piauí
Avelino Lopes
Baixa Grande do Ribeiro
Barra D'Alcântara
Barras
Barreiras do Piauí
Bela Vista do Piauí
Campo Alegre do Fidalgo
Madre de Deus
Maetinga
Belém do Piauí
Beneditinos
Bertolínia
Betânia do Piauí
Boa Hora
Bocaina
Bom Jesus
Bom Princípio do Piauí
Bonfim do Piauí
Sítio Novo
Maiquinique
Mairi
Boqueirão do Piauí
Brasileira
Brejo do Piauí
Buriti dos Lopes
Buriti dos Montes
Malhada
Malhada de Pedras
Manoel Vitorino
Mansidão
Maracás
Maragogipe
Maraú
Marcionílio Souza
Mascote
Mata de São João
Matina
Medeiros Neto
Cabeceiras do Piauí
Cajazeiras do Piauí
Cajueiro da Praia
Caldeirão Grande do Piauí
Miguel Calmon
Milagres
Mirangaba
Mirante
Monte Santo
Morpará
Morro do Chapéu
Mortugaba
Mucugê
Mucuri
Campo Grande do Piauí
São Luis do Piauí
São Miguel da Baixa Grande
Mundo Novo
Campo Largo do Piauí
Campo Maior
Canavieira
Conceição do Canindé
Coronel José Dias
Corrente
Canto do Buriti
Capitão de Campos
Capitão Gervásio Oliveira
São Miguel do Fidalgo
São Miguel do Tapuio
Caracol
Caraúbas do Piauí
Cristalândia do Piauí
Cristino Castro
Curimatá
Currais
Muniz Ferreira
Muquém do São Francisco
Muritiba
Mutuípe
Nazaré
Nilo Peçanha
Caridade do Piauí
Castelo do Piauí
Caxingó
Curralinhos
Curral Novo do Piauí
Nordestina
Nova Canaã
Cocal
Demerval Lobão
São Pedro do Piauí
Cocal de Telha
Floresta do Piauí
São Raimundo Nonato
Cocal dos Alves
Francisco Ayres
Coivaras
Sebastião Barros
Tenente Ananias
Paulo Afonso
Pé de Serra
Pedrão
Pedro Alexandre
Piatã
Pilão Arcado
Colônia do Gurguéia
Pindaí
Pindobaçu
Pintadas
Piraí do Norte
Piripá
Piritiba
Planaltino
Planalto
Poções
Pojuca
Ponto Novo
Porto Seguro
Colônia do Piauí
Ilha Grande
Potiraguá
Prado
Dirceu Arcoverde
Dom Expedito Lopes
Domingos Mourão
Dom Inocêncio
Elesbão Veloso
Eliseu Martins
Esperantina
Fartura do Piauí
Flores do Piauí
Inhuma
Ipiranga do Piauí
Floriano
Francinópolis
Francisco Macedo
Francisco Santos
Fronteiras
Geminiano
Gilbués
Presidente Dutra
Presidente Jânio Quadros
Presidente Tancredo Neves
Queimadas
Quijingue
Guadalupe
Guaribas
Hugo Napoleão
Quixabeira
Rafael Jambeiro
Remanso
Itainópolis
Itaueira
Jacobina do Piauí
Jaicós
Retirolândia
Riachão das Neves
Jardim do Mulato
Jatobá do Piauí
Jurema
Riachão do Jacuípe
Riacho de Santana
Ribeira do Amparo
Jerumenha
João Costa
Joca Marques
José de Freitas
Juazeiro do Piauí
Ribeira do Pombal
Ribeirão do Largo
Rio de Contas
Rio do Antônio
Lagoa Alegre
Lagoa do Barro do Piauí
Lagoa de São Francisco
Marcos Parente
Rio do Pires
Rio Real
Rodelas
Ruy Barbosa
Lagoa do Piauí
Lagoa do Sítio
Landri Sales
Luís Correia
Luzilândia
Nazaré do Piauí
Nazária
Nossa Senhora de Nazaré
Madeiro
Manoel Emídio
Nossa Senhora dos Remédios
Novo Oriente do Piauí
Novo Santo Antônio
Oeiras
Carnaubais
Marcolândia
Ceará-Mirim
Cerro Corá
Santa Maria da Vitória
Santana
Santanópolis
Massapê do Piauí
Matias Olímpio
Coronel Ezequiel
Santa Rita de Cássia
Santa Terezinha
Santo Amaro
Santo Antônio de Jesus
Santo Estêvão
São Desidério
São Domingos
São Félix
São Félix do Coribe
Miguel Alves
Paes Landim
São Felipe
São Francisco do Conde
São Gabriel
São Gonçalo dos Campos
São José da Vitória
São José do Jacuípe
Miguel Leão
Milton Brandão
Pajeú do Piauí
Palmeira do Piauí
São Miguel das Matas
São Sebastião do Passé
Sapeaçu
Sátiro Dias
Monsenhor Gil
Monsenhor Hipólito
Saubara
Saúde
Seabra
Sebastião Laranjeiras
Senhor do Bonfim
Serra do Ramalho
Sento Sé
Monte Alegre do Piauí
Morro Cabeça no Tempo
Pavussu
Pedro II
Coronel João Pessoa
Serra Dourada
Serra Preta
Serrinha
Serrolândia
Simões Filho
Morro do Chapéu do Piauí
Murici dos Portelas
Timbaúba dos Batistas
Touros
Sítio do Mato
Sítio do Quinto
Sobradinho
Souto Soares
Olho D'Água do Piauí
Nova Santa Rita
Triunfo Potiguar
Tabocas do Brejo Velho
Tanhaçu
Tanque Novo
Tanquinho
Taperoá
Padre Marcos
Minador do Negrão
Palmeirais
Regeneração
Riacho Frio
Tapiramutá
Teixeira de Freitas
Teodoro Sampaio
Teofilândia
Teolândia
Terra Nova
Tremedal
Tucano
Uauá
Ubaíra
Ubaitaba
Ubatã
Uibaí
Umburanas
Una
Urandi
Paquetá
Parnaguá
Parnaíba
Passagem Franca do Piauí
Santana do Piauí
Santa Rosa do Piauí
Uruçuca
Patos do Piauí
Pau D'Arco do Piauí
Paulistana
Araújos
Araxá
Arceburgo
Arcos
Areado
Argirita
Pedro Laurentino
Aricanduva
Arinos
Astolfo Dutra
Ataléia
Augusto de Lima
Baependi
Baldim
Bambuí
Bandeira
Bandeira do Sul
Barão de Cocais
Barão de Monte Alto
Barbacena
Barra Longa
Barroso
Bela Vista de Minas
Belmiro Braga
Belo Horizonte
Belo Oriente
Picos
Pimenteiras
Pio IX
Santo Antônio de Lisboa
Belo Vale
Berilo
Bertópolis
Berizal
Betim
Piracuruca
Piripiri
Porto
Porto Alegre do Piauí
Bias Fortes
Bicas
Biquinhas
Boa Esperança
Prata do Piauí
Santo Antônio dos Milagres
Bocaina de Minas
Bocaiúva
Bom Despacho
Bom Jardim de Minas
Bom Jesus da Penha
Bom Jesus do Amparo
Bom Jesus do Galho
Bom Repouso
Bom Sucesso
Bonfim
Bonfinópolis de Minas
Bonito de Minas
Borda da Mata
Botelhos
Botumirim
Queimada Nova
Redenção do Gurguéia
Brasilândia de Minas
Brasília de Minas
Brás Pires
Braúnas
Brazópolis
Brumadinho
Bueno Brandão
Ribeira do Piauí
Ribeiro Gonçalves
Rio Grande do Piauí
Jurema
Buenópolis
Santa Cruz do Piauí
Santa Cruz dos Milagres
Santa Filomena
Bugre
Buritis
Buritizeiro
Cabeceira Grande
Cabo Verde
Cachoeira da Prata
Cachoeira de Minas
Cachoeira Dourada
Caetanópolis
Caeté
Caiana
Cajuri
Caldas
Camacho
Camanducaia
Santa Luz
Cambuí
Cambuquira
Campanário
Campanha
Campestre
Campina Verde
Campo Azul
Campo Belo
Campo do Meio
Campo Florido
Santo Inácio do Piauí
São Gonçalo do Piauí
São João da Canabrava
São Braz do Piauí
São Félix do Piauí
São Francisco de Assis do Piauí
São Francisco do Piauí
São Gonçalo do Gurguéia
São João da Fronteira
São João da Serra
Campos Altos
Campos Gerais
Canaã
Canápolis
Cana Verde
Candeias
Cantagalo
Caparaó
Capela Nova
Capelinha
Capetinga
Capim Branco
Capinópolis
São João da Varjota
São João do Arraial
São José do Peixe
Capitão Andrade
Capitão Enéas
Capitólio
São João do Piauí
São José do Divino
São
