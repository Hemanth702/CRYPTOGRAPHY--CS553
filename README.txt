The main directory contains 4 sub-directories:
	1. termPaper_teamCiphers
	2. Figures
	3. python_implementation
        4. Presentation
	
The sub-directory 'termPaper_teamCiphers' contains files:
	1. termPaper_teamCiphers.tex and termPaper_teamCiphers.pdf
	2. transcrypto.cls
	3. Figures: pride.pdf and structure.pdf
	
	Description of the files:
	1. termPaper_teamCiphers.tex and termPaper_teamCiphers.pdf : Term paper
	2. transcrypto.cls : Template for the paper in 'iacrtans class documentation'
	3. Figures: pride.pdf and structure.pdf - Contains the figures of overall structure and round function of the cipher
	
	
The sub-directory 'Figures' contains files:
	1. pride.tex and pride.pdf
	2. Structure.tex and structure.pdf

	Description of the files:
	1. pride.tex and pride.pdf : Figure of Overall structure of PRIDE cipher 
	2. Structure.tex and structure.pdf : Figure of Round function of PRIDE cipher
	

The sub-directory 'python_implementation' contains python (.py) files:
	1. Utilities.py
	2. RoundFunction.py
	3. PRIDE.py
	4. test.py

	Description of the files:
	1. Utilities.py : Contains the basic details of S-box, Permutation matrix and their corresponding inverses and the functions for the implementation of the same. It also has some basic methods for conversion of data types from int to byte, from byte to str and vice versa. It stores the values of Linear layer matrices like {L_i} and {L_i}^{-1} for i=0,1,2,3

	2. RoundFunction.py : Contains the implementation functions of Round operations of PRIDE cipher. It also includes Key-scheduling, Application of S-Box layer, P layer, L layer and L inverse layer. It uses Utilities class for the implementation of the above said.

	3. PRIDE.py : Contains the PRIDE cipher class and the implementation of Encryption and Decryption functions of the cipher. It uses RoundFunction and Utilities class to implement the same successfully.

	4. test.py : Driver code for testing the cipher. Uses PRIDE class by creating an object of it to work on encryption and decryption.


	Instructions for the execution:
	1. Required modules : binascii
	2. cmd : python3 test.py (or) python test.py based on the versions of python installed in your computer.

	Note: Do not change the files to different directories as it may give errors.


The sub-directory 'Presentation' contains files:
	1. presentation.tex
	2. intro.tex
	3. spec.tex
	4. attack.tex
	5. observe.tex
	6. bpnominate.tex
	7. conclu.tex


Video presentation :
        The drive link for our video presentation: https://drive.google.com/drive/folders/1v8Yyvt1ie97Ndgfk4Yadlo_nTSMEr5gi?usp=sharing
        Please download the whole folder for watching clearly as Google Drive may not allow for clear playing.

