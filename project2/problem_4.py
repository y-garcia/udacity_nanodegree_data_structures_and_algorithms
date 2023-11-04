class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user is None or group is None:
        return None

    if user in group.get_users():
        return True

    for child_group in group.get_groups():
        if is_user_in_group(user, child_group):
            return True

    return False


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values


# Test Case 1
print("\n1. Test main functionality")

parent = Group("parent")
child = Group("child")
sub_child = Group("sub_child")

parent_user = "parent_user"
child_user = "child_user"
sub_child_user = "sub_child_user"

parent.add_group(child)
child.add_group(sub_child)

parent.add_user(parent_user)
child.add_user(child_user)
sub_child.add_user(sub_child_user)

print("User 'parent_user':")
assert is_user_in_group(parent_user, parent) is True
print("  - is in group 'parent'")
assert is_user_in_group(parent_user, child) is False
print("  - is not in group 'child'")
assert is_user_in_group(parent_user, sub_child) is False
print("  - is not in group 'sub_child'")

print("User 'child_user':")
assert is_user_in_group(child_user, parent) is True
print("  - is in group 'parent'")
assert is_user_in_group(child_user, child) is True
print("  - is in group 'child'")
assert is_user_in_group(child_user, sub_child) is False
print("  - is not in group 'sub_child'")

print("User 'sub_child_user':")
assert is_user_in_group(sub_child_user, parent) is True
print("  - is in group 'parent'")
assert is_user_in_group(sub_child_user, child) is True
print("  - is in group 'child'")
assert is_user_in_group(sub_child_user, sub_child) is True
print("  - is in group 'sub_child'")

# Test Case 2
print("\n2. Return None if user or group is None")

assert is_user_in_group(None, parent) is None
print("is_user_in_group(None, parent) ==", is_user_in_group(None, parent))

assert is_user_in_group(parent_user, None) is None
print("is_user_in_group(parent_user, None) ==", is_user_in_group(parent_user, None))

# Test Case 3
print("\n2. Return False if group is empty")

empty_group = Group("empty_group")
assert is_user_in_group("any_user", empty_group) is False
print("is_user_in_group('any_user', empty_group) == ", is_user_in_group("any_user", empty_group))
