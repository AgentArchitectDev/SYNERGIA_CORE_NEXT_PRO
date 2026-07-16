from ai.kernel.kernel import kernel


def main():

    kernel.boot()

    while True:

        cmd = input("\n> ")

        if cmd == "exit":
            break

        result = kernel.execute(cmd)

        print(result)


if __name__ == "__main__":
    main()
