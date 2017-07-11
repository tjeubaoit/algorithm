Suppose we abstract our file system by a string in the following manner:




The string "root/subdir1/./subdir2/file.ext" represents:




root
  subdir1
  subdir2
    file.ext




The directory root contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.




The expression "subdir1/./subdir2" means subdir2 is at the same directory with subdir1 rather than nesting under subdir1.





The string "root/subdir1/file1.ext/./subsubdir1/../subdir2/subsubdir2/file2.ext/./file3.txt" represents:




root
  subdir1
    file1.ext
    subsubdir1
  subdir2
    subsubdir2
      file2.ext
      file3.txt
The directory root contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing two files file2.ext and file3.txt.




The expression "subsubdir1/../subdir2" means subdir2 is at the parent folder of subsubdir1




We are interestd in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "root/subdir2/subsubdir2/file3.txt", and its length is 34.




Given a string representing the file system in the above format, return the length of the longest absolute path to file in the abstracted file system. If there is no file in the system, return 0. If there are more than two files have same length, output the last file on the system. On the example above, file2.ext and file3.txt have same length, so the file3.txt is the answer.




Note:
The name of a file contains at least a . and an extension.
The name of a directory or sub-directory will not contain a ..