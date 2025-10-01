# Raindrop.io Developer Documentation

This documentation was scraped from https://developer.raindrop.io

---

<!-- Source: https://developer.raindrop.io -->

# https://developer.raindrop.io

This is the official documentation for Raindrop.io API. A reference to the functionality our public API provides with detailed description of each API endpoint, parameters, and examples.Please note that you must register your application and authenticate with OAuth when making requests. Before doing so, be sure to read our Terms & Guidelines to learn how the API may be used.FormatAPI endpoints accept arguments either as url-encoded values for non-POST requests or as json-encoded objects encoded in POST request body with Content-Type: application/json header.Where possible, the API strives to use appropriate HTTP verbs for each action.VerbDescriptionGETUsed for retrieving resources.POSTUsed for creating resources.PUTUsed for updating resources, or performing custom actions.DELETEUsed for deleting resources.This API relies on standard HTTP response codes to indicate operation result. The table below is a simple reference about the most used status codes:Status codeDescription200The request was processed successfully.204The request was processed successfully without any data to return.4xxThe request was processed with an error and should not be retried unmodified as they won’t be processed any different by an API.5xxThe request failed due to a server error, it’s safe to retry later.All 200 OK responses have the Content-type: application/json and contain a JSON-encoded representation of one or more objects.Payload of POST requests has to be JSON-encoded and accompanied with Content-Type: application/json header.TimestampsAll timestamps are returned in ISO 8601 format:CopyYYYY-MM-DDTHH:MM:SSZRate LimitingFor requests using OAuth, you can make up to 120 requests per minute per authenticated user.The headers tell you everything you need to know about your current rate limit status:Header nameDescriptionX-RateLimit-LimitThe maximum number of requests that the consumer is permitted to make per minute.RateLimit-RemainingThe number of requests remaining in the current rate limit window.X-RateLimit-ResetThe time at which the current rate limit window resets in UTC epoch seconds.Once you go over the rate limit you will receive an error response:CopyHTTP/1.1 429 Too Many Requests
Status: 429 Too Many Requests
X-RateLimit-Limit: 120
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1392321600 CORSThe API supports Cross Origin Resource Sharing (CORS) for AJAX requests. You can read the CORS W3C recommendation, or this intro from the HTML 5 Security Guide.Here’s a sample request sent from a browser hitting http://example.com:CopyHTTP/1.1 200 OK
Access-Control-Allow-Origin: http://example.com
Access-Control-Expose-Headers: ETag, Content-Type, Accept, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset
Access-Control-Allow-Credentials: trueNextTerms & GuidelinesLast updated 9 months agoWas this helpful?


---

<!-- Source: https://developer.raindrop.io/ -->

# https://developer.raindrop.io/

This is the official documentation for Raindrop.io API. A reference to the functionality our public API provides with detailed description of each API endpoint, parameters, and examples.Please note that you must register your application and authenticate with OAuth when making requests. Before doing so, be sure to read our Terms & Guidelines to learn how the API may be used.FormatAPI endpoints accept arguments either as url-encoded values for non-POST requests or as json-encoded objects encoded in POST request body with Content-Type: application/json header.Where possible, the API strives to use appropriate HTTP verbs for each action.VerbDescriptionGETUsed for retrieving resources.POSTUsed for creating resources.PUTUsed for updating resources, or performing custom actions.DELETEUsed for deleting resources.This API relies on standard HTTP response codes to indicate operation result. The table below is a simple reference about the most used status codes:Status codeDescription200The request was processed successfully.204The request was processed successfully without any data to return.4xxThe request was processed with an error and should not be retried unmodified as they won’t be processed any different by an API.5xxThe request failed due to a server error, it’s safe to retry later.All 200 OK responses have the Content-type: application/json and contain a JSON-encoded representation of one or more objects.Payload of POST requests has to be JSON-encoded and accompanied with Content-Type: application/json header.TimestampsAll timestamps are returned in ISO 8601 format:CopyYYYY-MM-DDTHH:MM:SSZRate LimitingFor requests using OAuth, you can make up to 120 requests per minute per authenticated user.The headers tell you everything you need to know about your current rate limit status:Header nameDescriptionX-RateLimit-LimitThe maximum number of requests that the consumer is permitted to make per minute.RateLimit-RemainingThe number of requests remaining in the current rate limit window.X-RateLimit-ResetThe time at which the current rate limit window resets in UTC epoch seconds.Once you go over the rate limit you will receive an error response:CopyHTTP/1.1 429 Too Many Requests
Status: 429 Too Many Requests
X-RateLimit-Limit: 120
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1392321600 CORSThe API supports Cross Origin Resource Sharing (CORS) for AJAX requests. You can read the CORS W3C recommendation, or this intro from the HTML 5 Security Guide.Here’s a sample request sent from a browser hitting http://example.com:CopyHTTP/1.1 200 OK
Access-Control-Allow-Origin: http://example.com
Access-Control-Expose-Headers: ETag, Content-Type, Accept, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset
Access-Control-Allow-Credentials: trueNextTerms & GuidelinesLast updated 9 months agoWas this helpful?


---

<!-- Source: https://developer.raindrop.io/cdn-cgi/l/email-protection -->

# https://developer.raindrop.io/cdn-cgi/l/email-protection

Email Protection | Cloudflare
Please enable cookies.
Email Protection
You are unable to access this email address developer.raindrop.io
The website from which you got to this page is protected by Cloudflare. Email addresses on that page have been hidden in order to keep them from being accessed by malicious bots. You must enable Javascript in your browser in order to decode the e-mail address.
If you have a website and are interested in protecting it in a similar way, you can sign up for Cloudflare.
How does Cloudflare protect email addresses on website from spammers?
Can I sign up for Cloudflare?
Cloudflare Ray ID: 986e625a1b7fba72
•
Your IP:
Click to reveal
2a02:a03f:8ad0:2400:d7f:7877:d4e0:34f7
•
Performance & security by Cloudflare


---

<!-- Source: https://developer.raindrop.io/more -->

# More

- [Changelog](/more/changelog.md)
- [Showcase](/more/showcase.md)



---

<!-- Source: https://developer.raindrop.io/more/changelog -->

# Changelog

### 1.0.4

* Please use `/filters/:collectionId` route instead of `/raindrops/:collectionId/filters`
* Route `GET /user/:id` removed
* Route `GET /tags/suggest` removed

### 1.0.3

* Merge and remove multiple collections endpoint

### 1.0.2

* Filters endpoint now support sorting results

### 1.0.1

* Raindrop now have `created` field
* Raindrop now update `lastUpdate` field on each update



---

<!-- Source: https://developer.raindrop.io/more/showcase -->

# Showcase

### iOS, Android

