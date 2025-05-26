```python
import pandas as pd
import numpy as np


```


```python
social_data=pd.read_csv(r'C:\DataScience\DATA\Social Media Engagement Dataset.csv')
```


```python
social_data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>post_id</th>
      <th>timestamp</th>
      <th>day_of_week</th>
      <th>platform</th>
      <th>user_id</th>
      <th>location</th>
      <th>language</th>
      <th>text_content</th>
      <th>hashtags</th>
      <th>mentions</th>
      <th>...</th>
      <th>comments_count</th>
      <th>impressions</th>
      <th>engagement_rate</th>
      <th>brand_name</th>
      <th>product_name</th>
      <th>campaign_name</th>
      <th>campaign_phase</th>
      <th>user_past_sentiment_avg</th>
      <th>user_engagement_growth</th>
      <th>buzz_change_rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>kcqbs6hxybia</td>
      <td>2024-12-09 11:26:15</td>
      <td>Monday</td>
      <td>Instagram</td>
      <td>user_52nwb0a6</td>
      <td>Melbourne, Australia</td>
      <td>pt</td>
      <td>Just tried the Chromebook from Google. Best pu...</td>
      <td>#Food</td>
      <td>NaN</td>
      <td>...</td>
      <td>701</td>
      <td>18991</td>
      <td>0.19319</td>
      <td>Google</td>
      <td>Chromebook</td>
      <td>BlackFriday</td>
      <td>Launch</td>
      <td>0.0953</td>
      <td>-0.3672</td>
      <td>19.1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>vkmervg4ioos</td>
      <td>2024-07-28 19:59:26</td>
      <td>Sunday</td>
      <td>Twitter</td>
      <td>user_ucryct98</td>
      <td>Tokyo, Japan</td>
      <td>ru</td>
      <td>Just saw an ad for Microsoft Surface Laptop du...</td>
      <td>#MustHave, #Food</td>
      <td>@CustomerService, @BrandCEO</td>
      <td>...</td>
      <td>359</td>
      <td>52764</td>
      <td>0.05086</td>
      <td>Microsoft</td>
      <td>Surface Laptop</td>
      <td>PowerRelease</td>
      <td>Post-Launch</td>
      <td>0.1369</td>
      <td>-0.4510</td>
      <td>-42.6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>memhx4o1x6yu</td>
      <td>2024-11-23 14:00:12</td>
      <td>Saturday</td>
      <td>Reddit</td>
      <td>user_7rrev126</td>
      <td>Beijing, China</td>
      <td>ru</td>
      <td>What's your opinion about Nike's Epic React?  ...</td>
      <td>#Promo, #Food, #Trending</td>
      <td>NaN</td>
      <td>...</td>
      <td>643</td>
      <td>8887</td>
      <td>0.45425</td>
      <td>Nike</td>
      <td>Epic React</td>
      <td>BlackFriday</td>
      <td>Post-Launch</td>
      <td>0.2855</td>
      <td>-0.4112</td>
      <td>17.4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>bhyo6piijqt9</td>
      <td>2024-09-16 04:35:25</td>
      <td>Monday</td>
      <td>YouTube</td>
      <td>user_4mxuq0ax</td>
      <td>Lagos, Nigeria</td>
      <td>en</td>
      <td>Bummed out with my new Diet Pepsi from Pepsi! ...</td>
      <td>#Reviews, #Sustainable</td>
      <td>@StyleGuide, @BrandSupport</td>
      <td>...</td>
      <td>743</td>
      <td>6696</td>
      <td>0.42293</td>
      <td>Pepsi</td>
      <td>Diet Pepsi</td>
      <td>LaunchWave</td>
      <td>Launch</td>
      <td>-0.2094</td>
      <td>-0.0167</td>
      <td>-5.5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>c9dkiomowakt</td>
      <td>2024-09-05 21:03:01</td>
      <td>Thursday</td>
      <td>Twitter</td>
      <td>user_l1vpox2k</td>
      <td>Berlin, Germany</td>
      <td>hi</td>
      <td>Just tried the Corolla from Toyota. Absolutely...</td>
      <td>#Health, #Travel</td>
      <td>@BrandSupport, @InfluencerName</td>
      <td>...</td>
      <td>703</td>
      <td>47315</td>
      <td>0.08773</td>
      <td>Toyota</td>
      <td>Corolla</td>
      <td>LocalTouchpoints</td>
      <td>Launch</td>
      <td>0.6867</td>
      <td>0.0807</td>
      <td>38.8</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 28 columns</p>
</div>




```python
social_data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 12000 entries, 0 to 11999
    Data columns (total 28 columns):
     #   Column                   Non-Null Count  Dtype  
    ---  ------                   --------------  -----  
     0   post_id                  12000 non-null  object 
     1   timestamp                12000 non-null  object 
     2   day_of_week              12000 non-null  object 
     3   platform                 12000 non-null  object 
     4   user_id                  12000 non-null  object 
     5   location                 12000 non-null  object 
     6   language                 12000 non-null  object 
     7   text_content             12000 non-null  object 
     8   hashtags                 12000 non-null  object 
     9   mentions                 8059 non-null   object 
     10  keywords                 12000 non-null  object 
     11  topic_category           12000 non-null  object 
     12  sentiment_score          12000 non-null  float64
     13  sentiment_label          12000 non-null  object 
     14  emotion_type             12000 non-null  object 
     15  toxicity_score           12000 non-null  float64
     16  likes_count              12000 non-null  int64  
     17  shares_count             12000 non-null  int64  
     18  comments_count           12000 non-null  int64  
     19  impressions              12000 non-null  int64  
     20  engagement_rate          12000 non-null  float64
     21  brand_name               12000 non-null  object 
     22  product_name             12000 non-null  object 
     23  campaign_name            12000 non-null  object 
     24  campaign_phase           12000 non-null  object 
     25  user_past_sentiment_avg  12000 non-null  float64
     26  user_engagement_growth   12000 non-null  float64
     27  buzz_change_rate         12000 non-null  float64
    dtypes: float64(6), int64(4), object(18)
    memory usage: 2.6+ MB
    


