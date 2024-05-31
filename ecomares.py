def exibir_programa ():
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
    print("Seja bem-vindo(a) ao Projeto EcoMares! Aqui você poderá aprender sobre a importância da preservação dos oceanos e da vida marinha. Vamos lá?\n")
    while True:
        for opcao in opcoes:
            print(opcao)

        escolha = input("Por favor, escolha uma opção: ")
        if escolha in [str(i+1) for i in range(len(opcoes))]:
            break
        else:
            print("Opção inválida. Por favor, tente novamente.\n")
    return int(escolha) - 1

def main():
    exibir_programa()
    
    opcoes = [
        "1 - Entenda o problema da proposto pela Ocean 20(O20)",
        "2 - Conheça a solução EcoMares?",
        "3 - Saiba como você pode ajudar",
        "4 - Conheça a equipe EcoMares",
        "5 - Sair\n" ]
    
    funcoes = [problema_o20, solucao_ecomares, como_ajudar, equipe_ecomares, sair]

    while True:
        escolha = exibir_opcoes(opcoes)
        if escolha == 4:
            break
        funcoes[escolha]()
        input("\nPressione ENTER para continuar ")
    
# Função sobre o problema proposto pela Ocean 20 (O20) 
def problema_o20():
    print("Fundamentais para a biodiversidade do planeta, os oceanos enfrentam enormes desafios como as ameaças aos ecossistemas marinhos, poluição, mudanças climáticas, entre outros, causando impacto direto na economia global. À medida que esses problemas ambientais aumentam, o mundo precisa cada vez mais de nós. \n")
    
    print("Neste contexto, devemos desenvolver soluções inteligentes relacionadas à Economia Azul, utilizando tecnologia e inovação. E com isso,  contribuir para transformar o futuro dos oceanos e, consequentemente, do nosso planeta. \n")
    
    print("O Desafio trazido pela Oceans 20 (O20) em 2024 visa envolver estudantes e entusiastas de tecnologia, inovação e sustentabilidade na criação de soluções para os problemas enfrentados pelos oceanos. Os projetos devem focar em educação e conscientização, tecnologias sustentáveis e gestão e monitoramento. A iniciativa busca mobilizar a criatividade e conhecimento técnico dos participantes para preservar e recuperar os oceanos, garantindo um futuro sustentável. \n")
    
    print("Caso queira saber mais sobre a empresa, acesse: https://www.oceans20.com.br/") # Link para acessar o site da O20

# Função sobre a solução proposta pela EcoMares
def solucao_ecomares():
    print("Conheça a EcoMares: Sistema de Monitoramento de Poluição Oceânica com Projeto Educacional para Crianças: \n")
    
    print("A EcoMares tem como objetivo desenvolver uma plataforma (site) que integra dados coletados em tempo real por sensores Arduino, capazes de capturar o nível de poluição da água e sua temperatura em diferentes regiões. Utilizando LDRs , LEDs e um sensor de temperatura, esses sensores “subaquáticos” fornecem informações precisas e atualizadas. \n")
    
    print("A plataforma apresentará esses dados através de um sistema de visualização interativo, tornando as informações claras e acessíveis para todos os usuários. Além disso, incluirá um projeto educativo para crianças e jovens, chamado Maré Limpa, que visa conscientizar sobre a importância da preservação ambiental. \n")
    
    resposta = input("Você gostaria de saber mais sobre o trabalho? (s/n): ")
    if resposta.lower() == 's':
        print("Aqui estão mais informações...")
        # Adicione mais informações aqui
    else:
        print("Obrigado por conhecer a EcoMares!")
    
def como_ajudar():
    print("Ajudando uai")
    
def equipe_ecomares():
    print("Obaa")
    
def sair():
    print("Obrigado por participar do Projeto EcoMares! Até a próxima!")

main()