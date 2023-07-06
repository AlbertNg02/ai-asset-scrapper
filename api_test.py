import requests
import json


LT_VALUE = "2023-07-05T10:16:40.526Z"
URL = "https://api.leonardo.ai/v1/graphql"
BEARER_TOKEN = "Bearer eyJraWQiOiJtM1IxVnh4VWlEa1Q3Z1lrc3dYWlBFb1JEcnRWU0E0M3E0bUtzc29ZWWpZPSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoid2ZVZ2JxZlJVQVU1dkdZdE00VjJuZyIsInN1YiI6IjMxNDE4ZmM5LWJlZjItNDU2Yi1iYTJlLTVmNjg3ZGRhYzhjYyIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJodHRwczpcL1wvaGFzdXJhLmlvXC9qd3RcL2NsYWltcyI6IntcIngtaGFzdXJhLXVzZXItaWRcIjpcIjM2MDZkN2I0LTQyNDMtNGNjNi04MWU5LTU4MmFlODFiNjhiOFwiLFwieC1oYXN1cmEtZGVmYXVsdC1yb2xlXCI6XCJ1c2VyXCIsXCJ4LWhhc3VyYS1hbGxvd2VkLXJvbGVzXCI6W1widXNlclwiXX0iLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV94a1ZNdUNxZXUiLCJjb2duaXRvOnVzZXJuYW1lIjoiMzE0MThmYzktYmVmMi00NTZiLWJhMmUtNWY2ODdkZGFjOGNjIiwib3JpZ2luX2p0aSI6IjQ5MjJkZTU0LTY1MTctNGI4Yi1iMjUyLTFkYzc2MWJiYjkyNCIsImF1ZCI6IjlzYTFkbGg2ajR1NmU0Zml2MWMxMjQ0cHEiLCJldmVudF9pZCI6ImY1ZTljOGE0LTUzM2UtNDE1Ny1iZDQ3LTM0ZmNhYTQ1YTI3NSIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNjg4NjMxMDA1LCJleHAiOjE2ODg2NDU3MTQsImlhdCI6MTY4ODY0MjExNCwianRpIjoiYmYyOGFlNTktZDE1OC00NjJiLWIwNDEtNzJkYTVhZmViOTg5IiwiZW1haWwiOiJ0aHV5ZXRwaGFtaXRAZ21haWwuY29tIn0.eRMpocCunohQ8GGr16FadJdip39iz7-OD-xBGBdEjeJqbC_fhl5krNMT564rNsXM3adfxOx3EbA8nW3WRK9lBU5EAycHMQo8AM8XVtT2WBpdBPS5cr8pCsJ4eJJ0auxGDYshqid5RgMyzTO0YOfFZCHdc3H04t_e4HL37uiaa6ju_N_aC21dvvHsLVQRzSUHKCRdKyI0GYhFUENZYZMyA0PXJxEAyzb9EkSwEIq22NMf6Ynjgo0f6OKMkSrh_QLXWUtn-L0D7QP-8GLC4QHm967wtAv2A5NlsomwxU-l0MhCLX0Ir1ziYFPFXg-nX1Rpu6nARknkJ_9MKeBz1WUszg"


