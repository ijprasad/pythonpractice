Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 27 2018, 03:37:03) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> nums = [39,33,38,89,0]
>>> nums
[39, 33, 38, 89, 0]
>>> nums.append(45)
>>> nums
[39, 33, 38, 89, 0, 45]
>>> nums.remove(0)
>>> nums
[39, 33, 38, 89, 45]
>>> nums.pop(1)
33
>>> nums
[39, 38, 89, 45]
>>> nums.pop()
45
>>> nums
[39, 38, 89]
>>> nums[2:]
[89]
>>> nums
[39, 38, 89]
>>> del nums[2:]
>>> nums
[39, 38]
>>> nums.extend([23, 3,2,5,6,7,88])
>>> nums
[39, 38, 23, 3, 2, 5, 6, 7, 88]
>>> min(nums)
2
>>> max(nums)
88
>>> sum(nums)
211
>>> avg(nums)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    avg(nums)
NameError: name 'avg' is not defined
>>> average(nums)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    average(nums)
NameError: name 'average' is not defined
>>> product(nums)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    product(nums)
NameError: name 'product' is not defined
>>> nums
[39, 38, 23, 3, 2, 5, 6, 7, 88]
>>> 
>>> 
>>> 


>>> 
>>> 


>>> 

>>> 

>>> 

>>> 

>>> nums.sort()
>>> nums
[2, 3, 5, 6, 7, 23, 38, 39, 88]
>>> Traceback (most recent call last):
	
SyntaxError: invalid syntax
>>> 
>>> clear
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> cls
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    cls
NameError: name 'cls' is not defined
>>> clear
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> cl scr
SyntaxError: invalid syntax
>>> clear
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> 
>>> screen_clear()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    screen_clear()
NameError: name 'screen_clear' is not defined
>>> screen_clear
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    screen_clear
NameError: name 'screen_clear' is not defined
>>> File "<pyshell#43>", line 1, in <module>
SyntaxError: invalid syntax
>>> 
>>> clear()
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    clear()
NameError: name 'clear' is not defined
>>> clear
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> cls()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    cls()
NameError: name 'cls' is not defined
>>> NameError: name 'cls' is not defined
SyntaxError: invalid syntax
>>> 
>>> cls
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    cls
NameError: name 'cls' is not defined
>>> quit
Use quit() or Ctrl-Z plus Return to exit
>>> clean
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    clean
NameError: name 'clean' is not defined
>>> python
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    python
NameError: name 'python' is not defined
>>> version
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    version
NameError: name 'version' is not defined
>>> version()
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    version()
NameError: name 'version' is not defined
>>> 
=============================== RESTART: Shell ===============================
>>> 
