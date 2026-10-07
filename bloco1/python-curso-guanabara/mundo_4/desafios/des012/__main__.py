from rpg import *
from rich import inspect
def main():
    p1 = Guerreiro('Pikachu', 1000)
    p2 = Mago('Gandolf', 2000)

    p1.atacar(p2, 200)
    p2.atacar(p1, 200)
    p1.curar()
    p2.atacar(p1, 20)

if __name__ == '__main__':
    main()