[Official Raindrop.io mobile app](https://github.com/raindropio/mobile) (Open source, JS, React Native, Redux)

{% hint style="info" %}
Currently, Raindrop.io mobile apps use a private API, but the methods and their parameters are almost equal to the ones described in this documentation
{% endhint %}

### Plugins

[Alfred Workflow](https://www.packal.org/workflow/search-raindropio) by Andreas Westerlind



---

<!-- Source: https://developer.raindrop.io/terms -->

# Terms & Guidelines

### How may I use the API? <a href="#how-may-i-use-the-api" id="how-may-i-use-the-api"></a>

#### DO <a href="#do" id="do"></a>

I encourage you to build applications that **extend** Raindrop.io to platforms beyond the web and offer services that Raindrop.io does not.

#### DON’T <a href="#dont" id="dont"></a>

Don’t build what I'm building. I invested a lot of time, money and hard work in Raindrop.io. I rely on Raindrop.io for income. As such, do not build an application, website, product, or business that attempts to harm, or replace Raindrop.io, website, or services.

In particular, do not use the API, or any Raindrop.io data, to build the following:

* A website that replicates or replaces raindrop.io

I'll do the best to communicate fair use of the Raindrop.io API in this space and others, but the onus is on you to contact me and inquire whether your use of the API is permitted.

### Commercial Use <a href="#commercial-use" id="commercial-use"></a>

You are free to use the Raindrop.io API for commercial use, provided that you abide by these terms and do not build an application or business that attempts to harm, compete with or replace Raindrop.io, our website, or our services.

### Be Gentle <a href="#be-gentle" id="be-gentle"></a>

Don’t overburden our servers. We’ve published some specifics with regard to rate limiting, but we reserve the right to determine abuse or excessive usage of the API and throttle or block any service accordingly. Attempts to circumvent rate limiting, such as leveraging multiple applications or generating bogus user accounts, are strictly prohibited.

### Termination <a href="#termination" id="termination"></a>

Raindrop.io can refuse API access at any time for any reason. This is not a card we hope to play often, but it’s impossible to anticipate every situation. We reserve the right to decline any request for API usage and block access to the API.

### Liability <a href="#liability" id="liability"></a>

Raindrop.io is not liable for any direct, indirect, incidental, special, consequential or exemplary damages arising from your use of the API. These include, but are not limited to, damages for loss of profits, goodwill, use, data or other intangible losses, resulting from your API usage or third-party products that access data via the API.

Your use of the Raindrop.io API is at your own discretion and risk, and you will be solely responsible for any damage that results its use, including, but not limited to, any damage to computer systems or loss of data incurred by you, your users, or your customers.

### Terms Can Change <a href="#terms-can-change" id="terms-can-change"></a>

Raindrop.io reserves the right to update and change these terms at any time without notice.\\



---

<!-- Source: https://developer.raindrop.io/v1 -->

# Rest API v1

- [Authentication](/v1/authentication.md)
- [Obtain access token](/v1/authentication/token.md)
- [Make authorized calls](/v1/authentication/calls.md): Build something great
- [Collections](/v1/collections.md)
- [Collection methods](/v1/collections/methods.md)
- [Nested structure](/v1/collections/nested-structure.md)
- [Sharing](/v1/collections/sharing.md): Collection can be shared with other users, which are then called collaborators, and this section describes the different commands that are related to sharing.
- [Covers/icons](/v1/collections/covers-icons.md)
- [Raindrops](/v1/raindrops.md): We call bookmarks (or items) as "raindrops"
- [Single raindrop](/v1/raindrops/single.md): In this page you will find how to retrieve, create, update or delete single raindrop.
- [Multiple raindrops](/v1/raindrops/multiple.md): In this page you will find how to retrieve, create, update or delete multiple raindrops at once.
- [Highlights](/v1/highlights.md)
- [User](/v1/user.md)
- [Authenticated user](/v1/user/authenticated.md)
- [Tags](/v1/tags.md)
- [Filters](/v1/filters.md)
- [Import](/v1/import.md): Handy methods to implement import functionality
- [Export](/v1/export.md): Export all raindrops in specific format
- [Backups](/v1/backups.md)



---

<!-- Source: https://developer.raindrop.io/v1/authentication -->

# Authentication

In order to make authorized calls to Raindrop.io API, you must do the following:

* [x] [Register your application](https://app.raindrop.io/#/settings/apps/dev)
* [x] [Obtain access token](https://developer.raindrop.io/v1/authentication/token)



---

<!-- Source: https://developer.raindrop.io/v1/authentication/calls -->

# Make authorized calls

Once you have received an **access\_token**, include it in all API calls in [authorization header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization) with value `Bearer access_token`

```http
Authorization: Bearer ae261404-11r4-47c0-bce3-e18a423da828
```



---

<!-- Source: https://developer.raindrop.io/v1/authentication/token -->

# Obtain access token

External applications could obtain a user authorized API token via the OAuth2 protocol. Before getting started, developers need to create their applications in [App Management Console](https://app.raindrop.io/settings/integrations) and configure a valid OAuth redirect URL. A registered Raindrop.io application is assigned a unique `Client ID` and `Client Secret` which are needed for the OAuth2 flow.

This procedure is comprised of several steps, which will be described below.

{% hint style="info" %}
If you just want to test your application, or do not plan to access any data except yours account you don't need to make all of those steps.

Just go to [App Management Console](https://app.raindrop.io/settings/integrations) and open your application settings. Copy **Test token** and use it as described in [**Make authorized calls**](https://developer.raindrop.io/v1/authentication/calls)**.**
{% endhint %}

## Step 1: The authorization request

<mark style="color:blue;">`GET`</mark> `https://raindrop.io/oauth/authorize`

Direct the user to our authorization URL with specified request parameters.\
— If the user is not logged in, they will be asked to log in\
— The user will be asked if he would like to grant your application access to his Raindrop.io data

#### Query Parameters

| Name          | Type   | Description                                                     |
| ------------- | ------ | --------------------------------------------------------------- |
| redirect\_uri | string | Redirect URL configured in your application setting             |
| client\_id    | string | The unique Client ID of the Raindrop.io app that you registered |

{% tabs %}
{% tab title="307 Check details in Step 2" %}

```
```

{% endtab %}
{% endtabs %}

![User will be asked if he would like to grant your application access to his Raindrop.io data](https://3611960587-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-M-GPP1TyNN8gNuijaj7%2F-M-of5es4601IU9HtzYf%2F-M-og97-rwxYlVDTb5mi%2Fauthorize.png?alt=media\&token=d81cc512-68bb-49a4-9342-f436f1b85c74)

Here example CURL request:

```bash
curl "https://api.raindrop.io/v1/oauth/authorize?client_id=5e1c382cf6f48c0211359083&redirect_uri=https:%2F%2Foauthdebugger.com%2Fdebug"
```

## Step 2: The redirection to your application site

When the user grants your authorization request, the user will be redirected to the redirect URL configured in your application setting. The redirect request will come with query parameter attached: `code` .

The `code` parameter contains the authorization code that you will use to exchange for an access token.

In case of error redirect request will come with `error` query parameter:

| Error                        | Description                                                                                                    |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------- |
| access\_denied               | When the user denies your authorization request                                                                |
| invalid\_application\_status | When your application exceeds the maximum token limit or when your application is being suspended due to abuse |

## Step 3: The token exchange

<mark style="color:green;">`POST`</mark> `https://raindrop.io/oauth/access_token`

Once you have the authorization `code`, you can exchange it for the `access_token` by doing a `POST` request with all required body parameters as JSON:

#### Headers

| Name         | Type   | Description      |
| ------------ | ------ | ---------------- |
| Content-Type | string | application/json |

#### Request Body

| Name           | Type   | Description                                                     |
| -------------- | ------ | --------------------------------------------------------------- |
| grant\_type    | string | **authorization\_code**                                         |
| code           | string | Code that you received in step 2                                |
| client\_id     | string | The unique Client ID of the Raindrop.io app that you registered |
| client\_secret | string | Client secret                                                   |
| redirect\_uri  | string | Same `redirect_uri` from step 1                                 |

{% tabs %}
{% tab title="200 " %}

```javascript
{
  "access_token": "ae261404-11r4-47c0-bce3-e18a423da828",
  "refresh_token": "c8080368-fad2-4a3f-b2c9-71d3z85011vb",
  "expires": 1209599768, //in miliseconds, deprecated
  "expires_in": 1209599, //in seconds, use this instead!!!
  "token_type": "Bearer"
}
```

{% endtab %}

{% tab title="400 Occurs when code parameter is invalid" %}

```javascript
{"error": "bad_authorization_code"}
```

{% endtab %}
{% endtabs %}

Here an example CURL request:

```bash
curl -X "POST" "https://raindrop.io/oauth/access_token" \
     -H 'Content-Type: application/json' \
     -d $'{
  "code": "c8983220-1cca-4626-a19d-801a6aae003c",
  "client_id": "5e1c589cf6f48c0211311383",
  "redirect_uri": "https://oauthdebugger.com/debug",
  "client_secret": "c3363988-9d27-4bc6-a0ae-d126ce78dc09",
  "grant_type": "authorization_code"
}'
```

## ♻️ The access token refresh

<mark style="color:green;">`POST`</mark> `https://raindrop.io/oauth/access_token`

For security reasons access tokens (except "test tokens") will **expire after two weeks**. In this case you should request the new one, by calling `POST` request with body parameters (JSON):

#### Headers

| Name         | Type   | Description      |
| ------------ | ------ | ---------------- |
| Content-Type | string | application/json |

#### Request Body

| Name           | Type   | Description                                          |
| -------------- | ------ | ---------------------------------------------------- |
| client\_id     | string | The unique Client ID of your app that you registered |
| client\_secret | string | Client secret of your app                            |
| grant\_type    | string | **refresh\_token**                                   |
| refresh\_token | string | Refresh token that you get in step 3                 |

{% tabs %}
{% tab title="200 " %}

```javascript
{
  "access_token": "ae261404-18r4-47c0-bce3-e18a423da898",
  "refresh_token": "c8080368-fad2-4a9f-b2c9-73d3z850111b",
  "expires": 1209599768, //in miliseconds, deprecated
  "expires_in": 1209599, //in seconds, use this instead!!!
  "token_type": "Bearer"
}
```

{% endtab %}
{% endtabs %}



---

<!-- Source: https://developer.raindrop.io/v1/backups -->

# Backups

## Get all

<mark style="color:blue;">`GET`</mark> `https://api.raindrop.io/rest/v1/backups`

Useful to get backup ID's that can be used in `/backup/{ID}.{format}` endpoint.

Sorted by date (new first)

{% tabs %}
{% tab title="200 " %}

```json
{
    "result": true,
    "items": [
        {
            "_id": "659d42a35ffbb2eb5ae1cb86",
            "created": "2024-01-09T12:57:07.630Z"
        }
    ]
}
```

{% endtab %}
{% endtabs %}

## Download file

<mark style="color:blue;">`GET`</mark> `https://api.raindrop.io/rest/v1/backup/{ID}.{format}`

For example:

`https://api.raindrop.io/rest/v1/backup/659d42a35ffbb2eb5ae1cb86.csv`

#### Path Parameters

| Name                                     | Type   | Description                  |
| ---------------------------------------- | ------ | ---------------------------- |
| ID<mark style="color:red;">\*</mark>     | String | Backup ID                    |
| format<mark style="color:red;">\*</mark> | String | File format: `html` or `csv` |

## Generate new

<mark style="color:blue;">`GET`</mark> `https://api.raindrop.io/rest/v1/backup`

Useful to create a brand new backup. This requires some time.

New backup will appear in the list of `/backups` endpoint

{% tabs %}
{% tab title="200 " %}

```
We will send you email with html export file when it be ready! Time depends on bookmarks count and queue.
```

{% endtab %}
{% endtabs %}



---

<!-- Source: https://developer.raindrop.io/v1/collections -->

# Collections

### Fields

| Field            | Type            | Description                                                                                                                                                                                              |
| ---------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \_id             | `Integer`       | The id of the collection.                                                                                                                                                                                |
| access           | `Object`        |                                                                                                                                                                                                          |
| access.level     | `Integer`       | <p></p><ol><li>read only access (equal to <code>public=true</code>)</li><li>collaborator with read only access</li><li>collaborator with write only access</li><li>owner</li></ol>                       |
| access.draggable | `Boolean`       | Does it possible to change parent of this collection?                                                                                                                                                    |
| collaborators    | `Object`        | <p>When this object is present, means that collections is shared. Content of this object is private and not very useful.<br>All sharing API methods <a href="collections/sharing">described here</a></p> |
| color            | `String`        | Primary color of collection cover as `HEX`                                                                                                                                                               |
| count            | `Integer`       | Count of raindrops in collection                                                                                                                                                                         |
| cover            | `Array<String>` | <p>Collection cover URL.<br>This array always have one item due to legacy reasons</p>                                                                                                                    |
| created          | `String`        | When collection is created                                                                                                                                                                               |
| expanded         | `Boolean`       | Whether the collection’s sub-collections are expanded                                                                                                                                                    |
| lastUpdate       | `String`        | When collection is updated                                                                                                                                                                               |
| parent           | `Object`        |                                                                                                                                                                                                          |
| parent.$id       | `Integer`       | The id of the parent collection. Not specified for root collections                                                                                                                                      |
| public           | `Boolean`       | Collection and raindrops that it contains will be accessible without authentication by public link                                                                                                       |
| sort             | `Integer`       | The order of collection (descending). Defines the position of the collection among all the collections with the same `parent.$id`                                                                        |
| title            | `String`        | Name of the collection                                                                                                                                                                                   |
| user             | `Object`        |                                                                                                                                                                                                          |
| user.$id         | `Integer`       | Owner ID                                                                                                                                                                                                 |
| view             | `String`        | <p>View style of collection, can be:</p><ul><li><code>list</code> (default)</li><li><code>simple</code></li><li><code>grid</code></li><li><code>masonry</code> Pinterest like grid</li></ul>             |

{% hint style="warning" %}
Our API response could contain **other fields**, not described above. It's **unsafe to use** them in your integration! They could be removed or renamed at any time.
{% endhint %}

### System collections

Every user have several system non-removable collections. They are not contained in any API responses.

| \_id    | Description               |
| ------- | ------------------------- |
| **-1**  | "**Unsorted**" collection |
| **-99** | "**Trash**" collection    |



---

<!-- Source: https://developer.raindrop.io/v1/collections/covers-icons -->

# Covers/icons

In your app you could easily make icon/cover selector from more than 10 000 icons

![](https://3611960587-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-M-GPP1TyNN8gNuijaj7%2F-M-of5es4601IU9HtzYf%2F-M-ogjIOcDvx33liprkE%2Ficon%20finder.png?alt=media\&token=4a945b4a-4fad-4671-bea9-43494e3e9136)

## Search for cover

<mark style="color:blue;">`GET`</mark> `https://api.raindrop.io/rest/v1/collections/covers/{text}`

Search for specific cover (icon)

#### Path Parameters

| Name | Type   | Description           |
| ---- | ------ | --------------------- |
| text | string | For example "pokemon" |

{% tabs %}
{% tab title="200 " %}

```javascript
{
  "items": [
    {
      "title": "Icons8",
      "icons": [
        {
          "png": "https://rd-icons-icons8.gumlet.com/color/5x/mystic-pokemon.png?fill-color=transparent"
        }
      ]
    },
    {
      "title": "Iconfinder",
      "icons": [
        {
          "png": "https://cdn4.iconfinder.com/data/icons/pokemon-go/512/Pokemon_Go-01-128.png",
          "svg": "https://api.iconfinder.com/v2/icons/1320040/formats/svg/1760420/download"
        }
      ]
    }
  ],
  "result": true
}
```

{% endtab %}
{% endtabs %}

## Featured covers

<mark style="color:blue;">`GET`</mark> `https://api.raindrop.io/rest/v1/collections/covers`

#### Path Parameters

| Name | Type   | Description |
| ---- | ------ | ----------- |
|      | string |             |

{% tabs %}
{% tab title="200 " %}

```javascript
{
  "items": [
    {
      "title": "Colors circle",
      "icons": [
        {
          "png": "https://up.raindrop.io/collection/templates/colors/ios1.png"
        }
      ]
    },
    {
      "title": "Hockey",
      "icons": [
        {
          "png": "https://up.raindrop.io/collection/templates/hockey-18/12i.png"
        }
      ]
    }
  ]
}
```

{% endtab %}
{% endtabs %}



---

<!-- Source: https://developer.raindrop.io/v1/collections/methods -->

# Collection methods

## Get root collections

<mark style="color:blue;">`GET`</mark> `https://api.raindrop.io/rest/v1/collections`

Returns JSON-encoded array containing all root collections

{% tabs %}
{% tab title="200 " %}

```javascript
{
  "result": true,
  "items": [
    {
      "_id": 8492393,
      "access": {
        "level": 4,
        "draggable": true
      },
      "collaborators": {
        "$id": "5dc1759a0e123be5f2654b6f"
      },
      "color": "#0c797d",
      "count": 16,
      "cover": [
        "https://up.raindrop.io/collection/thumbs/849/239/3/333ce18769311113836cf93a223a14a3.png"
      ],
      "created": "2019-10-09T11:49:53.518Z",
      "expanded": false,
      "lastUpdate": "2019-11-27T17:51:19.085Z",
      "public": false,
      "sort": 8492393,
      "title": "Development",
      "user": {
        "$id": 32
      },
      "view": "list"
    }
  ]
}
```

{% endtab %}
{% endtabs %}

## Get child collections

<mark style="color:blue;">`GET`</mark> `https://api.raindrop.io/rest/v1/collections/childrens`

Returns JSON-encoded array containing all nested collections (that have positive `parent.$id`)

{% tabs %}
{% tab title="200 " %}

```javascript
{
  "result": true,
  "items": [
    {
      "_id": 8492393,
      "access": {
        "level": 4,
        "draggable": true
      },
      "collaborators": {
        "$id": "5dc1759a0e123be5f2654b6f"
      },
      "color": "#0c797d",
      "count": 16,
      "cover": [
        "https://up.raindrop.io/collection/thumbs/849/239/3/333ce18769311113836cf93a223a14a3.png"
      ],
      "created": "2019-10-09T11:49:53.518Z",
      "expanded": false,
      "lastUpdate": "2019-11-27T17:51:19.085Z",
      "parent": { "$id": 1111 },
      "public": false,
      "sort": 8492393,
      "title": "Development",
      "user": {
        "$id": 32
      },
      "view": "list"
    }
  ]
}
```

{% endtab %}
{% endtabs %}

## Get collection

<mark style="color:blue;">`GET`</mark> `https://api.raindrop.io/rest/v1/collection/{id}`

#### Path Parameters

| Name | Type   | Description   |
| ---- | ------ | ------------- |
| id   | number | Collection ID |

{% tabs %}
{% tab title="200 " %}

```javascript
{
  "result": true,
  "item": {
    "_id": 8492393,
    "access": {
      "for": 32,
      "level": 4,
      "root": true,
      "draggable": true
    },
    "author": true,
    "collaborators": {
      "$id": "5dc1759a0e123be5f2654b6f"
    },
    "color": "#0c797d",
    "count": 16,
    "cover": [
      "https://up.raindrop.io/collection/thumbs/849/239/3/333ce18769311113836cf93a223a14a3.png"
    ],
    "created": "2019-10-09T11:49:53.518Z",
    "expanded": false,
    "lastUpdate": "2019-11-27T17:51:19.085Z",
    "public": false,
    "sort": 8492393,
    "title": "Development",
    "user": {
      "$id": 32
    },
    "view": "list"
  }
}
```

{% endtab %}
{% endtabs %}

## Create collection

<mark style="color:green;">`POST`</mark> `https://api.raindrop.io/rest/v1/collection`

Create a new collection

#### Request Body

| Name       | Type    | Description                                                                                                                       |
| ---------- | ------- | --------------------------------------------------------------------------------------------------------------------------------- |
| view       | string  | More details in "Fields"                                                                                                          |
| title      | string  | Name of the collection                                                                                                            |
| sort       | number  | The order of collection (descending). Defines the position of the collection among all the collections with the same `parent.$id` |
| public     | boolean | Collection and raindrops that it contains will be accessible without authentication?                                              |
| parent.$id | integer | The ID of parent collection. Empty for root collections                                                                           |
| cover      | array   | Collection cover url                                                                                                              |

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "result": true,
    "item": {
        ...
    }
}
```

{% endtab %}

{% tab title="400 Incorrect 'view' field value" %}

```javascript
{
    "result": false,
    "error": "view",
    "errorMessage": "Collection validation failed: view: `bla` is not a valid enum value for path `view`."
}
```

{% endtab %}
{% endtabs %}

## Update collection

<mark style="color:orange;">`PUT`</mark> `https://api.raindrop.io/rest/v1/collection/{id}`

Update an existing collection

#### Path Parameters

| Name | Type   | Description            |
| ---- | ------ | ---------------------- |
| id   | number | Existing collection id |

#### Request Body

| Name       | Type    | Description                                                                                                                       |
| ---------- | ------- | --------------------------------------------------------------------------------------------------------------------------------- |
| expanded   | boolean | Whether the collection\`s sub-collections are expanded                                                                            |
| view       | string  | More details in "Fields"                                                                                                          |
| title      | string  | Name of the collection                                                                                                            |
| sort       | number  | The order of collection (descending). Defines the position of the collection among all the collections with the same `parent.$id` |
| public     | boolean | Collection and raindrops that it contains will be accessible without authentication?                                              |
| parent.$id | integer | The ID of parent collection. Empty for root collections                                                                           |
| cover      | array   | Collection cover url                                                                                                              |

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "result": true,
    "item": {
        ...
    }
}
```

{% endtab %}
{% endtabs %}

## Upload cover

<mark style="color:orange;">`PUT`</mark> `https://api.raindrop.io/rest/v1/collection/{id}/cover`

It's possible to upload cover from desktop. PNG, GIF and JPEG supported

#### Path Parameters

| Name | Type   | Description            |
| ---- | ------ | ---------------------- |
| id   | string | Existing collection ID |

#### Headers

| Name         | Type   | Description         |
| ------------ | ------ | ------------------- |
| Content-Type | string | multipart/form-data |

#### Request Body

| Name  | Type   | Description |
| ----- | ------ | ----------- |
| cover | object | File        |

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "result": true,
    "item": {
        ...
    }
}
```

{% endtab %}
{% endtabs %}

## Remove collection

<mark style="color:red;">`DELETE`</mark> `https://api.raindrop.io/rest/v1/collection/{id}`

Remove an existing collection and all its descendants.\
Raindrops will be moved to "Trash" collection

#### Path Parameters

| Name | Type   | Description            |
| ---- | ------ | ---------------------- |
| id   | number | Existing collection ID |

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "result": true
}
```

{% endtab %}
{% endtabs %}

## Remove multiple collections

<mark style="color:red;">`DELETE`</mark> `https://api.raindrop.io/rest/v1/collections`

Remove multiple collections at once.\
Nested collections are ignored (include ID's in `ids` array to remove them)

#### Request Body

| Name | Type  | Description            |
| ---- | ----- | ---------------------- |
| ids  | array | Array of collection ID |

{% tabs %}
{% tab title="200 " %}

```
```

{% endtab %}
{% endtabs %}

## Reorder all collections

<mark style="color:orange;">`PUT`</mark> `https://api.raindrop.io/rest/v1/collections`

Updates order of all collections&#x20;

#### Request Body

| Name | Type   | Description                                                                                                                                                                                          |
| ---- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| sort | string | <p>Change order of all collections.<br>Possible values:<br>"title" - sort alphabetically ascending<br>"-title" - sort alphabetically descending<br>"-count" - sort by raindrops count descending</p> |

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "result": true
}
```

{% endtab %}
{% endtabs %}

## Expand/collapse all collections

<mark style="color:orange;">`PUT`</mark> `https://api.raindrop.io/rest/v1/collections`

#### Path Parameters

| Name     | Type    | Description                                      |
| -------- | ------- | ------------------------------------------------ |
| expanded | boolean | <p>TRUE = expand all<br>FALSE = collapse all</p> |

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "result": true
}
```

{% endtab %}
{% endtabs %}

## Merge collections

<mark style="color:orange;">`PUT`</mark> `https://api.raindrop.io/rest/v1/collections/merge`

Merge multiple collections

#### Request Body

| Name | Type   | Description                                                |
| ---- | ------ | ---------------------------------------------------------- |
| to   | number | Collection ID where listed collection `ids` will be merged |
| ids  | array  | Collection ID's                                            |

{% tabs %}
{% tab title="200 " %}

```
```

{% endtab %}
{% endtabs %}

## Remove all empty collections

<mark style="color:orange;">`PUT`</mark> `https://api.raindrop.io/rest/v1/collections/clean`

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "result": true,
    "count": 3
}
```

{% endtab %}
{% endtabs %}

## Empty Trash

<mark style="color:red;">`DELETE`</mark> `https://api.raindrop.io/rest/v1/collection/-99`

{% tabs %}
{% tab title="200 " %}

```javascript
{
  "result": true
}
```

{% endtab %}
{% endtabs %}

## Get system collections count

<mark style="color:blue;">`GET`</mark> `https://api.raindrop.io/rest/v1/user/stats`

{% tabs %}
{% tab title="200 " %}

```javascript
{
  "items": [
    {
      "_id": 0,
      "count": 1570
    },
    {
      "_id": -1,
      "count": 34
    },
    {
      "_id": -99,
      "count": 543
    }
  ],
  "meta": {
    "pro": true,
    "_id": 32,
    "changedBookmarksDate": "2020-02-11T11:23:43.143Z",
    "duplicates": {
      "count": 3
    },
    "broken": {
      "count": 31
    }
  },
  "result": true
}
```

{% endtab %}
{% endtabs %}



---

<!-- Source: https://developer.raindrop.io/v1/collections/nested-structure -->

# Nested structure

### Overview

If you look into Raindrop UI you will notice a sidebar in left corner, where collections are located. Collections itself divided by groups. Groups useful to create separate sets of collections, for example "Home", "Work", etc.

![](https://3611960587-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-M-GPP1TyNN8gNuijaj7%2F-M-odRbpHbUQpG6FIdE7%2F-M-oefnkLiSk6-lmT35A%2Fsidebar.png?alt=media\&token=e4070997-e45a-4310-a848-10995a597a6a)

`Groups` array is a single place where user **root** collection list and order is persisted. Why just not to save order position inside collection item itself? Because collections can be shared and they group and order can vary from user to user.

So to fully recreate sidebar like in our app you need to make 3 separate API calls (sorry, will be improved in future API updates):

#### 1. [Get user object](https://developer.raindrop.io/user/authenticated#get-user)

It contains `groups` array with exact collection ID's. Typically this array looks like this:

```javascript
{
  "groups": [
    {
      "title": "Home",
      "hidden": false,
      "sort": 0,
      "collections": [
        8364483,
        8364403,
        66
      ]
    },
    {
      "title": "Work",
      "hidden": false,
      "sort": 1,
      "collections": [
        8492393
      ]
    }
  ]
}
```

{% hint style="warning" %}
Collection ID's listed below is just first level of collections structure! To create full tree of nested collections you need to get child items separately.
{% endhint %}

To get name, count, icon and other info about collections, make those two separate calls:

#### 2. [Get root collections](https://developer.raindrop.io/v1/methods#get-root-collections)

Sort order of root collections persisted in `groups[].collections` array

#### 3. [Get child collections](https://developer.raindrop.io/v1/methods#get-child-collections)

Sort order of child collections persisted in collection itself in `sort` field



---

<!-- Source: https://developer.raindrop.io/v1/collections/sharing -->

# Sharing

### Collaborators

Every user who shares at least one collection with another user, has a collaborators record in the API response. The record contains a restricted subset of user-specific fields.

| Field      | Description                                                                                                                                                             |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \_id       | User ID of the collaborator                                                                                                                                             |
| email      | <p>Email of the collaborator</p><p>Empty when authorized user have read-only access</p>                                                                                 |
| email\_MD5 | MD5 hash of collaborator email. Useful for using with Gravatar for example                                                                                              |
| fullName   | Full name of the collaborator                                                                                                                                           |
| role       | <p>Access level:</p><p><strong><code>member</code></strong> have write access and can invite more users</p><p><strong><code>viewer</code></strong> read-only access</p> |

## Share collection

<mark style="color:green;">`POST`</mark> `https://api.raindrop.io/rest/v1/collection/{id}/sharing`

Share collection with another user(s). As result invitation(s) will be send to specified email(s) with link to join collection.

#### Path Parameters

| Name | Type   | Description            |
| ---- | ------ | ---------------------- |
| id   | number | Existing collection ID |

#### Request Body

| Name   | Type   | Description                                                                                                           |
| ------ | ------ | --------------------------------------------------------------------------------------------------------------------- |
| role   | string | <p>Access level. Possible values:<br><strong><code>member</code></strong><br><strong><code>viewer</code></strong></p> |
| emails | array  | <p>The user email(s) with whom to share the project.<br>Maximum 10</p>                                                |

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "result": true,
    "emails": [
        "some@user.com",
        "other@user.com"
    ]
}
```

{% endtab %}

{% tab title="400 " %}

```javascript
//'emails' array is empty
{
    "result": false,
    "errorMessage": "no emails"
}

//'emails' array larger than 10
{
    "result": false,
    "errorMessage": "you cant send more than 10 invites at once"
}
```

{% endtab %}

{% tab title="403 " %}

```javascript
//When user have more than 100 pending invitations:
{
    "result": false,
    "errorMessage": "you have too many pending invitations, you will be banned if you continue send more"
}

//User doesn't have enought permissions to invite more people
{
    "result": false,
    "errorMessage": "you dont have permissions to invite more people"
}
```

{% endtab %}
{% endtabs %}

## Get collaborators list of collection

<mark style="color:blue;">`GET`</mark> `https://api.raindrop.io/rest/v1/collection/{id}/sharing`

#### Path Parameters

| Name | Type   | Description            |
| ---- | ------ | ---------------------- |
| id   | number | Existing collection ID |

{% tabs %}
{% tab title="200 " %}

```javascript
{
  "items": [
    {
      "_id": 373381,
      "email": "some@mail.com",
      "email_MD5": "e12bda18ca265d3f3e30d247adea2549",
      "fullName": "Jakie Future",
      "registered": "2019-08-18T17:01:43.664Z",
      "role": "viewer"
    }
  ],
  "result": true
}
```

{% endtab %}
{% endtabs %}

## Unshare or leave collection

<mark style="color:red;">`DELETE`</mark> `https://api.raindrop.io/rest/v1/collection/{id}/sharing`

There two possible results of calling this method, depends on who authenticated user is:\
\- **Owner**: collection will be unshared and all collaborators will be removed\
\- **Member or viewer**: authenticated user will be removed from collaborators list

#### Path Parameters

| Name | Type   | Description            |
| ---- | ------ | ---------------------- |
| id   | number | Existing collection ID |

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "result": true
}
```

{% endtab %}
{% endtabs %}

## Change access level of collaborator

<mark style="color:orange;">`PUT`</mark> `https://api.raindrop.io/rest/v1/collection/{id}/sharing/{userId}`

#### Path Parameters

| Name   | Type   | Description             |
| ------ | ------ | ----------------------- |
| userId | number | User ID of collaborator |
| id     | number | Existing collection ID  |

#### Request Body

| Name | Type   | Description                  |
| ---- | ------ | ---------------------------- |
| role | string | **`member`** or **`viewer`** |

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "result": true
}
```

{% endtab %}
{% endtabs %}

## Delete a collaborator

<mark style="color:red;">`DELETE`</mark> `https://api.raindrop.io/rest/v1/collection/{id}/sharing/{userId}`

Remove an user from shared collection

#### Path Parameters

| Name   | Type   | Description             |
| ------ | ------ | ----------------------- |
| userId | number | User ID of collaborator |
| id     | number | Existing collection ID  |

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "result": true
}
```

{% endtab %}
{% endtabs %}

## Accept an invitation

<mark style="color:green;">`POST`</mark> `https://api.raindrop.io/rest/v1/collection/{id}/join`

