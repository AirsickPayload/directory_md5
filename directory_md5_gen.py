#===============================================================================
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#===============================================================================
import os
import sys
import hashlib

filepath = os.path.dirname(os.path.realpath(__file__))
file=open('%s' % os.path.join(filepath,'MD5GEN_LIST.txt'),'w+')
buffersize = 4096

def hashP(plik):
	MD5 = hashlib.md5()
	pl = open(plik,'rb')
	while True:
		buffer = pl.read(buffersize)
		if not buffer:
			break
		MD5.update(buffer)
	return(MD5.hexdigest())
	
def hash(text):
	MD5 = hashlib.md5()
	MD5.update(text.encode('utf-8'))
	return(MD5.hexdigest())
	
def lista_dir(path):
	lista=list()
	for f in os.listdir(path):
		if os.path.isdir(os.path.join(path,f)):
			lista.append(os.path.join(path,f))
	return lista

def lista_plikow(path):
	lista=list()
	for f in os.listdir(path): 
		if os.path.isfile(os.path.join(path, f)):
			lista.append(os.path.join(path,f))
	return lista
	
def znajdz(path,file):
	l = lista_dir(path)
	for f in range(0,len(lista_plikow(path))):
		file.write('%s -> %s\n' % (lista_plikow(path)[f], hashP(lista_plikow(path)[f])))
		file.flush()
	if len(l) > 0:
		for x in range(0,len(l)):
			znajdz(l[x],file)
		
def main():
	try:
		sys.argv[1]
		print(hash(sys.argv[1]))
	except(IndexError):
		znajdz(filepath,file)
		
main()
	