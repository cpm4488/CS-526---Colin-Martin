import sys

from problem4_FINAL import Q4_DoublyLinkedList as LinkedList

ONE_VALUE = ("add", "delete", "exists", "count")
NO_VALUE = ("total", "sum_middle_three", "median", "print_list")


def to_number(text, line):
    try:
        return int(text)
    except ValueError:
        pass
    try:
        return float(text)
    except ValueError:
        raise ValueError("value must be a number, got '" + line + "'")


def parse_line(line):
    parts = line.split()
    directive = parts[0].lower()
    if directive in ONE_VALUE:
        usage = directive + " <value>"
    elif directive in NO_VALUE:
        usage = directive
    else:
        raise ValueError("unknown directive '" + parts[0] + "'")
    if len(parts) != len(usage.split()):
        raise ValueError("expected '" + usage + "', got '" + line + "'")
    return directive, [to_number(text, line) for text in parts[1:]]


def run_directive(my_list, directive, args):
    result = getattr(my_list, directive)(*args)
    if directive == "delete" and not result:
        raise LookupError(str(args[0]) + " not found, nothing deleted")
    if directive in ("add", "delete"):
        print(directive + "(" + str(args[0]) + ")")
    elif directive in ("exists", "count"):
        print(directive + "(" + str(args[0]) + ") = " + str(result))
    elif directive != "print_list":
        print(directive + " = " + str(result))


def main():
    my_list = LinkedList()
    for line_number, line in enumerate(sys.stdin, start=1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            directive, args = parse_line(line)
            run_directive(my_list, directive, args)
        except (ValueError, LookupError) as error:
            print("line " + str(line_number) + ": " + str(error))
    print("Final list: ", end="")
    my_list.print_list()


if __name__ == "__main__":
    main()
