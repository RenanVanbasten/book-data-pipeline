import pandas as pd
import ast
import os

def transformar_dados():
    input_path = "data/raw/livros_brutos.csv"
    output_folder = "data/processed"
    output_path = f"{output_folder}/livros_limpos.csv"

    os.makedirs(output_folder, exist_ok=True)

    if not os.path.exists(input_path):
        return
    
    df = pd.read_csv(input_path)

    def extrair_primeiro_item(texto):
        try:
            lista = ast.literal_eval(texto)
            return lista[0] if isinstance(lista, list) and len(lista) > 0 else "Outros"
        except:
            return "Outros"

    df['authors'] = df['authors'].apply(extrair_primeiro_item)
    df['categories'] = df['categories'].apply(extrair_primeiro_item)

    df['published_year'] = df['publishedDate'].str[:4]

    df['book_size'] = pd.cut(
        df['pageCount'],
        bins=[0, 200, 400, float('inf')],
        labels=["short", "medium", "long"]
    )

    df.to_csv(output_path, index=False)
    print(f"Transformação concluída! Arquivo salvo em: {output_path}")

if __name__ == "__main__":
    transformar_dados()