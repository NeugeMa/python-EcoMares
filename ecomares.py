def exibir_programa (): # Função para exibir o programa | Site para pegar fonte: https://fsymbols.com/pt/letras/
    print("Seja bem-vindo(a) ao Projeto EcoMares 🐋! Aqui você poderá aprender sobre a importância da preservação dos oceanos e da vida marinha. Vamos lá?\n")
    print("""
███████╗░█████╗░░█████╗░███╗░░░███╗░█████╗░██████╗░███████╗░██████╗
██╔════╝██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔══██╗██╔════╝██╔════╝
█████╗░░██║░░╚═╝██║░░██║██╔████╔██║███████║██████╔╝█████╗░░╚█████╗░
██╔══╝░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══██║██╔══██╗██╔══╝░░░╚═══██╗
███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░░██║██║░░██║███████╗██████╔╝
╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═════╝░ 
""")

    
# Exibindo as opções do menu principal
def exibir_opcoes(opcoes): 
    print("Escolha uma das opções abaixo: \n")   
    while True: #Utilizando while True para garantir que o usuário escolha uma opção válida
        for opcao in opcoes:
            print(opcao)

        escolha = input("Por favor, escolha uma opção: ")
        if escolha in [str(i+1) for i in range(len(opcoes))]: #Verifica se a escolha existe na lista, onde N é o número de opções
            break
        else:
            print("Opção inválida. Por favor, tente novamente.\n")
    return int(escolha) - 1 #Converte a escolha do usuário para um índice valido

#Fun;cão principal do programa
def main():
    exibir_programa()
    
    opcoes = [
        "1 - Entenda o problema da proposto pela Ocean 20(O20)",
        "2 - Conheça a solução EcoMares?",
        "3 - Benefícios da EcoMares",
        "4 - Saiba como você pode ajudar",
        "5 - Conheça a equipe EcoMares",
        "6 - Sair\n" ]
    # Lista de funções que serão chamadas de acordo com a escolha do usuário
    funcoes = [problema_o20, solucao_ecomares, beneficios_ecomares, como_ajudar, equipe_ecomares, sair] 

    while True:
        escolha = exibir_opcoes(opcoes)
        if escolha == 5:
            break
        funcoes[escolha]()
        input("\nPressione ENTER para continuar \n")
    
# Função sobre o problema proposto pela Ocean 20 (O20) 
def problema_o20():
    print("""
█▀█ █▀█ █▀█ █▄▄ █░░ █▀▀ █▀▄▀█ ▄▀█   █▀█ █▀▀ █▀▀ ▄▀█ █▄░█   ▀█ █▀█   ▄▀ █▀█ ▀█ █▀█ ▀▄ ▀
█▀▀ █▀▄ █▄█ █▄█ █▄▄ ██▄ █░▀░█ █▀█   █▄█ █▄▄ ██▄ █▀█ █░▀█   █▄ █▄█   ▀▄ █▄█ █▄ █▄█ ▄▀ ▄""")
    
    print("\nFundamentais para a biodiversidade do planeta, os oceanos enfrentam enormes desafios como as ameaças aos ecossistemas marinhos, poluição, mudanças climáticas, entre outros, causando impacto direto na economia global. À medida que esses problemas ambientais aumentam, o mundo precisa cada vez mais de nós. \n")
    
    print("Neste contexto, devemos desenvolver soluções inteligentes relacionadas à Economia Azul, utilizando tecnologia e inovação. E com isso,  contribuir para transformar o futuro dos oceanos e, consequentemente, do nosso planeta. \n")
    
    print("O Desafio trazido pela Oceans 20 (O20) em 2024 visa envolver estudantes e entusiastas de tecnologia, inovação e sustentabilidade na criação de soluções para os problemas enfrentados pelos oceanos. Os projetos devem focar em educação e conscientização, tecnologias sustentáveis e gestão e monitoramento. A iniciativa busca mobilizar a criatividade e conhecimento técnico dos participantes para preservar e recuperar os oceanos, garantindo um futuro sustentável. \n")
    
    print("Caso queira saber mais sobre a empresa, acesse: https://www.oceans20.com.br/") # Link para acessar o site da O20

