import os
import pandas as pd

dataframe = pd.DataFrame(
    columns=['timestamp', 'carbon_intensity', 'low_emissions', 'renewable_emissions', 'total_production',
             'total_emissions'
        , 'nucleare_installed_capacity', 'nucleare_production', 'nucleare_emissions',
             'geotermico_installed_capacity', 'geotermico_production', 'geotermico_emissions'
        , 'biomassa_installed_capacity', 'biomassa_production', 'biomassa_emissions', 'carbone_installed_capacity',
             'carbone_production', 'carbone_emissions'
        , 'eolico_installed_capacity', 'eolico_production', 'eolico_emissions', 'fotovoltaico_installed_capacity',
             'fotovoltaico_production', 'fotovoltaico_emissions'
        , 'idroelettrico_installed_capacity', 'idroelettrico_production', 'idroelettrico_emissions',
             'accumuloidro_installed_capacity', 'accumuloidro_production', 'accumuloidro_emissions'
        , 'batterieaccu_installed_capacity', 'batterieaccu_production', 'batterieaccu_emissions',
             'gas_installed_capacity', 'gas_production', 'gas_emissions'
        , 'petrolio_installed_capacity', 'petrolio_production', 'petrolio_emissions',
             'sconosciuto_installed_capacity', 'sconosciuto_production', 'sconosciuto_emissions'
        , 'exchange_export', 'exchange_import'])

if __name__ == '__main__':

    path1 ='C:/workSpacepy/BigData/states/'
    path2 ='C:/workSpacepy/BigData/states/'

    path3='C:/workSpacepy/json/filefinali/'
    files = os.listdir(path1)
    print(files)

    for file in files:
        s=file
        print(s)
        #df = pd.DataFrame(columns=dataframe.columns)


        df = pd.read_excel(path1 + s)
        df = pd.concat([df,pd.read_excel(path2 + s)], ignore_index=True)
        #print(df)

        try :
            if (len(s) <= 30) :

                df.to_excel(path3 + s, sheet_name=s, index=False)
            else :
                s1 = s.split(" ")[0]
                df.to_excel(path3 + s, sheet_name=s1, index=False)

        except Exception as e :
            pass