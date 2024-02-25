TextMemento:
É uma classe simples que armazena o estado de um texto. Ela possui um
método get_text() que retorna o texto armazenado.

TextEditor:
Representa um editor de texto. Ele possui métodos para manipular o texto,
como append() para adicionar mais texto ao conteúdo atual, e get_text()
para obter o texto atual.
Ele também possui os métodos save() e restore(memento). O método
save() cria um objeto TextMemento com o estado atual do texto e retorna
esse objeto. O método restore(memento) recebe um objeto TextMemento e
restaura o estado do texto para o estado representado pelo memento
fornecido.

Historico:
É uma classe que mantém o histórico de estados do editor de texto. Ela
usa uma pilha (stack) para armazenar objetos TextMemento.
Possui os métodos push(memento) para adicionar um novo memento à
pilha e pop() para remover e retornar o último memento adicionado.

main():
No método principal, são criados uma instância do TextEditor (edita) e uma
instância do Historico (historico).
Texto é adicionado ao editor de texto (edita.append(...)), e o estado atual é
salvo no histórico (historico.push(edita.save())).
Depois de adicionar mais texto e salvar o estado novamente no histórico,
parte do texto é desfeita usando edita.restore(historico.pop()), que restaura
o estado anterior do texto com base nos objetos TextMemento
armazenados na pilha.
O resultado final é imprimir o texto atual e o texto após desfazer as
alterações.