Accept an invitation to join a shared collection

#### Path Parameters

| Name | Type   | Description            |
| ---- | ------ | ---------------------- |
| id   | number | Existing collection ID |

#### Request Body

| Name  | Type   | Description             |
| ----- | ------ | ----------------------- |
| token | string | Secret token from email |

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "result": true,
    "role": "member"
}
```

{% endtab %}

{% tab title="403 " %}

```javascript
//Incorrect token
{
    "result": false,
    "error": "CollaboratorsIncorrectToken",
    "errorMessage": "Incorrect or expired token"
}

//Collection no more exists
{
    "result": false,
    "error": "CollaboratorsNoCollection",
    "errorMessage": "Shared collection not found or removed"
}

{
    "result": false,
    "error": "CollaboratorsAlready",
    "errorMessage": "You already owner of this collection"
}
```

{% endtab %}
{% endtabs %}



---

<!-- Source: https://developer.raindrop.io/v1/export -->

# Export

## Export in format

<mark style="color:green;">`GET`</mark> `https://api.raindrop.io/rest/v1/raindrops/{collectionId}/export.{format}`

**Path Parameters**

<table><thead><tr><th width="243">Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>collectionId</code><mark style="color:red;">*</mark></td><td>number</td><td>Collection ID. Specify <code>0</code> to get all raindrops</td></tr><tr><td><code>format</code><mark style="color:red;">*</mark></td><td>string</td><td><code>csv</code>, <code>html</code> or <code>zip</code></td></tr></tbody></table>

