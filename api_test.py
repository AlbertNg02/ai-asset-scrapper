import requests
import json


LT_VALUE = "2023-07-05T10:16:40.526Z"
URL = "https://api.leonardo.ai/v1/graphql"
BEARER_TOKEN = "Bearer eyJraWQiOiJtM1IxVnh4VWlEa1Q3Z1lrc3dYWlBFb1JEcnRWU0E0M3E0bUtzc29ZWWpZPSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiVk1ZSzBMTTZvN0Nka1ZoVVJYTTFuZyIsInN1YiI6IjMxNDE4ZmM5LWJlZjItNDU2Yi1iYTJlLTVmNjg3ZGRhYzhjYyIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJodHRwczpcL1wvaGFzdXJhLmlvXC9qd3RcL2NsYWltcyI6IntcIngtaGFzdXJhLXVzZXItaWRcIjpcIjM2MDZkN2I0LTQyNDMtNGNjNi04MWU5LTU4MmFlODFiNjhiOFwiLFwieC1oYXN1cmEtZGVmYXVsdC1yb2xlXCI6XCJ1c2VyXCIsXCJ4LWhhc3VyYS1hbGxvd2VkLXJvbGVzXCI6W1widXNlclwiXX0iLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV94a1ZNdUNxZXUiLCJjb2duaXRvOnVzZXJuYW1lIjoiMzE0MThmYzktYmVmMi00NTZiLWJhMmUtNWY2ODdkZGFjOGNjIiwibm9uY2UiOiJydDVTMFVydmZLVWlUS2pQdXpaR0oyNlBlZzlWWkh5MzZwWFRiT3AxR09jIiwib3JpZ2luX2p0aSI6IjYyNTIzZWZkLTA1ZTUtNGU0Yy1hN2RhLWQ4NDQ3MDRhN2MwMSIsImF1ZCI6IjlzYTFkbGg2ajR1NmU0Zml2MWMxMjQ0cHEiLCJldmVudF9pZCI6Ijk3MTRjNDM3LTA3YjItNGE1Zi1iNjYzLTMyZDBkOTQ3NTY3MSIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNjg4NjYyMTUzLCJleHAiOjE2ODg2NjU3NTMsImlhdCI6MTY4ODY2MjE1MywianRpIjoiMGI4NTIxYmMtMjBiZC00MGM4LTg3MDQtYzZjODZkNTdiYjcxIiwiZW1haWwiOiJ0aHV5ZXRwaGFtaXRAZ21haWwuY29tIn0.hSKh-5H2ito7apmaEijf-fV67fGdYUgBC-R91YRfW5LV1nV3Emd_AGt7cxIToRApsXFsKkIYVm7MsiqCyk0la_jT-xjfFagMAhqIXa0Jl9pVXPp9_9SXKQ5_NzwFNcH3Q9_bMraLhhF3aKuFL93nd7pg_sUps2fluLU5Q8GGzZJU3kCPafK1H2QTP837FD455hg6qhpSOeIVeQGP-rRlW0hLVaZdw4fNzU4cIVIlA3T0yrQKaQfpEoQWCHnKYMZXChcRvVuKA9gpeIGZNH2VcQ4kP0SfU2u2aHFYGF5u7l5Fy0mDAOg40FE1p5X7GW32uZz2Vo3UBJfjUY7WBgwRTg"


