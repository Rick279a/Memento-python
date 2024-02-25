class TextMemento:
    def __init__(self, text):
        self._text = text

    def get_text(self):
        return self._text


class TextEditor:
    def __init__(self):
        self._text = ""

    def save(self):
        return TextMemento(self._text)

    def restore(self, memento):
        self._text = memento.get_text()

    def append(self, new_text):
        self._text += new_text

    def get_text(self):
        return self._text


class Historico:
    def __init__(self):
        self._stack = []

    def push(self, memento):
        self._stack.append(memento)

    def pop(self):
        if self._stack:
            return self._stack.pop()
        else:
            return None


def main():
    edita = TextEditor()
    historico = Historico()
    edita.append("Ricardo ")
    historico.push(edita.save())  # Salva o estado atual
    edita.append("Mazetto ")
    historico.push(edita.save())  # Salva o estado após a segunda alteração
    edita.append("Pereira")
    historico.push(edita.save())  # Salva o estado após a segunda alteração
    print("Texto atual:", edita.get_text())
    edita.restore(historico.pop())
    edita.restore(historico.pop())
    print("Texto após desfazer 1:", edita.get_text())
    edita.restore(historico.pop())
    print("Texto após desfazer 2:", edita.get_text())


if __name__ == "__main__":
    main()
