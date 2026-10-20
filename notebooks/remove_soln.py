import sys
import nbformat as nbf

filename = sys.argv[1]
ntbk = nbf.read(filename, nbf.NO_CONVERT)

keep_cells = []

colab = '[Click here to run this notebook on Colab]'

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

    # point the Colab link at this version
    if cell['cell_type'] == 'markdown' and source_str.startswith(colab):
        url = source_str.split('. For the exercises')[0]
        cell['source'] = url.replace('/solutions/', '/notebooks/')

    # remove solutions
    if cell['cell_type'] == 'code':
        if source_str.startswith('# Solution'):
            continue

        # remove the output of code cells
        cell['outputs'] = []

    # remove execution timing (from nbconvert)
    cell['metadata'].pop('execution', None)

    keep_cells.append(cell)

print('Removing solutions from', filename)

ntbk.cells = keep_cells
nbf.write(ntbk, filename)