**Query Parameters**

<table><thead><tr><th width="243">Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>sort</code></td><td>string</td><td>Check <a href="https://developer.raindrop.io/v1/raindrops/multiple">https://developer.raindrop.io/v1/raindrops/multiple</a></td></tr><tr><td><code>search</code></td><td>string</td><td>Check <a href="https://developer.raindrop.io/v1/raindrops/multiple">https://developer.raindrop.io/v1/raindrops/multiple</a></td></tr></tbody></table>



---

<!-- Source: https://developer.raindrop.io/v1/filters -->

# Filters

To help users easily find their content you can suggest context aware filters like we have in Raindrop.io app

![Filters right above search field](https://3611960587-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-M-GPP1TyNN8gNuijaj7%2F-M-oej2Q4_QeQb3lfFaV%2F-M-of2jvit9BqVisVU9y%2Ffilters.png?alt=media\&token=d1992f10-6dc3-401c-9332-81e69fc876ac)

## Fields

| Field            | Type            | Description                                              |
| ---------------- | --------------- | -------------------------------------------------------- |
| broken           | `Object`        |                                                          |
| broken.count     | `Integer`       | Broken links count                                       |
| duplicates       | `Object`        |                                                          |
| duplicates.count | `Integer`       | Duplicate links count                                    |
| important        | `Object`        |                                                          |
| important.count  | `Integer`       | Count of raindrops that marked as "favorite"             |
| notag            | `Object`        |                                                          |
| notag.count      | `Integer`       | Count of raindrops without any tag                       |
| tags             | `Array<Object>` | List of tags in format `{"_id": "tag name", "count": 1}` |
| types            | `Array<Object>` | List of types in format `{"_id": "type", "count": 1}`    |

## Get filters

<mark style="color:blue;">`GET`</mark> `https://api.raindrop.io/rest/v1/filters/{collectionId}`

#### Path Parameters

| Name         | Type   | Description                |
| ------------ | ------ | -------------------------- |
| collectionId | string | Collection ID. `0` for all |

#### Query Parameters

| Name     | Type   | Description                                                                                                                  |
| -------- | ------ | ---------------------------------------------------------------------------------------------------------------------------- |
| tagsSort | string | <p>Sort tags by:<br><strong><code>-count</code></strong> by count, default<br><strong><code>\_id</code></strong> by name</p> |
| search   | string | Check "raindrops" documentation for more details                                                                             |

{% tabs %}
{% tab title="200 " %}

```javascript
{
  "result": true,
  "broken": {
    "count": 31
  },
  "duplicates": {
    "count": 7
  },
  "important": {
    "count": 59
  },
  "notag": {
    "count": 1366
  },
  "tags": [
    {
      "_id": "performanc",
      "count": 19
    },
    {
      "_id": "guides",
      "count": 9
    }
  ],
  "types": [
    {
      "_id": "article",
      "count": 313
    },
    {
      "_id": "image",
      "count": 143
    },
    {
      "_id": "video",
      "count": 26
    },
    {
      "_id": "document",
      "count": 7
    }
  ]
}
```

{% endtab %}
{% endtabs %}



---

<!-- Source: https://developer.raindrop.io/v1/highlights -->

# Highlights

Single `highlight` object:

| Field   | Type     | Description                                                                                                                                                                                                                                                                                                          |
| ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \_id    | `String` | Unique id of highlight                                                                                                                                                                                                                                                                                               |
| text    | `String` | Text of highlight (required)                                                                                                                                                                                                                                                                                         |
| title   | `String` | Title of bookmark                                                                                                                                                                                                                                                                                                    |
| color   | `String` | <p>Color of highlight. <br>Default <code>yellow</code><br><br>Can be <code>blue</code>, <code>brown</code>, <code>cyan</code>, <code>gray</code>, <code>green</code>, <code>indigo</code>, <code>orange</code>, <code>pink</code>, <code>purple</code>, <code>red</code>, <code>teal</code>, <code>yellow</code></p> |
| note    | `String` | Optional note for highlight                                                                                                                                                                                                                                                                                          |
| created | `String` | Creation date of highlight                                                                                                                                                                                                                                                                                           |
| tags    | `Array`  | Tags list                                                                                                                                                                                                                                                                                                            |
| link    | `String` | Highlighted page URL                                                                                                                                                                                                                                                                                                 |

## Get all highlights

<mark style="color:blue;">`GET`</mark> `https://api.raindrop.io/rest/v1/highlights`

#### Query Parameters

| Name    | Type   | Description                                      |
| ------- | ------ | ------------------------------------------------ |
| page    | Number |                                                  |
| perpage | Number | How many highlights per page. 50 max. Default 25 |

{% tabs %}
{% tab title="200: OK " %}

```javascript
{
    "result": true,
    "items": [
        {
            "note": "Trully native macOS app",
            "color": "red",
            "text": "Orion is the new WebKit-based browser for Mac",
            "created": "2022-03-21T14:41:34.059Z",
            "tags": ["tag1", "tag2"],
            "_id": "62388e9e48b63606f41e44a6",
            "raindropRef": 123,
            "link": "https://apple.com",
            "title": "Orion Browser"
        },
        {
            "note": "",
            "color": "green",
            "text": "Built on WebKit, Orion gives you a fast, smooth and lightweight browsing experience",
            "created": "2022-03-21T15:13:21.128Z",
            "tags": ["tag1", "tag2"],
            "_id": "62389611058af151c840f667",
            "raindropRef": 123,
            "link": "https://apple.com",
            "title": "Apple"
        }
    ]
}
```

{% endtab %}
{% endtabs %}

## Get all highlights in a collection

<mark style="color:blue;">`GET`</mark> `https://api.raindrop.io/rest/v1/highlights/{collectionId}`

#### Path Parameters

| Name                                           | Type   | Description                                      |
| ---------------------------------------------- | ------ | ------------------------------------------------ |
| collectionId<mark style="color:red;">\*</mark> | Number | Collection ID                                    |
| page                                           | Number |                                                  |
| perpage                                        | Number | How many highlights per page. 50 max. Default 25 |

{% tabs %}
{% tab title="200: OK " %}

```javascript
{
    "result": true,
    "items": [
        {
            "note": "Trully native macOS app",
            "color": "red",
            "text": "Orion is the new WebKit-based browser for Mac",
            "created": "2022-03-21T14:41:34.059Z",
            "tags": ["tag1", "tag2"],
            "_id": "62388e9e48b63606f41e44a6",
            "raindropRef": 123,
            "link": "https://apple.com",
            "title": "Apple"
        },
        {
            "note": "",
            "color": "green",
            "text": "Built on WebKit, Orion gives you a fast, smooth and lightweight browsing experience",
            "created": "2022-03-21T15:13:21.128Z",
            "tags": ["tag1", "tag2"],
            "_id": "62389611058af151c840f667",
            "raindropRef": 123,
            "link": "https://apple.com",
            "title": "Apple"
        }
    ]
}
```

{% endtab %}
{% endtabs %}

## Get highlights of raindrop

<mark style="color:blue;">`GET`</mark> `https://api.raindrop.io/rest/v1/raindrop/{id}`

#### Path Parameters

| Name                                 | Type   | Description          |
| ------------------------------------ | ------ | -------------------- |
| id<mark style="color:red;">\*</mark> | number | Existing raindrop ID |

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "result": true,
    "item": {
        "_id": 373777232,
        "highlights": [
            {
                "note": "Trully native macOS app",
                "color": "red",
                "text": "Orion is the new WebKit-based browser for Mac",
                "created": "2022-03-21T14:41:34.059Z",
                "lastUpdate": "2022-03-22T14:30:52.004Z",
                "_id": "62388e9e48b63606f41e44a6"
            },
            {
                "note": "",
                "color": "green",
                "text": "Built on WebKit, Orion gives you a fast, smooth and lightweight browsing experience",
                "created": "2022-03-21T15:13:21.128Z",
                "lastUpdate": "2022-03-22T09:15:18.751Z",
                "_id": "62389611058af151c840f667"
            }
        ]
    }
}
```

{% endtab %}
{% endtabs %}

## Add highlight

<mark style="color:orange;">`PUT`</mark> `https://api.raindrop.io/rest/v1/raindrop/{id}`

