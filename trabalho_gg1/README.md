Temos o código principal, e quatro módulos que compõem o programa de estoque de uma loja.

O primeiro módulo é o menu_module, que servirá para mostrar ao usuário todas as funcionalidades disponíveis do programa. São 10 opções diferentes, sendo a úlitma delas um "botão de sair".

O stock_module se refere a tudo que tem a ver com o estoque diretamente. Dentro dele temos as seguintes funções:
- add_product: Adiciona produtos ao estoque, possibilitando o cadastro do produto incluindo quantidade, preço unitário e categoria. A função checa a existência prévia do produto e atualiza a quantidade disponível no estoque, além de registrar os dados iniciais do produto.
- search_for_product: Possibilita a pesquisa por um produto específico, exibindo em seguida toda a informação disponível previamente disponibilizada e o histórico de venda do produto em questão.
- search_product_by_category: Permite que o usuário procure por uma categoria específica e que veja todos os produtos inseridos nela, incluindo seus atributos.
- show_products: Mostra todos os produtos disponíveis no estoque, incluindo seus atributos.
- alter_price: Permite que o usuário ajuste o preço de um produto, e registra as mudanças em um local separado. O preço novo é utilizado em novas vendas.
- remove_product: Dá ao usuário a opção de remover um produto do estoque por completo, e registra as remoções em um local separado.

O sales_module possui apenas uma função, que consiste de:
- sell_product: Permite a venda de um produto, fazendo a verificação de quantidade previamente no estoque, o cálculo do total da compra, envia as informações da venda para um local separado e registra a data e a hora da mesma. Ela também mantém o usuário ciente da falta de produtos ou quantidade de produtos no estoque.

O historic_module é o local onde as informações das vendas, mudanças e demais registros ficam armazenados.
- sales_report: O registro de vendas de todos os produtos, e também registros individuais de cada produto disponível.
- alter_report: A função em questão possui três opções dentro dela, que possibilitam checar as adições de produtos no estoque, atualizações de preços de produtos e exclusões de produtos. É possível fazer múltiplas checagens nessa função.

Por fim, o main_code, onde os módulos são importados, listas e dicionários são abertos e funções são chamadas.

O código visa facilitar a vida do usuário e manter as informações sempre atualizadas e editáveis, otimizando o trabalho.