```python
social_data.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sentiment_score</th>
      <th>toxicity_score</th>
      <th>likes_count</th>
      <th>shares_count</th>
      <th>comments_count</th>
      <th>impressions</th>
      <th>engagement_rate</th>
      <th>user_past_sentiment_avg</th>
      <th>user_engagement_growth</th>
      <th>buzz_change_rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>12000.000000</td>
      <td>12000.000000</td>
      <td>12000.00000</td>
      <td>12000.000000</td>
      <td>12000.00000</td>
      <td>12000.000000</td>
      <td>12000.000000</td>
      <td>12000.000000</td>
      <td>12000.000000</td>
      <td>12000.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.000553</td>
      <td>0.503868</td>
      <td>2490.72025</td>
      <td>1007.167167</td>
      <td>504.34575</td>
      <td>49811.338500</td>
      <td>0.278137</td>
      <td>0.001472</td>
      <td>0.000998</td>
      <td>0.729692</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.583563</td>
      <td>0.288198</td>
      <td>1441.53253</td>
      <td>575.072282</td>
      <td>288.68416</td>
      <td>28930.289451</td>
      <td>1.149206</td>
      <td>0.576627</td>
      <td>0.289940</td>
      <td>57.787219</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-0.999800</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>130.000000</td>
      <td>0.001880</td>
      <td>-0.999600</td>
      <td>-0.499900</td>
      <td>-99.900000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.503200</td>
      <td>0.251400</td>
      <td>1236.00000</td>
      <td>510.000000</td>
      <td>253.00000</td>
      <td>24716.500000</td>
      <td>0.049100</td>
      <td>-0.495975</td>
      <td>-0.248400</td>
      <td>-48.700000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>-0.006200</td>
      <td>0.505950</td>
      <td>2496.00000</td>
      <td>1018.000000</td>
      <td>503.00000</td>
      <td>49674.000000</td>
      <td>0.080605</td>
      <td>0.001950</td>
      <td>0.002800</td>
      <td>0.900000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.513525</td>
      <td>0.756200</td>
      <td>3723.25000</td>
      <td>1501.000000</td>
      <td>755.00000</td>
      <td>74815.000000</td>
      <td>0.163123</td>
      <td>0.501725</td>
      <td>0.250700</td>
      <td>50.100000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>0.999900</td>
      <td>0.999900</td>
      <td>5000.00000</td>
      <td>2000.000000</td>
      <td>1000.00000</td>
      <td>99997.000000</td>
      <td>32.211710</td>
      <td>0.999400</td>
      <td>0.499900</td>
      <td>99.900000</td>
    </tr>
  </tbody>
</table>
</div>




```python
social_data.value_counts()
```




    post_id       timestamp            day_of_week  platform   user_id        location                    language  text_content                                                                                                                                                hashtags                               mentions                       keywords                                   topic_category  sentiment_score  sentiment_label  emotion_type  toxicity_score  likes_count  shares_count  comments_count  impressions  engagement_rate  brand_name  product_name   campaign_name          campaign_phase  user_past_sentiment_avg  user_engagement_growth  buzz_change_rate
    003s4ulm32tk  2024-12-31 05:38:50  Tuesday      Reddit     user_yn4ex64c  Dubai, UAE                  en        Any advice about Amazon's Eero WiFi? @CustomerService, @TechHelp #Sale, #SpecialOffer, #Lifestyle Would love to get your feedback!                          #Sale, #SpecialOffer, #Lifestyle       @CustomerService, @TechHelp    expensive, helpful, improved               Product         -0.4230          Negative         Excited       0.7631          4733         178           118             99787        0.05039          Amazon      Eero WiFi      EarthDay               Post-Launch     -0.3350                   0.4926                 -58.7               1
    o963212xtu9u  2025-03-11 08:30:55  Tuesday      Twitter    user_6a8of0de  New York, USA               ar        Comparing Samsung Galaxy Buds to the competition. Exceeded my expectations. #Trending, #Innovation Let me know what you think!                              #Trending, #Innovation                 @CustomerService               outdated, traditional                      Delivery         0.4556          Positive         Confused      0.9029          501          1635          37              47648        0.04560          Samsung     Galaxy Buds    BlackFriday            Post-Launch      0.1401                  -0.3420                  82.7               1
    obqhlzki202y  2024-07-04 15:16:13  Thursday     Twitter    user_90fl1odm  Delhi, India                zh        Just unboxed my new Surface Duo from Microsoft. Disappointed with the quality. Could someone explain #Deal, #Discount, #Sustainable                         #Deal, #Discount, #Sustainable         @NewsOutlet                    expensive, budget, value                   Support         -0.3081          Negative         Confused      0.9589          2673         1705          351             54639        0.08654          Microsoft   Surface Duo    BackToSchool           Pre-Launch       0.6247                  -0.2708                  79.3               1
    obp80hs1v2f0  2024-09-09 16:36:22  Monday       Facebook   user_cltxm73q  Berlin, Germany             ar        Just unboxed my new iPad Air from Apple. As expected. Loving it #Affordable Curious about your experience too.                                              #Affordable                            @CompetitorBrand               traditional, helpful                       Pricing         -0.1623          Neutral          Happy         0.9073          3705         481           504             57755        0.08120          Apple       iPad Air       ValentinesDeals        Launch          -0.2954                  -0.1398                 -6.8                1
    obijps85xqog  2024-12-19 12:17:53  Thursday     Facebook   user_zxbwmseq  Shanghai, China             es        Pepsi DigitalTransformation is subpar! Can't wait to see what's coming next. #Deal, #Affordable Curious about your experience too.                          #Deal, #Affordable                     @InfluencerName, @TechHelp     service, helpful, experience, traditional  Returns         -0.8156          Negative         Happy         0.6682          2200         868           922             45298        0.08808          Pepsi       Crystal Pepsi  BackToSchool           Launch          -0.8426                   0.2766                 -33.8               1
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ..
    by16fmxaedom  2025-01-06 11:28:50  Monday       YouTube    user_7jwro19l  Manchester, UK              pt        Just unboxed my new Tacoma from Toyota. Best purchase ever. Fed up #Innovation Really interested in hearing your thoughts!                                  #Innovation                            @BrandCEO, @CompetitorBrand    feature, budget                            Delivery         0.8839          Positive         Angry         0.9684          610          581           674             76988        0.02422          Toyota      Tacoma         DigitalTransformation  Post-Launch     -0.3284                  -0.0981                 -89.4               1
    bxrtdaokqfep  2024-08-14 15:51:37  Wednesday    Instagram  user_2l2isva8  Toronto, Canada             pt        Just tried the Galaxy Tab from Samsung. Not worth the money. #Fashion Would love to get your feedback!                                                      #Fashion                               @StyleGuide, @CustomerService  improved, poor                             Returns         -0.4201          Negative         Sad           0.3319          4905         174           316             90599        0.05954          Samsung     Galaxy Tab     ReferralBonus          Launch          -0.9055                  -0.3766                 -12.6               1
    bxiq2dxd3wyt  2025-01-08 04:36:03  Wednesday    YouTube    user_f5zhw0la  Munich, Germany             de        Amazon ReferralBonus is fantastic! Can't wait to see what's coming next. #Sustainable, #Quality, #Beauty Really interested in hearing your thoughts!        #Sustainable, #Quality, #Beauty        @TechHelp                      design, responsive, unique, improved       Delivery         0.7018          Positive         Sad           0.0902          4445         1141          197             1348         4.29005          Amazon      Fire Tablet    BlackFriday            Post-Launch      0.5917                   0.1585                  17.6               1
    bxg8ficf80vj  2025-02-15 14:45:22  Saturday     YouTube    user_soj0hvzl  Milan, Italy                de        Has anyone else experienced delivery delays with Toyota's Prius? Wouldn't recommend. @CelebrityName #Limited, #CustomerService Let me know what you think!  #Limited, #CustomerService             @CelebrityName                 eco-friendly, user-friendly                Pricing         -0.7592          Negative         Happy         0.6500          4148         1029          968             78635        0.07814          Toyota      Prius          ValentinesDeals        Post-Launch     -0.4974                   0.2565                 -91.6               1
    zzpafpna0dr3  2024-06-30 20:06:04  Sunday       YouTube    user_ahhyjl9n  Johannesburg, South Africa  zh        What's your opinion about Toyota's Highlander? @ReviewSite #Affordable, #ProductLaunch, #Quality Let me know what you think!                                #Affordable, #ProductLaunch, #Quality  @ReviewSite                    budget, delivery, service                  Returns         -0.5735          Negative         Angry         0.7499          4793         1466          805             36663        0.19267          Toyota      Highlander     InnovationX            Pre-Launch       0.8764                   0.4792                 -38.3               1
    Name: count, Length: 8059, dtype: int64




```python
social_data.isnull().sum()
```




    post_id                       0
    timestamp                     0
    day_of_week                   0
    platform                      0
    user_id                       0
    location                      0
    language                      0
    text_content                  0
    hashtags                      0
    mentions                   3941
    keywords                      0
    topic_category                0
    sentiment_score               0
    sentiment_label               0
    emotion_type                  0
    toxicity_score                0
    likes_count                   0
    shares_count                  0
    comments_count                0
    impressions                   0
    engagement_rate               0
    brand_name                    0
    product_name                  0
    campaign_name                 0
    campaign_phase                0
    user_past_sentiment_avg       0
    user_engagement_growth        0
    buzz_change_rate              0
    dtype: int64




```python
social_data['mentions'].fillna(social_data['mentions'].mode()[0], inplace=True)
```

    C:\Users\abina\AppData\Local\Temp\ipykernel_2544\3192797824.py:1: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.
    The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.
    
    For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.
    
    
      social_data['mentions'].fillna(social_data['mentions'].mode()[0], inplace=True)
    


```python
social_data.isnull().sum()
```




    post_id                    0
    timestamp                  0
    day_of_week                0
    platform                   0
    user_id                    0
    location                   0
    language                   0
    text_content               0
    hashtags                   0
    mentions                   0
    keywords                   0
    topic_category             0
    sentiment_score            0
    sentiment_label            0
    emotion_type               0
    toxicity_score             0
    likes_count                0
    shares_count               0
    comments_count             0
    impressions                0
    engagement_rate            0
    brand_name                 0
    product_name               0
    campaign_name              0
    campaign_phase             0
    user_past_sentiment_avg    0
    user_engagement_growth     0
    buzz_change_rate           0
    dtype: int64




```python
social_data.duplicated().sum()
```




    0




```python
social_data.drop_duplicates(inplace=True)
```


```python
social_data["user_id"] = social_data["user_id"].str.strip()
social_data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>post_id</th>
      <th>timestamp</th>
      <th>day_of_week</th>
      <th>platform</th>
      <th>user_id</th>
      <th>location</th>
      <th>language</th>
      <th>text_content</th>
      <th>hashtags</th>
      <th>mentions</th>
      <th>...</th>
      <th>comments_count</th>
      <th>impressions</th>
      <th>engagement_rate</th>
      <th>brand_name</th>
      <th>product_name</th>
      <th>campaign_name</th>
      <th>campaign_phase</th>
      <th>user_past_sentiment_avg</th>
      <th>user_engagement_growth</th>
      <th>buzz_change_rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>kcqbs6hxybia</td>
      <td>2024-12-09 11:26:15</td>
      <td>Monday</td>
      <td>Instagram</td>
      <td>user_52nwb0a6</td>
      <td>Melbourne, Australia</td>
      <td>pt</td>
      <td>Just tried the Chromebook from Google. Best pu...</td>
      <td>#Food</td>
      <td>@RetailSupport</td>
      <td>...</td>
      <td>701</td>
      <td>18991</td>
      <td>0.19319</td>
      <td>Google</td>
      <td>Chromebook</td>
      <td>BlackFriday</td>
      <td>Launch</td>
      <td>0.0953</td>
      <td>-0.3672</td>
      <td>19.1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>vkmervg4ioos</td>
      <td>2024-07-28 19:59:26</td>
      <td>Sunday</td>
      <td>Twitter</td>
      <td>user_ucryct98</td>
      <td>Tokyo, Japan</td>
      <td>ru</td>
      <td>Just saw an ad for Microsoft Surface Laptop du...</td>
      <td>#MustHave, #Food</td>
      <td>@CustomerService, @BrandCEO</td>
      <td>...</td>
      <td>359</td>
      <td>52764</td>
      <td>0.05086</td>
      <td>Microsoft</td>
      <td>Surface Laptop</td>
      <td>PowerRelease</td>
      <td>Post-Launch</td>
      <td>0.1369</td>
      <td>-0.4510</td>
      <td>-42.6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>memhx4o1x6yu</td>
      <td>2024-11-23 14:00:12</td>
      <td>Saturday</td>
      <td>Reddit</td>
      <td>user_7rrev126</td>
      <td>Beijing, China</td>
      <td>ru</td>
      <td>What's your opinion about Nike's Epic React?  ...</td>
      <td>#Promo, #Food, #Trending</td>
      <td>@RetailSupport</td>
      <td>...</td>
      <td>643</td>
      <td>8887</td>
      <td>0.45425</td>
      <td>Nike</td>
      <td>Epic React</td>
      <td>BlackFriday</td>
      <td>Post-Launch</td>
      <td>0.2855</td>
      <td>-0.4112</td>
      <td>17.4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>bhyo6piijqt9</td>
      <td>2024-09-16 04:35:25</td>
      <td>Monday</td>
      <td>YouTube</td>
      <td>user_4mxuq0ax</td>
      <td>Lagos, Nigeria</td>
      <td>en</td>
      <td>Bummed out with my new Diet Pepsi from Pepsi! ...</td>
      <td>#Reviews, #Sustainable</td>
      <td>@StyleGuide, @BrandSupport</td>
      <td>...</td>
      <td>743</td>
      <td>6696</td>
      <td>0.42293</td>
      <td>Pepsi</td>
      <td>Diet Pepsi</td>
      <td>LaunchWave</td>
      <td>Launch</td>
      <td>-0.2094</td>
      <td>-0.0167</td>
      <td>-5.5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>c9dkiomowakt</td>
      <td>2024-09-05 21:03:01</td>
      <td>Thursday</td>
      <td>Twitter</td>
      <td>user_l1vpox2k</td>
      <td>Berlin, Germany</td>
      <td>hi</td>
      <td>Just tried the Corolla from Toyota. Absolutely...</td>
      <td>#Health, #Travel</td>
      <td>@BrandSupport, @InfluencerName</td>
      <td>...</td>
      <td>703</td>
      <td>47315</td>
      <td>0.08773</td>
      <td>Toyota</td>
      <td>Corolla</td>
      <td>LocalTouchpoints</td>
      <td>Launch</td>
      <td>0.6867</td>
      <td>0.0807</td>
      <td>38.8</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 28 columns</p>