# Função sobre a solução proposta pela EcoMares
def solucao_ecomares():
    print("""
█▀ █▀█ █░░ █░█ █▀▀ ▄▀█ █▀█   █▀▀ █▀▀ █▀█ █▀▄▀█ ▄▀█ █▀█ █▀▀ █▀
▄█ █▄█ █▄▄ █▄█ █▄▄ █▀█ █▄█   ██▄ █▄▄ █▄█ █░▀░█ █▀█ █▀▄ ██▄ ▄█""")
    
    print("Conheça a EcoMares: Sistema de Monitoramento de Poluição Oceânica com Projeto Educacional para Crianças: \n")
    print("A EcoMares tem como objetivo desenvolver uma plataforma (site) que integra dados coletados em tempo real por sensores Arduino, capazes de capturar o nível de poluição da água e sua temperatura em diferentes regiões. Utilizando LDRs , LEDs e um sensor de temperatura, esses sensores “subaquáticos” fornecem informações precisas e atualizadas. \n")
    print("A plataforma apresentará esses dados através de um sistema de visualização interativo, tornando as informações claras e acessíveis para todos os usuários. Além disso, incluirá um projeto educativo para crianças e jovens, chamado Maré Limpa, que visa conscientizar sobre a importância da preservação ambiental. \n")
    
    print("Gostaria de ver nossos repositórios? Acesse:")
    print("Repositório de Front: https://github.com/NeugeMa/projeto-EcoMares \n"
        "Repositório de Python: https://github.com/NeugeMa/python-EcoMares \n")
    
    while True: # Utilizando uma função com While + Try para garantir que o usuário escolha uma opção válida
        try:    
        #Pedindo que nosso usuário escolha entre três opções
            resposta = input("Você gostaria de saber sobre os objetivos (1) ou nosso público-alvo (2)? Caso não queira, apenas aperte (3): ") 
        
            if resposta == '1':
                print("""
█▀█ █▄▄ ░░█ █▀▀ ▀█▀ █ █░█ █▀█ █▀ ▄▄   █▀█ █▀█ █▀█ ░░█ █▀▀ ▀█▀ █▀█
█▄█ █▄█ █▄█ ██▄ ░█░ █ ▀▄▀ █▄█ ▄█ ░░   █▀▀ █▀▄ █▄█ █▄█ ██▄ ░█░ █▄█ """)
                print("Quais são os objetivos do projeto EcoMares? \n")
                
                print("01. Mapeamento: Exibição em tempo real com dados geoespaciais que destacam as áreas mais afetadas. \n") 
                print("02. Sensores Inteligentes: Utilizando sensores subaquáticos equipados com tecnologia de monitoramento ambiental (temperatura, poluição, pH, etc.) \n")
                print("03. Integração com Mídias: Compartilhamento de dados relevantes e alertas em plataformas, para aumentar a conscientização. \n")
                print("04. Colaboração de comunidades: Funcionalidades que permitem aos cidadãos reportar avistamentos de poluição e poderem participar do monitoramento. \n")
                print("05. Atividades Práticas: Campanhas de limpeza nas praias/lagos, oficinas de reciclagem e visitas a centros marinhos. \n")
                print("06. Educação e Conscientização: O projeto Maré Limpa educa as crianças sobre a importância da conservação oceânica, preparando-as para serem futuros defensores do meio ambiente.")
            
            elif resposta == '2':
                print("""
█▀█ █░█ █▄▄ █░░ █ █▀▀ █▀█   ▄▀█ █░░ █░█ █▀█   ▄▄   █▀█ █▀█ █▀█ ░░█ █▀▀ ▀█▀ █▀█
█▀▀ █▄█ █▄█ █▄▄ █ █▄▄ █▄█   █▀█ █▄▄ ▀▄▀ █▄█   ░░   █▀▀ █▀▄ █▄█ █▄█ ██▄ ░█░ █▄█""")
                print("\nQuem é o nosso público alvo?")
                print("Tivemos um foco mais restrito em jovens e adultos, o público-alvo do projeto ECOMARES pode ser descrito da seguinte forma: \n")
                
                #Apresentando público-alvo
                print("01. Jovens Estudantes e Universitários: ")
                print("Objetivo: Proporcionar uma base educacional sólida em ciências ambientais e incentivar a participação ativa em projetos de monitoramento e conservação marinha. \n")

                print("02. Cidadãos Adultos Conscientes: ")
                print("Objetivo: Conscientizar sobre a importância da conservação oceânica e incentivar a participação em atividades de preservação, como campanhas de limpeza de praias e oficinas de reciclagem. \n")
                
                print("03. Pesquisadores e Especialistas Ambientais:")
                print("Objetivo: Utilizar os dados fornecidos pela plataforma para conduzir pesquisas científicas, desenvolver políticas de conservação e implementar medidas de preservação ambiental. \n")
                
            elif resposta == '3':
                break
        
            else:
                print("Por favor, insira um número válido (1, 2 ou 3).")
                continue
            break
        except:
            print("Por favor, insira um número válido (1, 2 ou 3).")
                
