import pandas as panda

cell_count_file = panda.read_csv('cell-count.csv')

# Columns with cell population
cell_types = ['b_cell', 'cd8_t_cell', 'cd4_t_cell', 'nk_cell', 'monocyte']

cell_count_file['total_population'] = cell_count_file[cell_types].sum(axis=1)

# Change DataFrame to give each cell type their own row
new_df = cell_count_file.melt(
    id_vars=['sample', 'total_population'],
    value_vars=cell_types,
    var_name='population',
    value_name='count'
)

new_df['percentage'] = (new_df['count'] / new_df['total_population']) * 100

# Reorder columns so they are like the given instructions
finalCSV = new_df[['sample', 'total_population', 'population', 'count', 'percentage']]

finalCSV.to_csv('cell_count_percentages.csv', index=False)