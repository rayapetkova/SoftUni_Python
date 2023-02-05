def find_version(version):
    version_num = int("".join(version))
    new_version_num = str(version_num + 1)
    result = ".".join(new_version_num)
    return result


current_version = input().split(".")
print(find_version(current_version))