# Função sobre os benefícios da EcoMares
def beneficios_ecomares():  
    print("""
█▄▄ █▀▀ █▄░█ █▀▀ █▀▀ █ █▀▀ █ █▀█ █▀   ▄▄   █▀█ █▀█ █▀█ ░░█ █▀▀ ▀█▀ █▀█
█▄█ ██▄ █░▀█ ██▄ █▀░ █ █▄▄ █ █▄█ ▄█   ░░   █▀▀ █▀▄ █▄█ █▄█ ██▄ ░█░ █▄█ """)    

    print("O que a EcoMares pode trazer de benefícios? \n")
    print("Levando em conta o objetivo de monitorar a saúde marinha, a solução busca demonstrar os níveis de poluição do mar, por meio da utilização de sensores para arduino e uma plataforma que possibilita a visualização dos dados obtidos pelo o sistema em tempo real, buscando conscientizar pessoas leigas no assunto ou até mesmo especialistas, juntamente com um projeto educacional para crianças / jovens. \n")
    
    print("Monitoramento Ambiental:")
    print("Utilização de sensores Arduino para monitorar níveis de poluição e biodiversidade marinha em tempo real oferece vantagens na gestão ambiental, permitindo detecção precoce e intervenções rápidas.")
    print("A plataforma de mapeamento com dados geoespaciais ajuda a identificar áreas afetadas pela poluição, priorizar ações de conservação e alocar recursos de forma eficiente. A visualização interativa facilita a compreensão dos dados. \n")
    
    print("Sensores Inteligentes:")
    print("Sensores subaquáticos com tecnologia de monitoramento ambiental fornecem dados importantes para a conservação dos habitats marinhos. \n")
    
    print("Integração com Mídias:")
    print("Compartilhar dados e alertas em plataformas de mídias sociais aumenta a conscientização sobre a saúde dos oceanos, facilitando disseminação de informações e promovendo a participação da comunidade. \n")
    
    print("Colaboração Comunitária:")
    print("As funcionalidades de reporte de poluição e monitoramento incentivam o envolvimento comunitário e a conscientização ambiental. A colaboração das comunidades locais é essencial para o sucesso das iniciativas de conservação. \n")
    
    print("Projeto Maré Limpa:")
    print("O programa educativo Maré Limpa é fundamental no projeto, educando e conscientizando as crianças sobre a conservação oceânica. Através de atividades práticas, como limpezas e reciclagem, incentiva comportamentos sustentáveis desde cedo. Essa preparação garante a continuidade dos esforços de conservação. \n")
    
    
