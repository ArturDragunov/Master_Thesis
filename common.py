import requests
import pandas as pd


def get_estated_detail(url,querystring, key,host):
    """
    url - API url
    querystring - conditions
    key - API key
    host - API host
    """
    url = url

    querystring = querystring
    headers = {
      "X-RapidAPI-Key": key,
      "X-RapidAPI-Host": host
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    

    return response


def dataframe_generation(element,country,url,querystring,keys,host,API_index):
  """
  Trigger API and get a df
  element - value to move from json format
  country - UK, France, USA
  url, querystring, key, host are related to get_estated_detail function
  API_index - counter of API key's sequence number
  """
  key = keys[API_index]
  API_index = API_index
  try:
    response = get_estated_detail(url,querystring,key,host)
    if response.status_code == 429: # run out of quota. Need to change API key
      print(querystring)
      API_index +=1
      for i in keys[API_index:]:
        if API_index == 5:
            print(f'YOU RAN OUT OF ALL QUOTAS FOR {country}, see {querystring}')
            result = [pd.DataFrame(),API_index]
            break
        else:
          key = keys[i]
          response = get_estated_detail(url,querystring,key,host)
          if response.status_code != 429:
            break
    response_json = response.json()
    if len(response_json):
        df_state = pd.json_normalize(data=response_json[element])
        df_state['date_of_data_generation'] = pd.to_datetime('today',format='%Y-%m-%d')
        df_state['date_of_data_generation'] = pd.to_datetime(df_state['date_of_data_generation']).dt.normalize()
        df_state['country']=country
        result = [df_state,API_index]
  except:
    print(querystring)
    result = [pd.DataFrame(),API_index]
  return result