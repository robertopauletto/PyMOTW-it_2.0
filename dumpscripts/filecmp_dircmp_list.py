import filecmp

dc = filecmp.dircmp('esempio/dir1', 'esempio/dir2')
print 'Left :', dc.left_list
print 'Right:', dc.right_list


