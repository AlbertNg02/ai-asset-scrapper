import requests
import json

def make_api_request(lt_value):
    url = "https://api.leonardo.ai/v1/graphql"

    payload = json.dumps({
        "operationName": "GetFeedImages",
        "variables": {
            "order_by": [
                {},
                {
                    "createdAt": "desc"
                }
            ],
            "where": {
                "createdAt": {
                    "_lt": lt_value
                },
                "nsfw": {
                    "_eq": False
                },
                "generation": {
                    "status": {
                        "_eq": "COMPLETE"
                    },
                    "canvasRequest": {
                        "_eq": False
                    },
                    "category": {},
                    "_or": [
                        {
                            "prompt": {
                                "_ilike": "%%"
                            }
                        }
                    ],
                    "_and": [
                        {
                            "_or": [
                                {
                                    "promptMagic": {
                                        "_eq": True
                                    }
                                },
                                {
                                    "initStrength": {
                                        "_is_null": True
                                    }
                                }
                            ]
                        }
                    ],
                    "public": {
                        "_eq": True
                    }
                }
            },
            "limit": 50,
            "userId": "3606d7b4-4243-4cc6-81e9-582ae81b68b8"
        },
        "query": "query GetFeedImages($where: generated_images_bool_exp, $limit: Int, $userId: uuid!, $order_by: [generated_images_order_by!] = [{createdAt: desc}], $offset: Int) {\n  generated_images(\n    where: $where\n    limit: $limit\n    order_by: $order_by\n    offset: $offset\n  ) {\n    ...FeedParts\n    __typename\n  }\n}\n\nfragment FeedParts on generated_images {\n  createdAt\n  id\n  url\n  user_liked_generated_images(limit: 1, where: {userId: {_eq: $userId}}) {\n    generatedImageId\n    __typename\n  }\n  user {\n    username\n    id\n    __typename\n  }\n  generation {\n    id\n    alchemy\n    contrastRatio\n    highResolution\n    prompt\n    negativePrompt\n    imageWidth\n    imageHeight\n    sdVersion\n    modelId\n    coreModel\n    guidanceScale\n    inferenceSteps\n    seed\n    scheduler\n    tiling\n    highContrast\n    promptMagic\n    imagePromptStrength\n    custom_model {\n      id\n      name\n      userId\n      modelHeight\n      modelWidth\n      __typename\n    }\n    initStrength\n    category\n    public\n    __typename\n  }\n  generated_image_variation_generics(order_by: [{createdAt: desc}]) {\n    url\n    id\n    status\n    transformType\n    upscale_details {\n      oneClicktype\n      __typename\n    }\n    __typename\n  }\n  likeCount\n  __typename\n}"
    })
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJraWQiOiJtM1IxVnh4VWlEa1Q3Z1lrc3dYWlBFb1JEcnRWU0E0M3E0bUtzc29ZWWpZPSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiUFZScUJqaEV3cWlUS21YSHVvWFdldyIsInN1YiI6IjMxNDE4ZmM5LWJlZjItNDU2Yi1iYTJlLTVmNjg3ZGRhYzhjYyIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJodHRwczpcL1wvaGFzdXJhLmlvXC9qd3RcL2NsYWltcyI6IntcIngtaGFzdXJhLXVzZXItaWRcIjpcIjM2MDZkN2I0LTQyNDMtNGNjNi04MWU5LTU4MmFlODFiNjhiOFwiLFwieC1oYXN1cmEtZGVmYXVsdC1yb2xlXCI6XCJ1c2VyXCIsXCJ4LWhhc3VyYS1hbGxvd2VkLXJvbGVzXCI6W1widXNlclwiXX0iLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV94a1ZNdUNxZXUiLCJjb2duaXRvOnVzZXJuYW1lIjoiMzE0MThmYzktYmVmMi00NTZiLWJhMmUtNWY2ODdkZGFjOGNjIiwibm9uY2UiOiJqVXNFR0ppNkhDWUR0MWtXNjRDc0JMUEg0eXNuZkxxNWZ2YXR5NGJLeHp3Iiwib3JpZ2luX2p0aSI6IjJlOWE5NjExLTVlYWQtNGE2OS05Mzg5LTU5MGI2ZGY0M2I0YSIsImF1ZCI6IjlzYTFkbGg2ajR1NmU0Zml2MWMxMjQ0cHEiLCJldmVudF9pZCI6ImMxM2VlZTExLTZkNjEtNDM4OS05MDY1LTM0OWY5Y2VlMDRjNCIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNjg4NTQ5NzQwLCJleHAiOjE2ODg1NTMzNDAsImlhdCI6MTY4ODU0OTc0MCwianRpIjoiNGExYmQ0ZDItZTlmNC00NjI2LWIzYjgtZTczZThhMzg0ZWExIiwiZW1haWwiOiJ0aHV5ZXRwaGFtaXRAZ21haWwuY29tIn0.Z4nEeLxJTO0fXNrV95N0Nl76XhVY3eGc7JMifYhEW3Ob9oFDiaQwW8D4S38bCI4rQRvj_bOK3f2tPMrwDWPUdcTokufod29BPzohZX-BRyQEyV4flUPLxetnyLARMYC3snRhjrWAvp8pfdNgvdn8nF89gspe9vWE6I3F9S8POSJOf7WFthCBQ98ew_gZdyOww5xZwEHOzxXICa0AG-EoKY7RQo9Hcfn2CYJOsFXHTKtg51yD1M6XHykTmxrNJObC9hrXkVyImPQYd9NBpUgvg8Cc3U4xOSBKYEZ59QLf_YmrFuB3Wo2yko_ThWT-myEClg3bMLOODBFSPT2Y_YNY_A'
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJraWQiOiJtM1IxVnh4VWlEa1Q3Z1lrc3dYWlBFb1JEcnRWU0E0M3E0bUtzc29ZWWpZPSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiUFZScUJqaEV3cWlUS21YSHVvWFdldyIsInN1YiI6IjMxNDE4ZmM5LWJlZjItNDU2Yi1iYTJlLTVmNjg3ZGRhYzhjYyIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJodHRwczpcL1wvaGFzdXJhLmlvXC9qd3RcL2NsYWltcyI6IntcIngtaGFzdXJhLXVzZXItaWRcIjpcIjM2MDZkN2I0LTQyNDMtNGNjNi04MWU5LTU4MmFlODFiNjhiOFwiLFwieC1oYXN1cmEtZGVmYXVsdC1yb2xlXCI6XCJ1c2VyXCIsXCJ4LWhhc3VyYS1hbGxvd2VkLXJvbGVzXCI6W1widXNlclwiXX0iLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV94a1ZNdUNxZXUiLCJjb2duaXRvOnVzZXJuYW1lIjoiMzE0MThmYzktYmVmMi00NTZiLWJhMmUtNWY2ODdkZGFjOGNjIiwibm9uY2UiOiJqVXNFR0ppNkhDWUR0MWtXNjRDc0JMUEg0eXNuZkxxNWZ2YXR5NGJLeHp3Iiwib3JpZ2luX2p0aSI6IjJlOWE5NjExLTVlYWQtNGE2OS05Mzg5LTU5MGI2ZGY0M2I0YSIsImF1ZCI6IjlzYTFkbGg2ajR1NmU0Zml2MWMxMjQ0cHEiLCJldmVudF9pZCI6ImMxM2VlZTExLTZkNjEtNDM4OS05MDY1LTM0OWY5Y2VlMDRjNCIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNjg4NTQ5NzQwLCJleHAiOjE2ODg1NTMzNDAsImlhdCI6MTY4ODU0OTc0MCwianRpIjoiNGExYmQ0ZDItZTlmNC00NjI2LWIzYjgtZTczZThhMzg0ZWExIiwiZW1haWwiOiJ0aHV5ZXRwaGFtaXRAZ21haWwuY29tIn0.Z4nEeLxJTO0fXNrV95N0Nl76XhVY3eGc7JMifYhEW3Ob9oFDiaQwW8D4S38bCI4rQRvj_bOK3f2tPMrwDWPUdcTokufod29BPzohZX-BRyQEyV4flUPLxetnyLARMYC3snRhjrWAvp8pfdNgvdn8nF89gspe9vWE6I3F9S8POSJOf7WFthCBQ98ew_gZdyOww5xZwEHOzxXICa0AG-EoKY7RQo9Hcfn2CYJOsFXHTKtg51yD1M6XHykTmxrNJObC9hrXkVyImPQYd9NBpUgvg8Cc3U4xOSBKYEZ59QLf_YmrFuB3Wo2yko_ThWT-myEClg3bMLOODBFSPT2Y_YNY_A'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    
    response_data = response.json()
    _lt = response_data["data"]["generated_images"][0]["createdAt"]
    lt_value = _lt
    
    # Continue the loop or add conditions to exit the loop

# Call the function to start making requests
make_api_request("2023-07-05T10:16:40.526Z")
