import sys
import nbformat as nbf

filename = sys.argv[1]
ntbk = nbf.read(filename, nbf.NO_CONVERT)

keep_cells = []

for cell in ntbk.cells:
    # normalize source to string (nbformat v4+ uses list of strings)
    source = cell['source']
    if isinstance(source, list):
        source_str = ''.join(source)
    else:
        source_str = source
    
    # skip empty cells
    if len(source_str) == 0:
        continue

    # remove solutions
    if cell['cell_type'] == 'code':
        if source_str.startswith('# Solution'):
            continue

        # remove the output of code cells
        cell['outputs'] = []

    keep_cells.append(cell)

print('Removing solutions from', filename)

ntbk.cells = keep_cells
nbf.write(ntbk, filename)