Just specify a `highlights` array in body with `object` for each highlight

**Fore example:**

`{"highlights": [ { "text": "Some quote", "color": "red", "note": "Some note" } ] }`

#### Path Parameters

| Name                                 | Type   | Description          |
| ------------------------------------ | ------ | -------------------- |
| id<mark style="color:red;">\*</mark> | number | Existing raindrop ID |

#### Request Body

| Name                                                 | Type   | Description |
| ---------------------------------------------------- | ------ | ----------- |
| highlights<mark style="color:red;">\*</mark>         | array  |             |
| highlights\[].text<mark style="color:red;">\*</mark> | String |             |
| highlights\[].note                                   | String |             |
| highlights\[].color                                  | String |             |

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "result": true,
    "item": {
        "_id": 373777232,
        "highlights": [
            {
                "note": "Trully native macOS app",
                "color": "red",
                "text": "Orion is the new WebKit-based browser for Mac",
                "created": "2022-03-21T14:41:34.059Z",
                "lastUpdate": "2022-03-22T14:30:52.004Z",
                "_id": "62388e9e48b63606f41e44a6"
            },
            {
                "note": "",
                "color": "green",
                "text": "Built on WebKit, Orion gives you a fast, smooth and lightweight browsing experience",
                "created": "2022-03-21T15:13:21.128Z",
                "lastUpdate": "2022-03-22T09:15:18.751Z",
                "_id": "62389611058af151c840f667"
            }
        ]
    }
}
```

{% endtab %}
{% endtabs %}

## Update highlight

<mark style="color:orange;">`PUT`</mark> `https://api.raindrop.io/rest/v1/raindrop/{id}`

Just specify a `highlights` array in body with `object` containing particular `_id` of highlight you want to update and all other fields you want to change.

**Fore example:**

`{"highlights": [ { "_id": "62388e9e48b63606f41e44a6", "note": "New note" } ] }`

#### Path Parameters

| Name                                 | Type   | Description          |
| ------------------------------------ | ------ | -------------------- |
| id<mark style="color:red;">\*</mark> | number | Existing raindrop ID |

#### Request Body

| Name                                                 | Type   | Description                                  |
| ---------------------------------------------------- | ------ | -------------------------------------------- |
| highlights<mark style="color:red;">\*</mark>         | array  |                                              |
| highlights\[].\_id<mark style="color:red;">\*</mark> | String | Particular highlight \_id you want to remove |
| highlights\[].text                                   | String | Should be empty string                       |
| highlights\[].note                                   | String |                                              |
| highlights\[].color                                  | String |                                              |

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "result": true,
    "item": {
        "_id": 373777232,
        "highlights": [
            {
                "note": "Trully native macOS app",
                "color": "red",
                "text": "Orion is the new WebKit-based browser for Mac",
                "created": "2022-03-21T14:41:34.059Z",
                "lastUpdate": "2022-03-22T14:30:52.004Z",
                "_id": "62388e9e48b63606f41e44a6"
            },
            {
                "note": "",
                "color": "green",
                "text": "Built on WebKit, Orion gives you a fast, smooth and lightweight browsing experience",
                "created": "2022-03-21T15:13:21.128Z",
                "lastUpdate": "2022-03-22T09:15:18.751Z",
                "_id": "62389611058af151c840f667"
            }
        ]    }}
```

{% endtab %}
{% endtabs %}

## Remove highlight

<mark style="color:orange;">`PUT`</mark> `https://api.raindrop.io/rest/v1/raindrop/{id}`

Just specify a `highlights` array in body with `object` containing particular `_id` of highlight you want to remove and empty string for `text` field.

**Fore example:**

`{"highlights": [ { "_id": "62388e9e48b63606f41e44a6", "text": "" } ] }`

#### Path Parameters

| Name                                 | Type   | Description          |
| ------------------------------------ | ------ | -------------------- |
| id<mark style="color:red;">\*</mark> | number | Existing raindrop ID |

#### Request Body

| Name                                                 | Type   | Description                                  |
| ---------------------------------------------------- | ------ | -------------------------------------------- |
| highlights<mark style="color:red;">\*</mark>         | array  |                                              |
| highlights\[].\_id<mark style="color:red;">\*</mark> | String | Particular highlight \_id you want to remove |
| highlights\[].text<mark style="color:red;">\*</mark> | String | Should be empty string                       |

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "result": true,
    "item": {
        "_id": 373777232,
        "highlights": [
            {
                "note": "Trully native macOS app",
                "color": "red",
                "text": "Orion is the new WebKit-based browser for Mac",
                "created": "2022-03-21T14:41:34.059Z",
                "lastUpdate": "2022-03-22T14:30:52.004Z",
                "_id": "62388e9e48b63606f41e44a6"
            },
            {
                "note": "",
                "color": "green",
                "text": "Built on WebKit, Orion gives you a fast, smooth and lightweight browsing experience",
                "created": "2022-03-21T15:13:21.128Z",
                "lastUpdate": "2022-03-22T09:15:18.751Z",
                "_id": "62389611058af151c840f667"
            }
        ]
    }}
```

{% endtab %}
{% endtabs %}



---

<!-- Source: https://developer.raindrop.io/v1/import -->

# Import

## Parse URL

<mark style="color:blue;">`GET`</mark> `https://api.raindrop.io/rest/v1/import/url/parse`

Parse and extract useful info from any URL

#### Query Parameters

