import sys
import os
from cx_Freeze import setup,Executable

files = [''] # pode haver um erro aqui!

target = Executable(
	script="main.py",
	base="Win32GUI"
	
)

setup(
	nome="SINFOR",
	version="1.0",
	description="Vacinação Covid-19",
	author="Eva,Humberto,Vitor,Wendel",
	options={'build.exe': {'include_files': files}},
	executables = [target]

)
