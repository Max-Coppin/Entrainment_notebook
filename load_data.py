# load_data.py
import xarray as xr

class Data:
    def __init__(self):
        self.data = {}

    def load_data(self, exp_id, instrument, file_path):
        if exp_id not in self.data:
            self.data[exp_id] = {}
        self.data[exp_id][instrument] = xr.open_dataset(file_path)

    def get_data(self, exp_id, instrument):
        return self.data.get(exp_id, {}).get(instrument, None)

    def get_variable(self, exp_id, instrument, variable):
        dataset = self.get_data(exp_id, instrument)
        if dataset is not None:
            if variable in dataset.variables:
                return dataset[variable]
            else:
                print(f"La variable '{variable}' n'existe pas dans le jeu de données.")
                print(f"Variables disponibles : {list(dataset.variables)}")
                return None
        else:
            print(f"Aucun jeu de données trouvé pour l'expérience '{exp_id}' et l'instrument '{instrument}'.")
            return None

    def get_available_variables(self, exp_id, instrument):
        dataset = self.get_data(exp_id, instrument)
        if dataset is not None:
            return list(dataset.data_vars.keys())
        else:
            return None




# Initialiser le gestionnaire de données et charger les fichiers
data = Data()

folder = '/Volumes/Data/data_KP/'
data_type_Stereo = 'Stereo_KP/'
data_type_Jai = 'PIV_JAI_KP/'
data_type_lab ='labview_KP/'
data_type_ADV = 'ADV_KP/'
data_type_Probe = 'ProbeT_KP/'


#_______________________________________________________________________________
# Import EXP02
data.load_data('EXP02', 'ADV', folder    + data_type_ADV +'EXP02_ADV.nc')
#data.load_data('EXP02', 'LAB', folder    + data_type_lab +'EXP02_lab.nc')
#data.load_data('EXP02', 'JAI', folder    + data_type_Jai +'EXP02_Jai.nc')
#data.load_data('EXP02', 'PROBE_T', folder    + data_type_Probe +'EXP02_T.nc')

#_______________________________________________________________________________
# Import EXP03
data.load_data('EXP03', 'ADV', folder    + data_type_ADV +'EXP03_ADV.nc')
#data.load_data('EXP03', 'LAB', folder    + data_type_lab +'EXP03_lab.nc')
#data.load_data('EXP03', 'JAI', folder    + data_type_Jai +'EXP03_Jai.nc')
#data.load_data('EXP03', 'PROBE_T', folder    + data_type_Probe +'EXP03_T.nc')

#_______________________________________________________________________________
# Import EXP04
data.load_data('EXP04', 'ADV', folder    + data_type_ADV +'EXP04_ADV.nc')
#data.load_data('EXP04', 'LAB', folder    + data_type_lab +'EXP04_lab.nc')
data.load_data('EXP04', 'JAI', folder    + data_type_Jai +'EXP04_Jai.nc')
#data.load_data('EXP04', 'PROBE_T', folder    + data_type_Probe +'EXP04_T.nc')

#_______________________________________________________________________________
# Import EXP05
data.load_data('EXP05', 'ADV', folder    + data_type_ADV +'EXP05_ADV.nc')
data.load_data('EXP05', 'LAB', folder    + data_type_lab +'EXP05_lab.nc')
#data.load_data('EXP05', 'JAI', folder    + data_type_Jai +'EXP05_Jai.nc')
#data.load_data('EXP05', 'PROBE_T', folder    + data_type_Probe +'EXP05_T.nc')

#_______________________________________________________________________________
# Import EXP06
data.load_data('EXP06', 'ADV', folder    + data_type_ADV +'EXP06_ADV.nc')
data.load_data('EXP06', 'LAB', folder    + data_type_lab +'EXP06_lab.nc')
data.load_data('EXP06', 'JAI', folder    + data_type_Jai +'EXP06_Jai.nc')
#data.load_data('EXP06', 'PROBE_T', folder    + data_type_Probe +'EXP06_T.nc')

#_______________________________________________________________________________
# Import EXP07
data.load_data('EXP07', 'ADV', folder    + data_type_ADV +'EXP07_ADV.nc')
data.load_data('EXP07', 'LAB', folder    + data_type_lab +'EXP07_lab.nc')
data.load_data('EXP07', 'JAI', folder    + data_type_Jai +'EXP07_Jai.nc')
#data.load_data('EXP07', 'PROBE_T', folder    + data_type_Probe +'EXP07_T.nc')

#_______________________________________________________________________________
# Import EXP08
data.load_data('EXP08', 'ADV', folder    + data_type_ADV +'EXP08_ADV.nc')
data.load_data('EXP08', 'LAB', folder    + data_type_lab +'EXP08_lab.nc')
data.load_data('EXP08', 'JAI', folder    + data_type_Jai +'EXP08_Jai.nc')
#data.load_data('EXP08', 'PROBE_T', folder    + data_type_Probe +'EXP08_T.nc')

