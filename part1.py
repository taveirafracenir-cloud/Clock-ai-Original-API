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