def como_ajudar():
    print("""
█▀▀ █▀█ █▀▄▀█ █▀█   ▄▀█ ░░█ █░█ █▀▄ ▄▀█ █▀█ ▀█
█▄▄ █▄█ █░▀░█ █▄█   █▀█ █▄█ █▄█ █▄▀ █▀█ █▀▄ ░▄ """)
    
    print("Ok! Você chegou até aqui, imagino que tenha bastante consiencia em como a preservação dos oceanos é importante.")
    print("Mas, agora vem a pergunta mais importante, como ajudar? \n")
    
    #Perguntando ao usuário se ele gostaria de ajudar 
    while True:
        resposta = input("Você gostaria de ajudar? Escolhe entre ajuda(a) ou formulário (f): ")

        if resposta.lower() == 'a': #Explicando como a ajuda dele será importante!
            print("Que bom, que tenha escolhido está opção.. Já que toda ajuda é sempre bem-vinda <3") 
            print("A conservação dos oceanos é uma responsabilidade compartilhada que começa com pequenas ações no dia a dia. Aqui estão algumas maneiras pelas quais uma pessoa comum pode contribuir para a limpeza do oceano, integrando essas práticas em sua rotina: \n")
            
            print("1. Reduzir, Reutilizar e Reciclar")
            print("Reduza o uso de plásticos: Evite produtos de uso único, como sacolas plásticas, garrafas e canudos. Opte por alternativas reutilizáveis.")
            print("Reutilize: Utilize recipientes e sacolas reutilizáveis para suas compras e armazenamento de alimentos.")
            print("Recicle: Separe corretamente o lixo reciclável e descarte-o em pontos de coleta apropriados. \n")
            
            print("2. Participar de Limpezas de Praia")
            print("Voluntarie-se em campanhas de limpeza: Participe de eventos organizados por grupos locais ou ONGs como a EcoMares. \n")
            
            print("3. Reportar Poluição")
            print("Utilize plataformas de monitoramento: Use a plataforma da EcoMares para reportar avistamentos de poluição em sua área.")
            print("Aja localmente: Informe autoridades locais sobre áreas afetadas pela poluição para que ações possam ser tomadas rapidamente. \n")
            
            print("4. Educação e Conscientização")
            print("Aprenda e compartilhe conhecimento: Informe-se sobre a poluição oceânica e compartilhe o que aprende com amigos e familiares. ")
            print("Envolva as crianças: Participe em projetos educativos como o Maré Limpa da EcoMares para ensinar as próximas gerações sobre a importância da conservação. \n")
            
            print("Agora você possui uma base do que fazer, ficamos felizes em poder contribuir a um futuro mais azul \n")
            break
        elif resposta.lower() == 'f': #Caso o usuário não queira ajudar, ele pode contribuir com um forms de avaliação
            print("Preparamos um fórmulario de avaliação para você! Avalie e deixe um feedback, para nós <3")
            
            nome = input("Como gostaria de ser chamado?: ")
            print(f"Obrigado, {nome}! Sua opinião é muito importante para nós. Por favor, responda às seguintes perguntas: \n")
                
            avaliacao = int(input("1. Como você avaliaria o projeto EcoMares? (1-5): "))
            feedback = input("2. Escreva um pouco do que acha sobre o projeto EcoMares? ")
            sugestao = input("2. O que você acresentaria no projeto EcoMares? ")
            recomendacao = input("3. Você recomendaria o projeto EcoMares para outras pessoas? (s/n): ")
            
            resultado = print(f"Obrigado por avaliar o projeto EcoMares, {nome}! \n"
                            f"Suas respostas foram: \n -{avaliacao} \n -{feedback} \n -{sugestao} \n -{recomendacao} \n"
                            "Agradecemos por sua participação e feedback!")
            print("Respostas Enviadas!")
            break
        else: 
            print("Resposta inválida. Por favor, responda com 's' para sim ou 'n' para não.")
    
def equipe_ecomares():
    print(""" 
█▀▀ █░█ █▄░█ █▀▄ ▄▀█ █▀▄ █▀█ █▀█ ▄▀█ █▀
█▀░ █▄█ █░▀█ █▄▀ █▀█ █▄▀ █▄█ █▀▄ █▀█ ▄█ """)
    print("Conheça as fundadoras do projeto EcoMares: \n")
    
    while True:
        resposta = input("Quem você gostaria de ver? Mariana (m) ou Beatriz (b): ")
        if resposta.lower() == 'm':
            print("Conheça Mariana Neugebauer Dourado: \n")
            print("Foi responsável pela criação do Front-End + WebDevelopment | desenvolvimento da aplicação em Python | Criadora da persona, responsável por todo o design e história. \n"
            "Sendo uma pessoa simpática e muito carismática, que adora ajudar as pessoas e sempre está disposta a aprender coisas novas. \n")
            
            print("Acesse suas mídias socias: \n"
                "GitHub: https://github.com/NeugeMa | LinkedIn: https://www.linkedin.com/in/neugema/ \n")
            break 
        elif resposta.lower() == 'b':
            print("Conheça Beatriz Vieira de Novais: \n")
            print("Responsável pela criação do projeto em Arduino | produzindo cálculo | e desenvolvimento do backlog. \n"
                "Ama ler mangas e assistir séries e filmes. Além de que comida gostosa é minha maior felicidade. \n")
            
            print("Acesse suas mídias socias: \n"
                "GitHub: https://github.com/triz14 | LinkedIn: https://www.linkedin.com/in/beatriznovais/ \n")             
            break
        else: 
            print("Resposta inválida. Por favor, responda com 'm' para Mariana ou 'b' para Beatriz.")
    
def sair():
    print("Obrigado por participar do Projeto EcoMares! Até a próxima!")
main()