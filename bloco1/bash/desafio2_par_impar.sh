echo 'Bem vindo ao par e impar!'
echo "Vamos escolha um numero!!"
read numero
echo "Exclente escolha pelo numero $numero"


if [ $((numero % 2)) = 0 ]; then
	echo 'NUMERO PAR'

else
	echo "Numero impar"
fi