def make_api_request(URL, BEARER_TOKEN, LT_VALUE):

    # Original payload
    # payload = "{{\"operationName\":\"GetFeedImages\",\"variables\":{{\"order_by\":[{{}},{{\"createdAt\":\"desc\"}}],\"where\":{{\"createdAt\":{{\"_lt\":\"{_lt}\"}},\"nsfw\":{{\"_eq\":false}},\"generation\":{{\"status\":{{\"_eq\":\"COMPLETE\"}},\"canvasRequest\":{{\"_eq\":false}},\"category\":{{}},\"_or\":[{{\"prompt\":{{\"_ilike\":\"%%\"}}}}],\"_and\":[{{\"_or\":[{{\"promptMagic\":{{\"_eq\":true}}}},{{\"initStrength\":{{\"_is_null\":true}}}}]}}],\"public\":{{\"_eq\":true}}}}}},\"limit\":50,\"userId\":\"3606d7b4-4243-4cc6-81e9-582ae81b68b8\"}},\"query\":\"query GetFeedImages($where: generated_images_bool_exp, $limit: Int, $userId: uuid!, $order_by: [generated_images_order_by!] = [{{createdAt: desc}}], $offset: Int) {{\\n  generated_images(\\n    where: $where\\n    limit: $limit\\n    order_by: $order_by\\n    offset: $offset\\n  ) {{\\n    ...FeedParts\\n    __typename\\n  }}\\n}}\\n\\nfragment FeedParts on generated_images {{\\n  createdAt\\n  id\\n  url\\n  user_liked_generated_images(limit: 1, where: {{userId: {{_eq: $userId}}}}) {{\\n    generatedImageId\\n    __typename\\n  }}\\n  user {{\\n    username\\n    id\\n    __typename\\n  }}\\n  generation {{\\n    id\\n    alchemy\\n    contrastRatio\\n    highResolution\\n    prompt\\n    negativePrompt\\n    imageWidth\\n    imageHeight\\n    sdVersion\\n    modelId\\n    coreModel\\n    guidanceScale\\n    inferenceSteps\\n    seed\\n    scheduler\\n    tiling\\n    highContrast\\n    promptMagic\\n    imagePromptStrength\\n    custom_model {{\\n      id\\n      name\\n      userId\\n      modelHeight\\n      modelWidth\\n      __typename\\n    }}\\n    initStrength\\n    category\\n    public\\n    __typename\\n  }}\\n  generated_image_variation_generics(order_by: [{{createdAt: desc}}]) {{\\n    url\\n    id\\n    status\\n    transformType\\n    upscale_details {{\\n      oneClicktype\\n      __typename\\n    }}\\n    __typename\\n  }}\\n  likeCount\\n  __typename\\n}}\"}}".format( _lt =LT_VALUE)

    # Trending payload
    # payload = "{{\"operationName\":\"GetFeedImages\",\"variables\":{{\"order_by\":[{{\"trendingScore\":\"desc\"}},{{\"createdAt\":\"desc\"}}],\"where\":{{\"createdAt\":{{\"_lt\":\"{_lt}\"}},\"nsfw\":{{\"_eq\":false}},\"generation\":{{\"status\":{{\"_eq\":\"COMPLETE\"}},\"canvasRequest\":{{\"_eq\":false}},\"category\":{{}},\"_or\":[{{\"prompt\":{{\"_ilike\":\"%%\"}}}}],\"_and\":[{{\"_or\":[{{\"promptMagic\":{{\"_eq\":true}}}},{{\"initStrength\":{{\"_is_null\":true}}}}]}}],\"public\":{{\"_eq\":true}}}},\"trendingScore\":{{\"_gt\":0}}}},\"limit\":50,\"userId\":\"3606d7b4-4243-4cc6-81e9-582ae81b68b8\"}},\"query\":\"query GetFeedImages($where: generated_images_bool_exp, $limit: Int, $userId: uuid!, $order_by: [generated_images_order_by!] = [{{createdAt: desc}}], $offset: Int) {{\\n  generated_images(\\n    where: $where\\n    limit: $limit\\n    order_by: $order_by\\n    offset: $offset\\n  ) {{\\n    ...FeedParts\\n    __typename\\n  }}\\n}}\\n\\nfragment FeedParts on generated_images {{\\n  createdAt\\n  id\\n  url\\n  user_liked_generated_images(limit: 1, where: {{userId: {{_eq: $userId}}}}) {{\\n    generatedImageId\\n    __typename\\n  }}\\n  user {{\\n    username\\n    id\\n    __typename\\n  }}\\n  generation {{\\n    id\\n    alchemy\\n    contrastRatio\\n    highResolution\\n    prompt\\n    negativePrompt\\n    imageWidth\\n    imageHeight\\n    sdVersion\\n    modelId\\n    coreModel\\n    guidanceScale\\n    inferenceSteps\\n    seed\\n    scheduler\\n    tiling\\n    highContrast\\n    promptMagic\\n    imagePromptStrength\\n    custom_model {{\\n      id\\n      name\\n      userId\\n      modelHeight\\n      modelWidth\\n      __typename\\n    }}\\n    initStrength\\n    category\\n    public\\n    __typename\\n  }}\\n  generated_image_variation_generics(order_by: [{{createdAt: desc}}]) {{\\n    url\\n    id\\n    status\\n    transformType\\n    upscale_details {{\\n      oneClicktype\\n      __typename\\n    }}\\n    __typename\\n  }}\\n  likeCount\\n  __typename\\n}}\"}}".format(_lt=LT_VALUE)

    # New payload
    

    headers = {
        'Content-Type': 'text/plain',
        'Authorization': BEARER_TOKEN,
    }

    response = requests.request("POST", URL, headers=headers, data=payload)
    # print(response.text)
    return json.loads(response.text)


def store_data(response):
    images = response["data"]["generated_images"]
    entries = []
    total_images = len(images)
    
    for index, image in enumerate(images):
        # print(image.keys())
        entry = {'src': image['url'], 'prompt': image['generation']['prompt'], 'negativePrompt': image['generation']['negativePrompt']}
        entries.append(entry)
        print("index: ", index, "total images: ", total_images)

        if index == total_images - 1:
            new_lt_value = image['createdAt']

    with open("extrac2.json", mode='a', encoding='utf-8') as f:
        json.dump(entries, f)
    return new_lt_value

    
# with open("extrac2.json", mode='w', encoding='utf-8') as f:
#     json.dump([], f)


while True:

    response = make_api_request(URL, BEARER_TOKEN, LT_VALUE)
    # print(response)
    new_lt = store_data(response)
    if new_lt is None:
        break
    LT_VALUE = new_lt