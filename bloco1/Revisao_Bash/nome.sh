#!/bin/bash

echo 'Escrave seu nome:'
read nome
if [ "$nome" = 'joao' ]; then
	echo "Bem vindo! Operador"
else
	echo "Ola $nome"
fi
