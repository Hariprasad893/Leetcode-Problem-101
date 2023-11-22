class Solution:
  def isMirror(self,p1,p2):
    '''This helper function to check if tree is symmetric tree or not'''
    # if both the pointers are pointing to None
    if p1==None and p2==None:
      return True
    # if either one of the pointers is pointing to None
    if p1==None or p2==None:
      return False
    # if neither are none
    return (p1.val==p2.val
            and self.isMirror(p1.left,p2.right)
            and self.isMirror(p1.right,p2.left)
           )
  def isSymmetric(self, root):
    # calling the helper function
    ans = self.isMirror(root,root)
    return ans
