import argparse


def main(args):
    problem = getattr(__import__(f"day_{args.day}", fromlist=["main"]), "main")
    problem(data_file=f"data/day_{args.day}.txt", verbose=args.verbose)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--day", "-d", help="problem day", required=True)
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()

    main(args)