def make_api_request(URL, BEARER_TOKEN, LT_VALUE):

    # Original payload
    # payload = "{{\"operationName\":\"GetFeedImages\",\"variables\":{{\"order_by\":[{{}},{{\"createdAt\":\"desc\"}}],\"where\":{{\"createdAt\":{{\"_lt\":\"{_lt}\"}},\"nsfw\":{{\"_eq\":false}},\"generation\":{{\"status\":{{\"_eq\":\"COMPLETE\"}},\"canvasRequest\":{{\"_eq\":false}},\"category\":{{}},\"_or\":[{{\"prompt\":{{\"_ilike\":\"%%\"}}}}],\"_and\":[{{\"_or\":[{{\"promptMagic\":{{\"_eq\":true}}}},{{\"initStrength\":{{\"_is_null\":true}}}}]}}],\"public\":{{\"_eq\":true}}}}}},\"limit\":50,\"userId\":\"3606d7b4-4243-4cc6-81e9-582ae81b68b8\"}},\"query\":\"query GetFeedImages($where: generated_images_bool_exp, $limit: Int, $userId: uuid!, $order_by: [generated_images_order_by!] = [{{createdAt: desc}}], $offset: Int) {{\\n  generated_images(\\n    where: $where\\n    limit: $limit\\n    order_by: $order_by\\n    offset: $offset\\n  ) {{\\n    ...FeedParts\\n    __typename\\n  }}\\n}}\\n\\nfragment FeedParts on generated_images {{\\n  createdAt\\n  id\\n  url\\n  user_liked_generated_images(limit: 1, where: {{userId: {{_eq: $userId}}}}) {{\\n    generatedImageId\\n    __typename\\n  }}\\n  user {{\\n    username\\n    id\\n    __typename\\n  }}\\n  generation {{\\n    id\\n    alchemy\\n    contrastRatio\\n    highResolution\\n    prompt\\n    negativePrompt\\n    imageWidth\\n    imageHeight\\n    sdVersion\\n    modelId\\n    coreModel\\n    guidanceScale\\n    inferenceSteps\\n    seed\\n    scheduler\\n    tiling\\n    highContrast\\n    promptMagic\\n    imagePromptStrength\\n    custom_model {{\\n      id\\n      name\\n      userId\\n      modelHeight\\n      modelWidth\\n      __typename\\n    }}\\n    initStrength\\n    category\\n    public\\n    __typename\\n  }}\\n  generated_image_variation_generics(order_by: [{{createdAt: desc}}]) {{\\n    url\\n    id\\n    status\\n    transformType\\n    upscale_details {{\\n      oneClicktype\\n      __typename\\n    }}\\n    __typename\\n  }}\\n  likeCount\\n  __typename\\n}}\"}}".format( _lt =LT_VALUE)

    # Trending payload
    payload = "{{\"operationName\":\"GetFeedImages\",\"variables\":{{\"order_by\":[{{\"trendingScore\":\"desc\"}},{{\"createdAt\":\"desc\"}}],\"where\":{{\"createdAt\":{{\"_lt\":\"{_lt}\"}},\"nsfw\":{{\"_eq\":false}},\"generation\":{{\"status\":{{\"_eq\":\"COMPLETE\"}},\"canvasRequest\":{{\"_eq\":false}},\"category\":{{}},\"_or\":[{{\"prompt\":{{\"_ilike\":\"%%\"}}}}],\"_and\":[{{\"_or\":[{{\"promptMagic\":{{\"_eq\":true}}}},{{\"initStrength\":{{\"_is_null\":true}}}}]}}],\"public\":{{\"_eq\":true}}}},\"trendingScore\":{{\"_gt\":0}}}},\"limit\":50,\"userId\":\"3606d7b4-4243-4cc6-81e9-582ae81b68b8\"}},\"query\":\"query GetFeedImages($where: generated_images_bool_exp, $limit: Int, $userId: uuid!, $order_by: [generated_images_order_by!] = [{{createdAt: desc}}], $offset: Int) {{\\n  generated_images(\\n    where: $where\\n    limit: $limit\\n    order_by: $order_by\\n    offset: $offset\\n  ) {{\\n    ...FeedParts\\n    __typename\\n  }}\\n}}\\n\\nfragment FeedParts on generated_images {{\\n  createdAt\\n  id\\n  url\\n  user_liked_generated_images(limit: 1, where: {{userId: {{_eq: $userId}}}}) {{\\n    generatedImageId\\n    __typename\\n  }}\\n  user {{\\n    username\\n    id\\n    __typename\\n  }}\\n  generation {{\\n    id\\n    alchemy\\n    contrastRatio\\n    highResolution\\n    prompt\\n    negativePrompt\\n    imageWidth\\n    imageHeight\\n    sdVersion\\n    modelId\\n    coreModel\\n    guidanceScale\\n    inferenceSteps\\n    seed\\n    scheduler\\n    tiling\\n    highContrast\\n    promptMagic\\n    imagePromptStrength\\n    custom_model {{\\n      id\\n      name\\n      userId\\n      modelHeight\\n      modelWidth\\n      __typename\\n    }}\\n    initStrength\\n    category\\n    public\\n    __typename\\n  }}\\n  generated_image_variation_generics(order_by: [{{createdAt: desc}}]) {{\\n    url\\n    id\\n    status\\n    transformType\\n    upscale_details {{\\n      oneClicktype\\n      __typename\\n    }}\\n    __typename\\n  }}\\n  likeCount\\n  __typename\\n}}\"}}".format(_lt=LT_VALUE)

    # New payload
    # payload = "{{\"operationName\":\"GetFeedImages\",\"variables\":{{\"order_by\":[{{}},{{\"createdAt\":\"desc\"}}],\"where\":{{\"createdAt\":{{\"_lt\":\"{_lt}\"}},\"nsfw\":{{\"_eq\":false}},\"generation\":{{\"status\":{{\"_eq\":\"COMPLETE\"}},\"canvasRequest\":{{\"_eq\":false}},\"category\":{{}},\"_or\":[{{\"prompt\":{{\"_ilike\":\"%%\"}}}}],\"_and\":[{{\"_or\":[{{\"promptMagic\":{{\"_eq\":true}}}},{{\"initStrength\":{{\"_is_null\":true}}}}]}}],\"public\":{{\"_eq\":true}}}}}},\"limit\":50,\"userId\":\"3606d7b4-4243-4cc6-81e9-582ae81b68b8\"}},\"query\":\"query GetFeedImages($where: generated_images_bool_exp, $limit: Int, $userId: uuid!, $order_by: [generated_images_order_by!] = [{{createdAt: desc}}], $offset: Int) {{\\n  generated_images(\\n    where: $where\\n    limit: $limit\\n    order_by: $order_by\\n    offset: $offset\\n  ) {{\\n    ...FeedParts\\n    __typename\\n  }}\\n}}\\n\\nfragment FeedParts on generated_images {{\\n  createdAt\\n  id\\n  url\\n  user_liked_generated_images(limit: 1, where: {{userId: {{_eq: $userId}}}}) {{\\n    generatedImageId\\n    __typename\\n  }}\\n  user {{\\n    username\\n    id\\n    __typename\\n  }}\\n  generation {{\\n    id\\n    alchemy\\n    contrastRatio\\n    highResolution\\n    prompt\\n    negativePrompt\\n    imageWidth\\n    imageHeight\\n    sdVersion\\n    modelId\\n    coreModel\\n    guidanceScale\\n    inferenceSteps\\n    seed\\n    scheduler\\n    tiling\\n    highContrast\\n    promptMagic\\n    imagePromptStrength\\n    custom_model {{\\n      id\\n      name\\n      userId\\n      modelHeight\\n      modelWidth\\n      __typename\\n    }}\\n    initStrength\\n    category\\n    public\\n    __typename\\n  }}\\n  generated_image_variation_generics(order_by: [{{createdAt: desc}}]) {{\\n    url\\n    id\\n    status\\n    transformType\\n    upscale_details {{\\n      oneClicktype\\n      __typename\\n    }}\\n    __typename\\n  }}\\n  likeCount\\n  __typename\\n}}\"}}".format(_lt=LT_VALUE)
    

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
    new_lt_value = ""
    
    for index, image in enumerate(images):
        # print(image.keys())
        if len(image["generated_image_variation_generics"])>0:
            for variation in image["generated_image_variation_generics"]:
                if len(variation["upscale_details"])>0:
                    if variation["upscale_details"][0]["oneClicktype"] == "ALTERNATE":
                        entry = {'src': image['url'], 'prompt': image['generation']['prompt'], 'negativePrompt': image['generation']['negativePrompt']}
                        entries.append(entry)
                        print("Alternate with index: ", index, "total images: ", total_images)
                    # else:
                    #     print("Not Alternate")

        if index == total_images - 1:
            new_lt_value = image['createdAt']
            


    with open("./extrac2.json", mode='a', encoding='utf-8') as f:
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