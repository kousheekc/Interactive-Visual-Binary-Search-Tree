from ui.interface import Interface
from core.bst import BST

def main():
    bst = BST()
    interface = Interface(bst)

    loop_active = True

    while loop_active:
        interface.update()


if __name__ == '__main__':
    main()