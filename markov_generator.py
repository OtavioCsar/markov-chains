import markovify
import sys

def read_text_file(file_path):
    """Read the content of a text file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def build_markov_model(text):
    """Build a Markov model from the given text."""
    try:
        # Cria o modelo de texto com markovify
        # state_size=2 significa que considera duas palavras anteriores
        text_model = markovify.Text(text, state_size=2)
        return text_model
    except Exception as e:
        print(f"An error occurred while building the Markov model: {e}")
        sys.exit(1)

def generate_sentence(model, max_attempts=5):
    """Generate a sentence using the Markov model."""
    sentences = []
    for _ in range(num_sentences):
        # Gera uma sentença (máxmimo de 280 caracteres, como um tweet(x?))
        sentence = model.make_short_sentence(max_chars=200)
        if sentence:
            sentences.append(sentence)
        else:
            print("Failed to generate a sentence after multiple attempts.")
            break
    return sentences

def main():
    # Verifica se o caminho do arquivo foi fornecido
    if len(sys.argv) != 2:
        print("Usage: python markov_generator.py <path_to_text_file>")
        sys.exit(1)
    # Lê o arquivo de texto
    input_file = sys.argv[1]
    text = read_text_file(input_file)

    # Constrói o modelo de Markov
    model = build_markov_model(text)

    # Gera e exibe 5 sentenças
    sentences = generate_sentence(model, num_sentences=5)
    print("\nSentenças geradas:")
    for i, sentence in enumerate(sentences, 1):
        print(f"{i}: {sentence}")

if __name__ == "__main__":
    main()
