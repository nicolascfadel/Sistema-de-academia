import json
import os
from typing import Any, Dict

CAMINHO_ARQUIVO = "banco_dados.json"

def inicializar_arquivo(caminho: str) -> None:
    """Cria o arquivo JSON com estrutura padrão, se não existir."""
    estrutura_base = {"exercicios": [], "treinos": []}
    os.makedirs(os.path.dirname(caminho) or ".", exist_ok=True) 
    if not os.path.exists(caminho):
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(estrutura_base, f, indent=4, ensure_ascii=False)


def carregar_dados(caminho: str = CAMINHO_ARQUIVO) -> Dict[str, Any]:
    """Carrega o conteúdo do arquivo JSON. Cria o arquivo se não existir."""
    inicializar_arquivo(caminho)
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)
            if not isinstance(dados, dict):
                raise ValueError("Formato inválido de JSON.")
            dados.setdefault("exercicios", [])
            dados.setdefault("treinos", [])
            return dados
    except (json.JSONDecodeError, ValueError):
        inicializar_arquivo(caminho)
        return {"exercicios": [], "treinos": []}


def salvar_dados(caminho: str, dados: Dict[str, Any]) -> None:
    """Salva os dados em formato JSON, garantindo estrutura válida."""
    os.makedirs(os.path.dirname(caminho) or ".", exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