</div>




```python
social_data['day_of_week'] = social_data['day_of_week'].str.upper()
social_data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>post_id</th>
      <th>timestamp</th>
      <th>day_of_week</th>
      <th>platform</th>
      <th>user_id</th>
      <th>location</th>
      <th>language</th>
      <th>text_content</th>
      <th>hashtags</th>
      <th>mentions</th>
      <th>...</th>
      <th>comments_count</th>
      <th>impressions</th>
      <th>engagement_rate</th>
      <th>brand_name</th>
      <th>product_name</th>
      <th>campaign_name</th>
      <th>campaign_phase</th>
      <th>user_past_sentiment_avg</th>
      <th>user_engagement_growth</th>
      <th>buzz_change_rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>kcqbs6hxybia</td>
      <td>2024-12-09 11:26:15</td>
      <td>MONDAY</td>
      <td>Instagram</td>
      <td>user_52nwb0a6</td>
      <td>Melbourne, Australia</td>
      <td>pt</td>
      <td>Just tried the Chromebook from Google. Best pu...</td>
      <td>#Food</td>
      <td>@RetailSupport</td>
      <td>...</td>
      <td>701</td>
      <td>18991</td>
      <td>0.19319</td>
      <td>Google</td>
      <td>Chromebook</td>
      <td>BlackFriday</td>
      <td>Launch</td>
      <td>0.0953</td>
      <td>-0.3672</td>
      <td>19.1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>vkmervg4ioos</td>
      <td>2024-07-28 19:59:26</td>
      <td>SUNDAY</td>
      <td>Twitter</td>
      <td>user_ucryct98</td>
      <td>Tokyo, Japan</td>
      <td>ru</td>
      <td>Just saw an ad for Microsoft Surface Laptop du...</td>
      <td>#MustHave, #Food</td>
      <td>@CustomerService, @BrandCEO</td>
      <td>...</td>
      <td>359</td>
      <td>52764</td>
      <td>0.05086</td>
      <td>Microsoft</td>
      <td>Surface Laptop</td>
      <td>PowerRelease</td>
      <td>Post-Launch</td>
      <td>0.1369</td>
      <td>-0.4510</td>
      <td>-42.6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>memhx4o1x6yu</td>
      <td>2024-11-23 14:00:12</td>
      <td>SATURDAY</td>
      <td>Reddit</td>
      <td>user_7rrev126</td>
      <td>Beijing, China</td>
      <td>ru</td>
      <td>What's your opinion about Nike's Epic React?  ...</td>
      <td>#Promo, #Food, #Trending</td>
      <td>@RetailSupport</td>
      <td>...</td>
      <td>643</td>
      <td>8887</td>
      <td>0.45425</td>
      <td>Nike</td>
      <td>Epic React</td>
      <td>BlackFriday</td>
      <td>Post-Launch</td>
      <td>0.2855</td>
      <td>-0.4112</td>
      <td>17.4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>bhyo6piijqt9</td>
      <td>2024-09-16 04:35:25</td>
      <td>MONDAY</td>
      <td>YouTube</td>
      <td>user_4mxuq0ax</td>
      <td>Lagos, Nigeria</td>
      <td>en</td>
      <td>Bummed out with my new Diet Pepsi from Pepsi! ...</td>
      <td>#Reviews, #Sustainable</td>
      <td>@StyleGuide, @BrandSupport</td>
      <td>...</td>
      <td>743</td>
      <td>6696</td>
      <td>0.42293</td>
      <td>Pepsi</td>
      <td>Diet Pepsi</td>
      <td>LaunchWave</td>
      <td>Launch</td>
      <td>-0.2094</td>
      <td>-0.0167</td>
      <td>-5.5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>c9dkiomowakt</td>
      <td>2024-09-05 21:03:01</td>
      <td>THURSDAY</td>
      <td>Twitter</td>
      <td>user_l1vpox2k</td>
      <td>Berlin, Germany</td>
      <td>hi</td>
      <td>Just tried the Corolla from Toyota. Absolutely...</td>
      <td>#Health, #Travel</td>
      <td>@BrandSupport, @InfluencerName</td>
      <td>...</td>
      <td>703</td>
      <td>47315</td>
      <td>0.08773</td>
      <td>Toyota</td>
      <td>Corolla</td>
      <td>LocalTouchpoints</td>
      <td>Launch</td>
      <td>0.6867</td>
      <td>0.0807</td>
      <td>38.8</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 28 columns</p>
</div>




```python
social_data["
```
