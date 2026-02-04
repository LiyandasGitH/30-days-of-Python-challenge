def all_unique(items):
        """Return True if all items in the list are unique."""
        # item = ""
        # for char in items:
        #     if char.lower() not in item:
        #         item += char
        #     else:
        #         return False
        # return True
        return len(items) == len(set(items))
print(all_unique([1,1,2]))