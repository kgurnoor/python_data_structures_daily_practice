class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        note,mag = Counter(ransomNote), Counter(magazine)
        if note & mag == note: return True
        return False
