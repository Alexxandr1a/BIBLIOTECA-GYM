import gym # Importa a biblioteca Gym, que é usada para criar e interagir com ambientes de aprendizado por reforço

from tqdm import tqdm # Importa a biblioteca tqdm, usada para exibir uma barra de progresso


n = 500 # Define o número de iterações para o loop principal


env = gym.make("CartPole-v1", render_mode="human") # Cria um ambiente do Gym para o jogo "CartPole-v1" com renderização habilitada no modo "human"

env.action_space.seed(82) # Define a semente do espaço de ação para garantir resultados reproduzíveis


observation, info = env.reset(seed=82) # Reinicia o ambiente, obtendo o estado inicial (observation) e informações adicionais (info)

# Loop principal para executar n interações com o ambiente
for _ in tqdm(range(n)):  # tqdm é usado para exibir uma barra de progresso durante a execução

    action = env.action_space.sample()   # Seleciona uma ação aleatória no espaço de ações do ambiente

    observation, reward, terminated, truncated, info = env.step(action)  # Realiza a ação no ambiente e obtém o próximo estado, a recompensa, e informações de terminação/truncamento

    print("info : ", info) # Exibe informações adicionais fornecidas pelo ambiente

    # Reinicia o ambiente se o episódio terminar (terminated ou truncated for True)
    if terminated or truncated:
        observation, info = env.reset()


env.close() # Encerra o ambiente após o término do loop