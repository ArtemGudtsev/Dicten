import sys
import action
import argument
import action_factory

if __name__ == '__main__':
    print("+-----------------------------------------+")
    print("|                                         |")
    print("|                Dicten                   |")
    print("|       Dictionary based crypto tool.     |")
    print("|                                         |")
    print("+-----------------------------------------+")
    print("\n")

    if len(sys.argv) < 2:
        print('Error! Please provide at least one argument, use --help in case of concerns.')
        exit(1)

    actions = action_factory.build_actions()

