import sys

def main():
    try:
        print(f"number divide by zero :  {1/0}" )
    except ZeroDivisionError as err:
        print(f"ZeroDivisionError : {err.args}", file=sys.stderr)
    except BaseException as err:
        print(f"BaseException : {err}", file=sys.stderr)
    else:
        print(f"try else block ")
    finally:
        print(f"try finally block")

    return None

if __name__ == "__main__":
    main()
    sys.exit(0)