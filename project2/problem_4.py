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
    if user in group.get_users():
        print(f"User '{user}' is in group '{group.get_name()}'")
        return True

    for child_group in group.get_groups():
        if is_user_in_group(user, child_group):
            print(f"User '{user}' is in group '{group.get_name()}'")
            return True

    print(f"User '{user}' is not in group '{group.get_name()}'")
    return False


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values


# Test Case 1
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

assert is_user_in_group(parent_user, parent) is True
assert is_user_in_group(parent_user, child) is False
assert is_user_in_group(parent_user, sub_child) is False

assert is_user_in_group(child_user, parent) is True
assert is_user_in_group(child_user, child) is True
assert is_user_in_group(child_user, sub_child) is False

assert is_user_in_group(sub_child_user, parent) is True
assert is_user_in_group(sub_child_user, child) is True
assert is_user_in_group(sub_child_user, sub_child) is True
# Test Case 2

# Test Case 3
