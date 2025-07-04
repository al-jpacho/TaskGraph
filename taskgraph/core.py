def parse_dependencies(line: str):
    """
    Parse a task dependency chain from a single line of input.
    Splits by '->' to extract parent, child pairs.
    Single task return (parent, None) tuples.

    Args:
        line (str): ` _description_

    Returns:
        _type_: _description_
    """
    tokens = [t.strip() for t in line.split("->")]

    if len(tokens) < 2: 
        return [(tokens[0], None)]

    pairs = []
    for i in range(len(tokens) - 1):
        parent = tokens[i]
        child = tokens[i + 1]
        pairs.append((parent, child))

    return pairs