| Name | Type   | Description |
| ---- | ------ | ----------- |
| url  | string | URL         |

{% tabs %}
{% tab title="200 " %}

```javascript
//Success
{
  "item": {
    "title": "Яндекс",
    "excerpt": "Найдётся всё",
    "media": [
      {
        "type": "image",
        "link": "http://yastatic.net/s3/home/logos/share/share-logo_ru.png"
      }
    ],
    "type": "link",
    "meta": {
      "possibleArticle": false,
      "canonical": "https://ya.ru",
      "site": "Яндекс",
      "tags": []
    }
  },
  "result": true
}

//Invalid URL
{
  "error": "not_found",
  "errorMessage": "invalid_url",
  "item": {
    "title": "Fdfdfdf",
    "excerpt": "",
    "media": [
      {
        "link": "<screenshot>"
      }
    ],
    "type": "link",
    "parser": "local",
    "meta": {
      "possibleArticle": false,
      "tags": []
    }
  },
  "result": true
}

//Not found
{
  "error": "not_found",
  "errorMessage": "url_status_404",
  "item": {
    "title": "Some",
    "excerpt": "",
    "media": [
      {
        "link": "<screenshot>"
      }
    ],
    "type": "link",
    "parser": "local",
    "meta": {
      "possibleArticle": false,
      "tags": []
    }
  },
  "result": true
}
```

{% endtab %}
{% endtabs %}

## Check URL(s) existence&#x20;

<mark style="color:green;">`POST`</mark> `https://api.raindrop.io/rest/v1/import/url/exists`

Does specified URL's are already saved?

#### Request Body

| Name | Type  | Description |
| ---- | ----- | ----------- |
| urls | array | URL's       |

{% tabs %}
{% tab title="200 ids array contains ID of existing bookmarks" %}

```javascript
//Found
{
    "result": true,
    "ids": [
        3322,
        12323
    ]
}

//Not found
{
    "result": false,
    "ids": []
}
```

{% endtab %}
{% endtabs %}

## Parse HTML import file

<mark style="color:green;">`POST`</mark> `https://api.raindrop.io/rest/v1/import/file`

Convert HTML bookmark file to JSON. \
Support Nestcape, Pocket and Instapaper file formats

#### Headers

| Name         | Type   | Description         |
| ------------ | ------ | ------------------- |
| Content-Type | string | multipart/form-data |

#### Request Body

| Name   | Type   | Description |
| ------ | ------ | ----------- |
| import | string | File        |

{% tabs %}
{% tab title="200 " %}

```javascript
{
  "result": true,
  "items": [
    {
      "title": "Web",
      "folders": [
        {
          "title": "Default",
          "folders": [],
          "bookmarks": [
            {
              "link": "https://aaa.com/a",
              "title": "Name 1",
              "lastUpdate": "2016-09-13T11:17:09.000Z",
              "tags": ["tag"],
              "excerpt": ""
            }
          ]
        }
      ],
      "bookmarks": [
        {
          "link": "https://bbb.com/b",
          "title": "Name 2",
          "lastUpdate": "2016-09-13T11:17:09.000Z",
          "tags": ["tag"],
          "excerpt": ""
        }
      ]
    },
    {
      "title": "Home",
      "folders": [
        {
          "title": "Inspiration",
          "folders": [],
          "bookmarks": [
            {
              "link": "https://ccc.com/c",
              "title": "Name 3",
              "lastUpdate": "2016-09-13T11:17:09.000Z",
              "tags": ["tag"],
              "excerpt": ""
            }
          ]
        }
      ],
      "bookmarks": []
    }
  ]
}
```

{% endtab %}
{% endtabs %}



---

<!-- Source: https://developer.raindrop.io/v1/raindrops -->

# Raindrops

### Main fields

| Field          | Type            | Description                                                                       |
| -------------- | --------------- | --------------------------------------------------------------------------------- |
| \_id           | `Integer`       | Unique identifier                                                                 |
| collection     | `Object`        | ​                                                                                 |
| collection.$id | `Integer`       | Collection that the raindrop resides in                                           |
| cover          | `String`        | Raindrop cover URL                                                                |
| created        | `String`        | Creation date                                                                     |
| domain         | `String`        | <p>Hostname of a link.<br>Files always have <code>raindrop.io</code> hostname</p> |
| excerpt        | `String`        | Description; max length: 10000                                                    |
| note           | `String`        | Note; max length: 10000                                                           |
| lastUpdate     | `String`        | Update date                                                                       |
| link           | `String`        | URL                                                                               |
| media          | `Array<Object>` | ​Covers list in format: `[ {"link":"url"} ]`                                      |
| tags           | `Array<String>` | Tags list                                                                         |
| title          | `String`        | Title; max length: 1000                                                           |
| type           | `String`        | `link` `article` `image` `video` `document` or `audio`                            |
| user           | `Object`        | ​                                                                                 |
| user.$id       | `Integer`       | Raindrop owner                                                                    |

### Other fields

| Field                 | Type      | Description                                                                                                                                                                                                                                                                                                          |
| --------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| broken                | `Boolean` | Marked as broken (original `link` is not reachable anymore)                                                                                                                                                                                                                                                          |
| cache                 | `Object`  | Permanent copy (cached version) details                                                                                                                                                                                                                                                                              |
| cache.status          | `String`  | `ready` `retry` `failed` `invalid-origin` `invalid-timeout` or `invalid-size`                                                                                                                                                                                                                                        |
| cache.size            | `Integer` | Full size in bytes                                                                                                                                                                                                                                                                                                   |
| cache.created         | `String`  | Date when copy is successfully made                                                                                                                                                                                                                                                                                  |
| creatorRef            | `Object`  | <p>Sometime raindrop may belong to other user, not to the one who created it. <br>For example when this raindrop is created in shared collection by other user.<br>This object contains info about original author.</p>                                                                                              |
| creatorRef.\_id       | `Integer` | Original author (user ID) of a raindrop                                                                                                                                                                                                                                                                              |
| creatorRef.fullName   | `String`  | Original author name of a raindrop                                                                                                                                                                                                                                                                                   |
| file                  | `Object`  | <p>This raindrop uploaded from desktop</p><p><a href="https://help.raindrop.io/article/48-uploading-files">Supported file formats</a></p>                                                                                                                                                                            |
| file.name             | `String`  | File name                                                                                                                                                                                                                                                                                                            |
| file.size             | `Integer` | File size in bytes                                                                                                                                                                                                                                                                                                   |
| file.type             | `String`  | Mime type                                                                                                                                                                                                                                                                                                            |
| important             | `Boolean` | Marked as "favorite"                                                                                                                                                                                                                                                                                                 |
| highlights            | `Array`   |                                                                                                                                                                                                                                                                                                                      |
| highlights\[].\_id    | `String`  | Unique id of highlight                                                                                                                                                                                                                                                                                               |
| highlights\[].text    | `String`  | Text of highlight (required)                                                                                                                                                                                                                                                                                         |
| highlights\[].color   | `String`  | <p>Color of highlight. <br>Default <code>yellow</code><br><br>Can be <code>blue</code>, <code>brown</code>, <code>cyan</code>, <code>gray</code>, <code>green</code>, <code>indigo</code>, <code>orange</code>, <code>pink</code>, <code>purple</code>, <code>red</code>, <code>teal</code>, <code>yellow</code></p> |
| highlights\[].note    | `String`  | Optional note for highlight                                                                                                                                                                                                                                                                                          |
| highlights\[].created | `String`  | Creation date of highlight                                                                                                                                                                                                                                                                                           |
| reminder              | `Object`  | Specify this object to attach reminder                                                                                                                                                                                                                                                                               |
| reminder.data         | `Date`    | YYYY-MM-DDTHH:mm:ss.sssZ                                                                                                                                                                                                                                                                                             |

{% hint style="warning" %}
Our API response could contain **other fields**, not described above. It's **unsafe to use** them in your integration! They could be removed or renamed at any time.
{% endhint %}



---

<!-- Source: https://developer.raindrop.io/v1/raindrops/multiple -->

# Multiple raindrops

### Common parameters

To filter, sort or limit raindrops use one of the parameters described below. Check each method for exact list of supported parameters.

| Parameter    | Type             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------ | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| collectionId | `Integer`        | <p>Path parameter that specify from which collection to get raindrops. Or specify one of system:</p><p><code>0</code> to get all (except Trash)</p><p><code>-1</code> to get from "Unsorted"</p><p><code>-99</code> to get from "Trash"</p><p></p><p>Warning: update or remove methods not support <code>0</code> yet. Will be fixed in future.</p>                                                                                                              |
| search       | `String`         | <p>As text, check all <a href="https://help.raindrop.io/using-search#operators">examples here</a></p><p>You can first test your searches in Raindrop app and if it works correctly, just copy content of search field and use it here</p>                                                                                                                                                                                                                        |
| sort         | `String`         | <p>Query parameter for sorting:</p><p><code>-created</code> by date descending (default)</p><p><code>created</code> by date ascending</p><p><code>score</code> by relevancy (only applicable when search is specified)</p><p><code>-sort</code> by order</p><p><code>title</code> by title (ascending)</p><p><code>-title</code> by title (descending)</p><p><code>domain</code> by hostname (ascending)</p><p><code>-domain</code> by hostname (descending)</p> |
| page         | `Integer`        | Query parameter. 0, 1, 2, 3 ...                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| perpage      | `Integer`        | Query parameter. How many raindrops per page. 50 max                                                                                                                                                                                                                                                                                                                                                                                                             |
| ids          | `Array<Integer>` | You can specify exact raindrop ID's for batch update/remove methods                                                                                                                                                                                                                                                                                                                                                                                              |
| nested       | `Boolean`        | Also include bookmarks from nested collections (true/false)                                                                                                                                                                                                                                                                                                                                                                                                      |

## Get raindrops

<mark style="color:blue;">`GET`</mark> `https://api.raindrop.io/rest/v1/raindrops/{collectionId}`

#### Path Parameters

| Name                                           | Type   | Description                                   |
| ---------------------------------------------- | ------ | --------------------------------------------- |
| collectionId<mark style="color:red;">\*</mark> | number | Collection ID. Specify 0 to get all raindrops |

#### Query Parameters

| Name    | Type    | Description |
| ------- | ------- | ----------- |
| sort    | string  |             |
| perpage | number  |             |
| page    | number  |             |
| search  | string  |             |
| nested  | boolean |             |

{% tabs %}
{% tab title="200 " %}

```
```

{% endtab %}
{% endtabs %}

## Create many raindrops

<mark style="color:green;">`POST`</mark> `https://api.raindrop.io/rest/v1/raindrops`

#### Request Body

