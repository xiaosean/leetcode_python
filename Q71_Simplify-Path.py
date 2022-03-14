class Solution:
    def simplifyPath(self, path: str) -> str:
        path_stack = []
        paths = path.split('/')
        for dir_ in paths:
            if dir_ in ["", "."]:
                continue
            elif dir_ == "..":
                if path_stack:
                    path_stack.pop()
            else:
                path_stack += [dir_]
        return "/" + "/".join(path_stack)
            