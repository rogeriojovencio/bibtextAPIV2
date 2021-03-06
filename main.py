import bibtexparser
import pandas as pd
import json
import yaml
import requests
# Read a yaml file.


def read_yaml(name):
    with open(name+'.yaml') as file:
        try:
            databaseConfig = yaml.safe_load(file)
            return databaseConfig
        except yaml.YAMLError as exc:
            print(exc)

# Read a bibtext file and convert to dataframe.


def read_bib(name):
    print('Loading file/'+name+'.bib file')
    with open('file/'+name+'.bib', encoding='utf-8') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    return pd.DataFrame.from_records(bib_database.entries)


12345678
# Convert a row to xml


def to_xml(row):
    xml = ['<item>']
    for field in row.index:
        xml.append('  <field name="{0}">{1}</field>'.format(field, row[field]))
    xml.append('</item>')
    return '\n'.join(xml)

# Load all bib files and return their concatenation.


def load_bibs():
    iee = read_bib('iee')
    sciencedirect = read_bib('sciencedirect')
    dlacm = read_bib('dlacm')

    # Correct columns position based on pattern.
    columns = ["author", "title", "keywords",
               "abstract", "year", "type_publication", "doi"]
    iee = iee.reindex(columns=columns)
    sciencedirect = sciencedirect.reindex(columns=columns)
    dlacm = dlacm.reindex(columns=columns)

    return pd.concat([iee, sciencedirect, dlacm], ignore_index=True)

# Load all csv files and return theis concatenation.


def load_csvs():
    jcr = pd.read_csv('file/jcr_2020.csv', delimiter=';')
    scimago = pd.read_csv('file/scimagojr_2020.csv',
                          delimiter=';', low_memory=False)

    jcr.rename(columns={'Rank': 'rank', 'Total Cites': 'total_cities',
               'Full Journal Title': 'title', 'Journal Impact Factor': 'jcr_value'}, inplace=True)
    scimago.rename(columns={'Rank': 'rank', 'Title': 'title', 'Total Cites (3years)': 'total_cities',
                   'Type': 'type_publication', "SJR": "scimago_value"}, inplace=True)

    columns = ["rank", "title", "total_cities",
               "type_publication", "jcr_value", "scimago_value"]
    jcr = jcr.reindex(columns=columns)
    scimago = scimago.reindex(columns=columns)

    scimago['scimago_value'] = scimago['scimago_value'].str.replace(',', '.')
    jcr['jcr_value'] = jcr['jcr_value'].str.replace('Not Available', '0')

    return pd.concat([jcr, scimago], ignore_index=True)


def load_apiex():
    print('####################')
    print('####Consulta CEP####')
    print('####################')
    print()

    # cep_input = input("Digite o CEP para consulta:")
    # if len(cep_input) != 8:
    #     print('Quantidade de digitos inv??lidos!')
    #     exit()
    # else:
    #  request = requests.get(
    #     'https://viacep.com.br/ws/{}/json/'.format(cep_input))
    # print(request.json())
    # exit()

    request = requests.get(
        'https://www.sciencedirect.com/search?tak=apple&apiKey=fab175511ea4725a068b2d461a632a5e')
    print(request.pdf())
    exit()


configuration = read_yaml('config')

if (configuration['type'] not in ['json', 'yaml', 'csv', 'xml']):
    print('Invalid value')
   # exit()
else:
    load_apiex()


df_bib = load_bibs()
df_csv = load_csvs()

df_bib['title'] = df_bib['title'].str.upper()
df_csv['title'] = df_csv['title'].str.upper()

df = pd.merge(df_csv, df_bib, on=['title'], how='outer')

df = df.drop_duplicates(subset='title', ignore_index=True)

df['scimago_value'] = pd.to_numeric(df['scimago_value'])
df['jcr_value'] = pd.to_numeric(df['jcr_value'])
# print(df.dtypes)

# Check if there is a filter
key = 'filter'
if key in configuration.keys():
    print('active filter')
    df = df.query(configuration['filter'])

# Generate output file.
if (configuration['type'] == 'json'):
    df.to_json(configuration['file_name'] + '.json', orient='records')

elif (configuration['type'] == 'csv'):
    df.to_csv(configuration['file_name'] + ".csv")

elif (configuration['type'] == 'yaml'):
    # Convert dataframe into json object (easier to convert to yaml)
    data = json.loads(df.to_json(orient='records'))
    with open(configuration['file_name'] + '.yaml', 'w') as yml:
        yaml.dump(data, yml, allow_unicode=False)

elif (configuration['type'] == 'xml'):
    file = open(configuration['file_name'] + ".xml", "w", encoding='UTF-8')
    file.write('\n'.join(df.apply(to_xml, axis=1)),)
    file.close()

else:
    print('Option is not available')
