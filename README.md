# Google Books Data Pipeline & Analysis

Este projeto é um pipeline de dados completo que extrai, transforma e analisa dados da API do Google Books. O objetivo é transformar dados brutos em insights estratégicos sobre diferentes nichos literários.

## O Diferencial: Pipeline "Coringa" (Agnóstico ao Tema)

Diferente de uma análise estática, este projeto foi construído como um **Framework de Análise de Mercado**. 
- **Versatilidade:** Embora a demonstração atual foque no nicho de *Investing*, o código é parametrizado.
- **Reuso:** Um analista ou pesquisador pode alterar apenas a palavra-chave de busca no módulo de ingestão para gerar instantaneamente um novo relatório completo sobre qualquer outro tema (ex: IA, Medicina, Ficção).
- **Escalabilidade:** A separação entre as camadas Bronze (bruto) e Silver (limpo) permite que novas fontes de dados sejam acopladas no futuro.

## Tecnologias Utilizadas

- **Python 3.12+**
- **Pandas:** Limpeza, transformação e engenharia de atributos (Feature Engineering).
- **Plotly Express:** Visualizações interativas e dinâmicas.
- **Google Books API:** Fonte de extração dos dados.
- **Git/GitHub:** Controle de versionamento e documentação.

## Arquitetura do Projeto

1. **Ingestão (Layer Bronze):** Coleta de dados via API e salvamento em JSON bruto.
2. **Transformação (Layer Silver):** Limpeza de dados, tratamento de nulos, normalização de categorias e criação da métrica personalizada `book_size`.
3. **Análise (Visual):** Notebook interativo com Data Storytelling explorando formatos, temporalidade e volume editorial.

## Desafios Técnicos e Decisões

Durante o desenvolvimento, foram tomadas decisões importantes baseadas na qualidade dos dados coletados e na ética analítica:

- **Pivô de Tema:** Inicialmente o projeto explorou outros nichos, mas ao identificar inconsistências críticas nos dados retornados pela API (como excesso de nulos em campos essenciais), o tema foi alterado para garantir uma entrega mais íntegra. (Porém, depois de escolher outros temas, foi observado que era um problema da API e não do tema escolhido.)
- **Tratamento de Dados Inconsistentes:** As colunas de `price`, `ratingsCount` e `averageRating` apresentaram baixa completude (muitos valores zerados ou nulos). Optou-se por desconsiderar métricas financeiras e de avaliações para evitar conclusões enviesadas.
- **Normalização de Categorias:** Devido à alta fragmentação das categorias da API (mais de 80 gêneros distintos), a análise focou na segmentação por volume de páginas e nos termos mais frequentes.
- **Limitações de Conclusão:** Por se tratar de uma amostra dependente da disponibilidade da API, os resultados são interpretados como observações sobre o catálogo disponível e não como verdades definitivas sobre o mercado literário.

> [!IMPORTANT]
> Mais do que uma análise estatística de nicho, este projeto foca na **viabilidade técnica de um pipeline reutilizável**. Os gráficos e interpretações no arquivo **notebooks/analysis.ipynb** servem como prova de conceito da ferramenta.

---
*Este projeto foi desenvolvido com fins acadêmicos e de estudo pessoal, servindo como um laboratório para a prática de coleta, manipulação e visualização de dados. Ele compõe meu portfólio técnico, demonstrando a aplicação prática de lógica de programação em Python, consumo de APIs reais e a transformação de dados brutos em informações visuais.*