def read_flie(filename):
	with open(filename,'r',encoding = 'utf-8-sig') as f:
		lines = []
		for line in f:
			lines.append(line.strip())
	return lines

def covert(lines):
	new = []
	
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		new.append(person+':'+line)	
	return new
def write_file(filename,lines):
	with open(filename,'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_flie('input.txt')
	lines = covert(lines)
	write_file('output.txt',lines)
main()