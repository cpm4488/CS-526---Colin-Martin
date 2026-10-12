import sys
from HW2_SinglyLinkedList_Final import SinglyLinkedList as LinkedList

DIRECTIVES = {
    "append":     ["value"],
    "prepend":    ["value"],
    "insert":     ["index", "value"],
    "get":        ["index"],
    "find":       ["value"],
    "len":        [],
    "update":     ["index", "value"],
    "delete":     ["value"],
    "delete_at":  ["index"],
    "print_list": [],
}

def to_value(text):
    try:
        return int(text)
    except ValueError:
        return text

def parse_line(line):
    parts = line.split()
    directive = parts[0]

    if directive not in DIRECTIVES:
        raise ValueError("unknown directive '" + directive + "'")

    kinds = DIRECTIVES[directive]
    if len(parts) - 1 != len(kinds):
        usage = " ".join([directive] + ["<" + kind + ">" for kind in kinds])
        raise ValueError("expected '" + usage + "', got '" + line + "'")

    args = []
    for kind, text in zip(kinds, parts[1:]):
        if kind == "index":
            try:
                args.append(int(text))
            except ValueError:
                raise ValueError("index must be a whole number, got '" + line + "'")
        else:
            args.append(to_value(text))
    return directive, args

def run_directive(my_list, directive, args):
    if directive == "len":
        print("len = " + str(len(my_list)))
        return
    try:
        result = getattr(my_list, directive)(*args)
    except IndexError:
        raise IndexError("index " + str(args[0]) + " out of range")

    if directive in ("get", "find", "delete_at"):
        print(directive + "(" + str(args[0]) + ") = " + str(result))
    elif directive == "delete" and not result:
        raise LookupError(str(args[0]) + " not found, nothing deleted")

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