#_______________________________________________________________________________
# Import EXP09
data.load_data('EXP09', 'ADV', folder    + data_type_ADV +'EXP09_ADV.nc')
data.load_data('EXP09', 'LAB', folder    + data_type_lab +'EXP09_lab.nc')
data.load_data('EXP09', 'JAI', folder    + data_type_Jai +'EXP09_Jai.nc')
#data.load_data('EXP09', 'PROBE_T', folder    + data_type_Probe +'EXP09_T.nc')

#_______________________________________________________________________________
# Import EXP10
data.load_data('EXP10', 'ADV', folder    + data_type_ADV +'EXP10_ADV.nc')
data.load_data('EXP10', 'LAB', folder    + data_type_lab +'EXP10_lab.nc')
data.load_data('EXP10', 'JAI', folder    + data_type_Jai +'EXP10_Jai.nc')
#data.load_data('EXP10', 'PROBE_T', folder    + data_type_Probe +'EXP10_T.nc')

#_______________________________________________________________________________
# Import EXP11
data.load_data('EXP11', 'ADV', folder    + data_type_ADV +'EXP11_ADV.nc')
#data.load_data('EXP11', 'LAB', folder    + data_type_lab +'EXP11_lab.nc')
#data.load_data('EXP11', 'JAI', folder    + data_type_Jai +'EXP11_Jai.nc')
#data.load_data('EXP11', 'PROBE_T', folder    + data_type_Probe +'EXP11_T.nc')

#les donnée STEREO ne sont mises en place qu'a partir des exp12

#_______________________________________________________________________________
# Import EXP12
data.load_data('EXP12', 'STEREO', folder + data_type_Stereo +'EXP12_STEREO.nc')
#data.load_data('EXP12', 'ADV', folder    + data_type_ADV +'EXP12_ADV.nc')
data.load_data('EXP12', 'LAB', folder    + data_type_lab +'EXP12_lab.nc')
#data.load_data('EXP12', 'JAI', folder    + data_type_Jai +'EXP12_Jai.nc')
#data.load_data('EXP12', 'PROBE_T', folder    + data_type_Probe +'EXP12_T.nc')


#_______________________________________________________________________________
# Import EXP13
data.load_data('EXP13', 'STEREO', folder + data_type_Stereo +'EXP13_STEREO.nc')
data.load_data('EXP13', 'ADV', folder    + data_type_ADV +'EXP13_ADV.nc')
data.load_data('EXP13', 'LAB', folder    + data_type_lab +'EXP13_lab.nc')
data.load_data('EXP13', 'JAI', folder    + data_type_Jai +'EXP13_Jai.nc')
#data.load_data('EXP13', 'PROBE_T', folder    + data_type_Probe +'EXP13_T.nc')


#_______________________________________________________________________________
# Import EXP14
data.load_data('EXP14', 'STEREO', folder + data_type_Stereo +'EXP14_STEREO.nc')
data.load_data('EXP14', 'ADV', folder    + data_type_ADV +'EXP14_ADV.nc')
data.load_data('EXP14', 'LAB', folder    + data_type_lab +'EXP14_lab.nc')
#data.load_data('EXP14', 'JAI', folder    + data_type_Jai +'EXP14_Jai.nc')
#data.load_data('EXP14', 'PROBE_T', folder    + data_type_Probe +'EXP14_T.nc')

#_______________________________________________________________________________
# Import EXP15
data.load_data('EXP15', 'STEREO', folder + data_type_Stereo +'EXP15_STEREO.nc')
data.load_data('EXP15', 'ADV', folder    + data_type_ADV +'EXP15_ADV.nc')
data.load_data('EXP15', 'LAB', folder    + data_type_lab +'EXP15_lab.nc')
#data.load_data('EXP15', 'JAI', folder    + data_type_Jai +'EXP15_Jai.nc')
#data.load_data('EXP15', 'PROBE_T', folder    + data_type_Probe +'EXP15_T.nc')

#_______________________________________________________________________________
# Import EXP16
data.load_data('EXP16', 'STEREO', folder + data_type_Stereo +'EXP16_STEREO.nc')
data.load_data('EXP16', 'ADV', folder    + data_type_ADV +'EXP16_ADV.nc')
data.load_data('EXP16', 'LAB', folder    + data_type_lab +'EXP16_lab.nc')
#data.load_data('EXP16', 'JAI', folder    + data_type_Jai +'EXP16_Jai.nc')
#data.load_data('EXP16', 'PROBE_T', folder    + data_type_Probe +'EXP16_T.nc')

#_______________________________________________________________________________
# Import EXP17
#data.load_data('EXP17', 'STEREO', folder + data_type_Stereo +'EXP17_STEREO.nc')
data.load_data('EXP17', 'ADV', folder    + data_type_ADV +'EXP17_ADV.nc')
#data.load_data('EXP17', 'LAB', folder    + data_type_lab +'EXP17_lab.nc')
#data.load_data('EXP17', 'JAI', folder    + data_type_Jai +'EXP17_Jai.nc')
#data.load_data('EXP17', 'PROBE_T', folder    + data_type_Probe +'EXP17_T.nc')

# Exporter le gestionnaire de données pour utilisation ultérieure
import sys
sys.modules[__name__] = data
