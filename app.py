import pandas as pd
import plotly.express as px
import numpy as np
from datetime import date
from common import dataframe_generation


list_of_keys = list(pd.read_excel('API_keys.xlsx',sheet_name='API_key')['key'].values)

######################################################## UNITED KINGDOM PREPARATION ###############################


df_uk_city = pd.read_excel('elements.xlsx',sheet_name = 'UK')

element_uk = 'listing'
country_uk = 'UK'
columns_uk = ['agent_address',	'agent_logo','agent_name',	'agent_phone',	'agent_postcode','branch_id','brochure','bullet',	'category','company_id',
'country_code','description','details_url','displayable_address','document', 'epc_graph','floor_plan','featured_type','group_id','image_150_113_url','image_354_255_url',
'image_50_38_url',	'image_645_430_url',	'image_80_60_url',	'image_caption',	'image_url','images',	'incode','letting_fees','location_is_approximate','original_image','other_image',	'outcode','premium_listing_highlights',
'property_number','price_modifier','short_description','street_name','thumbnail_url',	'title'] # useless columns. Drop them to get smaller files
url_uk = "https://zoopla.p.rapidapi.com/properties/list"
host_uk = "zoopla.p.rapidapi.com"



######################################################## FRANCE PREPARATION #######################################
df_fr_zip = pd.read_excel('elements.xlsx',sheet_name = 'France')

range_fr = range(len(df_fr_zip))
element_fr = 'items'
country_fr = 'France'
columns_fr=['level','listingType','livingAreaUnit','medias','permalink','photos','polygon','priceAnnuity','priceUnit','priceVariation.status','professional.directoryId','professional.email',
'professional.id',	'professional.isExclusiveness',	'professional.latitude','professional.logoUrl','professional.longitude','professional.name','professional.phoneNumber','professional.publicationId','professional.publisherType','professional.type',
'thirdPartyId','urlVideo']
url_fr = "https://seloger.p.rapidapi.com/properties/list"
host_fr = "seloger.p.rapidapi.com"



######################################################## USA PREPARATION ##########################################
df_usa_city = pd.read_excel('elements.xlsx',sheet_name='USA')

range_usa = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51,53]
element_usa = 'homes'
country_usa = 'USA'
columns_usa = ['homeData.addressInfo.centroid.displayLevel','homeData.addressInfo.formattedStreetLine',	'homeData.addressInfo.location','homeData.addressInfo.countryCode','homeData.addressInfo.locationDisplayLevel','homeData.addressInfo.postalCodeDisplayLevel','homeData.addressInfo.streetlineDisplayLevel','homeData.addressInfo.unitNumber',
'homeData.addressInfo.unitNumberDisplayLevel','homeData.brokers.listingBrokerAndAgent.agentName','homeData.brokers.listingBrokerAndAgent.agentPhone','homeData.brokers.listingBrokerAndAgent.brokerName','homeData.brokers.listingBrokerAndAgent.brokerPhone',
'homeData.brokers.listingBrokerAndAgent.isRedfin','homeData.businessMarketId.value','homeData.dataSourceId.value','homeData.daysOnMarket.displayLevel','homeData.daysOnMarket.listingAddedDate.nanos','homeData.daysOnMarket.listingAddedDate.seconds',
'homeData.daysOnMarket.timeOnRedfin.nanos','homeData.daysOnMarket.timeOnRedfin.seconds','homeData.directAccessInfo.signId','homeData.directAccessInfo.supportPhoneNumber',	'homeData.directAccessInfo.supportedEntryTypes',
'homeData.hoaDues.displayLevel','homeData.directAccessInfo.timeZone.olsonTimeZoneIdString',	'homeData.directAccessInfo.timeZone.timeZoneIdString','homeData.hoaDues.displayLevel',
'homeData.insights.displayLevel','homeData.insights.hasInsight',	'homeData.lastSaleData.lastSoldDate.nanos',	'homeData.lastSaleData.lastSoldDate.seconds',	'homeData.listingDisplayLevel',	'homeData.listingId.value',
'homeData.lotSize.displayLevel','homeData.marketId.value','homeData.mlsId','homeData.mlsStatusId.value','homeData.openHouses','homeData.partialBaths.value',	'homeData.photosInfo.alternatePhotosInfo',	'homeData.photosInfo.photoRanges',
'homeData.photosInfo.posterFrameUrl','homeData.photosInfo.primaryPhotoDisplayLevel','homeData.photosInfo.scanUrl',	'homeData.photosInfo.secondaryPhotoDisplayLevel','homeData.priceInfo.displayLevel',	'homeData.priceInfo.homePrice.displayLevel',
'homeData.priceInfo.homePrice.int64Value','homeData.sashes','homeData.servicePolicyId.value',	'homeData.showMlsId.value','homeData.sqftInfo.displayLevel',	'homeData.timezone','homeData.yearBuilt.displayLevel']
url_usa = "https://unofficial-redfin.p.rapidapi.com/properties/list"
host_usa = "unofficial-redfin.p.rapidapi.com"