| Name                                    | Type  | Description                                                                                                              |
| --------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------ |
| items<mark style="color:red;">\*</mark> | array | <p>Array of objects. Format of single object described in "Create single raindrop".<br>Maximum 100 objects in array!</p> |

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "result": true,
    "items": [
        {
            ...
        }
    ]
}
```

{% endtab %}
{% endtabs %}

## Update many raindrops

<mark style="color:orange;">`PUT`</mark> `https://api.raindrop.io/rest/v1/raindrops/{collectionId}`

Specify optional `search` and/or `ids` parameters to limit raindrops that will be updated.\
Possible fields that could be updated are described in "Body Parameters"

#### Path Parameters

| Name                                           | Type    | Description |
| ---------------------------------------------- | ------- | ----------- |
| collectionId<mark style="color:red;">\*</mark> | number  |             |
| nested                                         | boolean |             |

#### Request Body

| Name       | Type    | Description                                                                                                                                      |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| ids        | array   |                                                                                                                                                  |
| important  | boolean | <p>TRUE - mark as "favorite"<br>FALSE - unmark as "favorite"</p>                                                                                 |
| tags       | array   | <p>Will append specified tags to raindrops.<br>Or will remove all tags from raindrops if <code>\[]</code> (empty array) is specified</p>         |
| media      | array   | <p>Will append specified media items to raindrops.<br>Or will remove all media from raindrops if <code>\[]</code> (empty array) is specified</p> |
| cover      | string  | <p>Set URL for cover.<br><em>Tip:</em> specify <code>\<screenshot></code> to set screenshots for all raindrops</p>                               |
| collection | object  | Specify `{"$id": collectionId}` to move raindrops to other collection                                                                            |

{% tabs %}
{% tab title="200 " %}

```
```

{% endtab %}
{% endtabs %}

## Remove many raindrops

<mark style="color:red;">`DELETE`</mark> `https://api.raindrop.io/rest/v1/raindrops/{collectionId}`

Specify optional `search` and/or `ids` parameters to limit raindrops that will be moved to "**Trash**"\
When `:collectionId` is **-99**, raindrops will be permanently removed!

#### Path Parameters

| Name                                           | Type    | Description |
| ---------------------------------------------- | ------- | ----------- |
| collectionId<mark style="color:red;">\*</mark> | number  |             |
| nested                                         | boolean |             |

#### Query Parameters

| Name   | Type   | Description |
| ------ | ------ | ----------- |
| search | string |             |

#### Request Body

| Name | Type  | Description |
| ---- | ----- | ----------- |
| ids  | array |             |

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "result": true,
    "modified": 330
}
```

{% endtab %}
{% endtabs %}



---

<!-- Source: https://developer.raindrop.io/v1/raindrops/single -->

# Single raindrop

## Get raindrop

<mark style="color:blue;">`GET`</mark> `https://api.raindrop.io/rest/v1/raindrop/{id}`

#### Path Parameters

| Name                                 | Type   | Description          |
| ------------------------------------ | ------ | -------------------- |
| id<mark style="color:red;">\*</mark> | number | Existing raindrop ID |

{% tabs %}
{% tab title="200 " %}

```
```

{% endtab %}
{% endtabs %}

## Create raindrop

<mark style="color:green;">`POST`</mark> `https://api.raindrop.io/rest/v1/raindrop`

Description and possible values of fields described in "Fields"

#### Request Body

| Name                                   | Type    | Description                                                                                                                                |
| -------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| pleaseParse                            | object  | Specify empty object to automatically parse meta data (cover, description, html) in the background                                         |
| created                                | string  |                                                                                                                                            |
| lastUpdate                             | string  |                                                                                                                                            |
| order                                  | number  | <p>Specify sort order (ascending).<br>For example if you want to move raindrop to the first place set this field to <strong>0</strong></p> |
| important                              | boolean |                                                                                                                                            |
| tags                                   | array   |                                                                                                                                            |
| media                                  | array   |                                                                                                                                            |
| cover                                  | string  |                                                                                                                                            |
| collection                             | object  |                                                                                                                                            |
| type                                   | string  |                                                                                                                                            |
| excerpt                                | string  |                                                                                                                                            |
| note                                   | string  |                                                                                                                                            |
| title                                  | string  |                                                                                                                                            |
| link<mark style="color:red;">\*</mark> | string  |                                                                                                                                            |
| highlights                             | array   |                                                                                                                                            |
| reminder                               | object  |                                                                                                                                            |

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "result": true,
    "item": {
        ...
    }
}
```

{% endtab %}
{% endtabs %}

## Update raindrop

<mark style="color:orange;">`PUT`</mark> `https://api.raindrop.io/rest/v1/raindrop/{id}`

Description and possible values of fields described in "Fields"

#### Path Parameters

| Name                                 | Type   | Description          |
| ------------------------------------ | ------ | -------------------- |
| id<mark style="color:red;">\*</mark> | number | Existing raindrop ID |

#### Request Body

| Name        | Type    | Description                                                                                                                                |
| ----------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| created     | string  |                                                                                                                                            |
| lastUpdate  | string  |                                                                                                                                            |
| pleaseParse | object  | Specify empty object to re-parse link meta data (cover, type, html) in the background                                                      |
| order       | number  | <p>Specify sort order (ascending).<br>For example if you want to move raindrop to the first place set this field to <strong>0</strong></p> |
| important   | boolean |                                                                                                                                            |
| tags        | array   |                                                                                                                                            |
| media       | array   |                                                                                                                                            |
| cover       | string  |                                                                                                                                            |
| collection  | object  |                                                                                                                                            |
| type        | string  |                                                                                                                                            |
| excerpt     | string  |                                                                                                                                            |
| note        | string  |                                                                                                                                            |
| title       | string  |                                                                                                                                            |
| link        | string  |                                                                                                                                            |
| highlights  | array   |                                                                                                                                            |
| reminder    | object  |                                                                                                                                            |

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "result": true,
    "item": {
        ...
    }
}
```

{% endtab %}
{% endtabs %}

## Remove raindrop

<mark style="color:red;">`DELETE`</mark> `https://api.raindrop.io/rest/v1/raindrop/{id}`

When you remove raindrop it will be moved to user `Trash` collection. But if you try to remove raindrop from `Trash`, it will be removed permanently.

#### Path Parameters

| Name                                 | Type   | Description          |
| ------------------------------------ | ------ | -------------------- |
| id<mark style="color:red;">\*</mark> | number | Existing raindrop ID |

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "result": true
}
```

{% endtab %}
{% endtabs %}

## Upload file

<mark style="color:orange;">`PUT`</mark> `https://api.raindrop.io/rest/v1/raindrop/file`

Make sure to send PUT request with [multipart/form-data](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST#example) body

#### Headers

| Name                                           | Type   | Description         |
| ---------------------------------------------- | ------ | ------------------- |
| Content-Type<mark style="color:red;">\*</mark> | string | multipart/form-data |

#### Request Body

| Name                                   | Type   | Description   |
| -------------------------------------- | ------ | ------------- |
| file<mark style="color:red;">\*</mark> | object | File          |
| collectionId                           | String | Collection Id |

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "result": true,
    "item": {
        "title": "File name",
        "type": "image",
        "link": "https://up.raindrop.io/raindrop/111/file.jpeg",
        "domain": "raindrop.io",
        "file": {
            "name": "File name.jpeg",
            "size": 10000
        }
        ...
    }
}
```

{% endtab %}

{% tab title="400 " %}

```javascript
//file is not specified
{
  "result": false,
  "error": -1,
  "errorMessage": "no file"
}

//unsupported file format
{
  "result": false,
  "error": "file_invalid",
  "errorMessage": "File is invalid"
}

//file size is big
{
  "result": false,
  "error": "file_size_limit",
  "errorMessage": "File size limit"
}
```

{% endtab %}
{% endtabs %}

## Upload cover

<mark style="color:orange;">`PUT`</mark> `https://api.raindrop.io/rest/v1/raindrop/{id}/cover`

PNG, GIF or JPEG

#### Path Parameters

| Name                                 | Type   | Description          |
| ------------------------------------ | ------ | -------------------- |
| id<mark style="color:red;">\*</mark> | number | Existing raindrop ID |

#### Headers

| Name                                           | Type   | Description         |
| ---------------------------------------------- | ------ | ------------------- |
| Content-Type<mark style="color:red;">\*</mark> | string | multipart/form-data |

#### Request Body

| Name                                    | Type   | Description |
| --------------------------------------- | ------ | ----------- |
| cover<mark style="color:red;">\*</mark> | object | File        |

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "result": true,
    "item": {
        "cover": "https://up.raindrop.io/raindrop/...",
        "media": [
            {
                "link": "https://up.raindrop.io/raindrop/..."
            }
        ]
        ...
    }
}
```

{% endtab %}

{% tab title="400 " %}

```javascript
//file is not specified
{
  "result": false,
  "error": -1,
  "errorMessage": "no file"
}

//unsupported file format
{
  "result": false,
  "error": "file_invalid",
  "errorMessage": "File is invalid"
}

//file size is big
{
  "result": false,
  "error": "file_size_limit",
  "errorMessage": "File size limit"
}
```

{% endtab %}
{% endtabs %}

## Get permanent copy

<mark style="color:blue;">`GET`</mark> `https://api.raindrop.io/rest/v1/raindrop/{id}/cache`

Links permanently saved with all content (only in PRO plan). Using this method you can navigate to this copy.

#### Path Parameters

| Name                                 | Type   | Description          |
| ------------------------------------ | ------ | -------------------- |
| id<mark style="color:red;">\*</mark> | number | Existing raindrop ID |

{% tabs %}
{% tab title="307 " %}

```http
Location: https://s3.aws...
```

{% endtab %}
{% endtabs %}

## Suggest collection and tags for new bookmark

<mark style="color:green;">`POST`</mark> `https://api.raindrop.io/rest/v1/raindrop/suggest`

#### Request Body

| Name                                   | Type   | Description |
| -------------------------------------- | ------ | ----------- |
| link<mark style="color:red;">\*</mark> | string |             |

{% tabs %}
{% tab title="200 " %}

```json
{
    "result": true,
    "item": {
        "collections": [
            {
                "$id": 568368
            },
            {
                "$id": 8519567
            },
            {
                "$id": 1385626
            },
            {
                "$id": 8379661
            },
            {
                "$id": 20865985
            }
        ],
        "tags": [
            "fonts",
            "free",
            "engineering",
            "icons",
            "invalid_parser"
        ]
    }
}
```

{% endtab %}
{% endtabs %}

## Suggest collection and tags for existing bookmark

<mark style="color:blue;">`GET`</mark> `https://api.raindrop.io/rest/v1/raindrop/{id}/suggest`

#### Path Parameters

| Name                               | Type   | Description |
| ---------------------------------- | ------ | ----------- |
| <mark style="color:red;">\*</mark> | String | Bookmark id |

{% tabs %}
{% tab title="200 " %}

