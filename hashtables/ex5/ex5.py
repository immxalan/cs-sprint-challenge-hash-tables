# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []

    directory = dict()

    for file in files:
        parts = file.split("/")
        filename = parts[-1]
        if filename not in directory:
            directory[filename] = []
        directory[filename].append(file)

    for query in queries:
        if query in directory:
            result.extend(directory[query])

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
