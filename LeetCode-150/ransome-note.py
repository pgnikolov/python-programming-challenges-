# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         note_list = [el for el in ransomNote]
#         magazine_list = [el for el in magazine]
#         for char in magazine_list:
#             if not note_list:
#                 break
#             elif char in note_list:
#                 note_list.remove(char)
#         if len(note_list) == 0:
#             return True
#         else:
#             return False
#
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for c in ransomNote:
            if c in magazine:
                magazine = magazine.replace(c, '', 1)
            else:
                return False
        return True