```json
{
    "result": true,
    "item": {
        "collections": [
            {
                "$id": 568368
            },
            {
                "$id": 8519567
            },
            {
                "$id": 1385626
            },
            {
                "$id": 8379661
            },
            {
                "$id": 20865985
            }
        ],
        "tags": [
            "fonts",
            "free",
            "engineering",
            "icons",
            "invalid_parser"
        ]
    }
}
```

{% endtab %}
{% endtabs %}



---

<!-- Source: https://developer.raindrop.io/v1/tags -->

# Tags

## Get tags

<mark style="color:blue;">`GET`</mark> `https://api.raindrop.io/rest/v1/tags/{collectionId}`

#### Path Parameters

| Name         | Type   | Description                                                                                |
| ------------ | ------ | ------------------------------------------------------------------------------------------ |
| collectionId | number | Optional collection ID, when not specified all tags from all collections will be retrieved |

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "result": true,
    "items": [
        {
            "_id": "api",
            "count": 100
        }
    ]
}
```

{% endtab %}
{% endtabs %}

## Rename tag

<mark style="color:orange;">`PUT`</mark> `https://api.raindrop.io/rest/v1/tags/{collectionId}`

#### Path Parameters

| Name         | Type   | Description                                                                   |
| ------------ | ------ | ----------------------------------------------------------------------------- |
| collectionId | number | It's possible to restrict rename action to just one collection. It's optional |

#### Request Body

| Name    | Type   | Description                                                |
| ------- | ------ | ---------------------------------------------------------- |
| replace | string | New name                                                   |
| tags    | array  | Specify **array** with **only one** string (name of a tag) |

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "result": true
}
```

{% endtab %}
{% endtabs %}

## Merge tags

<mark style="color:orange;">`PUT`</mark> `https://api.raindrop.io/rest/v1/tags/{collectionId}`

Basically this action rename bunch of `tags` to new name (`replace` field)

#### Path Parameters

| Name         | Type   | Description                                                                  |
| ------------ | ------ | ---------------------------------------------------------------------------- |
| collectionId | string | It's possible to restrict merge action to just one collection. It's optional |

#### Request Body

| Name    | Type   | Description  |
| ------- | ------ | ------------ |
| replace | string | New name     |
| tags    | array  | List of tags |

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "result": true
}
```

{% endtab %}
{% endtabs %}

## Remove tag(s)

<mark style="color:red;">`DELETE`</mark> `https://api.raindrop.io/rest/v1/tags/{collectionId}`

#### Path Parameters

| Name         | Type   | Description                                                                   |
| ------------ | ------ | ----------------------------------------------------------------------------- |
| collectionId | string | It's possible to restrict remove action to just one collection. It's optional |

#### Request Body

| Name | Type  | Description  |
| ---- | ----- | ------------ |
| tags | array | List of tags |

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "result": true
}
```

{% endtab %}
{% endtabs %}



---

<!-- Source: https://developer.raindrop.io/v1/user -->

# User

### Main fields

| Field                | Publicly visible | Type            | Description                                                   |
| -------------------- | ---------------- | --------------- | ------------------------------------------------------------- |
| \_id                 | **Yes**          | `Integer`       | Unique user ID                                                |
| config               | No               | `Object`        | More details in "Config fields"                               |
| email                | No               | `String`        | Only visible for you                                          |
| email\_MD5           | **Yes**          | `String`        | MD5 hash of email. Useful for using with Gravatar for example |
| files.used           | No               | `Integer`       | How much space used for files this month                      |
| files.size           | No               | `Integer`       | Total space for file uploads                                  |
| files.lastCheckPoint | No               | `String`        | When space for file uploads is reseted last time              |
| fullName             | **Yes**          | `String`        | Full name, max 1000 chars                                     |
| groups               | No               | `Array<Object>` | More details below in "Groups"                                |
| password             | No               | `Boolean`       | Does user have a password                                     |
| pro                  | **Yes**          | `Boolean`       | PRO subscription                                              |
| proExpire            | No               | `String`        | When PRO subscription will expire                             |
| registered           | No               | `String`        | Registration date                                             |

### Config fields

| Field                   | Publicly visible | Type      | Description                                                                                                                                                                                 |
| ----------------------- | ---------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| config.broken\_level    | No               | `String`  | <p>Broken links finder configuration, possible values:</p><p><code>basic</code> <code>default</code> <code>strict</code> or <code>off</code></p>                                            |
| config.font\_color      | No               | `String`  | Bookmark preview style: `sunset` `night` or empty                                                                                                                                           |
| config.font\_size       | No               | `Integer` | Bookmark preview font size: from 0 to 9                                                                                                                                                     |
| config.lang             | No               | `String`  | UI language in 2 char code                                                                                                                                                                  |
| config.last\_collection | No               | `Integer` | Last viewed collection ID                                                                                                                                                                   |
| config.raindrops\_sort  | No               | `String`  | <p>Default bookmark sort:</p><p><code>title</code> <code>-title</code> <code>-sort</code> <code>domain</code> <code>-domain</code> <code>+lastUpdate</code> or <code>-lastUpdate</code></p> |
| config.raindrops\_view  | No               | `String`  | <p>Default bookmark view:</p><p><code>grid</code> <code>list</code> <code>simple</code> or <code>masonry</code></p>                                                                         |

### Groups object fields <a href="#single-group-detail" id="single-group-detail"></a>

| Field       | Type             | Description              |
| ----------- | ---------------- | ------------------------ |
| title       | `String`         | Name of group            |
| hidden      | `Boolean`        | Does group is collapsed  |
| sort        | `Integer`        | Ascending order position |
| collections | `Array<Integer>` | Collection ID's in order |

### Other fields

| Field             | Publicly visible | Type      | Description                         |
| ----------------- | ---------------- | --------- | ----------------------------------- |
| facebook.enabled  | No               | `Boolean` | Does Facebook account is linked     |
| twitter.enabled   | No               | `Boolean` | Does Twitter account is linked      |
| vkontakte.enabled | No               | `Boolean` | Does Vkontakte account is linked    |
| google.enabled    | No               | `Boolean` | Does Google account is linked       |
| dropbox.enabled   | No               | `Boolean` | Does Dropbox backup is enabled      |
| gdrive.enabled    | No               | `Boolean` | Does Google Drive backup is enabled |

{% hint style="warning" %}
Our API response could contain **other fields**, not described above. It's **unsafe to use** them in your integration! They could be removed or renamed at any time.
{% endhint %}



---

<!-- Source: https://developer.raindrop.io/v1/user/authenticated -->

# Authenticated user

## Get user

<mark style="color:blue;">`GET`</mark> `https://api.raindrop.io/rest/v1/user`

Get currently authenticated user details

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "result": true,
    "user": {
      "_id": 32,
      "config": {
        "broken_level": "strict",
        "font_color": "",
        "font_size": 0,
        "lang": "ru_RU",
        "last_collection": 8492393,
        "raindrops_sort": "-lastUpdate",
        "raindrops_view": "list"
      },
      "dropbox": {
        "enabled": true
      },
      "email": "some@email.com",
      "email_MD5": "13a0a20681d8781912e5314150694bf7",
      "files": {
        "used": 6766094,
        "size": 10000000000,
        "lastCheckPoint": "2020-01-26T23:53:19.676Z"
      },
      "fullName": "Mussabekov Rustem",
      "gdrive": {
        "enabled": true
      },
      "groups": [
        {
          "title": "My Collections",
          "hidden": false,
          "sort": 0,
          "collections": [
            8364483,
            8364403,
            66
          ]
        }
      ],
      "password": true,
      "pro": true,
      "proExpire": "2028-09-27T22:00:00.000Z",
      "registered": "2014-09-30T07:51:15.406Z"
  }
}
```

{% endtab %}

{% tab title="401 " %}

```http
Unauthorized
```

{% endtab %}
{% endtabs %}

## Get user by name

<mark style="color:blue;">`GET`</mark> `https://api.raindrop.io/rest/v1/user/{name}`

Get's publicly available user details

#### Path Parameters

| Name                                   | Type   | Description |
| -------------------------------------- | ------ | ----------- |
| name<mark style="color:red;">\*</mark> | number | Username    |

{% tabs %}
{% tab title="200 " %}

```javascript
{
  "result": true,
  "user": {
    "_id": 32,
    "email_MD5": "13a0a20681d8781912e5314150694bf7",
    "fullName": "Mussabekov Rustem",
    "pro": true,
    "registered": "2014-09-30T07:51:15.406Z"
  }
}
```

{% endtab %}

{% tab title="404 " %}

```javascript
{
  "error": -1,
  "errorMessage": "not found",
  "result": false
}
```

{% endtab %}
{% endtabs %}

## Update user

<mark style="color:orange;">`PUT`</mark> `https://api.raindrop.io/rest/v1/user`

To change email, config, password, etc... you can do it from single endpoint&#x20;

#### Request Body

| Name        | Type   | Description |
| ----------- | ------ | ----------- |
| groups      | array  |             |
| config      | object |             |
| newpassword | string |             |
| oldpassword | string |             |
| fullName    | string |             |
| email       | string |             |

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "result": true,
    "user": {
        ...
    }
}
```

{% endtab %}

{% tab title="400 " %}

```javascript
//email specified but empty
{
  "result": false,
  "error": 1,
  "errorMessage": "email required"
}

//fullName specified but empty
{
  "result": false,
  "error": 2,
  "errorMessage": "User validation failed: fullName: is required"
}

//newpassword specified, but oldpassword is empty
{
  "result": false,
  "error": 3,
  "errorMessage": "oldpassword incorrect"
}

//incorrect config key value
{
  "result": false,
  "error": "config.raindrops_sort",
  "errorMessage": "User validation failed: config.raindrops_sort: `1` is not a valid enum value for path `raindrops_sort`., config: Validation failed: raindrops_sort: `1` is not a valid enum value for path `raindrops_sort`."
}
```

{% endtab %}
{% endtabs %}

## Connect social network account

<mark style="color:blue;">`GET`</mark> `https://api.raindrop.io/rest/v1/user/connect/{provider}`

Connect social network account as sign in authentication option

#### Path Parameters

| Name     | Type   | Description                                                     |
| -------- | ------ | --------------------------------------------------------------- |
| provider | string | `facebook` `google` `twitter` `vkontakte` `dropbox` or `gdrive` |

{% tabs %}
{% tab title="307 " %}

```http
Location: https://some.com/...
```

{% endtab %}
{% endtabs %}

## Disconnect social network account

<mark style="color:blue;">`GET`</mark> `https://api.raindrop.io/rest/v1/user/connect/{provider}/revoke`

Disconnect social network account from available authentication options

#### Path Parameters

| Name     | Type   | Description                                                     |
| -------- | ------ | --------------------------------------------------------------- |
| provider | string | `facebook` `google` `twitter` `vkontakte` `dropbox` or `gdrive` |

{% tabs %}
{% tab title="200 " %}

```
```

{% endtab %}
{% endtabs %}

