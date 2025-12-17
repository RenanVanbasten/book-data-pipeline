import requests
import pandas as pd
import time
import os

def extrair_livros_completo(tema, total_livros=200):
    os.makedirs("data/raw", exist_ok=True)
    
    livros_total = []
     
    for start_index in range(0, total_livros, 40):
        
        url = f"https://www.googleapis.com/books/v1/volumes?q={tema}&startIndex={start_index}&maxResults={40}"
        
        try:
            response = requests.get(url)
            dados = response.json()
            items = dados.get('items', [])
            
            if not items:
                break
                
            for item in items:
                info = item.get('volumeInfo', {})
                venda = item.get('saleInfo', {})
                lista_preço = venda.get('listPrice', {})
                
                livro = {
                    'title': info.get('title'),
                    'authors': info.get('authors', ['Desconhecido']),
                    'categories': info.get('categories', ['Outros']),
                    'averageRating': info.get('averageRating', 0),
                    'ratingsCount': info.get('ratingsCount', 0),
                    'pageCount': info.get('pageCount', 0),
                    'publishedDate': info.get('publishedDate', 'N/A'),
                    'description': info.get('description', 'Sem descrição'),
                    'price': lista_preço.get('amount', 0),
                    'currency': lista_preço.get('currencyCode', 'N/A'),
                    'isEbook': venda.get('isEbook', False)
                }
                livros_total.append(livro)
            
            time.sleep(1.5)
            
        except Exception as e:
            print(f"Erro no índice {start_index}: {e}")
            break
            
    df = pd.DataFrame(livros_total)
    df.to_csv("data/raw/livros_brutos.csv", index=False)
    print(f"Processo finalizado. {len(df)} livros salvos em data/raw/livros_brutos.csv")
    return df

df_raw = extrair_livros_completo("data engineering")
