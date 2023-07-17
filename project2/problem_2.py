import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if suffix is None or suffix == "":
        print("Suffix must not be empty. Aborting...")
        return []

    if path is None or not os.path.exists(path):
        print(f"Path '{path}' does not exist. Aborting...")
        return []

    items = os.listdir(path)

    c_files = []

    for item in items:
        child = os.path.join(path, item)

        if os.path.isfile(child) and item.endswith(suffix):
            c_files.append(child)

        elif os.path.isdir(child):
            c_files.extend(find_files(suffix, child))

    return c_files


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
print("1. Test main functionality (find all '.c' files under 'testdir')")

result = find_files(".c", "testdir")
print(result)

assert result == ['testdir\\subdir1\\a.c', 'testdir\\subdir3\\subsubdir1\\b.c', 'testdir\\subdir5\\a.c', 'testdir\\t1.c']

# Test Case 2
print("\n2. Return empty result if suffix is empty or path does not exist")

result = find_files("", "testdir")
print(result)
assert result == []

result = find_files(".c", "dummy")
print(result)
assert result == []

# Test Case 3
print("\n3. Return empty result if suffix or path is None")
result = find_files(None, "testdir")
print(result)
assert result == []

result = find_files(".c", None)
print(result)
assert result == []