####################################################### UNITED KINGDOM EXECUTION ##################################

df_uk = pd.DataFrame()
API_index = 0


for index in range(len(df_uk_city)):
    area = df_uk_city['value'].values[index]
    querystring_uk = {"area":area,"category":"residential","include_retirement_homes":"no","include_shared_accommodation":"no","include_shared_ownership":"no","include_sold":"1","listing_status":"sale","order_by":"age","ordering":"descending","page_number":"1","page_size":"40"}

    result = dataframe_generation(element_uk,country_uk,url_uk,querystring_uk,list_of_keys,host_uk,API_index)
    df_uk_state = result[0]
    API_index = result[1]
    df_uk = pd.concat([df_uk,df_uk_state],ignore_index=True,sort=True)

df_uk = df_uk.drop(columns_uk,axis=1)
df_uk.to_csv(f'{country_uk}_{str(date.today())}.csv')

####################################################### FRANCE EXECUTION ##########################################

df_fr = pd.DataFrame()
API_index = 0


for index in range(len(df_fr_zip)):

    zip_code = df_fr_zip['Index'].values[index]
    querystring_fr = {"zipCodes":str(zip_code),"pageSize":"50","realtyTypes":"1","transactionType":"2","includeNewConstructions":"true"}

    result =  dataframe_generation(element_fr,country_fr,url_fr,querystring_fr,list_of_keys,host_fr,API_index)
    df_fr_state = result[0]
    API_index = result[1]
    df_fr = pd.concat([df_fr,df_fr_state],ignore_index=True,sort=True) 

df_fr = df_fr.drop(columns_fr,axis=1)
df_fr.to_csv(f'{country_fr}_{str(date.today())}.csv')


######################################################## USA EXECUTION############################################

df_usa=pd.DataFrame()

API_index = 0


for state_id in range_usa: # for some reason some states are missing

    querystring_usa = {"region_id":state_id,"region_type":'4',"uipt":"1,2,3,4","status":"9"} # where region_type is state, region_id - first is alabama


    result = dataframe_generation(element_usa,country_usa,url_usa,querystring_usa,list_of_keys,host_usa, API_index)
    df_usa_state = result[0]
    API_index = result[1]
    df_usa = pd.concat([df_usa,df_usa_state],ignore_index=True,sort=True) 


for _,colval in df_usa_city.iteritems(): # separately for texas
    for city_id in colval.values:
        querystring_usa = {"region_id":city_id,"region_type":'6',"uipt":"1,2,3,4","status":"9"}

        result = dataframe_generation(element_usa,country_usa,url_usa,querystring_usa,list_of_keys,host_usa,API_index)
        df_usa_state = result[0]
        API_index = result[1]
        df_usa = pd.concat([df_usa,df_usa_state],ignore_index=True,sort=True) 

df_usa = df_usa.drop(columns_usa,axis=1)
df_usa.to_csv(f'{country_usa}_{str(date.today())}.csv')


# ############################################### IF YOU WANT TO SEE A GRAPH FOR UK AND USA#######################################
# df_uk_graph = df_uk[['latitude','longitude']]
# df_map=pd.read_excel('API_keys.xlsx',sheet_name='map')
# df_graph=pd.DataFrame()
# df_graph['latitude'] = df_usa["homeData.addressInfo.centroid.centroid.latitude"]
# df_graph['longitude'] = df_usa["homeData.addressInfo.centroid.centroid.longitude"]
# df_graph = pd.concat([df_uk_graph,df_graph],ignore_index=True)

# px.set_mapbox_access_token(df_map['key'].values[0])
# fig = px.scatter_mapbox(df_graph, 
#                         lat="latitude", 
#                         lon="longitude",     
#                         color_continuous_scale=px.colors.cyclical.IceFire, 
#                         zoom=3,
#                         title="Observations in USA and UK")
# fig.show()

