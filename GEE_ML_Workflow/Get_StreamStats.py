#!/usr/bin/env python
# coding: utf-8

# In[1]:


import dataretrieval.nwis as nwis
##https://streamstats-python.readthedocs.io/en/latest/gallery_vignettes/plot_get_characteristics.html
import streamstats
import pandas as pd    
from progressbar import ProgressBar


def get_USGS_site_info(site_ids):

    #set up Pandas DF for state streamstats

    Streamstats_cols = ['NWIS_siteid','Lat', 'Long', 'Drainage_area_mi2', 'Mean_Basin_Elev_ft', 'Perc_Forest', 'Perc_Develop',
                     'Perc_Imperv', 'Perc_Herbace', 'Perc_Slop_30', 'Mean_Ann_Precip_in']

    NWIS_Stats = pd.DataFrame(columns = Streamstats_cols)


    print('Calculating NWIS streamflow id characteristics for ', len(site_ids), 'sites')

    pbar = ProgressBar()
    for site in pbar(site_ids):
        print('NWIS site: ', site)
        #try:
        NWISinfo = nwis.get_record(sites=site, service='site')

        lat, lon = NWISinfo['dec_lat_va'][0],NWISinfo['dec_long_va'][0]
        ws = streamstats.Watershed(lat=lat, lon=lon)

        NWISindex = ['NWIS_site_id', 'Lat', 'Long', 'Drainage_area_mi2', 'Mean_Basin_Elev_ft', 'Perc_Forest', 'Perc_Develop',
                     'Perc_Imperv', 'Perc_Herbace', 'Perc_Slop_30', 'Mean_Ann_Precip_in']

        print('Retrieving Drainage Area')
        try:
            darea = ws.get_characteristic('DRNAREA')['value']
        except KeyError:
            darea = np.nan
        except ValueError:
            darea = np.nan

        print('Retrieving Mean Catchment Elevation')
        try:
            elev = ws.get_characteristic('ELEV')['value']
        except KeyError:
            elev = np.nan
        except ValueError:
            elev = np.nan

        print('Retrieving Catchment Land Cover Information')
        try:
            forest = ws.get_characteristic('FOREST')['value']
        except KeyError:
            forest = np.nan
        except ValueError:
            forest = np.nan

        try:
            dev_area = ws.get_characteristic('LC11DEV')['value']
        except KeyError:
            dev_area = np.nan
        except ValueError:
            dev_area = np.nan

        try:
            imp_area = ws.get_characteristic('LC11IMP')['value']
        except KeyError:
            imp_area = np.nan
        except ValueError:
            imp_area = np.nan

        try:
            herb_area = ws.get_characteristic('LU92HRBN')['value']
        except KeyError:
            herb_area = np.nan
        except ValueError:
            herb_area = np.nan

        print('Retrieving Catchment Topographic Complexity')
        try:
            perc_slope = ws.get_characteristic('SLOP30_10M')['value']
        except KeyError:
            perc_slope = np.nan
        except ValueError:
            perc_slope = np.nan

        print('Retrieving Catchment Average Precip')
        try:
            precip = ws.get_characteristic('PRECIP')['value']
        except KeyError:
            precip = np.nan
        except ValueError:
            precip = np.nan


        NWISvalues = [site,
                      lat,
                      lon,
                      darea, 
                      elev,forest, 
                      dev_area,
                      imp_area, 
                      herb_area,
                      perc_slope,
                      precip]

        print(NWISvalues)
        Catchment_Stats = pd.DataFrame(data = NWISvalues, index = NWISindex).T

        NWIS_Stats = NWIS_Stats.append(Catchment_Stats)

    #except:
     #   print('Taking three minute break to prevent the blocking of IP Address') 
      #  time.sleep(181)


    colorder =['NWIS_site_id', 'Lat', 'Long', 'Drainage_area_mi2', 'Mean_Basin_Elev_ft', 'Perc_Forest', 
               'Perc_Develop','Perc_Imperv', 'Perc_Herbace', 'Perc_Slop_30', 'Mean_Ann_Precip_in']



    NWIS_Stats = NWIS_Stats[colorder]

    NWIS_Stats.reset_index(drop = True, inplace = True)
    
    return NWIS_Stats


# In[ ]:




