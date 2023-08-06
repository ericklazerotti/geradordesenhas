import random
import string


def gerar_senha(tamanho=12, usa_letras=True, usa_numeros=True, usa_caracteres_especiais=True):
    caracteres = ''
    if usa_letras:
        caracteres += string.ascii_letters
    if usa_numeros:
        caracteres += string.digits
    if usa_caracteres_especiais:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Selecione pelo menos um tipo de caractere para gerar a senha.")

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

    if usa_letras and not any(c.isalpha() for c in senha):
        senha += random.choice(string.ascii_letters)
    if usa_numeros and not any(c.isdigit() for c in senha):
        senha += random.choice(string.digits)
    if usa_caracteres_especiais and not any(c in string.punctuation for c in senha):
        senha += random.choice(string.punctuation)

    senha_embaralhada = ''.join(random.sample(senha, len(senha)))

    return senha_embaralhada


def main():
    print("Gerador de Senhas")
    tamanho_senha = int(input("Digite o tamanho da senha desejada: "))
    usa_letras = input("Incluir letras (s/n)? ").lower() == 's'
    usa_numeros = input("Incluir números (s/n)? ").lower() == 's'
    usa_caracteres_especiais = input("Incluir caracteres especiais (s/n)? ").lower() == 's'

    try:
        senha_gerada = gerar_senha(tamanho_senha, usa_letras, usa_numeros, usa_caracteres_especiais)
        print("Senha gerada:", senha_gerada)
    except ValueError as e:
        print("Erro:", e)


if __name__ == "__main__":
    main()
