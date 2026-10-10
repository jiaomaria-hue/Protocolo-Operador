# Comandos Bash — Referência

## Variável e leitura de usuário
read nome          # guarda input em "nome"
echo "$nome"        # usa aspas duplas pra interpretar variável

## Condicional
if [ "$var" = "valor" ]; then
    comando
else
    comando
fi

## Operador de módulo (resto da divisão)
$((numero % 2))     # usado pra par/ímpar
